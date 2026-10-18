"""Rebuild the prompt corpus into the v0.2 study design.

This script is intentionally deterministic. It performs only corpus-construction
changes agreed before model evaluation:

1. rebalance difficulty to 25 easy / 50 medium / 25 hard per domain;
2. normalize unnatural Bengali technical terminology;
3. regenerate Bengali-English code-switching from the natural Bengali prompt so
   Bengali remains the matrix language;
4. replace SYN091-SYN100 with substantially longer, context-dense synthesis tasks;
5. preserve task IDs, English/Bengali semantic pairing, and the seven-column
   prompt-corpus schema.

Run from the repository root:
    python scripts/revise_corpus_v02.py
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT_DIR = ROOT / "data" / "prompts"

PROMPT_FILES = [
    "technical_troubleshooting_001_050.csv",
    "technical_troubleshooting_051_100.csv",
    "cybersecurity_digital_safety_001_050.csv",
    "cybersecurity_digital_safety_051_100.csv",
    "procedural_instructional_001_050.csv",
    "procedural_instructional_051_100.csv",
    "decision_support_001_050.csv",
    "decision_support_051_100.csv",
    "information_synthesis_001_050.csv",
    "information_synthesis_051_100.csv",
]

PREFIXES = ["TECH", "CYBER", "PROC", "DEC", "SYN"]

# Each domain began at 30/40/30. Moving five easy and five hard items to
# medium produces the agreed 25/50/25 distribution without changing task text.
# These IDs are distributed across the domain instead of clustering at one end.
DIFFICULTY_TO_MEDIUM = {
    f"{prefix}{number:03d}"
    for prefix in PREFIXES
    for number in (3, 8, 23, 28, 43, 48, 63, 68, 83, 88)
}

# Technical Bengali should be natural for contemporary Bengali-speaking users.
# These transformations are conditional on the English semantic specification,
# so ordinary Bengali senses (for example, an identification document) are not
# accidentally replaced by a computing term.
BN_TECHNICAL_RULES = [
    ("working directory", [("কার্যকরী ফোল্ডার", "ওয়ার্কিং ডিরেক্টরি")]),
    ("continuous integration", [("ধারাবাহিক সমন্বয়", "CI (Continuous Integration)")]),
    ("build caching", [("নির্মাণ সঞ্চয়", "বিল্ড ক্যাশিং")]),
    ("production api", [("বাস্তব এপিআই", "প্রোডাকশন API")]),
    ("consumer failures", [("গ্রাহক ব্যর্থতা", "কনজিউমার ফেইলিউর")]),
    ("idempotency", [("পুনরাবৃত্তি-নিরাপত্তা", "idempotency")]),
    ("acknowledgments", [("স্বীকৃতি", "acknowledgment")]),
    ("connection pools", [("সংযোগ পুল", "connection pool")]),
    ("observability data", [("পর্যবেক্ষণ তথ্য", "observability data")]),
    ("driver", [("চালক", "ড্রাইভার")]),
    ("drivers", [("চালক", "ড্রাইভার")]),
    ("credential", [("পরিচয়পত্র", "ক্রেডেনশিয়াল")]),
    ("credentials", [("পরিচয়পত্র", "ক্রেডেনশিয়াল")]),
    ("cache", [("সঞ্চয়", "ক্যাশ")]),
    ("caching", [("সঞ্চয়", "ক্যাশিং")]),
    ("deployment", [("স্থাপনার ক্রম", "ডিপ্লয়মেন্টের ক্রম"), ("স্থাপনের সময়", "ডিপ্লয়মেন্টের সময়")]),
    ("timeout", [("সময় শেষ হওয়ার", "টাইমআউটের")]),
]

# Bengali-matrix code-switching lexicon. We regenerate BN-CS from prompt_bn,
# rather than translating English independently, so syntax, constraints, and
# pragmatic force stay aligned with the Bengali condition. Only common lexical
# items and domain terminology are switched to Latin-script English.
COMMON_CS_REPLACEMENTS = [
    ("অগ্রাধিকার", "priority"),
    ("পরিকল্পনা", "plan"),
    ("সিদ্ধান্ত", "decision"),
    ("প্রতিবেদন", "report"),
    ("বিশ্লেষণ", "analysis"),
    ("মূল্যায়ন", "evaluation"),
    ("পর্যালোচনা", "review"),
    ("প্রকল্প", "project"),
    ("ব্যবহারকারী", "user"),
    ("গ্রাহক", "customer"),
    ("কর্মশালা", "workshop"),
    ("প্রশিক্ষণ", "training"),
    ("নিবন্ধন", "registration"),
    ("সময়সীমা", "deadline"),
    ("বাজেট", "budget"),
    ("ঝুঁকি", "risk"),
    ("বিকল্প", "option"),
    ("সিস্টেম", "system"),
    ("সার্ভার", "server"),
    ("ডেটাসেট", "dataset"),
    ("ডাটাবেস", "database"),
    ("ডেটাবেস", "database"),
    ("ফাইল", "file"),
    ("ফোল্ডার", "folder"),
    ("ল্যাপটপ", "laptop"),
    ("কম্পিউটার", "computer"),
    ("অ্যাপ্লিকেশন", "application"),
    ("অ্যাপ", "app"),
    ("সফটওয়্যার", "software"),
    ("হার্ডওয়্যার", "hardware"),
    ("নেটওয়ার্ক", "network"),
    ("ওয়াই-ফাই", "Wi-Fi"),
    ("ভিপিএন", "VPN"),
    ("ফায়ারওয়াল", "firewall"),
    ("ক্লাউড", "cloud"),
    ("ব্যাকআপ", "backup"),
    ("কনফিগারেশন", "configuration"),
    ("ডিপ্লয়মেন্ট", "deployment"),
    ("ড্রাইভার", "driver"),
    ("ক্যাশিং", "caching"),
    ("ক্যাশ", "cache"),
    ("ক্রেডেনশিয়াল", "credential"),
    ("লগইন", "login"),
    ("পাসওয়ার্ড", "password"),
    ("ইমেইল", "email"),
    ("রেকর্ড", "record"),
    ("পাইলট", "pilot"),
    ("মডেল", "model"),
    ("জরিপ", "survey"),
    ("ডকুমেন্টেশন", "documentation"),
    ("ডকুমেন্ট", "document"),
    ("মাইগ্রেশন", "migration"),
    ("ভ্যালিডেশন", "validation"),
    ("রোলব্যাক", "rollback"),
    ("API", "API"),
]

# Extra domain terminology. These are intentionally nouns/noun phrases rather
# than whole English clauses; Bengali grammar remains dominant.
DOMAIN_CS_REPLACEMENTS = {
    "technical_troubleshooting": [
        ("ত্রুটি", "error"),
        ("স্টোরেজ", "storage"),
        ("পারফরম্যান্স", "performance"),
        ("রাউটিং", "routing"),
        ("গেটওয়ে", "gateway"),
        ("সাবনেট", "subnet"),
        ("প্রক্সি", "proxy"),
        ("ফার্মওয়্যার", "firmware"),
    ],
    "cybersecurity_digital_safety": [
        ("নিরাপত্তা", "security"),
        ("আক্রমণ", "attack"),
        ("ঘটনা", "incident"),
        ("ম্যালওয়্যার", "malware"),
        ("ফিশিং", "phishing"),
        ("এনক্রিপশন", "encryption"),
        ("অ্যাক্সেস", "access"),
        ("অনুমতি", "permission"),
    ],
    "procedural_instructional": [
        ("চেকলিস্ট", "checklist"),
        ("ক্যালেন্ডার", "calendar"),
        ("বুকিং", "booking"),
        ("অ্যাপয়েন্টমেন্ট", "appointment"),
    ],
    "decision_support": [
        ("খরচ", "cost"),
        ("সময়সূচি", "schedule"),
        ("প্রভাব", "impact"),
        ("প্রমাণ", "evidence"),
        ("অনিশ্চয়তা", "uncertainty"),
    ],
    "information_synthesis": [
        ("সারাংশ", "summary"),
        ("ফলাফল", "result"),
        ("তথ্য", "data"),
        ("প্রমাণ", "evidence"),
        ("অজানা", "unknown"),
    ],
}


def normalize_bn(prompt_en: str, prompt_bn: str) -> str:
    en = prompt_en.lower()
    out = prompt_bn
    for trigger, replacements in BN_TECHNICAL_RULES:
        if trigger in en:
            for old, new in replacements:
                out = out.replace(old, new)
    return out


def make_code_switched(prompt_bn: str, domain: str) -> str:
    out = prompt_bn
    replacements = COMMON_CS_REPLACEMENTS + DOMAIN_CS_REPLACEMENTS.get(domain, [])
    # Longest first prevents a short term from partially consuming a phrase.
    for old, new in sorted(replacements, key=lambda pair: len(pair[0]), reverse=True):
        out = out.replace(old, new)
    return out


# SYN091-SYN100: extended-context tasks. These are deliberately much longer
# than the rest of the corpus and contain multiple facts, dependencies,
# caveats, and unknowns that must be retained without unsupported inference.
EXTENDED_CONTEXT = {
    "SYN091": {
        "en": """Read the full operational note and produce a six-sentence briefing for attendees. Preserve every requirement that affects whether someone can participate successfully, but do not add assumptions. The professional-development workshop is scheduled for Friday, October 16, from 1:00 PM to 3:00 PM in Room 310 of the North Building. Check-in opens at 12:30 PM outside the room. Participants must bring a laptop that can connect to Wi-Fi, and the required analysis software must be installed before arrival because the first activity begins immediately after introductions. Installation instructions were emailed on Monday, but the help desk will also hold a remote installation clinic Thursday from 4:00 PM to 5:30 PM. Anyone who cannot install the software should attend that clinic rather than wait until Friday. The room has power outlets at every table, but only eight loaner laptops are available, and those are reserved for participants who requested one by Wednesday at noon. Coffee, tea, and water will be available; lunch will not be provided. Participants may bring food, but food is not allowed near the demonstration equipment at the front of the room. The workshop has 42 registered attendees and a room capacity of 50. Walk-ins may be accepted only if seats remain after 12:50 PM. Attendance certificates require staying through the final exercise and submitting the short exit form. The organizer has not announced whether the session will be recorded, so the briefing must not promise a recording.""",
        "bn": """সম্পূর্ণ কার্যক্রমের নোটটি পড়ে অংশগ্রহণকারীদের জন্য ছয় বাক্যের একটি ব্রিফিং তৈরি করুন। সফলভাবে অংশ নিতে যেসব শর্ত জানা প্রয়োজন সেগুলো বাদ দেবেন না, তবে কোনো অনুমান যোগ করবেন না। পেশাগত উন্নয়ন কর্মশালাটি শুক্রবার, ১৬ অক্টোবর, দুপুর ১টা থেকে ৩টা পর্যন্ত নর্থ বিল্ডিংয়ের ৩১০ নম্বর কক্ষে হবে। কক্ষের বাইরে চেক-ইন শুরু হবে দুপুর ১২টা ৩০ মিনিটে। অংশগ্রহণকারীদের ওয়াই-ফাইতে যুক্ত হতে পারে এমন একটি ল্যাপটপ আনতে হবে এবং প্রয়োজনীয় বিশ্লেষণ সফটওয়্যার আগেই ইনস্টল করা থাকতে হবে, কারণ পরিচিতির পরপরই প্রথম কার্যক্রম শুরু হবে। ইনস্টলেশনের নির্দেশনা সোমবার ইমেইলে পাঠানো হয়েছে; পাশাপাশি বৃহস্পতিবার বিকেল ৪টা থেকে ৫টা ৩০ মিনিট পর্যন্ত হেল্প ডেস্ক একটি দূরবর্তী ইনস্টলেশন ক্লিনিক করবে। কেউ সফটওয়্যার ইনস্টল করতে না পারলে শুক্রবার পর্যন্ত অপেক্ষা না করে ওই ক্লিনিকে অংশ নেওয়া উচিত। প্রতিটি টেবিলে বিদ্যুৎ সংযোগ আছে, তবে ধার দেওয়ার জন্য মাত্র আটটি ল্যাপটপ আছে এবং সেগুলো কেবল বুধবার দুপুরের মধ্যে অনুরোধ করা অংশগ্রহণকারীদের জন্য সংরক্ষিত। কফি, চা ও পানি থাকবে, কিন্তু দুপুরের খাবার দেওয়া হবে না। অংশগ্রহণকারীরা খাবার আনতে পারবেন, তবে কক্ষের সামনের প্রদর্শনী সরঞ্জামের কাছে খাবার নেওয়া যাবে না। মোট ৪২ জন নিবন্ধিত এবং কক্ষের ধারণক্ষমতা ৫০। দুপুর ১২টা ৫০ মিনিটের পর আসন খালি থাকলে তবেই পূর্বনিবন্ধন ছাড়া অংশগ্রহণকারী নেওয়া হতে পারে। উপস্থিতির সনদ পেতে শেষ কার্যক্রম পর্যন্ত থাকতে হবে এবং সংক্ষিপ্ত প্রস্থান ফরম জমা দিতে হবে। সেশনটি রেকর্ড করা হবে কি না আয়োজক এখনো জানাননি, তাই ব্রিফিংয়ে রেকর্ডিংয়ের প্রতিশ্রুতি দেওয়া যাবে না।""",
    },
    "SYN092": {
        "en": """Summarize the registration rules in a clear participant-facing notice while preserving fees, deadlines, capacity rules, and exceptions. Registration for the annual student-success conference opens August 24. Current students may register at no charge if they use an institutional email address. Staff and alumni pay $25, while external guests pay $40. The main auditorium holds 80 people. Registration closes when 80 confirmed seats are reached or at 5:00 PM on September 10, whichever happens first. A registration that is started but not completed does not reserve a seat. Payment for staff, alumni, and guests must clear before the registration is confirmed. A waiting list opens automatically once capacity is reached. People on the waiting list are contacted in order if a confirmed attendee cancels, and they have 12 hours to accept the offered seat. Walk-ins are not permitted because building security requires an advance attendee list. Cancellations received by September 8 qualify for a full refund of paid fees; cancellations after that date are normally nonrefundable, although the organizer may approve an exception for documented emergencies. Students who registered for free should still cancel if they cannot attend so the seat can be offered to someone else. Accessibility accommodations should be requested by September 4, but requests received later will still be considered when feasible. The conference office has not guaranteed that late accommodation requests can be fulfilled. Registration confirmation emails contain a QR code that will be used for check-in, but attendees who cannot display the code may check in with a government- or school-issued photo ID.""",
        "bn": """ফি, সময়সীমা, ধারণক্ষমতার নিয়ম এবং ব্যতিক্রম অক্ষুণ্ন রেখে অংশগ্রহণকারীদের জন্য পরিষ্কার নিবন্ধন নোটিশ লিখুন। বার্ষিক শিক্ষার্থী-সাফল্য সম্মেলনের নিবন্ধন ২৪ আগস্ট খুলবে। বর্তমান শিক্ষার্থীরা প্রাতিষ্ঠানিক ইমেইল ব্যবহার করলে বিনা খরচে নিবন্ধন করতে পারবেন। কর্মী ও প্রাক্তন শিক্ষার্থীদের ফি ২৫ ডলার, আর বাইরের অতিথিদের ৪০ ডলার। প্রধান অডিটোরিয়ামের ধারণক্ষমতা ৮০ জন। ৮০টি নিশ্চিত আসন পূর্ণ হলে অথবা ১০ সেপ্টেম্বর বিকেল ৫টায়—যেটি আগে ঘটে—নিবন্ধন বন্ধ হবে। নিবন্ধন শুরু করলেও সম্পূর্ণ না করলে আসন সংরক্ষিত হবে না। কর্মী, প্রাক্তন শিক্ষার্থী ও অতিথিদের অর্থপ্রদান সম্পন্ন না হওয়া পর্যন্ত নিবন্ধন নিশ্চিত হবে না। ধারণক্ষমতা পূর্ণ হলে স্বয়ংক্রিয়ভাবে অপেক্ষমাণ তালিকা খুলবে। নিশ্চিত অংশগ্রহণকারী বাতিল করলে তালিকার ক্রম অনুযায়ী আসন প্রস্তাব করা হবে এবং প্রস্তাব পাওয়া ব্যক্তির গ্রহণ করার জন্য ১২ ঘণ্টা সময় থাকবে। ভবনের নিরাপত্তার জন্য আগাম অংশগ্রহণকারীর তালিকা প্রয়োজন, তাই সরাসরি এসে অংশ নেওয়া যাবে না। ৮ সেপ্টেম্বরের মধ্যে বাতিল করলে প্রদত্ত ফি পুরো ফেরত পাওয়া যাবে; এরপর সাধারণত ফেরত দেওয়া হবে না, তবে নথিভুক্ত জরুরি পরিস্থিতিতে আয়োজক ব্যতিক্রম অনুমোদন করতে পারেন। বিনা খরচে নিবন্ধিত শিক্ষার্থীরাও আসতে না পারলে বাতিল করবেন যাতে আসন অন্য কাউকে দেওয়া যায়। প্রবেশগম্যতা-সংক্রান্ত সহায়তা ৪ সেপ্টেম্বরের মধ্যে চাওয়া উচিত, তবে পরে পাওয়া অনুরোধও সম্ভব হলে বিবেচনা করা হবে; দেরিতে করা অনুরোধ পূরণ হবে এমন নিশ্চয়তা দেওয়া হয়নি। নিশ্চিতকরণ ইমেইলে চেক-ইনের জন্য একটি QR কোড থাকবে, তবে কেউ কোড দেখাতে না পারলে সরকারি বা শিক্ষাপ্রতিষ্ঠান-প্রদত্ত ছবিযুক্ত পরিচয়পত্র দিয়ে চেক-ইন করতে পারবেন।""",
    },
    "SYN093": {
        "en": """Create a concise project-status synthesis that distinguishes completed work, work in progress, dependencies, and schedule risk. Dataset A contains 5,000 records. Its duplicate-removal and field-standardization steps are complete, and a quality check found no unresolved blocking errors. Dataset B contains 8,000 records. Sixty percent of Dataset B has been cleaned; the remaining records include older entries with inconsistent date formats and missing category labels. Two analysts are working on Dataset B today, but one will be unavailable tomorrow. The team originally planned to finish cleaning both datasets by Friday afternoon. Statistical analysis is not allowed to begin on the combined data until both datasets pass the same validation rules. A preliminary descriptive analysis has been run on the cleaned portion of Dataset A only, but those preliminary numbers must not be presented as final study results. The target date for the full analysis to begin is Monday morning. If Dataset B is not ready by Friday, the team can use Monday morning for final cleaning, but doing so would delay the first full analysis by at least one business day. The report deadline itself has not changed and remains the following Thursday at noon. The visualization specialist needs validated summary tables at least 24 hours before the report deadline. No additional analyst has yet been assigned. The project manager has asked the team to report by 3:00 PM Friday whether Monday analysis remains realistic. The available information does not establish how long the remaining inconsistent records will take to correct, so the synthesis should describe that as an uncertainty rather than inventing a completion estimate.""",
        "bn": """সম্পন্ন কাজ, চলমান কাজ, নির্ভরতা এবং সময়সূচির ঝুঁকি আলাদা করে একটি সংক্ষিপ্ত প্রকল্প-অবস্থা সারাংশ তৈরি করুন। ডেটাসেট A-তে ৫,০০০ রেকর্ড আছে। এর ডুপ্লিকেট সরানো ও ফিল্ড মানসম্মত করার কাজ শেষ এবং মান যাচাইয়ে কোনো অমীমাংসিত বাধাদানকারী ত্রুটি পাওয়া যায়নি। ডেটাসেট B-তে ৮,০০০ রেকর্ড আছে। B-এর ৬০ শতাংশ পরিষ্কার হয়েছে; বাকি রেকর্ডে পুরোনো এন্ট্রি, অসামঞ্জস্যপূর্ণ তারিখের বিন্যাস এবং অনুপস্থিত শ্রেণি-লেবেল রয়েছে। আজ দুইজন বিশ্লেষক B নিয়ে কাজ করছেন, তবে তাঁদের একজন আগামীকাল থাকবেন না। দলের মূল পরিকল্পনা ছিল শুক্রবার বিকেলের মধ্যে দুই ডেটাসেটের পরিষ্কার কাজ শেষ করা। একই যাচাইয়ের নিয়মে দুই ডেটাসেট পাস না করা পর্যন্ত একত্রিত ডেটার পরিসংখ্যান বিশ্লেষণ শুরু করা যাবে না। কেবল A-এর পরিষ্কার অংশে একটি প্রাথমিক বর্ণনামূলক বিশ্লেষণ চালানো হয়েছে, কিন্তু ওই প্রাথমিক সংখ্যা চূড়ান্ত গবেষণা-ফল হিসেবে দেখানো যাবে না। পূর্ণ বিশ্লেষণ শুরুর লক্ষ্য সোমবার সকাল। শুক্রবার B প্রস্তুত না হলে সোমবার সকালের কিছু সময় শেষ পরিষ্কারের কাজে ব্যবহার করা যাবে, কিন্তু তাতে প্রথম পূর্ণ বিশ্লেষণ অন্তত এক কর্মদিবস পিছোবে। প্রতিবেদনের সময়সীমা পরিবর্তন হয়নি; এটি পরের বৃহস্পতিবার দুপুর ১২টা। ভিজ্যুয়ালাইজেশন বিশেষজ্ঞের প্রতিবেদন জমার অন্তত ২৪ ঘণ্টা আগে যাচাইকৃত সারাংশ-টেবিল প্রয়োজন। অতিরিক্ত কোনো বিশ্লেষক এখনো বরাদ্দ করা হয়নি। প্রকল্প ব্যবস্থাপক শুক্রবার বিকেল ৩টার মধ্যে জানতে চেয়েছেন সোমবার বিশ্লেষণ শুরু করা বাস্তবসম্মত কি না। বাকি অসামঞ্জস্যপূর্ণ রেকর্ড ঠিক করতে কত সময় লাগবে সে বিষয়ে কোনো প্রমাণ নেই, তাই সারাংশে এটিকে অনিশ্চয়তা হিসেবে দেখাতে হবে; নিজের মতো সম্পন্ন হওয়ার সময় বানানো যাবে না।""",
    },
    "SYN094": {
        "en": """Write a handoff briefing for the next technical shift. Separate verified status, pending work, decision points, and time constraints. The application-server upgrade finished at 6:40 PM and post-upgrade health checks passed. A full backup of the production database completed before maintenance began, and the backup checksum was verified successfully. The database migration itself has not started. The migration package was tested in staging yesterday, but production has a larger table that is not present in staging. The maintenance window ends at 2:00 AM. The vendor database engineer will be available remotely from 9:00 PM until midnight and has asked to be contacted before any production rollback. The internal database administrator is available for the entire window. The team estimates that the planned migration usually takes 70 to 90 minutes and that validation normally takes another 30 minutes, but those estimates do not account for the additional production-only table. A rollback from the pre-maintenance backup is estimated to take about two hours after the decision to roll back. Production cutover cannot be declared complete until migration and validation both pass. The customer-support team expects normal service by 6:00 AM and needs an update by 1:00 AM if that expectation is at risk. No one has yet defined an explicit latest-start time for migration or an automatic rollback threshold. There are currently no reported user transactions because the system is in the announced maintenance window. The handoff must not state that the production-only table will cause a delay; it should identify it as an unresolved risk that may affect the estimate.""",
        "bn": """পরবর্তী প্রযুক্তি শিফটের জন্য একটি হস্তান্তর ব্রিফিং লিখুন। যাচাইকৃত অবস্থা, বাকি কাজ, সিদ্ধান্তের জায়গা এবং সময়ের সীমা আলাদা রাখুন। অ্যাপ্লিকেশন-সার্ভার আপগ্রেড সন্ধ্যা ৬টা ৪০ মিনিটে শেষ হয়েছে এবং আপগ্রেড-পরবর্তী স্বাস্থ্য পরীক্ষা সফল। রক্ষণাবেক্ষণ শুরুর আগে প্রোডাকশন ডেটাবেসের পূর্ণ ব্যাকআপ শেষ হয়েছে এবং ব্যাকআপের চেকসমও সফলভাবে যাচাই করা হয়েছে। ডেটাবেস মাইগ্রেশন এখনো শুরু হয়নি। মাইগ্রেশন প্যাকেজটি গতকাল স্টেজিং পরিবেশে পরীক্ষা করা হয়েছে, কিন্তু প্রোডাকশনে একটি বড় টেবিল আছে যা স্টেজিংয়ে নেই। রক্ষণাবেক্ষণের সময়সীমা রাত ২টায় শেষ হবে। ভেন্ডরের ডেটাবেস প্রকৌশলী রাত ৯টা থেকে ১২টা পর্যন্ত দূর থেকে পাওয়া যাবেন এবং কোনো প্রোডাকশন রোলব্যাকের আগে তাঁর সঙ্গে যোগাযোগ করতে বলেছেন। অভ্যন্তরীণ ডেটাবেস প্রশাসক পুরো সময়জুড়ে থাকবেন। পরিকল্পিত মাইগ্রেশন সাধারণত ৭০ থেকে ৯০ মিনিট এবং যাচাই আরও প্রায় ৩০ মিনিট লাগে বলে দলের অনুমান, তবে এই অনুমানে শুধু প্রোডাকশনে থাকা অতিরিক্ত টেবিলটি ধরা হয়নি। রক্ষণাবেক্ষণের আগের ব্যাকআপ থেকে রোলব্যাক করতে সিদ্ধান্ত নেওয়ার পর প্রায় দুই ঘণ্টা লাগবে বলে অনুমান। মাইগ্রেশন ও যাচাই—দুটোই সফল না হওয়া পর্যন্ত প্রোডাকশন কাটওভার সম্পন্ন বলা যাবে না। গ্রাহক-সহায়তা দল সকাল ৬টার মধ্যে স্বাভাবিক সেবা আশা করছে এবং সেই সময় ঝুঁকিতে পড়লে রাত ১টার মধ্যে আপডেট চায়। মাইগ্রেশন সর্বশেষ কখন শুরু করা যাবে বা কোন অবস্থায় স্বয়ংক্রিয়ভাবে রোলব্যাক হবে—এমন স্পষ্ট সীমা এখনো নির্ধারিত হয়নি। ঘোষিত রক্ষণাবেক্ষণ চলায় বর্তমানে কোনো ব্যবহারকারী লেনদেনের প্রতিবেদন নেই। ব্রিফিংয়ে প্রোডাকশন-শুধু টেবিলটি অবশ্যই দেরি ঘটাবে বলা যাবে না; বরং এটিকে এমন একটি অমীমাংসিত ঝুঁকি হিসেবে দেখাতে হবে যা সময়ের অনুমানে প্রভাব ফেলতে পারে।""",
    },
    "SYN095": {
        "en": """Prepare a manager-facing summary of a four-week pilot without hiding subgroup differences or study limitations. The pilot involved 75 employees across Departments A, B, and C. Thirty employees were from A, 25 from B, and 20 from C. Across all participants, average task-completion time improved by 10 percent compared with the four weeks immediately before the pilot. Department A improved by 14 percent, Department B improved by 9 percent, and Department C showed no measurable improvement. Overall error rates declined from 4.0 percent to 3.5 percent, but the pilot team has not yet tested whether that change is statistically distinguishable from normal variation. Support requests increased sharply during the first week, were still above baseline in week two, and returned approximately to the previous baseline by week three. Participants received a two-hour training session before the pilot. Department C scheduled its training at the end of a busy reporting period and had the lowest attendance rate at 65 percent; the other two departments exceeded 90 percent attendance. The pilot did not randomly assign employees to use or not use the new workflow, and there was no concurrent control group. Managers knew the pilot was being evaluated. Satisfaction averaged 4.1 out of 5 overall, but Department C averaged 3.4. No staff reductions occurred during the pilot. The study covers only four weeks, so the team has no evidence yet about long-term retention, seasonal workloads, or whether support demand will remain at baseline. The summary should distinguish observed outcomes from possible explanations and should not claim that training attendance caused Department C's result.""",
        "bn": """চার সপ্তাহের পরীক্ষামূলক কার্যক্রমের ব্যবস্থাপক-উপযোগী সারাংশ তৈরি করুন; বিভাগভিত্তিক পার্থক্য ও গবেষণার সীমাবদ্ধতা আড়াল করবেন না। পরীক্ষায় A, B ও C—এই তিন বিভাগের মোট ৭৫ কর্মী অংশ নেন। A থেকে ৩০, B থেকে ২৫ এবং C থেকে ২০ জন ছিলেন। সব অংশগ্রহণকারী মিলিয়ে পরীক্ষার আগের চার সপ্তাহের তুলনায় গড় কাজ-সম্পন্ন সময় ১০ শতাংশ উন্নত হয়েছে। A বিভাগে উন্নতি ১৪ শতাংশ, B-তে ৯ শতাংশ, আর C-তে পরিমাপযোগ্য উন্নতি পাওয়া যায়নি। সামগ্রিক ত্রুটির হার ৪.০ শতাংশ থেকে ৩.৫ শতাংশে নেমেছে, কিন্তু এই পরিবর্তন স্বাভাবিক ওঠানামা থেকে পরিসংখ্যানগতভাবে আলাদা কি না দল এখনো পরীক্ষা করেনি। প্রথম সপ্তাহে সহায়তা অনুরোধ অনেক বেড়েছিল, দ্বিতীয় সপ্তাহেও আগের চেয়ে বেশি ছিল এবং তৃতীয় সপ্তাহে প্রায় আগের পর্যায়ে ফিরে আসে। পরীক্ষার আগে অংশগ্রহণকারীদের দুই ঘণ্টার প্রশিক্ষণ দেওয়া হয়। C বিভাগের প্রশিক্ষণ ব্যস্ত রিপোর্টিং সময়ের শেষে হয়েছিল এবং সেখানে উপস্থিতির হার ছিল সবচেয়ে কম—৬৫ শতাংশ; অন্য দুই বিভাগে ৯০ শতাংশের বেশি। কর্মীদের এলোমেলোভাবে নতুন ও পুরোনো পদ্ধতিতে ভাগ করা হয়নি এবং একই সময়ে কোনো নিয়ন্ত্রণ দল ছিল না। ব্যবস্থাপকরা জানতেন যে পরীক্ষাটি মূল্যায়ন করা হচ্ছে। সামগ্রিক সন্তুষ্টির গড় ৫-এর মধ্যে ৪.১, কিন্তু C বিভাগের গড় ৩.৪। পরীক্ষার সময়ে কর্মীসংখ্যা কমানো হয়নি। গবেষণাটি মাত্র চার সপ্তাহের, তাই দীর্ঘমেয়াদি দক্ষতা ধরে রাখা, মৌসুমি কাজের চাপ বা সহায়তা অনুরোধ ভবিষ্যতেও আগের পর্যায়ে থাকবে কি না সে বিষয়ে প্রমাণ নেই। সারাংশে পর্যবেক্ষিত ফল ও সম্ভাব্য ব্যাখ্যা আলাদা রাখতে হবে এবং প্রশিক্ষণে উপস্থিতির হারই C বিভাগের ফলের কারণ—এমন দাবি করা যাবে না।""",
    },
    "SYN096": {
        "en": """Create a decision brief that compares the available procurement options against the stated constraints rather than simply selecting the option with the most features. Option A costs $20,000, can be deployed in two weeks, supports all mandatory requirements, and lacks one preferred reporting feature. The vendor says that preferred feature may be added later, but no date is committed. Option B costs $28,000, includes all mandatory and preferred features, and requires approximately six weeks for deployment. Option C costs $23,500 and could be deployed in four weeks, but one mandatory integration is currently available only through a beta connector. The approved project budget is capped at $25,000 unless a vice president authorizes an exception. The preferred reporting feature is explicitly classified as desirable rather than mandatory. The current system can remain in service for two more months, although support tickets have increased by 15 percent during the past quarter. A separate security review found no critical findings for A or B; C's beta connector has not yet completed the organization's security review. Procurement reports that Vendor A offers a one-year price guarantee, Vendor B offers three years, and Vendor C has not committed to future pricing. The operations team prefers deployment within one month but has said six weeks is tolerable if there is a strong justification. No option has yet been tested with the organization's full production data volume. The brief should identify which constraints each option satisfies or violates, distinguish mandatory requirements from preferences, and identify unresolved evidence that a decision-maker should consider before approval.""",
        "bn": """শুধু সবচেয়ে বেশি বৈশিষ্ট্য আছে এমন বিকল্প বেছে না নিয়ে ঘোষিত সীমাবদ্ধতার সঙ্গে তিনটি ক্রয়-বিকল্প তুলনা করে একটি সিদ্ধান্ত-সংক্ষিপ্ত নোট তৈরি করুন। বিকল্প A-এর খরচ ২০,০০০ ডলার, দুই সপ্তাহে ডিপ্লয় করা যায়, সব বাধ্যতামূলক শর্ত পূরণ করে, কিন্তু একটি পছন্দনীয় রিপোর্টিং বৈশিষ্ট্য নেই। বিক্রেতা বলেছে বৈশিষ্ট্যটি পরে যোগ হতে পারে, তবে কোনো তারিখ নিশ্চিত করা হয়নি। বিকল্প B-এর খরচ ২৮,০০০ ডলার, সব বাধ্যতামূলক ও পছন্দনীয় বৈশিষ্ট্য আছে এবং ডিপ্লয়মেন্টে প্রায় ছয় সপ্তাহ লাগে। বিকল্প C-এর খরচ ২৩,৫০০ ডলার এবং চার সপ্তাহে ডিপ্লয় করা সম্ভব, কিন্তু একটি বাধ্যতামূলক ইন্টিগ্রেশন এখন কেবল বেটা কানেক্টরের মাধ্যমে পাওয়া যায়। অনুমোদিত প্রকল্প বাজেট সর্বোচ্চ ২৫,০০০ ডলার; এর বেশি হলে ভাইস প্রেসিডেন্টের ব্যতিক্রমী অনুমোদন লাগবে। পছন্দনীয় রিপোর্টিং বৈশিষ্ট্যটি স্পষ্টভাবে ‘ভালো হলে ভালো’ হিসেবে চিহ্নিত, বাধ্যতামূলক নয়। বর্তমান সিস্টেম আরও দুই মাস ব্যবহার করা যাবে, যদিও গত ত্রৈমাসিকে সহায়তা টিকিট ১৫ শতাংশ বেড়েছে। আলাদা নিরাপত্তা পর্যালোচনায় A ও B-তে কোনো গুরুতর সমস্যা পাওয়া যায়নি; C-এর বেটা কানেক্টর এখনো প্রতিষ্ঠানের নিরাপত্তা পর্যালোচনা শেষ করেনি। ক্রয় বিভাগ জানিয়েছে A-এর বিক্রেতা এক বছরের দাম-নিশ্চয়তা দেয়, B তিন বছরের এবং C ভবিষ্যৎ দামের বিষয়ে কোনো নিশ্চয়তা দেয়নি। অপারেশন দল এক মাসের মধ্যে ডিপ্লয়মেন্ট পছন্দ করে, তবে শক্ত যুক্তি থাকলে ছয় সপ্তাহও গ্রহণযোগ্য বলেছে। কোনো বিকল্পই এখনো প্রতিষ্ঠানের পূর্ণ প্রোডাকশন ডেটা-ভলিউম দিয়ে পরীক্ষা করা হয়নি। নোটে কোন বিকল্প কোন সীমা পূরণ বা লঙ্ঘন করছে তা দেখাতে হবে, বাধ্যতামূলক শর্ত ও পছন্দ আলাদা করতে হবে এবং অনুমোদনের আগে কোন প্রমাণ এখনো অনির্ধারিত তা চিহ্নিত করতে হবে।""",
    },
    "SYN097": {
        "en": """Summarize the operational situation for incident leadership and explicitly separate observations from possible causes. On Monday the service processed 20 percent more requests than the average Monday during the previous eight weeks. Median response time increased from 4 minutes to 7 minutes between 10:15 AM and 12:40 PM. Staffing was at the normal Monday level, and no scheduled staff absence was recorded. One internal case-routing tool was intermittently unavailable during parts of the same period. Monitoring shows three tool interruptions lasting 6, 11, and 4 minutes, but the slower response time continued for more than 30 minutes after the final recorded interruption. The queue of unassigned cases reached 86 at 11:20 AM; the normal Monday peak is approximately 45. A database dashboard showed CPU utilization within its usual range, while one application server briefly reached 88 percent memory utilization. No application crash was recorded. At 11:35 AM supervisors temporarily reassigned four employees from nonurgent work to the queue, and the backlog began declining at 12:05 PM. Response time returned below 5 minutes by 1:10 PM. No configuration deployment occurred Monday morning. A network-maintenance event occurred Sunday night and was reported complete before 5:00 AM Monday; no evidence currently links it to the slowdown. The routing-tool team is still investigating its interruptions. The available observations support several plausible contributors—including higher volume and tool instability—but do not establish one verified root cause. The summary must not state that the internal tool, staffing, database, application server, or Sunday maintenance caused the slowdown unless the evidence above actually supports that conclusion.""",
        "bn": """ইনসিডেন্ট নেতৃত্বের জন্য কার্যগত পরিস্থিতি সংক্ষেপ করুন এবং পর্যবেক্ষিত তথ্যকে সম্ভাব্য কারণ থেকে স্পষ্টভাবে আলাদা রাখুন। সোমবার সেবাটি আগের আট সপ্তাহের গড় সোমবারের তুলনায় ২০ শতাংশ বেশি অনুরোধ প্রক্রিয়াকরণ করেছে। সকাল ১০টা ১৫ মিনিট থেকে দুপুর ১২টা ৪০ মিনিটের মধ্যে মধ্যম প্রতিক্রিয়া সময় ৪ মিনিট থেকে ৭ মিনিটে বেড়েছে। কর্মীসংখ্যা স্বাভাবিক সোমবারের মতো ছিল এবং নির্ধারিত কোনো অনুপস্থিতি ছিল না। একই সময়ের কিছু অংশে একটি অভ্যন্তরীণ কেস-রাউটিং টুল মাঝে মাঝে অপ্রাপ্য ছিল। পর্যবেক্ষণ ব্যবস্থায় যথাক্রমে ৬, ১১ ও ৪ মিনিটের তিনটি টুল-বিঘ্ন দেখা গেছে, তবে শেষ বিঘ্ন শেষ হওয়ার পরও ৩০ মিনিটের বেশি সময় প্রতিক্রিয়া ধীর ছিল। সকাল ১১টা ২০ মিনিটে অর্পণ না করা কেসের সারি ৮৬-তে পৌঁছায়; সাধারণ সোমবারে সর্বোচ্চ প্রায় ৪৫ থাকে। একটি ডেটাবেস ড্যাশবোর্ডে CPU ব্যবহার স্বাভাবিক সীমায় ছিল, আর একটি অ্যাপ্লিকেশন সার্ভারে অল্প সময়ের জন্য মেমরি ব্যবহার ৮৮ শতাংশে পৌঁছায়। কোনো অ্যাপ্লিকেশন ক্র্যাশ রেকর্ড হয়নি। সকাল ১১টা ৩৫ মিনিটে সুপারভাইজাররা কম জরুরি কাজ থেকে চার কর্মীকে সাময়িকভাবে কেসের সারিতে দেন এবং দুপুর ১২টা ০৫ মিনিটে জমে থাকা কাজ কমতে শুরু করে। দুপুর ১টা ১০ মিনিটের মধ্যে প্রতিক্রিয়া সময় আবার ৫ মিনিটের নিচে আসে। সোমবার সকালে কোনো কনফিগারেশন ডিপ্লয়মেন্ট হয়নি। রবিবার রাতে নেটওয়ার্ক রক্ষণাবেক্ষণ হয়েছিল এবং সোমবার ভোর ৫টার আগেই তা সম্পন্ন বলে জানানো হয়; বর্তমান প্রমাণে সেটির সঙ্গে ধীরগতির যোগসূত্র পাওয়া যায়নি। রাউটিং টুলের দল এখনো বিঘ্নের কারণ তদন্ত করছে। পাওয়া পর্যবেক্ষণ উচ্চ কাজের পরিমাণ ও টুলের অস্থিতিশীলতাসহ কয়েকটি সম্ভাব্য অবদানকারী কারণের সঙ্গে সামঞ্জস্যপূর্ণ, কিন্তু একটি নিশ্চিত মূল কারণ প্রতিষ্ঠা করে না। উপরের প্রমাণ সমর্থন না করলে সারাংশে টুল, কর্মীসংখ্যা, ডেটাবেস, অ্যাপ্লিকেশন সার্ভার বা রবিবারের রক্ষণাবেক্ষণকে ধীরগতির কারণ বলা যাবে না।""",
    },
    "SYN098": {
        "en": """Produce a structured migration brief with four sections: verified facts, current risks, unknowns, and immediate decision points. The migration is reported as 90 percent complete by table count. All completed tables have matching source and destination record counts, and sampled checksums match for the completed high-priority tables. One large transaction-history table remains. That table contains approximately 38 percent of the total rows in the source database even though it is only one of the remaining tables. The maintenance window ends in three hours. The migration team estimates that copying the remaining table could take between 70 and 110 minutes based on a staging test, but staging held only about 60 percent of the production row count. Post-copy validation requires at least 25 minutes if no discrepancy is found. A full rollback would take approximately two hours after the rollback decision, and the rollback procedure has been tested once this quarter. The team did not define a formal rollback decision threshold before maintenance began. Source writes are currently paused. The business owner can tolerate up to 30 minutes of service degradation after the maintenance window but has not approved an extension beyond that. The application team needs at least 20 minutes after database validation to complete its own smoke tests. No data-loss indicator is currently present. One engineer has raised concern that the remaining table contains a type of index that slowed the staging migration, but the production effect has not been measured. The vendor is available by phone for the next 90 minutes. The brief must make the timing dependency visible: waiting too long to decide can reduce the time available for either validation or rollback. Do not invent a go/no-go threshold; identify the missing threshold itself as a governance risk.""",
        "bn": """মাইগ্রেশন পরিস্থিতির একটি কাঠামোবদ্ধ ব্রিফ তৈরি করুন, যেখানে চারটি অংশ থাকবে: যাচাইকৃত তথ্য, বর্তমান ঝুঁকি, অজানা বিষয় এবং তাৎক্ষণিক সিদ্ধান্তের জায়গা। টেবিলের সংখ্যা অনুযায়ী মাইগ্রেশন ৯০ শতাংশ সম্পন্ন বলা হয়েছে। সম্পন্ন সব টেবিলে উৎস ও গন্তব্যের রেকর্ড সংখ্যা মিলেছে এবং সম্পন্ন উচ্চ-অগ্রাধিকার টেবিলগুলোর নমুনা চেকসমও মিলেছে। একটি বড় লেনদেন-ইতিহাস টেবিল এখনো বাকি। টেবিলটি অবশিষ্ট টেবিলের মাত্র একটি হলেও উৎস ডেটাবেসের মোট সারির প্রায় ৩৮ শতাংশ এতে আছে। রক্ষণাবেক্ষণের সময় শেষ হতে তিন ঘণ্টা বাকি। স্টেজিং পরীক্ষার ভিত্তিতে বাকি টেবিল কপি করতে ৭০ থেকে ১১০ মিনিট লাগতে পারে বলে দলের অনুমান, কিন্তু স্টেজিংয়ে প্রোডাকশনের সারির মাত্র প্রায় ৬০ শতাংশ ছিল। কপি শেষ হওয়ার পর কোনো অমিল না থাকলেও যাচাইয়ে অন্তত ২৫ মিনিট লাগবে। রোলব্যাকের সিদ্ধান্ত নেওয়ার পর পূর্ণ রোলব্যাক করতে প্রায় দুই ঘণ্টা লাগবে এবং এই ত্রৈমাসিকে রোলব্যাক পদ্ধতি একবার পরীক্ষা করা হয়েছে। রক্ষণাবেক্ষণ শুরুর আগে দল আনুষ্ঠানিক কোনো রোলব্যাক সিদ্ধান্তসীমা নির্ধারণ করেনি। উৎসে নতুন লেখা বর্তমানে বন্ধ। ব্যবসায়িক মালিক রক্ষণাবেক্ষণ সময় শেষ হওয়ার পর সর্বোচ্চ ৩০ মিনিট সেবা-অবনতি সহ্য করতে পারবেন, কিন্তু এর বেশি সময় বাড়ানোর অনুমোদন দেননি। ডেটাবেস যাচাইয়ের পর অ্যাপ্লিকেশন দলের নিজস্ব স্মোক টেস্টে অন্তত ২০ মিনিট লাগবে। বর্তমানে কোনো ডেটা-ক্ষতির সূচক নেই। একজন প্রকৌশলী উদ্বেগ জানিয়েছেন যে বাকি টেবিলে এমন একটি ইনডেক্স আছে যা স্টেজিং মাইগ্রেশন ধীর করেছিল, কিন্তু প্রোডাকশনে এর প্রভাব মাপা হয়নি। ভেন্ডর পরবর্তী ৯০ মিনিট ফোনে পাওয়া যাবে। ব্রিফে সময়ের নির্ভরতা স্পষ্ট করতে হবে: সিদ্ধান্ত নিতে বেশি দেরি করলে যাচাই বা রোলব্যাক—যেকোনোটির জন্য সময় কমে যেতে পারে। নিজের মতো go/no-go সীমা তৈরি করবেন না; বরং এমন সীমা আগে নির্ধারিত না থাকাকেই একটি শাসন-ঝুঁকি হিসেবে চিহ্নিত করুন।""",
    },
    "SYN099": {
        "en": """Write a balanced research synthesis that preserves subgroup findings and methodological limitations. Model X achieved 84 percent overall accuracy and Model Y achieved 80 percent on the same held-out test set of 6,000 items. The test set contains four language groups. The largest group represents 52 percent of the items, while the smallest language group represents only 6 percent. On the smallest group, Model Y scored 71 percent and Model X scored 64 percent. On the largest group, X scored 88 percent and Y scored 82 percent. The remaining two groups show differences of less than three percentage points. The researchers report bootstrap confidence intervals for overall accuracy, and those intervals do not overlap, but they did not report subgroup confidence intervals. Both models used the same decoding settings. Model X has approximately twice as many parameters as Model Y. The study reports no latency, memory-use, energy, or inference-cost comparison. Human annotators created the reference labels, and a second annotator independently reviewed 20 percent of the test set. Agreement on that reviewed subset was 91 percent. The paper does not report whether disagreement rates differed by language group. The smallest language group also contains a higher proportion of long-form items than the overall test set. The authors state that X has higher overall accuracy and that Y performs better on the smallest language group; those descriptive statements are supported by the reported scores. However, the available evidence does not establish why the subgroup reversal occurs, whether it would persist in a larger sample, or which model is preferable for deployment. The synthesis should not collapse the overall and subgroup results into a single winner.""",
        "bn": """ভাষাভিত্তিক ফল এবং পদ্ধতিগত সীমাবদ্ধতা অক্ষুণ্ন রেখে ভারসাম্যপূর্ণ গবেষণা-সংশ্লেষ লিখুন। একই ৬,০০০ আইটেমের আলাদা রাখা পরীক্ষামূলক সেটে Model X-এর সামগ্রিক নির্ভুলতা ৮৪ শতাংশ এবং Model Y-এর ৮০ শতাংশ। পরীক্ষামূলক সেটে চারটি ভাষা-দল আছে। সবচেয়ে বড় দল মোট আইটেমের ৫২ শতাংশ, আর সবচেয়ে ছোট ভাষা-দল মাত্র ৬ শতাংশ। সবচেয়ে ছোট দলে Y-এর স্কোর ৭১ শতাংশ এবং X-এর ৬৪ শতাংশ। সবচেয়ে বড় দলে X ৮৮ শতাংশ এবং Y ৮২ শতাংশ পেয়েছে। বাকি দুই দলে পার্থক্য তিন শতাংশ-পয়েন্টের কম। গবেষকেরা সামগ্রিক নির্ভুলতার জন্য bootstrap confidence interval দিয়েছেন এবং সেগুলো একে অপরের সঙ্গে ওভারল্যাপ করে না, কিন্তু ভাষাভিত্তিক confidence interval দেননি। দুই মডেলেই একই decoding settings ব্যবহার করা হয়েছে। Model X-এর parameter সংখ্যা Y-এর প্রায় দ্বিগুণ। গবেষণায় latency, memory use, energy বা inference cost-এর তুলনা নেই। মানব annotator-রা reference label তৈরি করেছেন এবং দ্বিতীয় annotator পরীক্ষামূলক সেটের ২০ শতাংশ স্বাধীনভাবে পর্যালোচনা করেছেন। ওই অংশে agreement ছিল ৯১ শতাংশ। ভাষা-দলভেদে disagreement rate আলাদা ছিল কি না তা প্রতিবেদনে নেই। সবচেয়ে ছোট ভাষা-দলে দীর্ঘ উত্তর-প্রয়োজন এমন আইটেমের অনুপাতও পুরো পরীক্ষামূলক সেটের তুলনায় বেশি। লেখকেরা বলেছেন X-এর সামগ্রিক নির্ভুলতা বেশি এবং সবচেয়ে ছোট ভাষা-দলে Y ভালো করেছে; প্রকাশিত স্কোর এই বর্ণনামূলক দাবিগুলো সমর্থন করে। তবে কেন ভাষাভিত্তিক ফল উল্টে গেছে, বড় নমুনাতেও এটি থাকবে কি না, অথবা ডিপ্লয়মেন্টের জন্য কোন মডেল বেশি উপযোগী—এসব বর্তমান প্রমাণে প্রতিষ্ঠিত নয়। সংশ্লেষে সামগ্রিক ও ভাষাভিত্তিক ফল একত্র করে একটিমাত্র ‘বিজয়ী’ ঘোষণা করা যাবে না।""",
    },
    "SYN100": {
        "en": """Create an executive-ready synthesis that reports gains, trade-offs, implementation context, and evidence limits without dropping caveats. During the first eight weeks after launch, the new case-management system processed 2,400 completed cases. Average processing time was 16 percent lower than during the eight weeks immediately before launch. The measured error rate declined from 3.1 percent to 2.6 percent. At the same time, average staff satisfaction fell from 4.1 to 3.6 on a five-point survey scale. The pre-launch survey had an 81 percent response rate and the post-launch survey had a 68 percent response rate. Staff received two days of formal training, although 14 percent of staff missed at least half a day because of scheduling conflicts. Help-desk requests about the new system were highest in weeks one and two and then declined each week through week eight. The organization added two temporary implementation specialists during the first six weeks; they are not part of the normal staffing model. Monthly software licensing cost is 12 percent higher than the previous system, while infrastructure cost is 8 percent lower. The finance team has not yet calculated total cost of ownership because support labor and future upgrade costs are incomplete. Two departments adopted the new workflow fully by week three, while a third continued using a hybrid old/new workflow through week six. The processing-time improvement is therefore an observed system-period association rather than a clean causal estimate of the software alone. No critical outage occurred during the eight-week evaluation period, but the previous system also had no critical outage during its final eight weeks. The evaluation contains no data on long-term retention, annual peak workload, future satisfaction, or performance after the temporary specialists leave. The executive synthesis should clearly state what improved, what worsened, what remains unknown, and why the short observation period and implementation differences limit causal conclusions.""",
        "bn": """উন্নতি, বিনিময়মূলক প্রভাব, বাস্তবায়নের প্রেক্ষাপট এবং প্রমাণের সীমা—সবকিছু সতর্কতা বাদ না দিয়ে নির্বাহী-উপযোগী সংশ্লেষে উপস্থাপন করুন। চালুর পর প্রথম আট সপ্তাহে নতুন কেস-ম্যানেজমেন্ট সিস্টেম ২,৪০০টি সম্পন্ন কেস প্রক্রিয়াকরণ করেছে। চালুর আগের ঠিক আট সপ্তাহের তুলনায় গড় প্রক্রিয়াকরণ সময় ১৬ শতাংশ কম ছিল। পরিমাপ করা ত্রুটির হার ৩.১ শতাংশ থেকে ২.৬ শতাংশে নেমেছে। একই সময়ে কর্মীদের গড় সন্তুষ্টি পাঁচ-পয়েন্ট স্কেলে ৪.১ থেকে ৩.৬-এ নেমেছে। চালুর আগের জরিপে সাড়া ছিল ৮১ শতাংশ এবং পরের জরিপে ৬৮ শতাংশ। কর্মীরা দুই দিনের আনুষ্ঠানিক প্রশিক্ষণ পেয়েছেন, তবে সময়সূচি-সংঘাতের কারণে ১৪ শতাংশ কর্মী অন্তত অর্ধদিন প্রশিক্ষণ মিস করেছেন। নতুন সিস্টেম নিয়ে হেল্প-ডেস্ক অনুরোধ প্রথম ও দ্বিতীয় সপ্তাহে সবচেয়ে বেশি ছিল এবং এরপর অষ্টম সপ্তাহ পর্যন্ত প্রতি সপ্তাহে কমেছে। প্রথম ছয় সপ্তাহে প্রতিষ্ঠান দুইজন অস্থায়ী বাস্তবায়ন বিশেষজ্ঞ যোগ করেছিল; তাঁরা স্বাভাবিক কর্মী কাঠামোর অংশ নন। মাসিক সফটওয়্যার লাইসেন্সিং খরচ আগের সিস্টেমের তুলনায় ১২ শতাংশ বেশি, আর অবকাঠামো খরচ ৮ শতাংশ কম। সহায়তা-শ্রম ও ভবিষ্যৎ আপগ্রেড খরচ অসম্পূর্ণ থাকায় অর্থ বিভাগ এখনো মোট মালিকানা-খরচ হিসাব করেনি। দুই বিভাগ তৃতীয় সপ্তাহের মধ্যে নতুন কার্যপ্রবাহ পুরোপুরি গ্রহণ করেছে, আর তৃতীয় বিভাগ ষষ্ঠ সপ্তাহ পর্যন্ত পুরোনো ও নতুন পদ্ধতির মিশ্র ব্যবহার করেছে। তাই প্রক্রিয়াকরণ সময়ের উন্নতি একটি পর্যবেক্ষিত সিস্টেম-সময়কাল সম্পর্ক; কেবল সফটওয়্যারের পরিষ্কার কারণগত প্রভাব বলা যায় না। আট সপ্তাহে কোনো গুরুতর বিভ্রাট হয়নি, তবে আগের সিস্টেমের শেষ আট সপ্তাহেও গুরুতর বিভ্রাট ছিল না। দীর্ঘমেয়াদি দক্ষতা ধরে রাখা, বার্ষিক সর্বোচ্চ কাজের চাপ, ভবিষ্যৎ সন্তুষ্টি বা অস্থায়ী বিশেষজ্ঞরা চলে যাওয়ার পর কর্মক্ষমতা—এসব বিষয়ে কোনো তথ্য নেই। নির্বাহী সংশ্লেষে কী উন্নত হয়েছে, কী খারাপ হয়েছে, কী অজানা এবং কেন স্বল্প পর্যবেক্ষণকাল ও ভিন্ন বাস্তবায়ন-পদ্ধতি কারণগত সিদ্ধান্ত সীমিত করে—তা স্পষ্টভাবে বলতে হবে।""",
    },
}


def apply_extended_context(row: dict[str, str]) -> None:
    replacement = EXTENDED_CONTEXT.get(row["task_id"])
    if not replacement:
        return
    row["subdomain"] = "extended_context"
    row["prompt_en"] = replacement["en"]
    row["prompt_bn"] = replacement["bn"]


def revise_file(path: Path) -> int:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        rows = list(reader)

    expected_fields = [
        "task_id",
        "domain",
        "subdomain",
        "difficulty",
        "prompt_en",
        "prompt_bn",
        "prompt_bn_cs",
    ]
    if fieldnames != expected_fields:
        raise ValueError(f"Unexpected schema in {path}: {fieldnames}")

    for row in rows:
        if row["task_id"] in DIFFICULTY_TO_MEDIUM:
            row["difficulty"] = "medium"

        apply_extended_context(row)
        row["prompt_bn"] = normalize_bn(row["prompt_en"], row["prompt_bn"])
        row["prompt_bn_cs"] = make_code_switched(row["prompt_bn"], row["domain"])

        # Normalize accidental repeated whitespace introduced by replacements,
        # without altering punctuation or semantic content.
        for key in ("prompt_en", "prompt_bn", "prompt_bn_cs"):
            row[key] = re.sub(r"[ \t]+", " ", row[key]).strip()

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=expected_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    return len(rows)


def main() -> None:
    total = 0
    for filename in PROMPT_FILES:
        path = PROMPT_DIR / filename
        if not path.exists():
            raise FileNotFoundError(path)
        count = revise_file(path)
        total += count
        print(f"Revised {filename}: {count} rows")

    if total != 500:
        raise RuntimeError(f"Expected 500 prompt rows, found {total}")

    print(f"Corpus v0.2 revision complete: {total} tasks / {total * 3} prompt instances")


if __name__ == "__main__":
    import sys
    if "--force-historical" not in sys.argv:
        raise SystemExit(
            "Historical v0.2 corpus script: running it would overwrite the hand-written v0.3 "
            "Bengali conditions. See data/prompts/CORPUS_CHANGELOG.md. Pass --force-historical "
            "only to reproduce v0.2 on a separate checkout."
        )
    sys.argv.remove("--force-historical")
    main()
