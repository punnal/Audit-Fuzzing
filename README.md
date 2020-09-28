# Audit-Fuzzing
Using different tools to fuzz audit deamon

## Getting Syzkaller
This will be used to fuzz the linux kernel

Download syzkaller can be set up from [here](https://github.com/google/syzkaller)

Replace executor.cc in syzkaller/executor/ directory with this [executor.cc](https://github.com/punnal/Audit-Fuzzing/tree/master/syzkaller/syz-executor)
Build syzkaller

## Setup
Setup QEMU as described [here](https://github.com/google/syzkaller/blob/master/docs/linux/setup_ubuntu-host_qemu-vm_x86-64-kernel.md#qemu)
Install Ubuntu 20.04 LTS version on virtual machine.

Get the kernel(5.8.0-rc4) from www.kernel.org

Build the custom kernel using the this [config](https://github.com/punnal/Audit-Fuzzing/blob/master/custom_kernel_config/kernel.config). It enabling some options that syzkaller needs.

Run Ubuntu 20.04 on a virtual machine using qemu. Setup ssh using ssh
keys and then install auditd on it.

Use this [file](https://github.com/punnal/Audit-Fuzzing/blob/master/auditd/audit.rules) as audit.rules.

Use this [file](https://github.com/punnal/Audit-Fuzzing/blob/master/auditd/auditd.conf) as audit.conf.

## Run Syzkaller

Run syzkaller using this [config](https://github.com/punnal/Audit-Fuzzing/tree/master/syzkaller/syzkallerConfig) in debug mode(required to get sequence of systems calls made).
```
./syz-manager -config=syz-ub-all-red.config -debug 

```


