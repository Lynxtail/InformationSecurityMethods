# Задание 3. Нахождение сетевых функций в PE-файле.
 
# Разработать программу, которая анализирует структуру PE-файла и 
# находит в нем обращение к сетевым функциям. В результате прорамма 
# дожна автоматически найти все файлы с сетевыми фикциями в указанном каталоге.
# Поиск функций ведется в секции импорта PE файла.
import os, pefile

NETWORK_FUNCTIONS = {
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
EXTENSIONS = {'.acm', '.ax', '.cpl', '.dll', '.drv', '.efi', '.exe', '.mui', '.ocx', '.scr', '.sys', '.tsp', '.mun',
              '.ACM', '.AX', '.CPL', '.DLL', '.DRV', '.EFI', '.EXE', '.MUI', '.OCX', '.SCR', '.SYS', '.TSP', '.MUN'}

PATH = '/media/lynxtail/521CF7021CF6DFC1/Program Files/7-Zip'           

def find_network_functions(path:str=PATH):
    res = set()
    pe = pefile.PE(path)
    # pe.parse_data_directories()
    # pe.get_import_ort_table()
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        for import_ in entry.imports:
            if import_.name:
                func = import_.name.decode()
                if func in NETWORK_FUNCTIONS:
                    res.add(func)
    return res

if __name__ == '__main__':
    total_files_count = 0
    files_with_functions_count = 0
    for root, dirs, files in os.walk(PATH):
        for file in files:
            if any(ext in file for ext in EXTENSIONS):
                total_files_count += 1
                print(f'Analyze {file}...')
                res = find_network_functions(os.path.join(root, file))
                if res:
                    files_with_functions_count += 1
                    print(f"Founded functions in {file}:\n")
                    [print('\t' + item) for item in res]
                else:
                    print(f"There is no network functions in {file}")
                print()
    print(f"{'-'*50}\nSearch is ended\nTotal files checked: {total_files_count}\nFiles with given functions: {files_with_functions_count}")