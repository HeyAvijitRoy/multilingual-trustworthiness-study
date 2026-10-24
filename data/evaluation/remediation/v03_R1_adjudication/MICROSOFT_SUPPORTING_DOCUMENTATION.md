# Supporting technical documentation for adjudication

Checked October 24, 2026. These source notes supply technical context; they do not decide the case or add requirements to its frozen prompt or rubric.

Microsoft's [DiskPart `list` documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/list) distinguishes disk, partition and volume inventories. Its `volume` entry states: “Displays a list of basic and dynamic volumes on all disks.” The `disk` entry describes disk size and available free-space information. An adjudication should distinguish these views when considering what the response's proposed command can establish. These descriptions alone do not decide whether an inaccuracy is operationally material in the complete response.

Microsoft's [volume-extension documentation](https://learn.microsoft.com/en-us/windows-server/storage/disk-management/extend-a-basic-volume) explains how Disk Management displays unallocated space and how Extend Volume uses it. Its listed prerequisites include unallocated space immediately following the target volume on the same drive and NTFS or ReFS formatting. An intervening volume can prevent extension. These facts can inform evaluation of the proposed inspection and extension path, subject to the task's actual scope. Do not turn every documented prerequisite into a new required information unit.

The documentation is current supporting evidence, not proof of the date or model origin of a constructed calibration response. Final technical correctness, whole-response materiality and the adjudicated score remain for R1 to record separately.
