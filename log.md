default	13:16:04.528541-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:16:04.528753-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:16:04.531508-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:16:04.539195-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:16:04.540477-0500	runningboardd	Launch request for app<application.com.nexy.assistant.20360897.20360903(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:16:04.540594-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.20360897.20360903(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:46006] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-46006-1347001 target:app<application.com.nexy.assistant.20360897.20360903(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:16:04.540702-0500	runningboardd	Assertion 398-46006-1347001 (target:app<application.com.nexy.assistant.20360897.20360903(501)>) will be created as active
default	13:16:04.543837-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:16:04.543875-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.20360897.20360903(501)>
default	13:16:04.543888-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:16:04.544003-0500	runningboardd	app<application.com.nexy.assistant.20360897.20360903(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:16:04.610873-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] is not RunningBoard jetsam managed.
default	13:16:04.610889-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] This process will not be managed.
default	13:16:04.610902-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.20360897.20360903(501)>:60376]
default	13:16:04.611082-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:04.611824-0500	gamepolicyd	Hit the server for a process handle 7c781e40000ebd8 that resolved to: [app<application.com.nexy.assistant.20360897.20360903(501)>:60376]
default	13:16:04.611865-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:04.614427-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.20360897.20360903(501)>:60376]
default	13:16:04.614581-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-1347002 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:04.614746-0500	runningboardd	Assertion 398-398-1347002 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:04.614962-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:04.614996-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:04.615010-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Set darwin role to: UserInteractive
default	13:16:04.615026-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:04.615080-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:04.615150-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] reported to RB as running
default	13:16:04.616730-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:60376" ID:398-363-1347003 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:16:04.616849-0500	runningboardd	Assertion 398-363-1347003 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:04.616695-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x144a449 com.nexy.assistant starting stopped process.
default	13:16:04.617547-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:16:04.617758-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:16:04.620111-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:04.620137-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:04.620186-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:04.620230-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:04.620338-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.20360897.20360903(501)>:60376]
default	13:16:04.620418-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:04.620681-0500	runningboardd	Invalidating assertion 398-46006-1347001 (target:app<application.com.nexy.assistant.20360897.20360903(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:46006]
default	13:16:04.620707-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:04.620726-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:04.620743-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:04.620853-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:04.620795-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:04.623476-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:04.629376-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:04.629395-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:04.629405-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:04.629421-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:04.633332-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:04.727343-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:05.261368-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	13:16:05.263380-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=511.134, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	13:16:05.273937-0500	tccd	AUTHREQ_SUBJECT: msgID=511.134, subject=com.nexy.assistant,
default	13:16:05.274837-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:16:05.296030-0500	kernel	Nexy[60376] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x1963ee81bb209053. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:16:05.296050-0500	kernel	Nexy[60376] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0x1963ee81bb209053. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:16:05.639785-0500	Nexy	[0x103ee4790] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:16:05.639853-0500	Nexy	[0x103ee4d00] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	13:16:05.780750-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x103ecdf70 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:05.780982-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x103ecdf70 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:05.781199-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x103ecdf70 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:05.781404-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x103ecdf70 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:16:05.876115-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:16:05.879528-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:16:05.881468-0500	Nexy	[0x103eef800] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:16:05.885837-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20360897.20360903 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20360897.20360903>
default	13:16:05.890420-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:16:05.892491-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:16:05.892652-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:16:05.892793-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:16:05.892805-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:16:05.893030-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:16:05.893215-0500	Nexy	[0xbd0510000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:16:05.893419-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:16:05.893729-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60376.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:05.900110-0500	tccd	AUTHREQ_SUBJECT: msgID=60376.1, subject=com.nexy.assistant,
default	13:16:05.900713-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:05.914638-0500	Nexy	[0xbd0510000] invalidated after the last release of the connection object
default	13:16:05.914684-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:16:05.917268-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	13:16:05.918477-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7368, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:05.919306-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7368, subject=com.nexy.assistant,
default	13:16:05.920234-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
error	13:16:05.936964-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:16:05.937792-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7370, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:05.938496-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7370, subject=com.nexy.assistant,
default	13:16:05.939011-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:05.954242-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:16:05.954427-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xbd0c33600> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	13:16:05.976217-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	13:16:05.976228-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	13:16:05.979885-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:05.980007-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:05.985760-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:16:08.279942-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 9B1B060F-8093-4A9B-A025-1EF85E2FAB84 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52610,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x5d4c9758 tp_proto=0x06"
default	13:16:08.280042-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52610<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5019678 t_state: SYN_SENT process: Nexy:60376 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbd2f9562
default	13:16:08.280762-0500	kernel	tcp connected: [<IPv4-redacted>:52610<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5019678 t_state: ESTABLISHED process: Nexy:60376 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbd2f9562
default	13:16:08.281094-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52610<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5019678 t_state: FIN_WAIT_1 process: Nexy:60376 Duration: 0.002 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xbd2f9562
default	13:16:08.281105-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52610<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5019678 t_state: FIN_WAIT_1 process: Nexy:60376 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:16:08.317559-0500	Nexy	[0xbd0510000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:16:08.802092-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbd1baf140) Selecting device 85 from constructor
default	13:16:08.802109-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbd1baf140)
default	13:16:08.802118-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbd1baf140) not already running
default	13:16:08.802123-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xbd1baf140) nothing to teardown
default	13:16:08.802128-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbd1baf140) connecting device 85
default	13:16:08.802294-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xbd1baf140) Device ID: 85 (Input:No | Output:Yes): true
default	13:16:08.802921-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xbd1baf140) created ioproc 0xa for device 85
default	13:16:08.803071-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 7 device listeners to device 85
default	13:16:08.803276-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 0 device delegate listeners to device 85
default	13:16:08.803287-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xbd1baf140)
default	13:16:08.803388-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:08.803406-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:16:08.803417-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:08.803426-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:16:08.803435-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:08.803544-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xbd1baf140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:08.803555-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xbd1baf140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:08.803560-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:16:08.803565-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 0 device listeners from device 0
default	13:16:08.803570-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 0 device delegate listeners from device 0
default	13:16:08.803574-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbd1baf140)
default	13:16:08.803599-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:16:08.803709-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xbd1baf140) caller requesting device change from 85 to 91
default	13:16:08.803718-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbd1baf140)
default	13:16:08.803723-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbd1baf140) not already running
default	13:16:08.803728-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xbd1baf140) disconnecting device 85
default	13:16:08.803733-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xbd1baf140) destroying ioproc 0xa for device 85
default	13:16:08.803812-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:16:08.805433-0500	Nexy	[0xbd0510280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:16:08.807800-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef18f","name":"Nexy(60376)"}, "details":{"PID":60376,"session_type":"Primary"} }
default	13:16:08.807907-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":60376}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef18f, sessionType: 'prim', isRecording: false }, 
]
default	13:16:08.808877-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 60376, name = Nexy
default	13:16:08.809281-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xbd1a2e680 with ID: 0x1ef18f
default	13:16:08.811105-0500	Nexy	[0xbd05103c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	13:16:08.811312-0500	Nexy	No persisted cache on this platform.
error	13:16:08.811753-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=259312945463297 }
default	13:16:08.811772-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	13:16:08.811845-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:16:08.811996-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbd1baf140) connecting device 91
default	13:16:08.812134-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xbd1baf140) Device ID: 91 (Input:Yes | Output:No): true
default	13:16:08.813910-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7371, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:08.815388-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7371, subject=com.nexy.assistant,
default	13:16:08.816247-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:08.830073-0500	tccd	AUTHREQ_PROMPTING: msgID=401.7371, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	13:16:09.730335-0500	runningboardd	Assertion did invalidate due to timeout: 398-398-1347002 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376])
default	13:16:09.927299-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:09.927310-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:09.927320-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:09.927335-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:09.929883-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:09.930505-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:16.946923-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xbd1baf140) created ioproc 0xa for device 91
default	13:16:16.946856-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Passed, csid=com.apple.cloudd>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	13:16:16.947175-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 7 device listeners to device 91
default	13:16:16.947480-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 0 device delegate listeners to device 91
default	13:16:16.947498-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xbd1baf140)
default	13:16:16.947514-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	13:16:16.947530-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:16.947767-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	13:16:16.947782-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	13:16:16.947791-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:16:16.947937-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xbd1baf140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:16.947952-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xbd1baf140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:16.947961-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:16:16.947983-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 7 device listeners from device 85
default	13:16:16.948241-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 0 device delegate listeners from device 85
default	13:16:16.948256-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbd1baf140)
default	13:16:16.947613-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	13:16:16.949282-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:16:16.950910-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7372, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:16.952617-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7372, subject=com.nexy.assistant,
default	13:16:16.954341-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:16.971221-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:16:16.972651-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7373, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:16.973774-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7373, subject=com.nexy.assistant,
default	13:16:16.974513-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:16.990187-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:16:16.991914-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7374, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:16.992863-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7374, subject=com.nexy.assistant,
default	13:16:16.994725-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:17.008091-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:16:17.008536-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:16:17.008721-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:16:17.008891-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:16:17.010814-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:16:17.011552-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:16:17.012767-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa2700] Created node ADM::com.nexy.assistant_49923.49141.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:17.012840-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa2700] Created node ADM::com.nexy.assistant_49923.49141.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:17.092202-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:16:17.093808-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:49923 called from <private>
default	13:16:17.093908-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:16:17.093939-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:16:17.097019-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1347062 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:17.097106-0500	runningboardd	Assertion 398-334-1347062 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:17.100203-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:17.100301-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:17.100368-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:17.100517-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:17.101322-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:17.095529-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49923 called from <private>
default	13:16:17.102205-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:17.095758-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49923)
default	13:16:17.095787-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49923 called from <private>
default	13:16:17.095793-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49923 called from <private>
default	13:16:17.095866-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49922)
default	13:16:17.095880-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49922 called from <private>
default	13:16:17.096167-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49922 called from <private>
fault	13:16:17.104618-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20360897.20360903 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20360897.20360903>
default	13:16:17.105855-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49923)
default	13:16:17.105875-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49923)
default	13:16:17.105885-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49923)
default	13:16:17.105887-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:49923 called from <private>
default	13:16:17.105897-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:49923 called from <private>
default	13:16:17.105906-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:49923 called from <private>
default	13:16:17.105911-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:49923 called from <private>
default	13:16:17.105918-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49923 called from <private>
default	13:16:17.114620-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:17.105957-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49923)
default	13:16:17.105983-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49923 called from <private>
default	13:16:17.106054-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49923 called from <private>
default	13:16:17.106132-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49923 called from <private>
default	13:16:17.110620-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49923 called from <private>
default	13:16:17.110655-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49923 called from <private>
default	13:16:17.115078-0500	runningboardd	Invalidating assertion 398-334-1347062 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [osservice<com.apple.powerd>:334]
fault	13:16:17.117964-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20360897.20360903 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20360897.20360903>
default	13:16:17.119443-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef18f","name":"Nexy(60376)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:16:17.119515-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:16:17.119581-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:17.119642-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef18f, Nexy(60376), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:16:17.119762-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:17.119780-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:17.119940-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:17.119820-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:17.119926-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:17.120018-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:17.119880-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:16:17.119883-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:17.119910-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef18f, Nexy(60376), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 400 starting recording
default	13:16:17.120359-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:17.120387-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:16:17.120407-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef18f, Nexy(60376), 'prim'', displayID:'com.nexy.assistant'}
default	13:16:17.120493-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:16:17.120604-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:16:17.120616-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:16:17.122900-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49922 called from <private>
default	13:16:17.122910-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49922 called from <private>
default	13:16:17.124377-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49923)
default	13:16:17.124407-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49923 called from <private>
default	13:16:17.124706-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49922)
default	13:16:17.126614-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7375, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:17.130683-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7375, subject=com.nexy.assistant,
default	13:16:17.131702-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:17.134793-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:17.134861-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:17.134934-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:17.135436-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:49922 called from <private>
default	13:16:17.135363-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:17.136692-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.136806-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.136851-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:17.136907-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.136986-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:17.137011-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:17.135448-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:49922 called from <private>
default	13:16:17.135538-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49922)
default	13:16:17.138806-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:17.143121-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.143440-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.143484-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:17.143558-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.143593-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:17.143668-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:17.144102-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:17.145900-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49922)
default	13:16:17.159687-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:17.160167-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:17.160546-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:17.173439-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:49923 called from <private>
default	13:16:17.173470-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 1 1 id:49923 called from <private>
default	13:16:17.174010-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:16:17.183384-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7376, subject=com.nexy.assistant,
default	13:16:17.184413-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:17.187367-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.187378-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:17.187387-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.187396-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:17.187416-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:17.187808-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:17.201112-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:16:17.203062-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa2700] Created node ADM::com.nexy.assistant_49923.49141.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:17.203133-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa2700] Created node ADM::com.nexy.assistant_49923.49141.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:17.218513-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:17.218525-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:17.218535-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:17.218559-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:17.221266-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:17.221661-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:17.241115-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:16:17.242271-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1347065 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:17.242347-0500	runningboardd	Assertion 398-334-1347065 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:17.244615-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:49923 called from <private>
default	13:16:17.244682-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:49923 called from <private>
default	13:16:17.244852-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:16:17.245619-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:17.245632-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:17.246049-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:17.247117-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:17.248668-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49923 called from <private>
default	13:16:17.249001-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49923)
default	13:16:17.249048-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49923 called from <private>
default	13:16:17.249084-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49923 called from <private>
default	13:16:17.250356-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:17.250762-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:17.251434-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49923)
default	13:16:17.251578-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49923 called from <private>
default	13:16:17.251589-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49923 called from <private>
default	13:16:17.251600-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49923 called from <private>
default	13:16:17.253421-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7377, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:17.254792-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7377, subject=com.nexy.assistant,
default	13:16:17.255342-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:17.255608-0500	runningboardd	Invalidating assertion 398-334-1347065 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [osservice<com.apple.powerd>:334]
default	13:16:17.255968-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:17.256067-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:17.256248-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:17.256376-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:17.256438-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:17.256592-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:17.257222-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.257249-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.257273-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:17.257283-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.257292-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:17.257299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:17.257555-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:17.273037-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1347066 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:17.273114-0500	runningboardd	Assertion 398-334-1347066 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:17.274303-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:49923 called from <private>
default	13:16:17.286361-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.286401-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:17.286458-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:17.286539-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:17.287255-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.287266-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.287273-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:17.287281-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:17.287287-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:17.287293-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:17.287430-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:16:17.879957-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	13:16:18.299771-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:16:18.300263-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef18f","name":"Nexy(60376)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:16:18.300446-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:18.300539-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:16:18.300592-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef18f, Nexy(60376), 'prim'', displayID:'com.nexy.assistant'}
default	13:16:18.300664-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:16:18.300678-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef18f, Nexy(60376), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 400 stopping recording
default	13:16:18.300729-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:16:18.300767-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:18.300816-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:18.300971-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:16:18.300987-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:16:18.301099-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:16:18.301397-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:18.301449-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:18.301513-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:18.301556-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:18.301575-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:16:18.301604-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:18.301691-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:16:18.301711-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:18.301726-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:16:18.305310-0500	runningboardd	Invalidating assertion 398-334-1347066 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [osservice<com.apple.powerd>:334]
default	13:16:18.310125-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:18.315220-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:18.315236-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:18.315252-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:18.315259-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:18.315267-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:18.315274-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:18.315383-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:18.402132-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbd1baf140) Selecting device 0 from destructor
default	13:16:18.402165-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbd1baf140)
default	13:16:18.402180-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbd1baf140) not already running
default	13:16:18.402194-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xbd1baf140) disconnecting device 91
default	13:16:18.402209-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xbd1baf140) destroying ioproc 0xa for device 91
default	13:16:18.402268-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:16:18.402342-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:16:18.402678-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xbd1baf140) nothing to setup
default	13:16:18.402713-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 0 device listeners to device 0
default	13:16:18.402729-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 0 device delegate listeners to device 0
default	13:16:18.402745-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 7 device listeners from device 91
default	13:16:18.403264-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 0 device delegate listeners from device 91
default	13:16:18.403294-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbd1baf140)
default	13:16:18.409013-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:18.409073-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:18.409116-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:18.409177-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:18.413564-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:18.414486-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:18.663820-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60385.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=60385, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:16:18.665728-0500	tccd	AUTHREQ_SUBJECT: msgID=60385.1, subject=com.nexy.assistant,
default	13:16:18.666783-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:16:18.682182-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.13682, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=60385, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:18.683191-0500	tccd	AUTHREQ_SUBJECT: msgID=393.13682, subject=com.nexy.assistant,
default	13:16:18.683907-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:16:18.709253-0500	launchservicesd	CHECKIN:0x0-0x144a449 60385 com.nexy.assistant
default	13:16:18.710262-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:16:18.710408-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:16:18.711184-0500	runningboardd	Invalidating assertion 398-363-1347003 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	13:16:18.713953-0500	WindowServer	1897eb[CreateApplication]: Process creation: 0x0-0x144a449 (Nexy) connectionID: 1897EB pid: 60385 in session 0x101
default	13:16:18.716732-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:16:18.719532-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:16:18.767846-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:18.767863-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:18.767906-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Set darwin role to: None
default	13:16:18.767921-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:18.767940-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:18.770992-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-suspended (role: None) (endowments: (null))
default	13:16:18.771383-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-suspended-NotVisible
default	13:16:18.861860-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 60386: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 8c631e00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	13:16:18.873142-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:18.928056-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x144a449} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:16:18.928102-0500	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 21275721
default	13:16:18.928165-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:16:18.930525-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x144a449 (Nexy) connectionID: 1897EB pid: 60385 in session 0x101
default	13:16:18.930571-0500	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x144a449 (Nexy) acq:0x7fd724c20 count:1
default	13:16:18.930991-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x144a449 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x144a449 (Nexy)"
)}
default	13:16:18.931217-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xebe1 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x144a449 (Nexy)"
)}
default	13:16:19.112345-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbd1baf140) Selecting device 85 from constructor
default	13:16:19.112354-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbd1baf140)
default	13:16:19.112360-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbd1baf140) not already running
default	13:16:19.112364-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xbd1baf140) nothing to teardown
default	13:16:19.112368-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbd1baf140) connecting device 85
default	13:16:19.112474-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xbd1baf140) Device ID: 85 (Input:No | Output:Yes): true
default	13:16:19.112581-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xbd1baf140) created ioproc 0xb for device 85
default	13:16:19.112716-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 7 device listeners to device 85
default	13:16:19.112885-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 0 device delegate listeners to device 85
default	13:16:19.112894-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xbd1baf140)
default	13:16:19.112962-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	13:16:19.112968-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:16:19.112979-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	13:16:19.112984-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:16:19.112992-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:19.113100-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xbd1baf140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:19.113111-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xbd1baf140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:19.113117-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:16:19.113122-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 0 device listeners from device 0
default	13:16:19.113126-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 0 device delegate listeners from device 0
default	13:16:19.113130-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbd1baf140)
default	13:16:19.113141-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:16:19.113212-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xbd1baf140) caller requesting device change from 85 to 91
default	13:16:19.113219-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbd1baf140)
default	13:16:19.113224-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbd1baf140) not already running
default	13:16:19.113228-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xbd1baf140) disconnecting device 85
default	13:16:19.113231-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xbd1baf140) destroying ioproc 0xb for device 85
default	13:16:19.113250-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	13:16:19.113272-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:16:19.113357-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbd1baf140) connecting device 91
default	13:16:19.113437-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xbd1baf140) Device ID: 91 (Input:Yes | Output:No): true
default	13:16:19.114506-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7378, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:19.115371-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7378, subject=com.nexy.assistant,
default	13:16:19.115909-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:19.128062-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xbd1baf140) created ioproc 0xb for device 91
default	13:16:19.128168-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 7 device listeners to device 91
default	13:16:19.128330-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 0 device delegate listeners to device 91
default	13:16:19.128339-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xbd1baf140)
default	13:16:19.128348-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	13:16:19.128355-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:19.128467-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	13:16:19.128473-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	13:16:19.128479-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:16:19.128566-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xbd1baf140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:19.128576-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xbd1baf140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:19.128581-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:16:19.128585-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 7 device listeners from device 85
default	13:16:19.128734-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 0 device delegate listeners from device 85
default	13:16:19.128741-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbd1baf140)
default	13:16:19.129281-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:16:19.130162-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7379, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:19.130852-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7379, subject=com.nexy.assistant,
default	13:16:19.131346-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:19.143383-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:16:19.143532-0500	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0xbcfda1830, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	13:16:19.143738-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:16:19.144608-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7380, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:19.145353-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7380, subject=com.nexy.assistant,
default	13:16:19.145879-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:19.159117-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7381, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:19.159806-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7381, subject=com.nexy.assistant,
default	13:16:19.160303-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	13:16:19.175987-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:16:19.179698-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef18f","name":"Nexy(60376)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:16:19.179797-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1347080 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:19.179774-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:16:19.179796-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef18f, Nexy(60376), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	13:16:19.179820-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:19.179868-0500	runningboardd	Assertion 398-334-1347080 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:19.180003-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:19.179868-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef18f, Nexy(60376), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:16:19.180035-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:19.180075-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:19.180183-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:16:19.180198-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:19.180213-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef18f, Nexy(60376), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 400 starting recording
default	13:16:19.180252-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:19.180188-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:19.180233-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:19.180280-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:19.180340-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Set darwin role to: Background
default	13:16:19.180401-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:19.180396-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:19.180330-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:19.180449-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:16:19.180484-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:19.180351-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:19.180526-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef18f, Nexy(60376), 'prim'', displayID:'com.nexy.assistant'}
default	13:16:19.180661-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:16:19.180870-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:16:19.181072-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:19.181150-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:19.181175-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:19.181313-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	13:16:19.181324-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	13:16:19.181333-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	13:16:19.181446-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	13:16:19.181571-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:16:19.182801-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:16:19.182868-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:16:19.185005-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: Background) (endowments: (null))
default	13:16:19.185400-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:19.187288-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:19.187341-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:19.187381-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:19.187863-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:19.187871-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:19.187908-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:19.187943-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:19.187975-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:19.188000-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:19.188036-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:19.188069-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:19.188122-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:19.188153-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:19.188188-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:19.188237-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:19.188433-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:19.189301-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:19.189311-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:19.189322-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:19.189328-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:19.189337-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:19.189342-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:19.189495-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:16:20.910665-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	13:16:23.913259-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	13:16:26.949256-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	13:16:28.150273-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_49923.49141.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-33.639763], peaks:[-16.526222] ]
default	13:16:28.153070-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_49923.49141.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-36.477783], peaks:[-15.801090] ]
default	13:16:29.892635-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	13:16:32.263108-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:16:32.264367-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef18f","name":"Nexy(60376)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:16:32.264949-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:32.265085-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:16:32.265163-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef18f, Nexy(60376), 'prim'', displayID:'com.nexy.assistant'}
default	13:16:32.265472-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:16:32.265496-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef18f, Nexy(60376), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 400 stopping recording
default	13:16:32.265568-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:16:32.265650-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:32.265722-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:32.266161-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:16:32.266253-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:16:32.266388-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:16:32.266973-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:32.267070-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:32.267224-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:32.267312-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:32.267348-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:32.267393-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:16:32.267551-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:16:32.267590-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:32.267617-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:16:32.271816-0500	runningboardd	Invalidating assertion 398-334-1347080 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [osservice<com.apple.powerd>:334]
default	13:16:32.273423-0500	coreaudiod	Sending message. { reporterID=259312945463299, category=IO, type=error, message=["cause": Optional(ClientHALIODurationExceededBudget), "safety_violation": Optional(0), "deadline": Optional(313024), "io_cycle_usage": Optional(1), "wg_external_wakeups": Optional(3), "reporting_latency": Optional(62970625), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_user_time_mach": Optional(96904), "wg_instructions": Optional(7056574), "overload_type": Optional(Overload), "time_since_prev_overload": Optional(453590968374541), "is_recovering": Optional(0), "input_device_transport_list": Optional(Bluetooth), "wg_total_wakeups": Optional(5), "io_page_faults_duration": Optional(0), "anchor_sample_time": Optional(4), "sample_rate": Optional(24000), "num_continuous_silent_io_cycles": Optional(0), "smallest_buffer_frame_size": Optional(2147483647), "careporting_timestamp": 1762193792.273099, "io_page_faults": Optional(0), "input_device_source_list": Optional(Unknown), "input_device_uid_list": Optional(3:input), "scheduler_latency": Optional(13625), "io_fr<…> }
default	13:16:32.275027-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:32.282284-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:32.282299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:32.282325-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:32.282332-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:32.282340-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:32.282361-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:32.282475-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:32.373464-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:32.373478-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:32.373527-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Set darwin role to: None
default	13:16:32.373538-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:32.373569-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:32.380453-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-suspended (role: None) (endowments: (null))
default	13:16:32.381278-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-suspended-NotVisible
default	13:16:32.417699-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbd1baf140) Selecting device 0 from destructor
default	13:16:32.417720-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbd1baf140)
default	13:16:32.417730-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbd1baf140) not already running
default	13:16:32.417736-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xbd1baf140) disconnecting device 91
default	13:16:32.417743-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xbd1baf140) destroying ioproc 0xb for device 91
default	13:16:32.417788-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:16:32.417829-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:16:32.418047-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xbd1baf140) nothing to setup
default	13:16:32.418061-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 0 device listeners to device 0
default	13:16:32.418067-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbd1baf140) adding 0 device delegate listeners to device 0
default	13:16:32.418075-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 7 device listeners from device 91
default	13:16:32.418334-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbd1baf140) removing 0 device delegate listeners from device 91
default	13:16:32.418353-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbd1baf140)
default	13:16:32.440359-0500	Nexy	[0xbd0510500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:16:32.441904-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60376.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:32.445255-0500	tccd	AUTHREQ_SUBJECT: msgID=60376.2, subject=com.nexy.assistant,
default	13:16:32.446202-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:16:32.465270-0500	Nexy	[0xbd0510500] invalidated after the last release of the connection object
default	13:16:32.466938-0500	Nexy	[0xbd0510500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:16:32.467555-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60376.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:32.468724-0500	tccd	AUTHREQ_SUBJECT: msgID=60376.3, subject=com.nexy.assistant,
default	13:16:32.469340-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:16:32.486505-0500	Nexy	[0xbd0510500] invalidated after the last release of the connection object
default	13:16:32.486921-0500	Nexy	[0xbd0510500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:16:32.487479-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60376.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:32.488487-0500	tccd	AUTHREQ_SUBJECT: msgID=60376.4, subject=com.nexy.assistant,
default	13:16:32.489131-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:16:32.502202-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[60376], responsiblePID[60376], responsiblePath: /Applications/Nexy.app to UID: 501
default	13:16:32.502456-0500	Nexy	[0xbd0510500] invalidated after the last release of the connection object
default	13:16:32.592282-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	13:16:32.627526-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:16:32.635298-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:16:32.655494-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:16:32.656239-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:16:33.247626-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	13:16:33.253494-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:16:33.282052-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	13:16:34.495805-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49923)
default	13:16:34.495791-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49922)
default	13:16:34.495857-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49922 called from <private>
default	13:16:34.495867-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49922 called from <private>
default	13:16:34.495878-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49923 called from <private>
default	13:16:34.495898-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49923 called from <private>
default	13:16:34.531825-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49922)
default	13:16:34.531918-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49923)
default	13:16:34.531915-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49922 called from <private>
default	13:16:34.531929-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49922 called from <private>
default	13:16:34.531939-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49922 called from <private>
default	13:16:34.531960-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49922 called from <private>
default	13:16:34.532017-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49923 called from <private>
default	13:16:34.532030-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49923 called from <private>
default	13:16:34.532402-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49922)
default	13:16:34.532819-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49922)
default	13:16:34.533494-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49922 called from <private>
default	13:16:34.533574-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49922 called from <private>
default	13:16:34.603722-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49922 called from <private>
default	13:16:34.604054-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49922 called from <private>
default	13:16:34.604475-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49922)
default	13:16:34.604809-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49922)
default	13:16:40.100337-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	13:16:40.117583-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:16:40.127087-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:16:46.018105-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef18f","name":"Nexy(60376)"}, "details":null }
default	13:16:46.018203-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef18f from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":60376})
default	13:16:46.018233-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":60376})
default	13:16:46.026417-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:46.026983-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 400, PID = 60376, Name = sid:0x1ef18f, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:46.027548-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:46.028215-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:46.028486-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:46.028569-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:46.041521-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:16:46.041929-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:16:46.043961-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_49923.49141.0_airpods noise suppression studio::out-0 issue_detected_sample_time=336960.000000 ] -- [ rms:[-33.377594], peaks:[-10.021948] ]
default	13:16:46.043988-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_49923.49141.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-31.067619], peaks:[-10.486364] ]
default	13:16:46.049973-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:46.050087-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:46.223182-0500	Nexy	[0x1042ebeb0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:16:46.223259-0500	Nexy	[0x1042f1250] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	13:16:46.315202-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x1042f2200 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:46.315452-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x1042f2200 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:46.315670-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x1042f2200 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:46.315882-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x1042f2200 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:16:46.392103-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:16:46.397627-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:16:46.400417-0500	Nexy	[0x1042f9be0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	13:16:46.403386-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:16:46.405086-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:16:46.405345-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:16:46.405515-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:16:46.405528-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:16:46.405605-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:16:46.405869-0500	Nexy	[0x9ca894000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:16:46.406088-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:16:46.406721-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60376.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:46.414421-0500	tccd	AUTHREQ_SUBJECT: msgID=60376.1, subject=com.nexy.assistant,
default	13:16:46.415349-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9800 at /Applications/Nexy.app
default	13:16:46.430507-0500	Nexy	[0x9ca894000] invalidated after the last release of the connection object
default	13:16:46.430732-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:16:46.430778-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:16:46.431080-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:16:46.432701-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7382, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:46.433685-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7382, subject=com.nexy.assistant,
default	13:16:46.434257-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9800 at /Applications/Nexy.app
error	13:16:46.452168-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:16:46.456497-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7384, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:46.465701-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7384, subject=com.nexy.assistant,
default	13:16:46.466747-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9800 at /Applications/Nexy.app
default	13:16:46.506247-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:16:46.506282-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x9caf40020> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	13:16:46.530508-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	13:16:46.530523-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	13:16:46.534854-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:48.065613-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid B6FC13C6-4E9F-4163-9858-73EDF2A647BD flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52649,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xf8276bf0 tp_proto=0x06"
default	13:16:48.065692-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52649<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020268 t_state: SYN_SENT process: Nexy:60376 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa107acbf
default	13:16:48.066359-0500	kernel	tcp connected: [<IPv4-redacted>:52649<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020268 t_state: ESTABLISHED process: Nexy:60376 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa107acbf
default	13:16:48.066620-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52649<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020268 t_state: FIN_WAIT_1 process: Nexy:60376 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xa107acbf
default	13:16:48.066627-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52649<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020268 t_state: FIN_WAIT_1 process: Nexy:60376 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:16:48.083756-0500	Nexy	[0x9ca894000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:16:48.095571-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9cbffd540) Selecting device 85 from constructor
default	13:16:48.095582-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x9cbffd540)
default	13:16:48.095588-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x9cbffd540) not already running
default	13:16:48.095592-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x9cbffd540) nothing to teardown
default	13:16:48.095597-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9cbffd540) connecting device 85
default	13:16:48.095729-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x9cbffd540) Device ID: 85 (Input:No | Output:Yes): true
default	13:16:48.095849-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x9cbffd540) created ioproc 0xa for device 85
default	13:16:48.095990-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9cbffd540) adding 7 device listeners to device 85
default	13:16:48.096159-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9cbffd540) adding 0 device delegate listeners to device 85
default	13:16:48.096167-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x9cbffd540)
default	13:16:48.096252-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:48.096272-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:16:48.096278-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:48.096286-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:16:48.096292-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:48.096415-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x9cbffd540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:48.096426-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x9cbffd540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:48.096431-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:16:48.096461-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9cbffd540) removing 0 device listeners from device 0
default	13:16:48.096487-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9cbffd540) removing 0 device delegate listeners from device 0
default	13:16:48.096493-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x9cbffd540)
default	13:16:48.096553-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:16:48.096652-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x9cbffd540) caller requesting device change from 85 to 91
default	13:16:48.096668-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x9cbffd540)
default	13:16:48.096673-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x9cbffd540) not already running
default	13:16:48.096678-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x9cbffd540) disconnecting device 85
default	13:16:48.096682-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x9cbffd540) destroying ioproc 0xa for device 85
default	13:16:48.096800-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:16:48.097353-0500	Nexy	[0x9ca894280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:16:48.098371-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef190","name":"Nexy(60376)"}, "details":{"PID":60376,"session_type":"Primary"} }
default	13:16:48.098455-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":60376}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef190, sessionType: 'prim', isRecording: false }, 
]
default	13:16:48.098853-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x9cb276680 with ID: 0x1ef190
default	13:16:48.099534-0500	Nexy	[0x9ca8943c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	13:16:48.099673-0500	Nexy	No persisted cache on this platform.
error	13:16:48.099973-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=259312945463297 }
default	13:16:48.099987-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	13:16:48.100054-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:16:48.100162-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9cbffd540) connecting device 91
default	13:16:48.100270-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x9cbffd540) Device ID: 91 (Input:Yes | Output:No): true
default	13:16:48.101608-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7385, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:48.102658-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7385, subject=com.nexy.assistant,
default	13:16:48.103225-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9800 at /Applications/Nexy.app
default	13:16:48.115886-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x9cbffd540) created ioproc 0xa for device 91
default	13:16:48.116029-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9cbffd540) adding 7 device listeners to device 91
default	13:16:48.116199-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9cbffd540) adding 0 device delegate listeners to device 91
default	13:16:48.116209-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x9cbffd540)
default	13:16:48.116216-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	13:16:48.116225-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:48.116341-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	13:16:48.116348-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	13:16:48.116353-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:16:48.116452-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x9cbffd540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:48.116467-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x9cbffd540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:48.116475-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:16:48.116480-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9cbffd540) removing 7 device listeners from device 85
default	13:16:48.116646-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9cbffd540) removing 0 device delegate listeners from device 85
default	13:16:48.116652-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x9cbffd540)
default	13:16:48.117252-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:16:48.118242-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7386, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:48.119050-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7386, subject=com.nexy.assistant,
default	13:16:48.119576-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9800 at /Applications/Nexy.app
default	13:16:48.131942-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:16:48.132874-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7387, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:48.133735-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7387, subject=com.nexy.assistant,
default	13:16:48.134701-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9800 at /Applications/Nexy.app
default	13:16:48.147936-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:16:48.149434-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7388, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:48.150491-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7388, subject=com.nexy.assistant,
default	13:16:48.151340-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9800 at /Applications/Nexy.app
default	13:16:48.164093-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:16:48.164227-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:16:48.164963-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:16:48.165227-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa3300] Created node ADM::com.nexy.assistant_49935.49141.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:48.165293-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa3300] Created node ADM::com.nexy.assistant_49935.49141.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:48.231837-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:16:48.234190-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:49935 called from <private>
default	13:16:48.234229-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:16:48.234237-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:16:48.234955-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49934)
default	13:16:48.234992-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49934 called from <private>
default	13:16:48.234998-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49934 called from <private>
default	13:16:48.237418-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1347235 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:48.237449-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49935 called from <private>
default	13:16:48.237535-0500	runningboardd	Assertion 398-334-1347235 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:48.237615-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49935)
default	13:16:48.237629-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49935 called from <private>
default	13:16:48.237637-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49935 called from <private>
default	13:16:48.238152-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:48.238336-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:48.238428-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Set darwin role to: Background
default	13:16:48.238461-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:48.238543-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
fault	13:16:48.243859-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20360897.20360903 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20360897.20360903>
fault	13:16:48.246530-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20360897.20360903 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20360897.20360903>
default	13:16:48.247487-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:48.247895-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:48.250515-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: Background) (endowments: (null))
default	13:16:48.251559-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49935)
default	13:16:48.251274-0500	runningboardd	Invalidating assertion 398-334-1347235 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [osservice<com.apple.powerd>:334]
default	13:16:48.251848-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49935)
default	13:16:48.252139-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49935)
default	13:16:48.252176-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:48.252882-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49935)
default	13:16:48.263812-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:48.263988-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:48.264096-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:48.264345-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:48.268717-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49935 called from <private>
default	13:16:48.268309-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.269006-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.269021-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.269062-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.269082-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.269089-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:48.268748-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49935 called from <private>
default	13:16:48.268913-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49935)
default	13:16:48.270194-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:48.271042-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49934)
default	13:16:48.271178-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49935 called from <private>
default	13:16:48.271198-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49935 called from <private>
default	13:16:48.271239-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49935 called from <private>
default	13:16:48.271261-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49935 called from <private>
default	13:16:48.271270-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49935 called from <private>
error	13:16:48.271835-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	13:16:48.272721-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef190","name":"Nexy(60376)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:16:48.272808-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:16:48.272854-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:48.273149-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:48.272912-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef190, Nexy(60376), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:16:48.272950-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:48.273260-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7389, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:48.273041-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:48.273121-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:48.273287-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:16:48.273351-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef190, Nexy(60376), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 401 starting recording
default	13:16:48.273567-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:48.273448-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:48.273574-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:48.273669-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:16:48.273730-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef190, Nexy(60376), 'prim'', displayID:'com.nexy.assistant'}
default	13:16:48.273822-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:16:48.274211-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:16:48.274321-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:16:48.274357-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7389, subject=com.nexy.assistant,
default	13:16:48.275626-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9800 at /Applications/Nexy.app
default	13:16:48.277605-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.277620-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.277635-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.277642-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.277650-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.277656-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:48.277806-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:48.284044-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49934 called from <private>
default	13:16:48.284128-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49934 called from <private>
default	13:16:48.284302-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:49934 called from <private>
default	13:16:48.284498-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:49934 called from <private>
default	13:16:48.284733-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49934)
default	13:16:48.302397-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:48.303325-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:49934 called from <private>
default	13:16:48.303358-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:49934 called from <private>
default	13:16:48.303507-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49934)
default	13:16:48.302691-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:48.303767-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:16:48.327677-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49934 called from <private>
default	13:16:48.327697-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49934 called from <private>
default	13:16:48.328846-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49934 called from <private>
default	13:16:48.349309-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:16:48.350733-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa3300] Created node ADM::com.nexy.assistant_49935.49141.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:48.350797-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa3300] Created node ADM::com.nexy.assistant_49935.49141.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:48.352369-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:48.352380-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:48.352408-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Set darwin role to: None
default	13:16:48.352438-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:48.352494-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:48.355429-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-suspended (role: None) (endowments: (null))
default	13:16:48.355771-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-suspended-NotVisible
default	13:16:48.385422-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:16:48.386661-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1347238 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:48.387409-0500	runningboardd	Assertion 398-334-1347238 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:48.387523-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:49935 called from <private>
default	13:16:48.387662-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 1 1 id:49935 called from <private>
default	13:16:48.387830-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:48.387846-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:48.387885-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Set darwin role to: Background
default	13:16:48.387897-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:48.387996-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:48.387702-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:16:48.391937-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49935 called from <private>
default	13:16:48.392095-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49935)
default	13:16:48.392848-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:48.393115-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49935 called from <private>
default	13:16:48.393171-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49935 called from <private>
default	13:16:48.393227-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:48.393724-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49935)
default	13:16:48.396178-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49935 called from <private>
default	13:16:48.396404-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49935 called from <private>
default	13:16:48.396445-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49935 called from <private>
error	13:16:48.396756-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	13:16:48.396903-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: Background) (endowments: (null))
default	13:16:48.397208-0500	runningboardd	Invalidating assertion 398-334-1347238 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [osservice<com.apple.powerd>:334]
default	13:16:48.397618-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:48.398340-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7391, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:48.399324-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:48.399413-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:48.399446-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:48.399569-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7391, subject=com.nexy.assistant,
default	13:16:48.399619-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:48.400012-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.400038-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.400048-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.400055-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.400062-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.400070-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:48.400183-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:48.400296-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.400340-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.400357-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.418859-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1347239 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:48.419009-0500	runningboardd	Assertion 398-334-1347239 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:48.421384-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:49935 called from <private>
default	13:16:48.421415-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:49935 called from <private>
default	13:16:48.421509-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:16:48.422873-0500	runningboardd	Invalidating assertion 398-334-1347239 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [osservice<com.apple.powerd>:334]
default	13:16:48.422996-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49935 called from <private>
default	13:16:48.423398-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49935)
default	13:16:48.423454-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49935 called from <private>
default	13:16:48.423464-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49935 called from <private>
default	13:16:48.423980-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:48.424098-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:48.424423-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49935)
default	13:16:48.424629-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49935 called from <private>
default	13:16:48.424725-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49935 called from <private>
default	13:16:48.424818-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49935 called from <private>
error	13:16:48.425060-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	13:16:48.426215-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7392, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:48.427476-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7392, subject=com.nexy.assistant,
default	13:16:48.428210-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:48.428267-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:48.428383-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:48.428606-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:48.428925-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9800 at /Applications/Nexy.app
default	13:16:48.428946-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.428956-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.428967-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.428992-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.429003-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.429009-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:48.429241-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:48.429315-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.429326-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.429404-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.429440-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.429503-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.429574-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:48.429791-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:48.445432-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1347240 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:48.446033-0500	runningboardd	Assertion 398-334-1347240 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:48.450397-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:49935 called from <private>
default	13:16:48.454968-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:48.455017-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:48.455051-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:48.455415-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.455437-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.455460-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.455470-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.455477-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.455486-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:48.455507-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.455528-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.455537-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.455543-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.455574-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.455595-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:48.455692-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:48.456129-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.456142-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.456176-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.456183-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:48.456193-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:48.456199-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:48.456269-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:16:49.709553-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:16:49.710043-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef190","name":"Nexy(60376)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:16:49.710232-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:49.710329-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:16:49.710385-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef190, Nexy(60376), 'prim'', displayID:'com.nexy.assistant'}
default	13:16:49.710470-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:16:49.710475-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef190, Nexy(60376), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 401 stopping recording
default	13:16:49.710515-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:16:49.710900-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:16:49.710613-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:49.710771-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 401, PID = 60376, Name = sid:0x1ef190, Nexy(60376), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:49.711283-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:49.711360-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:49.711441-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:49.711486-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:49.711510-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:16:49.711497-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:16:49.711536-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:49.711571-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:16:49.711623-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:16:49.711643-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:49.711661-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:16:49.715091-0500	runningboardd	Invalidating assertion 398-334-1347240 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [osservice<com.apple.powerd>:334]
default	13:16:49.717832-0500	coreaudiod	Sending message. { reporterID=259312945463298, category=IO, type=error, message=["cause": Optional(ClientHALIODurationExceededBudget), "safety_violation": Optional(0), "deadline": Optional(28472), "io_cycle_usage": Optional(1), "wg_external_wakeups": Optional(3), "reporting_latency": Optional(84277000), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_user_time_mach": Optional(83085), "wg_instructions": Optional(7127846), "overload_type": Optional(Overload), "time_since_prev_overload": Optional(453608419597958), "is_recovering": Optional(0), "input_device_transport_list": Optional(Bluetooth), "wg_total_wakeups": Optional(5), "io_page_faults_duration": Optional(0), "anchor_sample_time": Optional(92), "sample_rate": Optional(24000), "num_continuous_silent_io_cycles": Optional(0), "smallest_buffer_frame_size": Optional(2147483647), "careporting_timestamp": 1762193809.717227, "io_page_faults": Optional(0), "input_device_source_list": Optional(Unknown), "input_device_uid_list": Optional(3:input), "scheduler_latency": Optional(39125), "io_fr<…> }
default	13:16:49.718740-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:49.723284-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:49.723300-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:49.723316-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:49.723325-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:49.723332-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:49.723340-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:49.723453-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:49.819195-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:49.819224-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:49.819305-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Set darwin role to: None
default	13:16:49.819331-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:49.819483-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:49.825330-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-suspended (role: None) (endowments: (null))
default	13:16:49.826129-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-suspended-NotVisible
default	13:16:49.858549-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x9cbffd540) Selecting device 0 from destructor
default	13:16:49.858580-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x9cbffd540)
default	13:16:49.858593-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x9cbffd540) not already running
default	13:16:49.858607-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x9cbffd540) disconnecting device 91
default	13:16:49.858622-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x9cbffd540) destroying ioproc 0xa for device 91
default	13:16:49.858676-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:16:49.858741-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:16:49.859085-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x9cbffd540) nothing to setup
default	13:16:49.859122-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9cbffd540) adding 0 device listeners to device 0
default	13:16:49.859141-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9cbffd540) adding 0 device delegate listeners to device 0
default	13:16:49.859155-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9cbffd540) removing 7 device listeners from device 91
default	13:16:49.859690-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9cbffd540) removing 0 device delegate listeners from device 91
default	13:16:49.859723-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x9cbffd540)
default	13:16:50.002973-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60446.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=60446, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:16:50.004339-0500	tccd	AUTHREQ_SUBJECT: msgID=60446.1, subject=com.nexy.assistant,
default	13:16:50.005004-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:16:50.019277-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.13705, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=60446, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:50.020184-0500	tccd	AUTHREQ_SUBJECT: msgID=393.13705, subject=com.nexy.assistant,
default	13:16:50.020832-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:16:50.053152-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:16:50.069729-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 60386: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 48641e00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	13:16:50.080259-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:50.930957-0500	Nexy	[0x9ca894640] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:16:50.932099-0500	Nexy	[0x9ca8948c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:16:50.935036-0500	Nexy	Received configuration update from daemon (initial)
default	13:16:50.981408-0500	Nexy	[0x9ca894a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:16:50.982036-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:16:50.982214-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60376.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:50.983916-0500	tccd	AUTHREQ_SUBJECT: msgID=60376.2, subject=com.nexy.assistant,
default	13:16:50.984636-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:16:50.997870-0500	Nexy	[0x9ca894a00] invalidated after the last release of the connection object
default	13:16:50.998677-0500	Nexy	[0x9ca894a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:16:50.999056-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:16:50.999219-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60376.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:51.000056-0500	tccd	AUTHREQ_SUBJECT: msgID=60376.3, subject=com.nexy.assistant,
default	13:16:51.000650-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:16:51.012953-0500	Nexy	[0x9ca894a00] invalidated after the last release of the connection object
default	13:16:51.013005-0500	Nexy	[0x9ca894a00] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:16:51.013093-0500	Nexy	[0x9ca894a00] invalidated after the last release of the connection object
default	13:16:51.013411-0500	Nexy	[0x9ca894b40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:16:51.013851-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60376.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:51.014719-0500	tccd	AUTHREQ_SUBJECT: msgID=60376.4, subject=com.nexy.assistant,
default	13:16:51.015357-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:16:51.027930-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[60376], responsiblePID[60376], responsiblePath: /Applications/Nexy.app to UID: 501
default	13:16:51.028199-0500	Nexy	[0x9ca894b40] invalidated after the last release of the connection object
default	13:16:51.032311-0500	Nexy	server port 0x0000ed0b, session port 0x0000bf0f
default	13:16:51.033377-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.13706, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:51.033412-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:51.034816-0500	tccd	AUTHREQ_SUBJECT: msgID=393.13706, subject=com.nexy.assistant,
default	13:16:51.035540-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:16:51.036484-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	13:16:51.057008-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	13:16:51.061511-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:16:51.079235-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 946D2265-AC5A-454B-9CAC-29F413517576 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52650,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xe1acbb9f tp_proto=0x06"
default	13:16:51.079319-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52650<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020278 t_state: SYN_SENT process: Nexy:60376 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xba053cf0
default	13:16:51.079936-0500	kernel	tcp connected: [<IPv4-redacted>:52650<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020278 t_state: ESTABLISHED process: Nexy:60376 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xba053cf0
default	13:16:51.080730-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	13:16:51.080821-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52650<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020278 t_state: FIN_WAIT_1 process: Nexy:60376 Duration: 0.002 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xba053cf0
default	13:16:51.080832-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52650<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020278 t_state: FIN_WAIT_1 process: Nexy:60376 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:16:51.080908-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	13:16:51.081154-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 1A2BE85E-7299-4E48-A3C7-96FC95B1A960 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52651,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xd86248ed tp_proto=0x06"
default	13:16:51.081182-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52651<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020279 t_state: SYN_SENT process: Nexy:60376 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9acc24f7
default	13:16:51.081343-0500	kernel	tcp connected: [<IPv4-redacted>:52651<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020279 t_state: ESTABLISHED process: Nexy:60376 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9acc24f7
default	13:16:51.081660-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52651<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020279 t_state: FIN_WAIT_1 process: Nexy:60376 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x9acc24f7
default	13:16:51.081670-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52651<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 5020279 t_state: FIN_WAIT_1 process: Nexy:60376 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:16:51.081841-0500	Nexy	nw_path_libinfo_path_check [A24C93B0-3377-442A-8102-9E99AC17F242 IPv4#82a5483b:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	13:16:51.082753-0500	Nexy	server port 0x0000bf0f, session port 0x0000bf0f
default	13:16:51.083208-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid BF93D416-9DE3-4E21-A7BA-2D77A46E6C94 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52652,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x473d579a tp_proto=0x06"
default	13:16:51.083235-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52652<-><IPv4-redacted>:443] interface: utun6 (skipped: 6743)
so_gencnt: 5020280 t_state: SYN_SENT process: Nexy:60376 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x936c65c7
default	13:16:51.083822-0500	kernel	tcp connected: [<IPv4-redacted>:52652<-><IPv4-redacted>:443] interface: utun6 (skipped: 6743)
so_gencnt: 5020280 t_state: ESTABLISHED process: Nexy:60376 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x936c65c7
default	13:16:51.084048-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.13707, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:51.084090-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:51.085431-0500	tccd	AUTHREQ_SUBJECT: msgID=393.13707, subject=com.nexy.assistant,
default	13:16:51.086251-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	13:16:51.097713-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:16:51.104938-0500	Nexy	[0x9ca894b40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:16:51.107500-0500	Nexy	New connection 0x1988ff main
default	13:16:51.107696-0500	Nexy	[0x9ca894c80] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:16:51.110877-0500	Nexy	[0x9ca894f00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:16:51.113039-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	13:16:51.116833-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:16:51.241398-0500	Nexy	[0x9ca894dc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:16:51.242098-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60376.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:51.248836-0500	tccd	AUTHREQ_SUBJECT: msgID=60376.5, subject=com.nexy.assistant,
default	13:16:51.249526-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	13:16:51.262557-0500	Nexy	[0x9ca894dc0] invalidated after the last release of the connection object
default	13:16:51.272767-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:16:51.275168-0500	Nexy	CHECKIN: pid=60376
default	13:16:51.282818-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:60376" ID:398-363-1347254 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:16:51.282876-0500	launchservicesd	CHECKIN:0x0-0x1459458 60376 com.nexy.assistant
default	13:16:51.282933-0500	runningboardd	Assertion 398-363-1347254 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:51.283484-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:60376" ID:398-363-1347255 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:16:51.283524-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:51.283569-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:51.283556-0500	runningboardd	Assertion 398-363-1347255 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:51.283669-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Set darwin role to: UserInteractive
default	13:16:51.283705-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:51.283765-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:51.283890-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:16:51.283606-0500	Nexy	CHECKEDIN: pid=60376 asn=0x0-0x1459458 foreground=0
default	13:16:51.284118-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:16:51.284068-0500	Nexy	[0x9ca895040] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	13:16:51.284621-0500	Nexy	[0x9ca895180] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:16:51.284631-0500	Nexy	[0x9ca895180] Connection returned listener port: 0x10203
default	13:16:51.284759-0500	Nexy	[0x9ca410600] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x9ca895180.peer[363].0x9ca410600
default	13:16:51.285604-0500	Nexy	FRONTLOGGING: version 1
default	13:16:51.285640-0500	Nexy	Registered, pid=60376 ASN=0x0,0x1459458
default	13:16:51.285835-0500	WindowServer	1988ff[CreateApplication]: Process creation: 0x0-0x1459458 (Nexy) connectionID: 1988FF pid: 60376 in session 0x101
default	13:16:51.287998-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:51.288335-0500	runningboardd	Invalidating assertion 398-363-1347254 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	13:16:51.288670-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:51.288794-0500	Nexy	[0x9ca895180] Connection returned listener port: 0x10203
default	13:16:51.289184-0500	Nexy	BringForward: pid=60376 asn=0x0-0x1459458 bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	13:16:51.289624-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:16:51.291632-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:16:51.292454-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:16:51.327111-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:16:51.327290-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:16:51.333815-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:16:51.333830-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:16:51.333901-0500	Nexy	Initializing connection
default	13:16:51.333964-0500	Nexy	Removing all cached process handles
default	13:16:51.333990-0500	Nexy	Sending handshake request attempt #1 to server
default	13:16:51.333997-0500	Nexy	Creating connection to com.apple.runningboard
default	13:16:51.334012-0500	Nexy	[0x9ca8952c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:16:51.334530-0500	Nexy	[0x9ca895180] Connection returned listener port: 0x10203
default	13:16:51.335134-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] as ready
default	13:16:51.336117-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 2d00000024 pid: 60376
default	13:16:51.336281-0500	Nexy	Handshake succeeded
default	13:16:51.336298-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.20360897.20360903(501)>
default	13:16:51.338756-0500	Nexy	[0x9ca895180] Connection returned listener port: 0x10203
default	13:16:51.341133-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:16:51.341181-0500	Nexy	[0x9ca895540] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:16:51.341335-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:16:51.341430-0500	Nexy	[0x9ca895680] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:16:51.345029-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "frontmost:60376" ID:398-363-1347263 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractiveFocal" sourceEnvironment:"(null)">
	]>
default	13:16:51.345118-0500	runningboardd	Assertion 398-363-1347263 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:51.345362-0500	WindowServer	1988ff[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x1459458 (Nexy) mainConnectionID: 1988FF;
} for reason: updated frontmost process
default	13:16:51.345468-0500	WindowServer	1988ff[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x1459458 (Nexy) -> <pid: 60376>
default	13:16:51.345602-0500	WindowServer	new deferring rules for pid:393: [
    [393-BECD]; <keyboardFocus; Nexy:0x0-0x1459458>; () -> <pid: 60376>; reason: frontmost PSN --> outbound target,
    [393-BECC]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x1459458; pid: 393>; reason: frontmost PSN,
    [393-BECB]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	13:16:51.345769-0500	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-BECD]; <keyboardFocus; Nexy:0x0-0x1459458>; () -> <pid: 60376>; reason: frontmost PSN --> outbound target,
    [393-BECC]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x1459458; pid: 393>; reason: frontmost PSN,
    [393-BECB]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	13:16:51.347435-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x1459458; pid: 393>,
    <pid: 60376>
]
default	13:16:51.349888-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:51.349942-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:51.350013-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Set darwin role to: UserInteractiveFocal
default	13:16:51.350039-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:51.350121-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:51.350111-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "notification:60376" ID:398-363-1347264 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	13:16:51.350258-0500	runningboardd	Assertion 398-363-1347264 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:51.354337-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	13:16:51.355201-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:51.355211-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:51.355222-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:51.355293-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:51.355663-0500	Nexy	[0x9ca895680] Connection returned listener port: 0x11803
default	13:16:51.366579-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	13:16:51.372488-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	13:16:51.386262-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x9caf21360
 (
    "<NSAquaAppearance: 0x9caf21400>",
    "<NSSystemAppearance: 0x9caf212c0>"
)>
default	13:16:51.409773-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:51.410957-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22120 <private>> attempting immediate handshake from activate
default	13:16:51.411077-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22120 <private>> sent handshake
default	13:16:51.411272-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	13:16:51.413851-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22120 <private>> was invalidated
default	13:16:51.413969-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	13:16:51.413922-0500	Nexy	FBSWorkspace unregistering source: <private>
default	13:16:51.416522-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	13:16:51.424283-0500	Nexy	Request for <FBSScene: 0x9caf223a0; com.apple.controlcenter:A10F4B8A-C9C2-48D2-98BA-EBC1C9E71CE0> complete!
default	13:16:51.424906-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:51.432936-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	13:16:51.439611-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	13:16:51.453752-0500	Nexy	Registering for test daemon availability notify post.
default	13:16:51.454030-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:16:51.454145-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:16:51.454258-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:16:51.456980-0500	Nexy	[0x9ca896580] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	13:16:51.457845-0500	Nexy	[0x9ca895180] Connection returned listener port: 0x10203
default	13:16:51.458261-0500	Nexy	SignalReady: pid=60376 asn=0x0-0x1459458
default	13:16:51.458597-0500	Nexy	SIGNAL: pid=60376 asn=0x0x-0x1459458
default	13:16:51.459333-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:16:51.462271-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
error	13:16:51.467458-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
default	13:16:51.472968-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	13:16:51.486519-0500	Nexy	[0x9ca896800] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:16:51.487071-0500	Nexy	[0x9ca896940] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:16:51.487080-0500	Nexy	[0x9ca896940] Connection returned listener port: 0x16003
default	13:16:51.490659-0500	WindowManager	Connection activated | (60376) Nexy
default	13:16:51.491166-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] from originator [app<application.com.nexy.assistant.20360897.20360903(501)>:60376] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-60376-1347267 target:60376 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:16:51.491241-0500	runningboardd	Assertion 398-60376-1347267 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) will be created as active
default	13:16:51.491568-0500	runningboardd	Invalidating assertion 398-60376-1347267 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [app<application.com.nexy.assistant.20360897.20360903(501)>:60376]
default	13:16:51.491619-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:51.516541-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:51.516577-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:51.516596-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:51.516628-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:51.592901-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	13:16:51.598581-0500	Nexy	Start service name com.apple.spotlightknowledged
default	13:16:51.599600-0500	Nexy	[GMS] availability notification token 75
default	13:16:51.727654-0500	Nexy	[0x9ca894a00] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	13:16:51.735415-0500	Nexy	+[IMKClient subclass]: chose IMKClient_Modern
default	13:16:51.735482-0500	Nexy	+[IMKInputSession subclass]: chose IMKInputSession_Modern
default	13:16:51.738495-0500	Nexy	[0x9ca8966c0] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	13:16:51.739588-0500	Nexy	[0x9ca896a80] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	13:16:51.740298-0500	Nexy	[0x9ca896bc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:16:51.740518-0500	Nexy	[0x9ca896e40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:16:51.740988-0500	DictationIM	setting current input controller = com.nexy.assistant
default	13:16:51.741733-0500	Nexy	[0x9ca896d00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:16:51.743283-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=60376, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:16:51.743386-0500	Nexy	[0x9ca896d00] invalidated after the last release of the connection object
default	13:16:51.748529-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) NSAccessibility Request Received
default	13:16:51.943075-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49935)
default	13:16:51.943120-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49935 called from <private>
default	13:16:51.943134-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49935 called from <private>
default	13:16:51.943305-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49934)
default	13:16:51.943322-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49934 called from <private>
default	13:16:51.943330-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49934 called from <private>
default	13:16:51.947468-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49934 called from <private>
default	13:16:51.947484-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49934 called from <private>
default	13:16:51.947632-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49934)
default	13:16:51.947649-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:49934 called from <private>
default	13:16:51.947654-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:49934 called from <private>
default	13:16:51.951899-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49934)
default	13:16:51.951920-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:49934 called from <private>
default	13:16:51.951925-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:49934 called from <private>
default	13:16:51.952975-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49934)
default	13:16:51.961509-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49934)
default	13:16:51.962146-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49934 called from <private>
default	13:16:51.962158-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49934 called from <private>
default	13:16:51.962167-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49934 called from <private>
default	13:16:51.962178-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49934 called from <private>
default	13:16:51.962186-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49934 called from <private>
default	13:16:51.962189-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49934 called from <private>
default	13:16:51.967756-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49934)
default	13:16:51.971257-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49935)
default	13:16:51.971283-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49935 called from <private>
default	13:16:51.971291-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49935 called from <private>
default	13:16:51.973015-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49934 called from <private>
default	13:16:51.973026-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49934 called from <private>
default	13:16:51.987785-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:49934 called from <private>
default	13:16:51.987802-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:49934 called from <private>
default	13:16:51.987951-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49934)
default	13:16:51.995975-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49934)
default	13:16:51.996248-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:49934 called from <private>
default	13:16:51.996262-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:49934 called from <private>
default	13:16:51.996416-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49934)
default	13:16:52.006916-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49934)
default	13:16:52.007481-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49934 called from <private>
default	13:16:52.007503-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49934 called from <private>
default	13:16:52.007589-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49934 called from <private>
default	13:16:52.007600-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49934 called from <private>
default	13:16:52.007616-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49934 called from <private>
default	13:16:52.007623-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49934 called from <private>
default	13:16:52.007745-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49934 called from <private>
default	13:16:52.008013-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49934 called from <private>
default	13:16:52.008070-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49934 called from <private>
default	13:16:52.008150-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49934 called from <private>
default	13:16:52.008188-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49934 called from <private>
default	13:16:52.008218-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49934 called from <private>
default	13:16:52.318922-0500	runningboardd	Invalidating assertion 398-363-1347263 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	13:16:52.325309-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	13:16:52.421363-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:52.421380-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:52.421432-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Set darwin role to: UserInteractive
default	13:16:52.421447-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:52.421466-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:52.424755-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:52.425175-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:52.468115-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:52.468149-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:52.468230-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> attempting immediate handshake from activate
default	13:16:52.468260-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> sent handshake
default	13:16:52.468597-0500	Nexy	Requesting scene <FBSScene: 0x9caf23020; com.apple.controlcenter:A931611B-F7D9-4941-94A6-BD2A92D98CA4> from com.apple.controlcenter.statusitems
default	13:16:52.468875-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> was invalidated
default	13:16:52.468913-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:16:52.469003-0500	Nexy	Error creating <FBSScene: 0x9caf23020; com.apple.controlcenter:A931611B-F7D9-4941-94A6-BD2A92D98CA4>: <NSError: 0x9cd00bed0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:16:52.469033-0500	Nexy	No scene exists for identity: com.apple.controlcenter:A931611B-F7D9-4941-94A6-BD2A92D98CA4
default	13:16:52.469355-0500	Nexy	Request for <FBSScene: 0x9caf23020; com.apple.controlcenter:A931611B-F7D9-4941-94A6-BD2A92D98CA4> complete!
default	13:16:52.469479-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	13:16:52.472166-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:52.472192-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:52.472271-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf230c0 <private>> attempting immediate handshake from activate
default	13:16:52.472294-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf230c0 <private>> sent handshake
default	13:16:52.472409-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	13:16:52.473011-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	13:16:52.473368-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf230c0 <private>> was invalidated
default	13:16:52.473396-0500	Nexy	FBSWorkspace unregistering source: <private>
default	13:16:52.473496-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	13:16:52.473552-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	13:16:52.474145-0500	Nexy	Requesting scene <FBSScene: 0x9caf22f80; com.apple.controlcenter:A931611B-F7D9-4941-94A6-BD2A92D98CA4-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	13:16:52.474400-0500	Nexy	Error creating <FBSScene: 0x9caf22f80; com.apple.controlcenter:A931611B-F7D9-4941-94A6-BD2A92D98CA4-Aux[1]-NSStatusItemView>: <NSError: 0x9cd00bf00; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	13:16:52.474488-0500	Nexy	Request for <FBSScene: 0x9caf22f80; com.apple.controlcenter:A931611B-F7D9-4941-94A6-BD2A92D98CA4-Aux[1]-NSStatusItemView> complete!
error	13:16:52.475100-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:52.475155-0500	Nexy	[com.apple.controlcenter:A931611B-F7D9-4941-94A6-BD2A92D98CA4] No matching scene to invalidate for this identity.
error	13:16:52.475191-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:52.475279-0500	Nexy	Unhandled disconnected scene <private>
error	13:16:52.475366-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:16:52.803575-0500	DictationIM	setting current input controller = com.nexy.assistant
default	13:16:53.476341-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:53.476368-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:53.476440-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> attempting immediate handshake from activate
default	13:16:53.476469-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> sent handshake
default	13:16:53.476728-0500	Nexy	Requesting scene <FBSScene: 0x9caf23020; com.apple.controlcenter:2E0A5CEE-DCD5-4719-8B6E-0DFC44DE7DF5> from com.apple.controlcenter.statusitems
default	13:16:53.477222-0500	Nexy	Request for <FBSScene: 0x9caf23020; com.apple.controlcenter:2E0A5CEE-DCD5-4719-8B6E-0DFC44DE7DF5> complete!
default	13:16:53.477401-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> was invalidated
default	13:16:53.477447-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:16:53.477608-0500	Nexy	Error creating <FBSScene: 0x9caf23020; com.apple.controlcenter:2E0A5CEE-DCD5-4719-8B6E-0DFC44DE7DF5>: <NSError: 0x9cb00bcf0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:16:53.477641-0500	Nexy	No scene exists for identity: com.apple.controlcenter:2E0A5CEE-DCD5-4719-8B6E-0DFC44DE7DF5
default	13:16:53.477686-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:53.477727-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:53.477777-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> attempting immediate handshake from activate
default	13:16:53.477797-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> sent handshake
default	13:16:53.477957-0500	Nexy	Requesting scene <FBSScene: 0x9caf23200; com.apple.controlcenter:2E0A5CEE-DCD5-4719-8B6E-0DFC44DE7DF5-Aux[2]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	13:16:53.478396-0500	Nexy	Request for <FBSScene: 0x9caf23200; com.apple.controlcenter:2E0A5CEE-DCD5-4719-8B6E-0DFC44DE7DF5-Aux[2]-NSStatusItemView> complete!
default	13:16:53.478473-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> was invalidated
default	13:16:53.478521-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:16:53.478606-0500	Nexy	Error creating <FBSScene: 0x9caf23200; com.apple.controlcenter:2E0A5CEE-DCD5-4719-8B6E-0DFC44DE7DF5-Aux[2]-NSStatusItemView>: <NSError: 0x9cb00bde0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:16:53.478646-0500	Nexy	No scene exists for identity: com.apple.controlcenter:2E0A5CEE-DCD5-4719-8B6E-0DFC44DE7DF5-Aux[2]-NSStatusItemView
default	13:16:53.479214-0500	Nexy	[com.apple.controlcenter:2E0A5CEE-DCD5-4719-8B6E-0DFC44DE7DF5-Aux[2]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	13:16:53.479527-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:53.479567-0500	Nexy	[com.apple.controlcenter:2E0A5CEE-DCD5-4719-8B6E-0DFC44DE7DF5] No matching scene to invalidate for this identity.
error	13:16:53.479599-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:53.479614-0500	Nexy	[com.apple.controlcenter:2E0A5CEE-DCD5-4719-8B6E-0DFC44DE7DF5-Aux[2]-NSStatusItemView] No matching scene to invalidate for this identity.
error	13:16:53.480262-0500	Nexy	Unhandled disconnected scene <private>
error	13:16:53.480411-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	13:16:53.480516-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	13:16:53.480611-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:16:54.482426-0500	Nexy	[com.apple.controlcenter:CD5C36BE-67F5-4F4A-B6DB-A69B798BD74A-Aux[3]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:16:54.482453-0500	Nexy	[com.apple.controlcenter:CD5C36BE-67F5-4F4A-B6DB-A69B798BD74A-Aux[3]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	13:16:55.489337-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:55.489361-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:55.489423-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23020 <private>> attempting immediate handshake from activate
default	13:16:55.489444-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23020 <private>> sent handshake
default	13:16:55.489644-0500	Nexy	Requesting scene <FBSScene: 0x9caf232a0; com.apple.controlcenter:000B6998-4139-4F61-8B23-20743B025F97> from com.apple.controlcenter.statusitems
default	13:16:55.489826-0500	Nexy	Request for <FBSScene: 0x9caf232a0; com.apple.controlcenter:000B6998-4139-4F61-8B23-20743B025F97> complete!
default	13:16:55.490082-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23020 <private>> was invalidated
default	13:16:55.490103-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:16:55.490178-0500	Nexy	Error creating <FBSScene: 0x9caf232a0; com.apple.controlcenter:000B6998-4139-4F61-8B23-20743B025F97>: <NSError: 0x9cb00bc00; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:16:55.490194-0500	Nexy	No scene exists for identity: com.apple.controlcenter:000B6998-4139-4F61-8B23-20743B025F97
default	13:16:55.490222-0500	Nexy	Requesting scene <FBSScene: 0x9caf23200; com.apple.controlcenter:000B6998-4139-4F61-8B23-20743B025F97-Aux[4]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	13:16:55.490313-0500	Nexy	Error creating <FBSScene: 0x9caf23200; com.apple.controlcenter:000B6998-4139-4F61-8B23-20743B025F97-Aux[4]-NSStatusItemView>: <NSError: 0x9cd00bf00; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	13:16:55.490350-0500	Nexy	Request for <FBSScene: 0x9caf23200; com.apple.controlcenter:000B6998-4139-4F61-8B23-20743B025F97-Aux[4]-NSStatusItemView> complete!
error	13:16:55.490479-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:55.490499-0500	Nexy	[com.apple.controlcenter:000B6998-4139-4F61-8B23-20743B025F97] No matching scene to invalidate for this identity.
error	13:16:55.490520-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:55.490545-0500	Nexy	Unhandled disconnected scene <private>
error	13:16:55.490586-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:16:56.491935-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:56.491977-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:56.492101-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> attempting immediate handshake from activate
default	13:16:56.492145-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> sent handshake
default	13:16:56.492485-0500	Nexy	Requesting scene <FBSScene: 0x9caf232a0; com.apple.controlcenter:624CBE28-1078-47F2-BD71-664210C0EA45> from com.apple.controlcenter.statusitems
default	13:16:56.492774-0500	Nexy	Request for <FBSScene: 0x9caf232a0; com.apple.controlcenter:624CBE28-1078-47F2-BD71-664210C0EA45> complete!
default	13:16:56.493186-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> was invalidated
default	13:16:56.493228-0500	Nexy	FBSWorkspace unregistering source: <private>
default	13:16:56.493299-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:56.493325-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:56.493401-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23020 <private>> attempting immediate handshake from activate
default	13:16:56.493433-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23020 <private>> sent handshake
error	13:16:56.493519-0500	Nexy	Error creating <FBSScene: 0x9caf232a0; com.apple.controlcenter:624CBE28-1078-47F2-BD71-664210C0EA45>: <NSError: 0x9cb00bcc0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:16:56.493540-0500	Nexy	No scene exists for identity: com.apple.controlcenter:624CBE28-1078-47F2-BD71-664210C0EA45
default	13:16:56.493603-0500	Nexy	Requesting scene <FBSScene: 0x9caf23160; com.apple.controlcenter:624CBE28-1078-47F2-BD71-664210C0EA45-Aux[5]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	13:16:56.493761-0500	Nexy	Request for <FBSScene: 0x9caf23160; com.apple.controlcenter:624CBE28-1078-47F2-BD71-664210C0EA45-Aux[5]-NSStatusItemView> complete!
default	13:16:56.493935-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23020 <private>> was invalidated
default	13:16:56.493952-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:16:56.493993-0500	Nexy	Error creating <FBSScene: 0x9caf23160; com.apple.controlcenter:624CBE28-1078-47F2-BD71-664210C0EA45-Aux[5]-NSStatusItemView>: <NSError: 0x9cb8580c0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:16:56.494004-0500	Nexy	No scene exists for identity: com.apple.controlcenter:624CBE28-1078-47F2-BD71-664210C0EA45-Aux[5]-NSStatusItemView
default	13:16:56.494203-0500	Nexy	[com.apple.controlcenter:624CBE28-1078-47F2-BD71-664210C0EA45-Aux[5]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	13:16:56.494499-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:56.494544-0500	Nexy	[com.apple.controlcenter:624CBE28-1078-47F2-BD71-664210C0EA45] No matching scene to invalidate for this identity.
error	13:16:56.494586-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:56.494611-0500	Nexy	[com.apple.controlcenter:624CBE28-1078-47F2-BD71-664210C0EA45-Aux[5]-NSStatusItemView] No matching scene to invalidate for this identity.
error	13:16:56.495028-0500	Nexy	Unhandled disconnected scene <private>
error	13:16:56.495114-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	13:16:56.495222-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	13:16:56.495274-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:16:56.619441-0500	runningboardd	Assertion did invalidate due to timeout: 398-363-1347264 (target:[app<application.com.nexy.assistant.20360897.20360903(501)>:60376])
default	13:16:56.818840-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring jetsam update because this process is not memory-managed
default	13:16:56.818859-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring suspend because this process is not lifecycle managed
default	13:16:56.818871-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring GPU update because this process is not GPU managed
default	13:16:56.818891-0500	runningboardd	[app<application.com.nexy.assistant.20360897.20360903(501)>:60376] Ignoring memory limit update because this process is not memory-managed
default	13:16:56.823890-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20360897.20360903(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:56.824487-0500	gamepolicyd	Received state update for 60376 (app<application.com.nexy.assistant.20360897.20360903(501)>, running-active-NotVisible
default	13:16:57.385858-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	13:16:57.401014-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:16:57.495748-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:57.495774-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:57.495834-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23160 <private>> attempting immediate handshake from activate
default	13:16:57.495887-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23160 <private>> sent handshake
default	13:16:57.496128-0500	Nexy	Requesting scene <FBSScene: 0x9caf232a0; com.apple.controlcenter:F0C86E68-5AED-48ED-B3A3-BA43F0C45B2A> from com.apple.controlcenter.statusitems
default	13:16:57.496293-0500	Nexy	Request for <FBSScene: 0x9caf232a0; com.apple.controlcenter:F0C86E68-5AED-48ED-B3A3-BA43F0C45B2A> complete!
default	13:16:57.496491-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23160 <private>> was invalidated
default	13:16:57.496546-0500	Nexy	FBSWorkspace unregistering source: <private>
default	13:16:57.496637-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:57.496651-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:57.496716-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> attempting immediate handshake from activate
default	13:16:57.496735-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> sent handshake
error	13:16:57.496814-0500	Nexy	Error creating <FBSScene: 0x9caf232a0; com.apple.controlcenter:F0C86E68-5AED-48ED-B3A3-BA43F0C45B2A>: <NSError: 0x9cb00bb40; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:16:57.496857-0500	Nexy	No scene exists for identity: com.apple.controlcenter:F0C86E68-5AED-48ED-B3A3-BA43F0C45B2A
default	13:16:57.496958-0500	Nexy	Requesting scene <FBSScene: 0x9caf23200; com.apple.controlcenter:F0C86E68-5AED-48ED-B3A3-BA43F0C45B2A-Aux[6]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	13:16:57.497095-0500	Nexy	Request for <FBSScene: 0x9caf23200; com.apple.controlcenter:F0C86E68-5AED-48ED-B3A3-BA43F0C45B2A-Aux[6]-NSStatusItemView> complete!
default	13:16:57.497117-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> was invalidated
default	13:16:57.497164-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:16:57.497234-0500	Nexy	Error creating <FBSScene: 0x9caf23200; com.apple.controlcenter:F0C86E68-5AED-48ED-B3A3-BA43F0C45B2A-Aux[6]-NSStatusItemView>: <NSError: 0x9cb858120; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:16:57.497267-0500	Nexy	No scene exists for identity: com.apple.controlcenter:F0C86E68-5AED-48ED-B3A3-BA43F0C45B2A-Aux[6]-NSStatusItemView
default	13:16:57.497484-0500	Nexy	[com.apple.controlcenter:F0C86E68-5AED-48ED-B3A3-BA43F0C45B2A-Aux[6]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	13:16:57.497643-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:57.497657-0500	Nexy	[com.apple.controlcenter:F0C86E68-5AED-48ED-B3A3-BA43F0C45B2A] No matching scene to invalidate for this identity.
error	13:16:57.497678-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:57.497688-0500	Nexy	[com.apple.controlcenter:F0C86E68-5AED-48ED-B3A3-BA43F0C45B2A-Aux[6]-NSStatusItemView] No matching scene to invalidate for this identity.
error	13:16:57.497931-0500	Nexy	Unhandled disconnected scene <private>
error	13:16:57.497986-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	13:16:57.498028-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	13:16:57.498058-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:16:58.498645-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:58.498703-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:58.498796-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> attempting immediate handshake from activate
default	13:16:58.498828-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> sent handshake
default	13:16:58.499156-0500	Nexy	Requesting scene <FBSScene: 0x9caf232a0; com.apple.controlcenter:9685E62A-9D63-4A85-8946-92D7F0545760> from com.apple.controlcenter.statusitems
default	13:16:58.499473-0500	Nexy	Request for <FBSScene: 0x9caf232a0; com.apple.controlcenter:9685E62A-9D63-4A85-8946-92D7F0545760> complete!
default	13:16:58.499890-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> was invalidated
default	13:16:58.499918-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:16:58.500024-0500	Nexy	Error creating <FBSScene: 0x9caf232a0; com.apple.controlcenter:9685E62A-9D63-4A85-8946-92D7F0545760>: <NSError: 0x9cb00bcc0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:16:58.500041-0500	Nexy	No scene exists for identity: com.apple.controlcenter:9685E62A-9D63-4A85-8946-92D7F0545760
default	13:16:58.500097-0500	Nexy	Requesting scene <FBSScene: 0x9caf22f80; com.apple.controlcenter:9685E62A-9D63-4A85-8946-92D7F0545760-Aux[7]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	13:16:58.500324-0500	Nexy	Error creating <FBSScene: 0x9caf22f80; com.apple.controlcenter:9685E62A-9D63-4A85-8946-92D7F0545760-Aux[7]-NSStatusItemView>: <NSError: 0x9cd00bf30; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	13:16:58.500422-0500	Nexy	Request for <FBSScene: 0x9caf22f80; com.apple.controlcenter:9685E62A-9D63-4A85-8946-92D7F0545760-Aux[7]-NSStatusItemView> complete!
error	13:16:58.500654-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:58.500684-0500	Nexy	[com.apple.controlcenter:9685E62A-9D63-4A85-8946-92D7F0545760] No matching scene to invalidate for this identity.
error	13:16:58.500710-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:58.500736-0500	Nexy	Unhandled disconnected scene <private>
error	13:16:58.500799-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:16:59.502130-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:59.502191-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:59.502334-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> attempting immediate handshake from activate
default	13:16:59.502387-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> sent handshake
default	13:16:59.502852-0500	Nexy	Requesting scene <FBSScene: 0x9caf232a0; com.apple.controlcenter:27286037-0041-4B91-95DE-EE9EF37496B9> from com.apple.controlcenter.statusitems
default	13:16:59.503262-0500	Nexy	Request for <FBSScene: 0x9caf232a0; com.apple.controlcenter:27286037-0041-4B91-95DE-EE9EF37496B9> complete!
default	13:16:59.503779-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> was invalidated
default	13:16:59.503844-0500	Nexy	FBSWorkspace unregistering source: <private>
default	13:16:59.503971-0500	Nexy	FBSWorkspace registering source: <private>
default	13:16:59.504009-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:16:59.504103-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> attempting immediate handshake from activate
default	13:16:59.504146-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> sent handshake
error	13:16:59.504261-0500	Nexy	Error creating <FBSScene: 0x9caf232a0; com.apple.controlcenter:27286037-0041-4B91-95DE-EE9EF37496B9>: <NSError: 0x9cb00bc00; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:16:59.504304-0500	Nexy	No scene exists for identity: com.apple.controlcenter:27286037-0041-4B91-95DE-EE9EF37496B9
default	13:16:59.504430-0500	Nexy	Requesting scene <FBSScene: 0x9caf23160; com.apple.controlcenter:27286037-0041-4B91-95DE-EE9EF37496B9-Aux[8]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	13:16:59.504750-0500	Nexy	Request for <FBSScene: 0x9caf23160; com.apple.controlcenter:27286037-0041-4B91-95DE-EE9EF37496B9-Aux[8]-NSStatusItemView> complete!
default	13:16:59.505098-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> was invalidated
default	13:16:59.505145-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:16:59.505249-0500	Nexy	Error creating <FBSScene: 0x9caf23160; com.apple.controlcenter:27286037-0041-4B91-95DE-EE9EF37496B9-Aux[8]-NSStatusItemView>: <NSError: 0x9cb8580c0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:16:59.505280-0500	Nexy	No scene exists for identity: com.apple.controlcenter:27286037-0041-4B91-95DE-EE9EF37496B9-Aux[8]-NSStatusItemView
default	13:16:59.505429-0500	Nexy	[com.apple.controlcenter:27286037-0041-4B91-95DE-EE9EF37496B9-Aux[8]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	13:16:59.505651-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:59.505667-0500	Nexy	[com.apple.controlcenter:27286037-0041-4B91-95DE-EE9EF37496B9] No matching scene to invalidate for this identity.
error	13:16:59.505693-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:16:59.505707-0500	Nexy	[com.apple.controlcenter:27286037-0041-4B91-95DE-EE9EF37496B9-Aux[8]-NSStatusItemView] No matching scene to invalidate for this identity.
error	13:16:59.506074-0500	Nexy	Unhandled disconnected scene <private>
error	13:16:59.506146-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	13:16:59.506195-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	13:16:59.506230-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:17:00.507308-0500	Nexy	FBSWorkspace registering source: <private>
default	13:17:00.507373-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:17:00.507519-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23160 <private>> attempting immediate handshake from activate
default	13:17:00.507571-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23160 <private>> sent handshake
default	13:17:00.508044-0500	Nexy	Requesting scene <FBSScene: 0x9caf232a0; com.apple.controlcenter:F54098A2-2EDC-4254-9FC2-6C706287FB09> from com.apple.controlcenter.statusitems
default	13:17:00.508500-0500	Nexy	Request for <FBSScene: 0x9caf232a0; com.apple.controlcenter:F54098A2-2EDC-4254-9FC2-6C706287FB09> complete!
default	13:17:00.508980-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23160 <private>> was invalidated
default	13:17:00.509018-0500	Nexy	FBSWorkspace unregistering source: <private>
default	13:17:00.509084-0500	Nexy	FBSWorkspace registering source: <private>
default	13:17:00.509103-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:17:00.509149-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> attempting immediate handshake from activate
default	13:17:00.509170-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> sent handshake
error	13:17:00.509236-0500	Nexy	Error creating <FBSScene: 0x9caf232a0; com.apple.controlcenter:F54098A2-2EDC-4254-9FC2-6C706287FB09>: <NSError: 0x9cb00bea0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:17:00.509253-0500	Nexy	No scene exists for identity: com.apple.controlcenter:F54098A2-2EDC-4254-9FC2-6C706287FB09
default	13:17:00.509327-0500	Nexy	Requesting scene <FBSScene: 0x9caf22f80; com.apple.controlcenter:F54098A2-2EDC-4254-9FC2-6C706287FB09-Aux[9]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	13:17:00.509510-0500	Nexy	Request for <FBSScene: 0x9caf22f80; com.apple.controlcenter:F54098A2-2EDC-4254-9FC2-6C706287FB09-Aux[9]-NSStatusItemView> complete!
default	13:17:00.509730-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf23200 <private>> was invalidated
default	13:17:00.509753-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:17:00.509803-0500	Nexy	Error creating <FBSScene: 0x9caf22f80; com.apple.controlcenter:F54098A2-2EDC-4254-9FC2-6C706287FB09-Aux[9]-NSStatusItemView>: <NSError: 0x9cb8580c0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:17:00.509850-0500	Nexy	No scene exists for identity: com.apple.controlcenter:F54098A2-2EDC-4254-9FC2-6C706287FB09-Aux[9]-NSStatusItemView
default	13:17:00.510036-0500	Nexy	[com.apple.controlcenter:F54098A2-2EDC-4254-9FC2-6C706287FB09-Aux[9]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	13:17:00.510339-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:17:00.510365-0500	Nexy	[com.apple.controlcenter:F54098A2-2EDC-4254-9FC2-6C706287FB09] No matching scene to invalidate for this identity.
error	13:17:00.510427-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:17:00.510462-0500	Nexy	[com.apple.controlcenter:F54098A2-2EDC-4254-9FC2-6C706287FB09-Aux[9]-NSStatusItemView] No matching scene to invalidate for this identity.
error	13:17:00.510936-0500	Nexy	Unhandled disconnected scene <private>
error	13:17:00.511023-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	13:17:00.511080-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	13:17:00.511111-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:17:01.511823-0500	Nexy	FBSWorkspace registering source: <private>
default	13:17:01.511873-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:17:01.511974-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> attempting immediate handshake from activate
default	13:17:01.512012-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> sent handshake
default	13:17:01.512346-0500	Nexy	Requesting scene <FBSScene: 0x9caf232a0; com.apple.controlcenter:A33E6A0A-9E78-4F91-BB94-FBBF7428D232> from com.apple.controlcenter.statusitems
default	13:17:01.512613-0500	Nexy	Request for <FBSScene: 0x9caf232a0; com.apple.controlcenter:A33E6A0A-9E78-4F91-BB94-FBBF7428D232> complete!
default	13:17:01.513072-0500	Nexy	Requesting scene <FBSScene: 0x9caf22ee0; com.apple.controlcenter:A33E6A0A-9E78-4F91-BB94-FBBF7428D232-Aux[10]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	13:17:01.513097-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> was invalidated
default	13:17:01.513127-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:17:01.513189-0500	Nexy	Error creating <FBSScene: 0x9caf232a0; com.apple.controlcenter:A33E6A0A-9E78-4F91-BB94-FBBF7428D232>: <NSError: 0x9cb858330; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	13:17:01.513195-0500	Nexy	LSExceptions shared instance invalidated for timeout.
error	13:17:01.513206-0500	Nexy	No scene exists for identity: com.apple.controlcenter:A33E6A0A-9E78-4F91-BB94-FBBF7428D232
error	13:17:01.513235-0500	Nexy	Error creating <FBSScene: 0x9caf22ee0; com.apple.controlcenter:A33E6A0A-9E78-4F91-BB94-FBBF7428D232-Aux[10]-NSStatusItemView>: <NSError: 0x9cb858090; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:17:01.513258-0500	Nexy	No scene exists for identity: com.apple.controlcenter:A33E6A0A-9E78-4F91-BB94-FBBF7428D232-Aux[10]-NSStatusItemView
default	13:17:01.513289-0500	Nexy	Request for <FBSScene: 0x9caf22ee0; com.apple.controlcenter:A33E6A0A-9E78-4F91-BB94-FBBF7428D232-Aux[10]-NSStatusItemView> complete!
error	13:17:01.513489-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:17:01.513511-0500	Nexy	[com.apple.controlcenter:A33E6A0A-9E78-4F91-BB94-FBBF7428D232] No matching scene to invalidate for this identity.
error	13:17:01.513546-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:17:01.513587-0500	Nexy	Unhandled disconnected scene <private>
error	13:17:01.513662-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:17:02.514230-0500	Nexy	FBSWorkspace registering source: <private>
default	13:17:02.514292-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:17:02.514441-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> attempting immediate handshake from activate
default	13:17:02.514492-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> sent handshake
default	13:17:02.514959-0500	Nexy	Requesting scene <FBSScene: 0x9caf232a0; com.apple.controlcenter:EFC33B09-693E-46DD-A693-C52413DFF54E> from com.apple.controlcenter.statusitems
default	13:17:02.515368-0500	Nexy	Request for <FBSScene: 0x9caf232a0; com.apple.controlcenter:EFC33B09-693E-46DD-A693-C52413DFF54E> complete!
default	13:17:02.515970-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> was invalidated
default	13:17:02.516031-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:17:02.516216-0500	Nexy	Error creating <FBSScene: 0x9caf232a0; com.apple.controlcenter:EFC33B09-693E-46DD-A693-C52413DFF54E>: <NSError: 0x9cb00bea0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:17:02.516282-0500	Nexy	No scene exists for identity: com.apple.controlcenter:EFC33B09-693E-46DD-A693-C52413DFF54E
default	13:17:02.516360-0500	Nexy	Requesting scene <FBSScene: 0x9caf22f80; com.apple.controlcenter:EFC33B09-693E-46DD-A693-C52413DFF54E-Aux[11]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	13:17:02.516596-0500	Nexy	Error creating <FBSScene: 0x9caf22f80; com.apple.controlcenter:EFC33B09-693E-46DD-A693-C52413DFF54E-Aux[11]-NSStatusItemView>: <NSError: 0x9cd00bea0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	13:17:02.516685-0500	Nexy	Request for <FBSScene: 0x9caf22f80; com.apple.controlcenter:EFC33B09-693E-46DD-A693-C52413DFF54E-Aux[11]-NSStatusItemView> complete!
error	13:17:02.516963-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:17:02.516990-0500	Nexy	[com.apple.controlcenter:EFC33B09-693E-46DD-A693-C52413DFF54E] No matching scene to invalidate for this identity.
error	13:17:02.517033-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:17:02.517071-0500	Nexy	Unhandled disconnected scene <private>
error	13:17:02.517154-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:17:03.518589-0500	Nexy	FBSWorkspace registering source: <private>
default	13:17:03.518647-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:17:03.518788-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> attempting immediate handshake from activate
default	13:17:03.518838-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> sent handshake
default	13:17:03.519278-0500	Nexy	Requesting scene <FBSScene: 0x9caf232a0; com.apple.controlcenter:0D5AFBC7-93CE-4064-A425-0F4D9D742411> from com.apple.controlcenter.statusitems
default	13:17:03.519690-0500	Nexy	Request for <FBSScene: 0x9caf232a0; com.apple.controlcenter:0D5AFBC7-93CE-4064-A425-0F4D9D742411> complete!
default	13:17:03.520286-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> was invalidated
default	13:17:03.520351-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:17:03.520531-0500	Nexy	Error creating <FBSScene: 0x9caf232a0; com.apple.controlcenter:0D5AFBC7-93CE-4064-A425-0F4D9D742411>: <NSError: 0x9cb00b900; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:17:03.520576-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0D5AFBC7-93CE-4064-A425-0F4D9D742411
default	13:17:03.520648-0500	Nexy	Requesting scene <FBSScene: 0x9caf22ee0; com.apple.controlcenter:0D5AFBC7-93CE-4064-A425-0F4D9D742411-Aux[12]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	13:17:03.520874-0500	Nexy	Error creating <FBSScene: 0x9caf22ee0; com.apple.controlcenter:0D5AFBC7-93CE-4064-A425-0F4D9D742411-Aux[12]-NSStatusItemView>: <NSError: 0x9cd00bed0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	13:17:03.520961-0500	Nexy	Request for <FBSScene: 0x9caf22ee0; com.apple.controlcenter:0D5AFBC7-93CE-4064-A425-0F4D9D742411-Aux[12]-NSStatusItemView> complete!
error	13:17:03.521239-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:17:03.521286-0500	Nexy	[com.apple.controlcenter:0D5AFBC7-93CE-4064-A425-0F4D9D742411] No matching scene to invalidate for this identity.
error	13:17:03.521338-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:17:03.521392-0500	Nexy	Unhandled disconnected scene <private>
error	13:17:03.521492-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:17:04.522810-0500	Nexy	FBSWorkspace registering source: <private>
default	13:17:04.522866-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:17:04.523001-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> attempting immediate handshake from activate
default	13:17:04.523052-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> sent handshake
default	13:17:04.523503-0500	Nexy	Requesting scene <FBSScene: 0x9caf232a0; com.apple.controlcenter:AF28D76F-76E7-4096-A8F2-2FB1B20BB54A> from com.apple.controlcenter.statusitems
default	13:17:04.523910-0500	Nexy	Request for <FBSScene: 0x9caf232a0; com.apple.controlcenter:AF28D76F-76E7-4096-A8F2-2FB1B20BB54A> complete!
default	13:17:04.524482-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22ee0 <private>> was invalidated
default	13:17:04.524533-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:17:04.524694-0500	Nexy	Error creating <FBSScene: 0x9caf232a0; com.apple.controlcenter:AF28D76F-76E7-4096-A8F2-2FB1B20BB54A>: <NSError: 0x9cb00bf00; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:17:04.524729-0500	Nexy	No scene exists for identity: com.apple.controlcenter:AF28D76F-76E7-4096-A8F2-2FB1B20BB54A
default	13:17:04.524801-0500	Nexy	Requesting scene <FBSScene: 0x9caf22f80; com.apple.controlcenter:AF28D76F-76E7-4096-A8F2-2FB1B20BB54A-Aux[13]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	13:17:04.525032-0500	Nexy	Error creating <FBSScene: 0x9caf22f80; com.apple.controlcenter:AF28D76F-76E7-4096-A8F2-2FB1B20BB54A-Aux[13]-NSStatusItemView>: <NSError: 0x9cd0082d0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	13:17:04.525119-0500	Nexy	Request for <FBSScene: 0x9caf22f80; com.apple.controlcenter:AF28D76F-76E7-4096-A8F2-2FB1B20BB54A-Aux[13]-NSStatusItemView> complete!
error	13:17:04.525404-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:17:04.525439-0500	Nexy	[com.apple.controlcenter:AF28D76F-76E7-4096-A8F2-2FB1B20BB54A] No matching scene to invalidate for this identity.
error	13:17:04.525491-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:17:04.525546-0500	Nexy	Unhandled disconnected scene <private>
error	13:17:04.525662-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	13:17:05.525976-0500	Nexy	FBSWorkspace registering source: <private>
default	13:17:05.526021-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:17:05.526114-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> attempting immediate handshake from activate
default	13:17:05.526149-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> sent handshake
default	13:17:05.526482-0500	Nexy	Requesting scene <FBSScene: 0x9caf232a0; com.apple.controlcenter:D3BB2117-764A-4560-9C5A-BFAC4FB9260A> from com.apple.controlcenter.statusitems
default	13:17:05.526762-0500	Nexy	Request for <FBSScene: 0x9caf232a0; com.apple.controlcenter:D3BB2117-764A-4560-9C5A-BFAC4FB9260A> complete!
default	13:17:05.527254-0500	Nexy	<FBSWorkspaceScenesClient:0x9caf22f80 <private>> was invalidated
default	13:17:05.527292-0500	Nexy	FBSWorkspace unregistering source: <private>
error	13:17:05.527368-0500	Nexy	Error creating <FBSScene: 0x9caf232a0; com.apple.controlcenter:D3BB2117-764A-4560-9C5A-BFAC4FB9260A>: <NSError: 0x9cb00b9c0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	13:17:05.527388-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D3BB2117-764A-4560-9C5A-BFAC4FB9260A
error	13:17:05.527426-0500	Nexy	Error creating <FBSScene: 0x9caf23160; com.apple.controlcenter:D3BB2117-764A-4560-9C5A-BFAC4FB9260A-Aux[14]-NSStatusItemView>: <NSError: 0x9cb00bf00; domain: FBSWorkspaceErrorDomain; code: 1 ("InvalidScene"); "scene <FBSScene: 0x9caf23160; com.apple.controlcenter:D3BB2117-764A-4560-9C5A-BFAC4FB9260A-Aux[14]-NSStatusItemView> was invalidated before activation com.apple.controlcenter.statusitems">
error	13:17:05.527450-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D3BB2117-764A-4560-9C5A-BFAC4FB9260A-Aux[14]-NSStatusItemView
error	13:17:05.527621-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	13:17:05.527640-0500	Nexy	[com.apple.controlcenter:D3BB2117-764A-4560-9C5A-BFAC4FB9260A] No matching scene to invalidate for this identity.
error	13:17:05.527669-0500	Nexy	auxiliary scene activation failed: Error Domain=FBSWorkspaceErrorDomain Code=1 UserInfo={BSErrorCodeDescription=InvalidScene, NSLocalizedFailureReason=<private>}
error	13:17:05.527700-0500	Nexy	Unhandled disconnected scene <private>
error	13:17:05.527784-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
