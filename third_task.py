# Задание 3. Нахождение сетевых функций в PE-файле.
 
# Разработать программу, которая анализирует структуру PE-файла и 
# находит в нем обращение к сетевым функциям. В результате прорамма 
# дожна автоматически найти все файлы с сетевыми фикциями в указанном каталоге.
# Поиск функций ведется в секции импорта PE файла.

import pefile

network_functions = {
    'DeleteIPAddress',
    'FreeMibTable',
    'GetAdaptersAddresses',
    'GetAnycastIpAddressEntry',
    'GetAnycastIpAddressTable',
    'GetBestRoute2',
    'GetHostNameW',
    'GetIpAddrTable',
    'GetIpStatisticsEx',
    'GetUnicastIpAddressTable',
    'IcmpCloseHandle',
    'IcmpCreateFile',
    'IcmpCloseHandle',
    'IcmpSendEcho',
    'MultinetGetConnectionPerformance',
    'MultinetGetConnectionPerformanceW',
    'NetAlertRaise',
    'NetAlertRaiseEx',
    'NetApiBufferAllocate',
    'NetApiBufferFree',
    'NetApiBufferReallocate',
    'NetApiBufferSize',
    'NetFreeAadJoinInformation',
    'NetGetAadJoinInformation',
    'NetAddAlternateComputerName',
    'NetCreateProvisioningPackage',
    'NetEnumerateComputerNames',
    'NetGetJoinableOUs',
    'NetGetJoinInformation',
    'NetJoinDomain',
    'NetProvisionComputerAccount',
    'NetRemoveAlternateComputerName',
    'NetRenameMachineInDomain',
    'NetRequestOfflineDomainJoin',
    'NetRequestProvisioningPackageInstall',
    'NetSetPrimaryComputerName',
    'NetUnjoinDomain',
    'NetValidateName',
    'NetGetAnyDCName',
    'NetGetDCName',
    'NetGetDisplayInformationIndex',
    'NetQueryDisplayInformation',
    'NetGroupAdd',
    'NetGroupAddUser',
    'NetGroupDel',
    'NetGroupDelUser',
    'NetGroupEnum',
    'NetGroupGetInfo',
    'NetGroupGetUsers',
    'NetGroupSetInfo',
    'NetGroupSetUsers',
    'NetLocalGroupAdd',
    'NetLocalGroupAddMembers',
    'NetLocalGroupDel',
    'NetLocalGroupDelMembers',
    'NetLocalGroupEnum',
    'NetLocalGroupGetInfo',
    'NetLocalGroupGetMembers',
    'NetLocalGroupSetInfo',
    'NetLocalGroupSetMembers',
    'NetMessageBufferSend',
    'NetMessageNameAdd',
    'NetMessageNameDel',
    'NetMessageNameEnum',
    'NetMessageNameGetInfo',
    'NetFileClose',
    'NetFileEnum',
    'NetFileGetInfo',
    'NetRemoteComputerSupports',
    'NetRemoteTOD',
    'NetScheduleJobAdd',
    'NetScheduleJobDel',
    'NetScheduleJobEnum',
    'NetScheduleJobGetInfo',
    'GetNetScheduleAccountInformation',
    'SetNetScheduleAccountInformation',
    'NetServerDiskEnum',
    'NetServerEnum',
    'NetServerGetInfo',
    'NetServerSetInfo',
    'NetServerComputerNameAdd',
    'NetServerComputerNameDel',
    'NetServerTransportAdd',
    'NetServerTransportAddEx',
    'NetServerTransportDel',
    'NetServerTransportEnum',
    'NetWkstaTransportEnum',
    'NetUseAdd',
    'NetUseDel',
    'NetUseEnum',
    'NetUseGetInfo',
    'NetUserAdd',
    'NetUserChangePassword',
    'NetUserDel',
    'NetUserEnum',
    'NetUserGetGroups',
    'NetUserGetInfo',
    'NetUserGetLocalGroups',
    'NetUserSetGroups',
    'NetUserSetInfo',
    'NetUserModalsGet',
    'NetUserModalsSet',
    'NetValidatePasswordPolicyFree',
    'NetValidatePasswordPolicy',
    'NetWkstaGetInfo',
    'NetWkstaSetInfo',
    'NetWkstaUserEnum',
    'NetWkstaUserGetInfo',
    'NetWkstaUserSetInfo',
    'NetAccessAdd',
    'NetAccessCheck',
    'NetAccessDel',
    'NetAccessEnum',
    'NetAccessGetInfo',
    'NetAccessGetUserPerms',
    'NetAccessSetInfo',
    'NetAuditClear',
    'NetAuditRead',
    'NetAuditWrite',
    'NetConfigGet',
    'NetConfigGetAll',
    'NetConfigSet',
    'NetErrorLogClear',
    'NetErrorLogRead',
    'NetErrorLogWrite',
    'NetLocalGroupAddMember',
    'NetLocalGroupDelMember',
    'NetServiceControl',
    'NetServiceEnum',
    'NetServiceGetInfo',
    'NetServiceInstall',
    'NetWkstaTransportAdd',
    'NetWkstaTransportDel',
    'NetpwNameValidate',
    'NetapipBufferAllocate',
    'NetpwPathType',
    'NetApiBufferFree',
    'NetApiBufferAllocate',
    'NetApiBufferReallocate',
    'WNetAddConnection2',
    'WNetAddConnection2W',
    'WNetAddConnection3',
    'WNetAddConnection3W',
    'WNetCancelConnection',
    'WNetCancelConnectionW',
    'WNetCancelConnection2',
    'WNetCancelConnection2W',
    'WNetCloseEnum',
    'WNetCloseEnumW',
    'WNetConnectionDialog',
    'WNetConnectionDialogW',
    'WNetConnectionDialog1',
    'WNetConnectionDialog1W',
    'WNetDisconnectDialog',
    'WNetDisconnectDialogW',
    'WNetDisconnectDialog1',
    'WNetDisconnectDialog1W',
    'WNetEnumResource',
    'WNetEnumResourceW',
    'WNetGetConnection',
    'WNetGetConnectionW',
    'WNetGetLastError',
    'WNetGetLastErrorW',
    'WNetGetNetworkInformation',
    'WNetGetNetworkInformationW',
    'WNetGetProviderName',
    'WNetGetProviderNameW',
    'WNetGetResourceInformation',
    'WNetGetResourceInformationW',
    'WNetGetResourceParent',
    'WNetGetResourceParentW',
    'WNetGetUniversalName',
    'WNetGetUniversalNameW',
    'WNetGetUser',
    'WNetGetUserW',
    'WNetOpenEnum',
    'WNetOpenEnumW',
    'WNetRestoreConnectionW',
    'WNetUseConnection',
    'WNetUseConnectionW'
}

# path = '/home/lynxtail/electronic-workbench.EXE'
# path = '/media/lynxtail/44B014D7B014D172/Game_distr/A Game of Thrones The Board Game/AGameOfThronesTheBoardGame.exe'
# path = '/media/lynxtail/44B014D7B014D172/Program Files (x86)/obs-studio/bin/64bit/obs64.exe'
path = '/media/lynxtail/44B014D7B014D172/Program Files (x86)/Steam/steam.exe'
pe = pefile.PE(path)

# for section in pe.sections:
#     print(section.Name, hex(section.VirtualAddress), hex(section.Misc_VirtualSize), section.SizeOfRawData)

pe.parse_data_directories()
pe.get_import_table()
with open('output.txt', 'w') as f:
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        # print(str(entry.dll))
        f.write(f'{str(entry.dll)}\n')
        for imp in entry.imports:
            # print('\t', hex(imp.address), str(imp.name))
            # print('\t', str(imp.name)[2:-1])
            f.write(f'\t{imp.name} {str(imp.name)[2:-1]}\n')
            if str(imp.name)[2:-1] in network_functions:
                print("FOUND!!!!!1")