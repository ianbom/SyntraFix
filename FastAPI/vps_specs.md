(base) sinopsis@Ollama4:~$ lscpu
Architecture:                x86_64
  CPU op-mode(s):            32-bit, 64-bit
  Address sizes:             40 bits physical, 48 bits virtual
  Byte Order:                Little Endian
CPU(s):                      2
  On-line CPU(s) list:       0,1
Vendor ID:                   GenuineIntel
  Model name:                QEMU Virtual CPU version 2.5+
    CPU family:              15
    Model:                   107
    Thread(s) per core:      1
    Core(s) per socket:      2
    Socket(s):               1
    Stepping:                1
    BogoMIPS:                4190.16
    Flags:                   fpu de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse
                             2 ht syscall nx lm constant_tsc nopl xtopology cpuid tsc_known_freq pni ssse3 cx16 sse4_1 ss
                             e4_2 x2apic popcnt aes hypervisor lahf_lm cpuid_fault pti
Virtualization features:
  Hypervisor vendor:         KVM
  Virtualization type:       full
Caches (sum of all):
  L1d:                       64 KiB (2 instances)
  L1i:                       64 KiB (2 instances)
  L2:                        8 MiB (2 instances)
  L3:                        16 MiB (1 instance)
NUMA:
  NUMA node(s):              1
  NUMA node0 CPU(s):         0,1
Vulnerabilities:
  Gather data sampling:      Not affected
  Indirect target selection: Mitigation; Aligned branch/return thunks
  Itlb multihit:             KVM: Mitigation: VMX unsupported
  L1tf:                      Mitigation; PTE Inversion
  Mds:                       Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown
  Meltdown:                  Mitigation; PTI
  Mmio stale data:           Unknown: No mitigations
  Reg file data sampling:    Not affected
  Retbleed:                  Not affected
  Spec rstack overflow:      Not affected
  Spec store bypass:         Vulnerable
  Spectre v1:                Mitigation; usercopy/swapgs barriers and __user pointer sanitization
  Spectre v2:                Mitigation; Retpolines; STIBP disabled; RSB filling; PBRSB-eIBRS Not affected; BHI Retpoline
  Srbds:                     Not affected
  Tsa:                       Not affected
  Tsx async abort:           Not affected
  Vmscape:                   Not affected
(base) sinopsis@Ollama4:~$ free -h
               total        used        free      shared  buff/cache   available
Mem:            15Gi       2.4Gi       160Mi        32Mi        13Gi        13Gi
Swap:          974Mi       974Mi          0B
(base) sinopsis@Ollama4:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            7.8G     0  7.8G   0% /dev
tmpfs           1.6G  680K  1.6G   1% /run
/dev/sda1       125G  111G  7.3G  94% /
tmpfs           7.9G     0  7.9G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           1.6G     0  1.6G   0% /run/user/1001
(base) sinopsis@Ollama4:~$ lspci | grep -i vga
00:02.0 VGA compatible controller: Device 1234:1111 (rev 02)
00:10.0 VGA compatible controller: NVIDIA Corporation GA106 [RTX A2000 12GB] (rev a1)
(base) sinopsis@Ollama4:~$ nvidia-smi
Tue Apr 21 10:42:49 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX A2000 12GB          Off |   00000000:00:10.0 Off |                  Off |
| 42%   65C    P2             43W /   70W |     733MiB /  12282MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A         2262870      C   /usr/local/bin/ollama                   724MiB |
+-----------------------------------------------------------------------------------------+

schema.org