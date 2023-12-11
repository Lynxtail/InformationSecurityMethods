﻿### Задание 1. Ревизор диска
Разработать программу, работающую по принципу «ревизора диска» и контролирующую целостность данных в заданном каталоге.

Программа должна уметь:

1. подсчитать ХЭШ-сумму файлов (для каждого файла отдельно) в заданном каталоге с обходом всех подкаталогов. Сохранить эти сведения для дальнейшей проверки целостности.

2. проверить целостность каталога с указанием на изменившиеся файлы.

Алгоритм подсчета ХЭШ-суммы. Файл читается как бинарный поток. Поток разбивается на 16-битные отрезки, которые складываются по XOR. Если в последнем отрезке не хватает бит до 16, недостающее дополняется нулями.

Хэш-сумма д.б. сохранена в файле, находящемся в контролируемом каталоге, при этом сам файл не является объектом контроля.


### Задание 2. Автоконтроль целостности исполняемого файла
Разработать программу, контролирующую целостность своего исполнимого файла.

Хэш-сумма м.б. сохранена отдельно от контролируемого файла, но программа должна контролировать наличие этого файла и без него не работать. 
Первый запуск программы определяет "волшебное слово" в файле-хранителе хэш-суммы и по нему выясняет, что происходит первый запуск для 
определения хэш-суммы. В дальнейшем, если в файле отсутствует "волшебное слово", то считается, то программа должна только сверять имеющуюся 
там хэш-сумму с вычисленной и сообщать о результатах.

Хэш-сумма вычислется как в Задаче 1.


### Задание 3. Нахождение сетевых функций в PE-файле.

Разработать программу, которая анализирует структуру PE-файла и находит в нем обращение к сетевым функциям. В результате прорамма дожна автоматически найти все файлы с сетевыми фикциями в указанном каталоге.

###### Набор обнаруживаемых сетевых функций - 
    * DeleteIPAddress
    * FreeMibTable
    * GetAdaptersAddresses
    * GetAnycastIpAddressEntry
    * GetAnycastIpAddressTable
    * GetBestRoute2
    * GetHostNameW
    * GetIpAddrTable
    * GetIpStatisticsEx
    * GetUnicastIpAddressTable
    * IcmpCloseHandle
    * IcmpCreateFile
    * IcmpCloseHandle
    * IcmpSendEcho
    * MultinetGetConnectionPerformance
    * MultinetGetConnectionPerformanceW
    * NetAlertRaise
    * NetAlertRaiseEx
    * NetApiBufferAllocate
    * NetApiBufferFree
    * NetApiBufferReallocate
    * NetApiBufferSize
    * NetFreeAadJoinInformation
    * NetGetAadJoinInformation
    * NetAddAlternateComputerName
    * NetCreateProvisioningPackage
    * NetEnumerateComputerNames
    * NetGetJoinableOUs
    * NetGetJoinInformation
    * NetJoinDomain
    * NetProvisionComputerAccount
    * NetRemoveAlternateComputerName
    * NetRenameMachineInDomain
    * NetRequestOfflineDomainJoin
    * NetRequestProvisioningPackageInstall
    * NetSetPrimaryComputerName
    * NetUnjoinDomain
    * NetValidateName
    * NetGetAnyDCName
    * NetGetDCName
    * NetGetDisplayInformationIndex
    * NetQueryDisplayInformation
    * NetGroupAdd
    * NetGroupAddUser
    * NetGroupDel
    * NetGroupDelUser
    * NetGroupEnum
    * NetGroupGetInfo
    * NetGroupGetUsers
    * NetGroupSetInfo
    * NetGroupSetUsers
    * NetLocalGroupAdd
    * NetLocalGroupAddMembers
    * NetLocalGroupDel
    * NetLocalGroupDelMembers
    * NetLocalGroupEnum
    * NetLocalGroupGetInfo
    * NetLocalGroupGetMembers
    * NetLocalGroupSetInfo
    * NetLocalGroupSetMembers
    * NetMessageBufferSend
    * NetMessageNameAdd
    * NetMessageNameDel
    * NetMessageNameEnum
    * NetMessageNameGetInfo
    * NetFileClose
    * NetFileEnum
    * NetFileGetInfo
    * NetRemoteComputerSupports
    * NetRemoteTOD
    * NetScheduleJobAdd
    * NetScheduleJobDel
    * NetScheduleJobEnum
    * NetScheduleJobGetInfo
    * GetNetScheduleAccountInformation
    * SetNetScheduleAccountInformation
    * NetServerDiskEnum
    * NetServerEnum
    * NetServerGetInfo
    * NetServerSetInfo
    * NetServerComputerNameAdd
    * NetServerComputerNameDel
    * NetServerTransportAdd
    * NetServerTransportAddEx
    * NetServerTransportDel
    * NetServerTransportEnum
    * NetWkstaTransportEnum
    * NetUseAdd
    * NetUseDel
    * NetUseEnum
    * NetUseGetInfo
    * NetUserAdd
    * NetUserChangePassword
    * NetUserDel
    * NetUserEnum
    * NetUserGetGroups
    * NetUserGetInfo
    * NetUserGetLocalGroups
    * NetUserSetGroups
    * NetUserSetInfo
    * NetUserModalsGet
    * NetUserModalsSet
    * NetValidatePasswordPolicyFree
    * NetValidatePasswordPolicy
    * NetWkstaGetInfo
    * NetWkstaSetInfo
    * NetWkstaUserEnum
    * NetWkstaUserGetInfo
    * NetWkstaUserSetInfo
    * NetAccessAdd
    * NetAccessCheck
    * NetAccessDel
    * NetAccessEnum
    * NetAccessGetInfo
    * NetAccessGetUserPerms
    * NetAccessSetInfo
    * NetAuditClear
    * NetAuditRead
    * NetAuditWrite
    * NetConfigGet
    * NetConfigGetAll
    * NetConfigSet
    * NetErrorLogClear
    * NetErrorLogRead
    * NetErrorLogWrite
    * NetLocalGroupAddMember
    * NetLocalGroupDelMember
    * NetServiceControl
    * NetServiceEnum
    * NetServiceGetInfo
    * NetServiceInstall
    * NetWkstaTransportAdd
    * NetWkstaTransportDel
    * NetpwNameValidate
    * NetapipBufferAllocate
    * NetpwPathType
    * NetApiBufferFree
    * NetApiBufferAllocate
    * NetApiBufferReallocate
    * WNetAddConnection2
    * WNetAddConnection2W
    * WNetAddConnection3
    * WNetAddConnection3W
    * WNetCancelConnection
    * WNetCancelConnectionW
    * WNetCancelConnection2
    * WNetCancelConnection2W
    * WNetCloseEnum
    * WNetCloseEnumW
    * WNetConnectionDialog
    * WNetConnectionDialogW
    * WNetConnectionDialog1
    * WNetConnectionDialog1W
    * WNetDisconnectDialog
    * WNetDisconnectDialogW
    * WNetDisconnectDialog1
    * WNetDisconnectDialog1W
    * WNetEnumResource
    * WNetEnumResourceW
    * WNetGetConnection
    * WNetGetConnectionW
    * WNetGetLastError
    * WNetGetLastErrorW
    * WNetGetNetworkInformation
    * WNetGetNetworkInformationW
    * WNetGetProviderName
    * WNetGetProviderNameW
    * WNetGetResourceInformation
    * WNetGetResourceInformationW
    * WNetGetResourceParent
    * WNetGetResourceParentW
    * WNetGetUniversalName
    * WNetGetUniversalNameW
    * WNetGetUser
    * WNetGetUserW
    * WNetOpenEnum
    * WNetOpenEnumW
    * WNetRestoreConnectionW
    * WNetUseConnection
    * WNetUseConnectionW


Поиск функций ведется в секции импорта PE файла.

С целью изучения структуры PE-файла можно пользоваться ресурсом

https://penet.azureedge.net/