# Title: HP ILO command line
<!-- Position: 1 -->
---
This commands are for the HP ILO connected via SSH or via the OA and into the ILO.

Create a new user.
```
$ create /map1/accounts1 username={NEW_USERNAME} password={NEW_PASSWORD}
```

Set password to user.
```
$ set /map1/accounts1/{USERNAME} password={NEW_PASSWORD}
```

Grant permissions to the user.
```
$ set /map1/accounts1/{USERNAME} group=admin,config,oemhp_rc,oemhp_power,oemhp_vm
```

Set ILO server name.
```
$ set /system1 oemhp_server_name={NEW_BLADE_SERVER_NAME}
```

Set ILO hostname / system name, this command reboot the ILO.
```
$ set /map1/enetport1 SystemName={NEW_BLADE_SYSTEM_NAME}
```

Set ILO Gateway.
```
$ set /map1/gateway1/ AccessInfo={GATEWAY}
```
