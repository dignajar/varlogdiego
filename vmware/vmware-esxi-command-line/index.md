# Title: VMware ESXi command line
<!-- Position: 1 -->
<!-- Tags: VMware, ESXi, Networking, ISCSI, Adapters -->
<!-- Date: 2016-03-10 18:20:00 -->
---
## Virtual machines

Show all virtual machines on the ESXi
```
$ vim-cmd vmsvc/getallvms
```

## Networking

List all VLANs names and ID
```
$ esxcli network vswitch standard portgroup list
```

Create a VLAN
```
$ esxcli network vswitch standard portgroup add -p "{VLAN-NAME}" -v {Virtual Switch}
$ esxcli network vswitch standard portgroup set -p "{VLAN-NAME}" --vlan-id {VLAN-ID}
```

```
# Example
$ esxcli network vswitch standard portgroup add -p "VLAN10" -v vSwitch0
$ esxcli network vswitch standard portgroup set -p "VLAN10" --vlan-id 10
```

<!-- pagebreak -->

## ISCSI

Enable ISCSI
```
$ esxcli iscsi software set -e true
```

List adapters
```
$ esxcli iscsi adapter list

Adapter  Driver     State   UID            Description
-------  ---------  ------  -------------  ----------------------------------------
vmhba33  iscsi_vmk  online  iscsi.vmhba33  iSCSI Software Adapter
```

Adapter information
```
$ esxcli iscsi adapter get -A {ADAPTER-NAME}
```

```
# Example
$ esxcli iscsi adapter get -A vmhba33
vmhba33
   Name: iqn.1998-01.com.vmware:esxi-a3333
   Alias:
   Vendor: VMware
   Model: iSCSI Software Adapter
   Description: iSCSI Software Adapter
   Serial Number:
   Hardware Version:
   Asic Version:
   Firmware Version:
   Option Rom Version:
   Driver Name: iscsi_vmk
   Driver Version:
   TCP Protocol Supported: false
   Bidirectional Transfers Supported: false
   Maximum Cdb Length: 64
   Can Be NIC: false
   Is NIC: false
   Is Initiator: true
   Is Target: false
   Using TCP Offload Engine: false
   Using ISCSI Offload Engine: false
```

Set adapter name (IQN)
```
$ esxcli iscsi adapter set --adapter={ADAPTER-NAME} --name={IQN-NAME}
```

```
# Example
$ esxcli iscsi adapter set --adapter=vmhba33 --name=iqn.1998-01.com.vmware:esxi-a3333
```

List dynamic IP for discovery
```
$ esxcli iscsi adapter discovery sendtarget list
```

Add discovery dynamic IP
```
$ esxcli iscsi adapter discovery sendtarget add --address={IP:PORT} --adapter={ADAPTER-ISCSI}
```

```
# Example
$ esxcli iscsi adapter discovery sendtarget add --address=10.20.20.1:3260 --adapter=vmhba33
```

Rescan
```
$ esxcli iscsi adapter discovery rediscover -A {ADAPTER-NAME}
```

```
# Example
$ esxcli iscsi adapter discovery rediscover -A vmhba33
```

## Suppress Shell Warning
```
ESXi->Configuration->Advanced Settings->UserVars->SuppressShellWarning, 0 to 1.
```
