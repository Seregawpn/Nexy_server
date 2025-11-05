default	20:13:36.718080-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:13:36.718225-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:13:36.719774-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	20:13:36.722811-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:13:36.725970-0500	runningboardd	Launch request for app<application.com.nexy.assistant.20753384.20753390(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:13:36.726048-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.20753384.20753390(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:17422] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-17422-1488841 target:app<application.com.nexy.assistant.20753384.20753390(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:13:36.726119-0500	runningboardd	Assertion 398-17422-1488841 (target:app<application.com.nexy.assistant.20753384.20753390(501)>) will be created as active
default	20:13:36.729353-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	20:13:36.729386-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.20753384.20753390(501)>
default	20:13:36.729398-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	20:13:36.729484-0500	runningboardd	app<application.com.nexy.assistant.20753384.20753390(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000954 ms (wallclock); resolved to {4294967295, (null)}
default	20:13:36.760057-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] is not RunningBoard jetsam managed.
default	20:13:36.760073-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] This process will not be managed.
default	20:13:36.760083-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.20753384.20753390(501)>:23856]
default	20:13:36.760251-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:13:36.760905-0500	gamepolicyd	Hit the server for a process handle dce6a2100005d30 that resolved to: [app<application.com.nexy.assistant.20753384.20753390(501)>:23856]
default	20:13:36.760941-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:13:36.764255-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.20753384.20753390(501)>:23856]
default	20:13:36.764334-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-1488842 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:13:36.764493-0500	runningboardd	Assertion 398-398-1488842 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:13:36.764689-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:13:36.764705-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:13:36.764724-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Set darwin role to: UserInteractive
default	20:13:36.764734-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:13:36.764753-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:13:36.764841-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] reported to RB as running
default	20:13:36.766252-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x1874873 com.nexy.assistant starting stopped process.
default	20:13:36.766387-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:23856" ID:398-363-1488843 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:13:36.766609-0500	runningboardd	Assertion 398-363-1488843 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:13:36.767622-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:13:36.769074-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:13:36.770199-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:13:36.770217-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:13:36.770271-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:13:36.770323-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:13:36.770484-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.20753384.20753390(501)>:23856]
default	20:13:36.773574-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:13:36.774044-0500	runningboardd	Invalidating assertion 398-17422-1488841 (target:app<application.com.nexy.assistant.20753384.20753390(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:17422]
default	20:13:36.774097-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:13:36.774139-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:13:36.774221-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:13:36.774243-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:13:36.774621-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:13:36.777565-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:13:36.879905-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:13:36.880031-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:13:36.880059-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:13:36.880110-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:13:36.881356-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:13:36.883645-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:13:36.884119-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:13:36.945131-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	20:13:36.946847-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=511.151, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	20:13:36.953850-0500	tccd	AUTHREQ_SUBJECT: msgID=511.151, subject=com.nexy.assistant,
default	20:13:36.954843-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	20:13:36.973814-0500	kernel	Nexy[23856] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xfeb0e483e2e02d7. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:13:36.973941-0500	kernel	Nexy[23856] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0xfeb0e483e2e02d7. While not abnormal for debuggers, this increases system memory footprint until the target exits.
error	20:13:37.388891-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x1045fd0f0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:13:37.389183-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x1045fd0f0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:13:37.389398-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x1045fd0f0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:13:37.389602-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x1045fd0f0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:13:37.626430-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:13:37.630601-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:13:37.632103-0500	Nexy	[0x1045fe1b0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:13:37.635271-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20753384.20753390 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20753384.20753390>
default	20:13:37.639480-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:13:37.641292-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:13:37.641472-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:13:37.641607-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:13:37.641618-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:13:37.641649-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:13:37.641822-0500	Nexy	[0xb6406c000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:13:37.642441-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23856.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:13:37.649271-0500	tccd	AUTHREQ_SUBJECT: msgID=23856.1, subject=com.nexy.assistant,
default	20:13:37.649920-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37139500 at /Applications/Nexy.app
default	20:13:37.662089-0500	Nexy	[0xb6406c000] invalidated after the last release of the connection object
default	20:13:37.662134-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:13:37.666590-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10935, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:37.667464-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10935, subject=com.nexy.assistant,
default	20:13:37.667993-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37139500 at /Applications/Nexy.app
error	20:13:37.680288-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	20:13:37.681153-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10937, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:37.681847-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10937, subject=com.nexy.assistant,
default	20:13:37.682348-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37139500 at /Applications/Nexy.app
default	20:13:37.695811-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:13:37.695827-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xb64868080> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	20:13:37.720160-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:13:37.720288-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:13:37.725294-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:13:39.978781-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 94CB1A07-34FB-45F7-B28E-1C0C1B50FC74 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.50516,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x55e714ba tp_proto=0x06"
default	20:13:39.978925-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:50516<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762786 t_state: SYN_SENT process: Nexy:23856 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb23e9e67
default	20:13:39.998105-0500	kernel	tcp connected: [<IPv4-redacted>:50516<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762786 t_state: ESTABLISHED process: Nexy:23856 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb23e9e67
default	20:13:39.998513-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:50516<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762786 t_state: FIN_WAIT_1 process: Nexy:23856 Duration: 0.020 sec Conn_Time: 0.020 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 20.000 ms rttvar: 10.000 ms base rtt: 20 ms so_error: 0 svc/tc: 0 flow: 0xb23e9e67
default	20:13:39.998526-0500	kernel	tcp_connection_summary [<IPv4-redacted>:50516<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762786 t_state: FIN_WAIT_1 process: Nexy:23856 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:13:40.029369-0500	Nexy	[0xb6406c000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:13:40.042285-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb65b34740) Selecting device 85 from constructor
default	20:13:40.042296-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb65b34740)
default	20:13:40.042303-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb65b34740) not already running
default	20:13:40.042306-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb65b34740) nothing to teardown
default	20:13:40.042311-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb65b34740) connecting device 85
default	20:13:40.042424-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb65b34740) Device ID: 85 (Input:No | Output:Yes): true
default	20:13:40.042527-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb65b34740) created ioproc 0xa for device 85
default	20:13:40.042629-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 7 device listeners to device 85
default	20:13:40.042792-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 0 device delegate listeners to device 85
default	20:13:40.042798-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb65b34740)
default	20:13:40.042867-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:13:40.042876-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	20:13:40.042889-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:13:40.042898-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	20:13:40.042906-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:13:40.042994-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb65b34740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:13:40.043003-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb65b34740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:13:40.043009-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:13:40.043014-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 0 device listeners from device 0
default	20:13:40.043018-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 0 device delegate listeners from device 0
default	20:13:40.043021-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb65b34740)
default	20:13:40.043035-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:13:40.043124-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb65b34740) caller requesting device change from 85 to 91
default	20:13:40.043133-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb65b34740)
default	20:13:40.043138-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb65b34740) not already running
default	20:13:40.043140-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb65b34740) disconnecting device 85
default	20:13:40.043144-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb65b34740) destroying ioproc 0xa for device 85
default	20:13:40.043195-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:13:40.043742-0500	Nexy	[0xb6406c280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:13:40.044651-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef286","name":"Nexy(23856)"}, "details":{"PID":23856,"session_type":"Primary"} }
default	20:13:40.044737-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":23856}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef286, sessionType: 'prim', isRecording: false }, 
]
default	20:13:40.045411-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 23856, name = Nexy
default	20:13:40.045666-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xb64a2a680 with ID: 0x1ef286
default	20:13:40.046348-0500	Nexy	[0xb6406c3c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	20:13:40.046483-0500	Nexy	No persisted cache on this platform.
error	20:13:40.046803-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=102460739813377 }
default	20:13:40.046818-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	20:13:40.046873-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:13:40.046960-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb65b34740) connecting device 91
default	20:13:40.047044-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb65b34740) Device ID: 91 (Input:Yes | Output:No): true
default	20:13:40.048398-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10938, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:40.049613-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10938, subject=com.nexy.assistant,
default	20:13:40.050647-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37139500 at /Applications/Nexy.app
default	20:13:40.065506-0500	tccd	AUTHREQ_PROMPTING: msgID=401.10938, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	20:13:42.081118-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	20:13:42.082963-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb65b34740) created ioproc 0xa for device 91
default	20:13:42.083224-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 7 device listeners to device 91
default	20:13:42.083498-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 0 device delegate listeners to device 91
default	20:13:42.083509-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb65b34740)
default	20:13:42.083523-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	20:13:42.083539-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:13:42.083775-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:13:42.083803-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	20:13:42.083873-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:13:42.084017-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb65b34740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:13:42.084036-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb65b34740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:13:42.084043-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:13:42.084062-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 7 device listeners from device 85
default	20:13:42.084300-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 0 device delegate listeners from device 85
default	20:13:42.084312-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb65b34740)
default	20:13:42.085249-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:13:42.087495-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10939, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:42.089528-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10939, subject=com.nexy.assistant,
default	20:13:42.090101-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:13:42.090639-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37139500 at /Applications/Nexy.app
default	20:13:42.106925-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:13:42.108239-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10940, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:42.109302-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10940, subject=com.nexy.assistant,
default	20:13:42.109920-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37139500 at /Applications/Nexy.app
default	20:13:42.123193-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:13:42.124684-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10941, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:42.125528-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10941, subject=com.nexy.assistant,
default	20:13:42.126108-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
default	20:13:42.138232-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:13:42.138623-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:13:42.138758-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:13:42.138788-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:13:42.139440-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:13:42.140482-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf76f4300] Created node ADM::com.nexy.assistant_60334.60271.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:13:42.140547-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf76f4300] Created node ADM::com.nexy.assistant_60334.60271.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:13:42.183732-0500	runningboardd	Assertion did invalidate due to timeout: 398-398-1488842 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856])
default	20:13:42.203007-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:13:42.204485-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:60334 called from <private>
default	20:13:42.204520-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:13:42.204550-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:13:42.206290-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60334 called from <private>
default	20:13:42.206410-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60334)
default	20:13:42.206429-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60334 called from <private>
default	20:13:42.207313-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1488852 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:13:42.207434-0500	runningboardd	Assertion 398-334-1488852 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:13:42.210124-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:13:42.210391-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:13:42.211652-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:13:42.206437-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60334 called from <private>
default	20:13:42.206710-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60333)
default	20:13:42.206727-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:60333 called from <private>
default	20:13:42.211966-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:13:42.206733-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60333 called from <private>
fault	20:13:42.214323-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20753384.20753390 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20753384.20753390>
default	20:13:42.215507-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:13:42.216204-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:13:42.222544-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60334)
default	20:13:42.222564-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60334)
default	20:13:42.222575-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60334)
default	20:13:42.222585-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60334)
fault	20:13:42.224050-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20753384.20753390 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20753384.20753390>
default	20:13:42.225531-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:13:42.225799-0500	runningboardd	Invalidating assertion 398-334-1488852 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [osservice<com.apple.powerd>:334]
default	20:13:42.226232-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:60334 called from <private>
default	20:13:42.226262-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:60334 called from <private>
default	20:13:42.226274-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:60334 called from <private>
default	20:13:42.226279-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:60334 called from <private>
default	20:13:42.226289-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60334 called from <private>
default	20:13:42.226298-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60334 called from <private>
default	20:13:42.226306-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60334 called from <private>
default	20:13:42.226311-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60334 called from <private>
default	20:13:42.226347-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60334 called from <private>
default	20:13:42.226392-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60334 called from <private>
default	20:13:42.226711-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:13:42.231422-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60333)
default	20:13:42.234778-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60334)
default	20:13:42.234801-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60334 called from <private>
default	20:13:42.235271-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef286","name":"Nexy(23856)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:13:42.235666-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60333 called from <private>
default	20:13:42.235677-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60333 called from <private>
default	20:13:42.235346-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:13:42.235390-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:13:42.235933-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:13:42.235485-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef286, Nexy(23856), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:13:42.236040-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:13:42.236167-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:13:42.236176-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:13:42.236211-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef286, Nexy(23856), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 647 starting recording
default	20:13:42.236476-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:13:42.236561-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:13:42.236363-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:13:42.236290-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:13:42.236752-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:13:42.236449-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:13:42.236764-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:13:42.236572-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef286, Nexy(23856), 'prim'', displayID:'com.nexy.assistant'}
default	20:13:42.236741-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:13:42.237667-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10942, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:42.239351-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10942, subject=com.nexy.assistant,
default	20:13:42.240170-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
default	20:13:42.249442-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:60333 called from <private>
default	20:13:42.249456-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:60333 called from <private>
default	20:13:42.249571-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60333)
default	20:13:42.250941-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:13:42.251017-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:13:42.251050-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:13:42.252221-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.252360-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.257009-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60333)
default	20:13:42.257230-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:60333 called from <private>
default	20:13:42.257241-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:60333 called from <private>
default	20:13:42.257348-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60333)
default	20:13:42.255522-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/centerstage-controlmode newValue: (null)
default	20:13:42.259572-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:13:42.259229-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/centerstage-enabled newValue: (null)
default	20:13:42.260550-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:13:42.259944-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/centerstage-unavailablereasons newValue: (null)
default	20:13:42.261667-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/portraiteffect-controlmode newValue: (null)
default	20:13:42.263968-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:60334 called from <private>
default	20:13:42.262717-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/portraiteffect-enabled newValue: (null)
default	20:13:42.266820-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60333)
default	20:13:42.267573-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60333 called from <private>
default	20:13:42.267580-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60333 called from <private>
default	20:13:42.267774-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60333 called from <private>
default	20:13:42.267781-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60333 called from <private>
default	20:13:42.267812-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60333 called from <private>
default	20:13:42.267821-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60333 called from <private>
default	20:13:42.267879-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60333 called from <private>
default	20:13:42.267971-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60333)
default	20:13:42.268316-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60333 called from <private>
default	20:13:42.268522-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60333 called from <private>
default	20:13:42.268640-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60333 called from <private>
default	20:13:42.268774-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60333 called from <private>
default	20:13:42.268836-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60333 called from <private>
default	20:13:42.268914-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60333 called from <private>
default	20:13:42.269047-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60333 called from <private>
default	20:13:42.269098-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60333 called from <private>
default	20:13:42.269134-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60333 called from <private>
default	20:13:42.268860-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/portraiteffect-unavailablereasons newValue: (null)
default	20:13:42.279923-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/reactions-enabled newValue: (null)
default	20:13:42.280338-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:13:42.280299-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/gestures-enabled newValue: (null)
default	20:13:42.280499-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:13:42.281270-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60334)
default	20:13:42.281431-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60334 called from <private>
default	20:13:42.281440-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60334 called from <private>
default	20:13:42.287185-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.287194-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.287201-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.287210-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.287255-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.287288-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:42.287390-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.287489-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.287561-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.287631-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.287669-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.287734-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:42.287894-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
default	20:13:42.287858-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:13:42.287889-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:13:42.305701-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:13:42.325932-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:13:42.328422-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.328448-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.328460-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.328474-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.328483-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.328494-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:42.328669-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:13:42.342611-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:13:42.343677-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1488855 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:13:42.343739-0500	runningboardd	Assertion 398-334-1488855 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:13:42.345000-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:60334 called from <private>
default	20:13:42.345048-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:60334 called from <private>
default	20:13:42.346184-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:13:42.349256-0500	runningboardd	Invalidating assertion 398-334-1488855 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [osservice<com.apple.powerd>:334]
default	20:13:42.349400-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60334 called from <private>
default	20:13:42.349855-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60334)
default	20:13:42.349880-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60334 called from <private>
default	20:13:42.349893-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60334 called from <private>
default	20:13:42.350616-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:13:42.350740-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:13:42.351098-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60334)
default	20:13:42.351231-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60334 called from <private>
default	20:13:42.351243-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60334 called from <private>
default	20:13:42.351258-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60334 called from <private>
default	20:13:42.352766-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10944, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:42.353943-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10944, subject=com.nexy.assistant,
default	20:13:42.354684-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
default	20:13:42.368716-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:13:42.368753-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:13:42.368788-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:13:42.369091-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.369102-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.369110-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.369117-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.369126-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.369132-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:42.369182-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.369227-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.369257-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.369384-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:13:42.369565-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.369576-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.369585-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:42.369612-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.369621-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.369627-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.369632-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.369637-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.369643-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:42.369693-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:13:42.373245-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:60334 called from <private>
default	20:13:42.374429-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1488856 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:13:42.374629-0500	runningboardd	Assertion 398-334-1488856 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:13:42.380362-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:13:42.380373-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:13:42.380382-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:13:42.380398-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:13:42.395858-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:13:42.396857-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.396874-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.396889-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.396898-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.396904-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.396912-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:42.397082-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:13:42.414501-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:13:42.414546-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:13:42.414587-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:13:42.414901-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.414931-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.414940-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.414947-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.414958-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.414968-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:42.415000-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.415018-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.415035-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.415045-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.415055-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.415091-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:42.415226-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:13:42.415437-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.415448-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.415466-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.415488-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:42.415504-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:13:42.415509-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:42.415517-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:43.404036-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:13:43.404489-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef286","name":"Nexy(23856)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:13:43.404742-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:13:43.404865-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:13:43.404939-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef286, Nexy(23856), 'prim'', displayID:'com.nexy.assistant'}
default	20:13:43.405041-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:13:43.405064-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef286, Nexy(23856), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 647 stopping recording
default	20:13:43.405122-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:13:43.405189-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:13:43.405261-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:13:43.405590-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	20:13:43.405546-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:13:43.405570-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:13:43.410823-0500	runningboardd	Invalidating assertion 398-334-1488856 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [osservice<com.apple.powerd>:334]
default	20:13:43.411016-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:13:43.411192-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:13:43.411103-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:13:43.411319-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:13:43.411413-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:13:43.411432-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:13:43.411516-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:13:43.411534-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:13:43.411545-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:13:43.434397-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:13:43.434977-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:43.434998-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:43.435014-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:43.435023-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:43.435033-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:43.435041-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:43.435235-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:13:43.506485-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb65b34740) Selecting device 0 from destructor
default	20:13:43.506519-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb65b34740)
default	20:13:43.506541-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb65b34740) not already running
default	20:13:43.506553-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb65b34740) disconnecting device 91
default	20:13:43.506568-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb65b34740) destroying ioproc 0xa for device 91
default	20:13:43.506633-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:13:43.506700-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:13:43.507029-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb65b34740) nothing to setup
default	20:13:43.507055-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 0 device listeners to device 0
default	20:13:43.507070-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 0 device delegate listeners to device 0
default	20:13:43.507085-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 7 device listeners from device 91
default	20:13:43.507603-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 0 device delegate listeners from device 91
default	20:13:43.507628-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb65b34740)
default	20:13:43.513113-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:13:43.513124-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:13:43.513137-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:13:43.513155-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:13:43.516655-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:13:43.517342-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:13:43.735727-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23862.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=23862, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:13:43.737447-0500	tccd	AUTHREQ_SUBJECT: msgID=23862.1, subject=com.nexy.assistant,
default	20:13:43.738236-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	20:13:43.753500-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16148, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=23862, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:13:43.754489-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16148, subject=com.nexy.assistant,
default	20:13:43.755131-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	20:13:43.784821-0500	launchservicesd	CHECKIN:0x0-0x1874873 23862 com.nexy.assistant
default	20:13:43.785974-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:13:43.786103-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:13:43.786817-0500	runningboardd	Invalidating assertion 398-363-1488843 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	20:13:43.787389-0500	WindowServer	12f60b[CreateApplication]: Process creation: 0x0-0x1874873 (Nexy) connectionID: 12F60B pid: 23862 in session 0x101
default	20:13:43.790636-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:13:43.795201-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	20:13:43.798420-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:13:43.798434-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:13:43.798486-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Set darwin role to: None
default	20:13:43.798573-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:13:43.798706-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:13:43.802865-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-suspended (role: None) (endowments: (null))
default	20:13:43.803410-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-suspended-NotVisible
default	20:13:43.911680-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 23863: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 39102500 };
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
default	20:13:43.921298-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:13:43.928150-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138f00 at /Applications/Nexy.app
default	20:13:43.940130-0500	tccd	Prompting for access to indirect object System Events by Nexy
default	20:13:44.572793-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x1874873 (Nexy) connectionID: 12F60B pid: 23862 in session 0x101
default	20:13:44.572876-0500	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x1874873 (Nexy) acq:0x80188b9a0 count:1
default	20:13:44.574420-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x1874873 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1874873 (Nexy)"
)}
default	20:13:44.574935-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x5d36 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1874873 (Nexy)"
)}
default	20:13:44.578533-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x1874873} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	20:13:44.578576-0500	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 25643123
default	20:13:44.578665-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:13:44.747889-0500	Nexy	[0xb6406c640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:13:44.748544-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23856.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:13:44.749664-0500	tccd	AUTHREQ_SUBJECT: msgID=23856.2, subject=com.nexy.assistant,
default	20:13:44.750294-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	20:13:44.763396-0500	Nexy	[0xb6406c640] invalidated after the last release of the connection object
default	20:13:44.764137-0500	Nexy	[0xb6406c640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:13:44.764636-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23856.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:13:44.765933-0500	tccd	AUTHREQ_SUBJECT: msgID=23856.3, subject=com.nexy.assistant,
default	20:13:44.766608-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	20:13:44.778914-0500	Nexy	[0xb6406c640] invalidated after the last release of the connection object
default	20:13:44.780489-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb65b34740) Selecting device 85 from constructor
default	20:13:44.780502-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb65b34740)
default	20:13:44.780508-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb65b34740) not already running
default	20:13:44.780512-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb65b34740) nothing to teardown
default	20:13:44.780515-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb65b34740) connecting device 85
default	20:13:44.780635-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb65b34740) Device ID: 85 (Input:No | Output:Yes): true
default	20:13:44.780777-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb65b34740) created ioproc 0xb for device 85
default	20:13:44.780911-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 7 device listeners to device 85
default	20:13:44.781095-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 0 device delegate listeners to device 85
default	20:13:44.781102-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb65b34740)
default	20:13:44.781203-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	20:13:44.781213-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	20:13:44.781219-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	20:13:44.781236-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	20:13:44.781244-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:13:44.781347-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb65b34740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:13:44.781361-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb65b34740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:13:44.781366-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:13:44.781371-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 0 device listeners from device 0
default	20:13:44.781375-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 0 device delegate listeners from device 0
default	20:13:44.781380-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb65b34740)
default	20:13:44.781397-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:13:44.781472-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb65b34740) caller requesting device change from 85 to 91
default	20:13:44.781481-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb65b34740)
default	20:13:44.781486-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb65b34740) not already running
default	20:13:44.781488-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb65b34740) disconnecting device 85
default	20:13:44.781497-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb65b34740) destroying ioproc 0xb for device 85
default	20:13:44.781519-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	20:13:44.781559-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:13:44.781657-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb65b34740) connecting device 91
default	20:13:44.781742-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb65b34740) Device ID: 91 (Input:Yes | Output:No): true
default	20:13:44.782872-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10945, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:44.783838-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10945, subject=com.nexy.assistant,
default	20:13:44.784411-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138f00 at /Applications/Nexy.app
default	20:13:44.796587-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb65b34740) created ioproc 0xb for device 91
default	20:13:44.796720-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 7 device listeners to device 91
default	20:13:44.796911-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 0 device delegate listeners to device 91
default	20:13:44.796921-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb65b34740)
default	20:13:44.796927-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	20:13:44.796938-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:13:44.797069-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:13:44.797077-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	20:13:44.797085-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:13:44.797195-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb65b34740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:13:44.797209-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb65b34740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:13:44.797215-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:13:44.797220-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 7 device listeners from device 85
default	20:13:44.797404-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 0 device delegate listeners from device 85
default	20:13:44.797410-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb65b34740)
default	20:13:44.798022-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:13:44.798959-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10946, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:44.799782-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10946, subject=com.nexy.assistant,
default	20:13:44.800328-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138f00 at /Applications/Nexy.app
default	20:13:44.812330-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	20:13:44.812436-0500	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0xb65faea60, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	20:13:44.812675-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:13:44.813565-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10947, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:44.814352-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10947, subject=com.nexy.assistant,
default	20:13:44.814876-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138f00 at /Applications/Nexy.app
default	20:13:44.828291-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10948, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:13:44.829082-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10948, subject=com.nexy.assistant,
default	20:13:44.829608-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138f00 at /Applications/Nexy.app
default	20:13:44.850159-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef286","name":"Nexy(23856)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:13:44.850245-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:13:44.845530-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:13:44.850275-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef286, Nexy(23856), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:13:44.850307-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:13:44.850661-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:13:44.851380-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:13:44.851501-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:13:44.851780-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:13:44.851370-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:13:44.851377-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:13:44.851852-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Set darwin role to: Background
default	20:13:44.851888-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	20:13:44.851891-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:13:44.852054-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:13:44.853446-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:13:44.853475-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:13:44.853339-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:13:44.853528-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	20:13:44.853542-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	20:13:44.853589-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	20:13:44.853676-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:13:44.857774-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: Background) (endowments: (null))
default	20:13:44.858360-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:13:44.870362-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:13:44.870413-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:13:44.870462-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:13:44.870769-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:44.870781-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:45.105490-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	20:13:45.192826-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37139200 at /Applications/Nexy.app
default	20:13:45.200014-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	20:13:45.201551-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:13:48.104769-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	20:13:51.105535-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	20:13:53.826270-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_60334.60271.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-42.490921], peaks:[-19.764332] ]
default	20:13:53.829277-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_60334.60271.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-41.450089], peaks:[-12.335763] ]
default	20:13:54.089293-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	20:13:57.105477-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	20:13:57.954338-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:13:57.954900-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef286","name":"Nexy(23856)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:13:57.955130-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:13:57.955245-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:13:57.955317-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef286, Nexy(23856), 'prim'', displayID:'com.nexy.assistant'}
default	20:13:57.955440-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:13:57.955449-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef286, Nexy(23856), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 647 stopping recording
default	20:13:57.955517-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:13:57.955601-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:13:57.955677-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:13:57.955904-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:13:57.955949-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	20:13:57.955962-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:13:57.961888-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:13:57.961998-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:13:57.961720-0500	runningboardd	Invalidating assertion 398-334-1488867 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [osservice<com.apple.powerd>:334]
default	20:13:57.962163-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:13:57.962239-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:13:57.962315-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:13:57.962330-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:13:57.962394-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:13:57.962409-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:13:57.962420-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:13:57.963979-0500	coreaudiod	Sending message. { reporterID=102460739813379, category=IO, type=error, message=["anchor_sample_time": Optional(4), "num_continuous_nonzero_io_cycles": Optional(0), "wg_user_time_mach": Optional(85554), "is_recovering": Optional(0), "smallest_buffer_frame_size": Optional(2147483647), "output_device_source_list": Optional(), "HostApplicationDisplayID": Optional(com.nexy.assistant), "scheduler_latency": Optional(21291), "overload_type": Optional(Overload), "cause_set": Optional(4), "HAL_client_IO_duration": Optional(82704750), "wg_external_wakeups": Optional(4), "other_page_faults": Optional(0), "deadline": Optional(313024), "wg_cycles": Optional(6910509), "start_time": Optional(12520890033316), "sample_rate": Optional(24000), "careporting_timestamp": 1762305237.963593, "io_page_faults": Optional(0), "io_buffer_size": Optional(480), "multi_cycle_io_page_faults": Optional(0), "wg_instructions": Optional(6942882), "output_device_transport_list": Optional(), "multi_cycle_io_page_faults_duration": Optional(0), "safety_violation": Optional(0), "other_acti<…> }
default	20:13:57.973411-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:13:57.973418-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:13:57.973463-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Set darwin role to: None
default	20:13:57.973473-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:13:57.973520-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:13:57.977581-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-suspended (role: None) (endowments: (null))
default	20:13:57.978105-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-suspended-NotVisible
default	20:13:57.980530-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:13:57.980947-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:57.980963-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:57.980977-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:57.980986-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:13:57.980993-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:13:57.980999-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:13:57.981098-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:13:58.148555-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb65b34740) Selecting device 0 from destructor
default	20:13:58.148590-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb65b34740)
default	20:13:58.148605-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb65b34740) not already running
default	20:13:58.148617-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb65b34740) disconnecting device 91
default	20:13:58.148631-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb65b34740) destroying ioproc 0xb for device 91
default	20:13:58.148684-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:13:58.148760-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:13:58.149068-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb65b34740) nothing to setup
default	20:13:58.149089-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 0 device listeners to device 0
default	20:13:58.149101-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb65b34740) adding 0 device delegate listeners to device 0
default	20:13:58.149111-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 7 device listeners from device 91
default	20:13:58.149513-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb65b34740) removing 0 device delegate listeners from device 91
default	20:13:58.149539-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb65b34740)
default	20:13:58.166368-0500	Nexy	[0xb6406c500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:13:58.167701-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23856.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:13:58.169662-0500	tccd	AUTHREQ_SUBJECT: msgID=23856.4, subject=com.nexy.assistant,
default	20:13:58.175602-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	20:13:58.191019-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[23856], responsiblePID[23856], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:13:58.191348-0500	Nexy	[0xb6406c500] invalidated after the last release of the connection object
default	20:13:58.260189-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	20:13:58.286427-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	20:13:58.293849-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:13:58.316485-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	20:13:58.316615-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	20:13:58.912612-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	20:13:58.917098-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	20:13:58.934472-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	20:14:00.226635-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60333)
default	20:14:00.226737-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60333 called from <private>
default	20:14:00.226787-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60333 called from <private>
default	20:14:00.227150-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60333 called from <private>
default	20:14:00.227164-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60333 called from <private>
default	20:14:00.227478-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60333)
default	20:14:00.227953-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60333)
default	20:14:00.228494-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60333 called from <private>
default	20:14:00.228519-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:60333 called from <private>
default	20:14:00.243165-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:60333 called from <private>
default	20:14:00.243216-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60333 called from <private>
default	20:14:00.244179-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60333)
default	20:14:00.257502-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60333)
default	20:14:00.258047-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60333 called from <private>
default	20:14:00.258064-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:60333 called from <private>
default	20:14:00.274825-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:60333 called from <private>
default	20:14:00.276315-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60333 called from <private>
default	20:14:00.276496-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60333 called from <private>
default	20:14:00.276536-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60333 called from <private>
default	20:14:00.276550-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60333 called from <private>
default	20:14:00.276561-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60333 called from <private>
default	20:14:00.276624-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60333 called from <private>
default	20:14:00.276635-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60333 called from <private>
default	20:14:00.276659-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60333 called from <private>
default	20:14:00.276710-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60333 called from <private>
default	20:14:00.277050-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60333)
default	20:14:04.229391-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	20:14:04.244749-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	20:14:04.254566-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:14:11.196830-0500	Nexy	[0xb6406c500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:14:11.198560-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23856.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:14:11.203799-0500	tccd	AUTHREQ_SUBJECT: msgID=23856.5, subject=com.nexy.assistant,
default	20:14:11.205239-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	20:14:11.226211-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[23856], responsiblePID[23856], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:14:11.226649-0500	Nexy	[0xb6406c500] invalidated after the last release of the connection object
default	20:14:11.284138-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	20:14:11.299829-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	20:14:11.303785-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:14:16.859314-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	20:14:16.874413-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	20:14:16.883105-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:14:24.755220-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef286","name":"Nexy(23856)"}, "details":null }
default	20:14:24.755394-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef286 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":23856})
default	20:14:24.755412-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":23856})
default	20:14:24.755790-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:14:24.755994-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 647, PID = 23856, Name = sid:0x1ef286, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:14:24.756305-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:24.756521-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:24.756443-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:24.756576-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:24.763395-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:14:24.763606-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:14:24.764822-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_60334.60271.0_airpods noise suppression studio::out-0 issue_detected_sample_time=336960.000000 ] -- [ rms:[-41.456902], peaks:[-20.369041] ]
default	20:14:24.764839-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_60334.60271.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-39.397949], peaks:[-17.307323] ]
default	20:14:24.769108-0500	kernel	Nexy[23856] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xd564430f366244af. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:14:24.769121-0500	kernel	Nexy[23856] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0xd564430f366244af. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:14:24.774315-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:24.774406-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:24.846579-0500	Nexy	[0x1052aee20] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:14:24.846662-0500	Nexy	[0x1052af360] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	20:14:24.981268-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x1052b7220 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:14:24.981508-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x1052b7220 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:14:24.981718-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x1052b7220 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:14:24.981920-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x1052b7220 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:14:25.109138-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:14:25.112723-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:14:25.114269-0500	Nexy	[0x1052bc6a0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	20:14:25.116339-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:14:25.118344-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:14:25.118648-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:14:25.118951-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:14:25.118983-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:14:25.119044-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:14:25.119309-0500	Nexy	[0x778094000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:14:25.119405-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:14:25.119956-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23856.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:14:25.126097-0500	tccd	AUTHREQ_SUBJECT: msgID=23856.1, subject=com.nexy.assistant,
default	20:14:25.126698-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
default	20:14:25.140417-0500	Nexy	[0x778094000] invalidated after the last release of the connection object
default	20:14:25.140634-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:14:25.140680-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:14:25.141042-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:14:25.142538-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10949, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:14:25.143491-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10949, subject=com.nexy.assistant,
default	20:14:25.144037-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
error	20:14:25.158499-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	20:14:25.159532-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10951, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:14:25.160672-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10951, subject=com.nexy.assistant,
default	20:14:25.161631-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
default	20:14:25.179651-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:14:25.179677-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x778e38060> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	20:14:25.202447-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	20:14:25.202467-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	20:14:25.205966-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:14:25.206110-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:14:25.211545-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:14:26.665477-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6D51335F-6941-495F-8F48-3FA0AC4B9F67 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.50519,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x53f1537f tp_proto=0x06"
default	20:14:26.665589-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:50519<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762901 t_state: SYN_SENT process: Nexy:23856 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 19 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa82192b1
default	20:14:26.679284-0500	kernel	tcp connected: [<IPv4-redacted>:50519<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762901 t_state: ESTABLISHED process: Nexy:23856 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 19 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa82192b1
default	20:14:26.679558-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:50519<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762901 t_state: FIN_WAIT_1 process: Nexy:23856 Duration: 0.015 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 14 ms so_error: 0 svc/tc: 0 flow: 0xa82192b1
default	20:14:26.679568-0500	kernel	tcp_connection_summary [<IPv4-redacted>:50519<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762901 t_state: FIN_WAIT_1 process: Nexy:23856 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:14:26.696454-0500	Nexy	[0x778094000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:14:26.708365-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7790f4e40) Selecting device 85 from constructor
default	20:14:26.708378-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7790f4e40)
default	20:14:26.708384-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7790f4e40) not already running
default	20:14:26.708388-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7790f4e40) nothing to teardown
default	20:14:26.708391-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7790f4e40) connecting device 85
default	20:14:26.708472-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7790f4e40) Device ID: 85 (Input:No | Output:Yes): true
default	20:14:26.708570-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7790f4e40) created ioproc 0xa for device 85
default	20:14:26.708666-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f4e40) adding 7 device listeners to device 85
default	20:14:26.708815-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f4e40) adding 0 device delegate listeners to device 85
default	20:14:26.708822-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7790f4e40)
default	20:14:26.708889-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:14:26.708905-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	20:14:26.708910-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:14:26.708916-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	20:14:26.708923-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:14:26.709019-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7790f4e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:14:26.709028-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7790f4e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:14:26.709033-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:14:26.709037-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f4e40) removing 0 device listeners from device 0
default	20:14:26.709041-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f4e40) removing 0 device delegate listeners from device 0
default	20:14:26.709044-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7790f4e40)
default	20:14:26.709059-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:14:26.709145-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7790f4e40) caller requesting device change from 85 to 91
default	20:14:26.709152-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7790f4e40)
default	20:14:26.709157-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7790f4e40) not already running
default	20:14:26.709161-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7790f4e40) disconnecting device 85
default	20:14:26.709165-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7790f4e40) destroying ioproc 0xa for device 85
default	20:14:26.709213-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:14:26.709733-0500	Nexy	[0x778094280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:14:26.710685-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef287","name":"Nexy(23856)"}, "details":{"PID":23856,"session_type":"Primary"} }
default	20:14:26.710777-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":23856}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef287, sessionType: 'prim', isRecording: false }, 
]
default	20:14:26.711119-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x778e5a680 with ID: 0x1ef287
default	20:14:26.711774-0500	Nexy	[0x7780943c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	20:14:26.711914-0500	Nexy	No persisted cache on this platform.
error	20:14:26.712238-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=102460739813377 }
default	20:14:26.712251-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	20:14:26.712302-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:14:26.712398-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7790f4e40) connecting device 91
default	20:14:26.712481-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7790f4e40) Device ID: 91 (Input:Yes | Output:No): true
default	20:14:26.713850-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10952, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:14:26.715126-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10952, subject=com.nexy.assistant,
default	20:14:26.715748-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
default	20:14:26.728976-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7790f4e40) created ioproc 0xa for device 91
default	20:14:26.729123-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f4e40) adding 7 device listeners to device 91
default	20:14:26.729311-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f4e40) adding 0 device delegate listeners to device 91
default	20:14:26.729320-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7790f4e40)
default	20:14:26.729326-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	20:14:26.729336-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:14:26.729451-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:14:26.729459-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	20:14:26.729464-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:14:26.729559-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7790f4e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:14:26.729573-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7790f4e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:14:26.729581-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:14:26.729584-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f4e40) removing 7 device listeners from device 85
default	20:14:26.729748-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f4e40) removing 0 device delegate listeners from device 85
default	20:14:26.729758-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7790f4e40)
default	20:14:26.730349-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:14:26.731347-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10953, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:14:26.732188-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10953, subject=com.nexy.assistant,
default	20:14:26.732748-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
default	20:14:26.744873-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:14:26.745829-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10954, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:14:26.746682-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10954, subject=com.nexy.assistant,
default	20:14:26.747251-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
default	20:14:26.760552-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:14:26.762175-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10955, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:14:26.763102-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10955, subject=com.nexy.assistant,
default	20:14:26.763689-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
default	20:14:26.776648-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:14:26.776820-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:14:26.777601-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:14:26.777898-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf76f6d00] Created node ADM::com.nexy.assistant_60347.60271.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:14:26.777966-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf76f6d00] Created node ADM::com.nexy.assistant_60347.60271.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:14:26.847083-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:14:26.849349-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:60347 called from <private>
default	20:14:26.849409-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:14:26.852212-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60347 called from <private>
default	20:14:26.852423-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60347)
default	20:14:26.852452-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60347 called from <private>
default	20:14:26.852463-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60347 called from <private>
default	20:14:26.853368-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1489046 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:14:26.852732-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60346)
default	20:14:26.853456-0500	runningboardd	Assertion 398-334-1489046 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:26.853035-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:60346 called from <private>
default	20:14:26.853080-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60346 called from <private>
default	20:14:26.854185-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:26.854235-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:26.854329-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Set darwin role to: Background
default	20:14:26.854501-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:26.855587-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:26.858652-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:14:26.859865-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	20:14:26.860575-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20753384.20753390 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20753384.20753390>
default	20:14:26.860887-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60347)
default	20:14:26.863215-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60347)
default	20:14:26.863337-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60347)
default	20:14:26.863621-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60347)
fault	20:14:26.864959-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20753384.20753390 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20753384.20753390>
default	20:14:26.867866-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: Background) (endowments: (null))
default	20:14:26.868196-0500	runningboardd	Invalidating assertion 398-334-1489046 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [osservice<com.apple.powerd>:334]
default	20:14:26.868630-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:14:26.877238-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60347 called from <private>
default	20:14:26.877278-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60347 called from <private>
default	20:14:26.877300-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60347 called from <private>
default	20:14:26.877383-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60347 called from <private>
default	20:14:26.877412-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60347 called from <private>
default	20:14:26.877420-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60347 called from <private>
default	20:14:26.877428-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60347 called from <private>
default	20:14:26.883554-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60347)
default	20:14:26.883898-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60346)
error	20:14:26.888084-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	20:14:26.888699-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef287","name":"Nexy(23856)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:14:26.888801-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:14:26.888859-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:14:26.888927-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef287, Nexy(23856), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:14:26.888958-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:26.889169-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:26.889029-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:14:26.889067-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:14:26.889197-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:14:26.889247-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef287, Nexy(23856), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 648 starting recording
default	20:14:26.889183-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:26.889487-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:26.889440-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:14:26.889525-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:14:26.889558-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef287, Nexy(23856), 'prim'', displayID:'com.nexy.assistant'}
default	20:14:26.889621-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:14:26.889878-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:14:26.889909-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:14:26.889977-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10956, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:14:26.892061-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10956, subject=com.nexy.assistant,
default	20:14:26.894248-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138600 at /Applications/Nexy.app
default	20:14:26.898380-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:14:26.898610-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:14:26.898663-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:14:26.901324-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:26.901545-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:26.901635-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:26.901968-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:26.902141-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:26.902359-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:26.904071-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:14:26.915035-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:26.916524-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:26.908840-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60346 called from <private>
default	20:14:26.917531-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	20:14:26.926207-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:14:26.926342-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:14:26.940121-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.10957, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:14:26.940166-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60346 called from <private>
default	20:14:26.940325-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:60346 called from <private>
default	20:14:26.940392-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:60346 called from <private>
default	20:14:26.940512-0500	runningboardd	Invalidating assertion 398-334-1489047 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [osservice<com.apple.powerd>:334]
default	20:14:26.940502-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60346 called from <private>
default	20:14:26.940546-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60346 called from <private>
default	20:14:26.940556-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:60346 called from <private>
default	20:14:26.941679-0500	tccd	AUTHREQ_SUBJECT: msgID=401.10957, subject=com.nexy.assistant,
default	20:14:26.949826-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:26.949836-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:26.949867-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:26.949877-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:26.949884-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:26.949891-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:26.950048-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:14:26.961082-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf76f6d00] Created node ADM::com.nexy.assistant_60347.60271.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:14:26.961146-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf76f6d00] Created node ADM::com.nexy.assistant_60347.60271.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:14:26.970994-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:26.971009-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:26.971040-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Set darwin role to: None
default	20:14:26.971051-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:26.971070-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:26.980724-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:14:26.989279-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:26.989306-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:26.989317-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:26.989324-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:26.989331-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:26.989340-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:26.989429-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:14:26.996506-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1489048 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:14:26.998212-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:60347 called from <private>
default	20:14:26.998325-0500	runningboardd	Assertion 398-334-1489048 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:26.998585-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:60347 called from <private>
default	20:14:27.999821-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:14:27.000490-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:27.000935-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:27.001039-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Set darwin role to: Background
default	20:14:27.001051-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:27.001085-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:27.023921-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:14:27.023966-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:14:27.024004-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:14:27.024358-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.024379-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.024398-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.024409-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.024435-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.024458-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:27.024477-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.024493-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.024542-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.024580-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.024616-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.024646-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:14:27.024655-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:27.024975-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.024983-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.024991-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:14:27.024991-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.025000-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.025007-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.025012-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:27.035661-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60347)
default	20:14:27.035820-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60347 called from <private>
default	20:14:27.035873-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60347 called from <private>
default	20:14:27.036565-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:14:27.036750-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:14:27.037069-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1489050 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:14:27.037194-0500	runningboardd	Assertion 398-334-1489050 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:27.051347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.051361-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.051371-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.051381-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.051388-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.051394-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:27.051552-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:14:27.060857-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1489051 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:14:27.061388-0500	runningboardd	Assertion 398-334-1489051 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:27.065572-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:60347 called from <private>
default	20:14:27.076198-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:14:27.076246-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:14:27.076289-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:14:27.093208-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:14:27.097050-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.097060-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.097069-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.097075-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.097083-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.097089-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:27.097229-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:14:27.111334-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:14:27.111377-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:14:27.111414-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:14:27.111675-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.111689-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.111701-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.111707-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.111712-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.111718-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:27.111748-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.111839-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.111942-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:14:27.111918-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.111990-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.112049-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.112091-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:27.112205-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.112214-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.112222-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.112241-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:14:27.112251-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:27.112325-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:27.112448-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:28.244693-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:14:28.245192-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef287","name":"Nexy(23856)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:14:28.245369-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:14:28.245451-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:14:28.245515-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef287, Nexy(23856), 'prim'', displayID:'com.nexy.assistant'}
default	20:14:28.245590-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:14:28.245596-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef287, Nexy(23856), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 648 stopping recording
default	20:14:28.245632-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:14:28.245671-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:14:28.245713-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:14:28.245912-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:14:28.245930-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:14:28.245992-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	20:14:28.252079-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:14:28.252130-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:14:28.251488-0500	runningboardd	Invalidating assertion 398-334-1489051 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [osservice<com.apple.powerd>:334]
default	20:14:28.252161-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:14:28.251827-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:14:28.252192-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:28.251974-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:28.252410-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:14:28.252521-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:28.252669-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:14:28.254456-0500	coreaudiod	Sending message. { reporterID=102460739813378, category=IO, type=error, message=["anchor_sample_time": Optional(108), "num_continuous_nonzero_io_cycles": Optional(0), "wg_user_time_mach": Optional(100612), "is_recovering": Optional(0), "smallest_buffer_frame_size": Optional(2147483647), "output_device_source_list": Optional(), "HostApplicationDisplayID": Optional(com.nexy.assistant), "scheduler_latency": Optional(30000), "overload_type": Optional(Overload), "cause_set": Optional(4), "HAL_client_IO_duration": Optional(71823000), "wg_external_wakeups": Optional(3), "other_page_faults": Optional(0), "deadline": Optional(27048), "wg_cycles": Optional(5154533), "start_time": Optional(12521617224264), "sample_rate": Optional(24000), "careporting_timestamp": 1762305268.254251, "io_page_faults": Optional(0), "io_buffer_size": Optional(480), "multi_cycle_io_page_faults": Optional(0), "wg_instructions": Optional(7059801), "output_device_transport_list": Optional(), "multi_cycle_io_page_faults_duration": Optional(0), "safety_violation": Optional(0), "other_ac<…> }
default	20:14:28.274620-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:14:28.275239-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:28.275257-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:28.275274-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:28.275280-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:14:28.275289-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:14:28.275295-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:14:28.275413-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:14:28.359837-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:28.359870-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:28.359944-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Set darwin role to: None
default	20:14:28.359970-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:28.360115-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:28.364963-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-suspended (role: None) (endowments: (null))
default	20:14:28.365729-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-suspended-NotVisible
default	20:14:28.428977-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7790f4e40) Selecting device 0 from destructor
default	20:14:28.428998-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7790f4e40)
default	20:14:28.429008-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7790f4e40) not already running
default	20:14:28.429016-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7790f4e40) disconnecting device 91
default	20:14:28.429023-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7790f4e40) destroying ioproc 0xa for device 91
default	20:14:28.429066-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:14:28.429109-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:14:28.429315-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x7790f4e40) nothing to setup
default	20:14:28.429332-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f4e40) adding 0 device listeners to device 0
default	20:14:28.429342-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f4e40) adding 0 device delegate listeners to device 0
default	20:14:28.429352-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f4e40) removing 7 device listeners from device 91
default	20:14:28.429630-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f4e40) removing 0 device delegate listeners from device 91
default	20:14:28.429649-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7790f4e40)
default	20:14:28.571775-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23907.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=23907, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:14:28.573503-0500	tccd	AUTHREQ_SUBJECT: msgID=23907.1, subject=com.nexy.assistant,
default	20:14:28.574117-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	20:14:28.589235-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16206, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=23907, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:14:28.590131-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16206, subject=com.nexy.assistant,
default	20:14:28.590688-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	20:14:28.623281-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	20:14:28.642110-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 23863: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 bf102500 };
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
default	20:14:28.655880-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:14:29.481013-0500	Nexy	[0x778094640] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:14:29.482073-0500	Nexy	[0x7780948c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:14:29.483700-0500	Nexy	Received configuration update from daemon (initial)
default	20:14:29.531006-0500	Nexy	[0x778094a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:14:29.531629-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:14:29.531812-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23856.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:14:29.533335-0500	tccd	AUTHREQ_SUBJECT: msgID=23856.2, subject=com.nexy.assistant,
default	20:14:29.534024-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	20:14:29.547070-0500	Nexy	[0x778094a00] invalidated after the last release of the connection object
default	20:14:29.547905-0500	Nexy	[0x778094a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:14:29.548309-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:14:29.548476-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23856.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:14:29.549376-0500	tccd	AUTHREQ_SUBJECT: msgID=23856.3, subject=com.nexy.assistant,
default	20:14:29.550019-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	20:14:29.562505-0500	Nexy	[0x778094a00] invalidated after the last release of the connection object
default	20:14:29.562556-0500	Nexy	[0x778094a00] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	20:14:29.562644-0500	Nexy	[0x778094a00] invalidated after the last release of the connection object
default	20:14:29.562990-0500	Nexy	[0x778094b40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:14:29.563424-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23856.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:14:29.564270-0500	tccd	AUTHREQ_SUBJECT: msgID=23856.4, subject=com.nexy.assistant,
default	20:14:29.564834-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	20:14:29.577446-0500	Nexy	[0x778094b40] invalidated after the last release of the connection object
default	20:14:29.577801-0500	Nexy	server port 0x0000bf0f, session port 0x0000be0b
default	20:14:29.578727-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16207, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:14:29.578756-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:14:29.579647-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16207, subject=com.nexy.assistant,
default	20:14:29.580226-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	20:14:29.585760-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	20:14:29.599782-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 1B783A8C-B11A-40B9-90AC-67E27C6C2F92 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.50520,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xfd752131 tp_proto=0x06"
default	20:14:29.599901-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:50520<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762903 t_state: SYN_SENT process: Nexy:23856 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb94574bc
default	20:14:29.604933-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	20:14:29.608494-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:14:29.613492-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:14:29.613672-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:14:29.616643-0500	Nexy	nw_path_libinfo_path_check [D9FF84D0-0E39-4A3B-A1AC-EE729590E175 IPv4#ad06ed87:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:14:29.617355-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3B254F39-6857-478E-A3F9-37127CE992D3 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.50521,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x192792e9 tp_proto=0x06"
default	20:14:29.617434-0500	kernel	tcp connected: [<IPv4-redacted>:50520<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762903 t_state: ESTABLISHED process: Nexy:23856 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb94574bc
default	20:14:29.617455-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:50521<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 5762904 t_state: SYN_SENT process: Nexy:23856 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb96ebdfd
default	20:14:29.617813-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:50520<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762903 t_state: FIN_WAIT_1 process: Nexy:23856 Duration: 0.018 sec Conn_Time: 0.017 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 17.000 ms rttvar: 8.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xb94574bc
default	20:14:29.617825-0500	kernel	tcp_connection_summary [<IPv4-redacted>:50520<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762903 t_state: FIN_WAIT_1 process: Nexy:23856 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:14:29.618016-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 58A192CE-196F-4862-A38A-898500C576C5 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.50522,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x455f4e80 tp_proto=0x06"
default	20:14:29.618036-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:50522<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762905 t_state: SYN_SENT process: Nexy:23856 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x93ca29da
default	20:14:29.631737-0500	kernel	tcp connected: [<IPv4-redacted>:50522<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762905 t_state: ESTABLISHED process: Nexy:23856 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x93ca29da
default	20:14:29.631941-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:50522<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762905 t_state: FIN_WAIT_1 process: Nexy:23856 Duration: 0.014 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x93ca29da
default	20:14:29.631951-0500	kernel	tcp_connection_summary [<IPv4-redacted>:50522<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5762905 t_state: FIN_WAIT_1 process: Nexy:23856 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:14:29.639741-0500	kernel	tcp connected: [<IPv4-redacted>:50521<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 5762904 t_state: ESTABLISHED process: Nexy:23856 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb96ebdfd
default	20:14:29.726895-0500	Nexy	[0x778094b40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:14:29.730153-0500	Nexy	[0x778094c80] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:14:29.732492-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:14:29.732994-0500	Nexy	server port 0x0000be0b, session port 0x0000be0b
default	20:14:29.733812-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16208, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:14:29.733840-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:14:29.734812-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16208, subject=com.nexy.assistant,
default	20:14:29.735394-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	20:14:29.736397-0500	Nexy	[0x778094dc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:14:29.736857-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23856.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:14:29.742217-0500	tccd	AUTHREQ_SUBJECT: msgID=23856.5, subject=com.nexy.assistant,
default	20:14:29.742794-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	20:14:29.754673-0500	Nexy	New connection 0x19dfd3 main
default	20:14:29.755038-0500	Nexy	[0x778094dc0] invalidated after the last release of the connection object
default	20:14:29.756460-0500	Nexy	CHECKIN: pid=23856
default	20:14:29.762269-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:23856" ID:398-363-1489054 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:14:29.762343-0500	runningboardd	Assertion 398-363-1489054 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:29.762782-0500	Nexy	CHECKEDIN: pid=23856 asn=0x0-0x188a889 foreground=0
default	20:14:29.762720-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:29.762754-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:23856" ID:398-363-1489055 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:14:29.762782-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:29.762860-0500	runningboardd	Assertion 398-363-1489055 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:29.762892-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Set darwin role to: UserInteractive
default	20:14:29.762994-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:29.763096-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:29.762459-0500	launchservicesd	CHECKIN:0x0-0x188a889 23856 com.nexy.assistant
default	20:14:29.763643-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:14:29.763174-0500	Nexy	[0x778094f00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	20:14:29.763447-0500	Nexy	[0x778095040] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:14:29.763787-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:14:29.763456-0500	Nexy	[0x778095040] Connection returned listener port: 0xe403
default	20:14:29.763799-0500	Nexy	[0x77a404180] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x778095040.peer[363].0x77a404180
default	20:14:29.764883-0500	Nexy	FRONTLOGGING: version 1
default	20:14:29.764897-0500	Nexy	Registered, pid=23856 ASN=0x0,0x188a889
default	20:14:29.765036-0500	Nexy	[0x778095180] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:14:29.765059-0500	WindowServer	19dfd3[CreateApplication]: Process creation: 0x0-0x188a889 (Nexy) connectionID: 19DFD3 pid: 23856 in session 0x101
default	20:14:29.767417-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:14:29.767658-0500	runningboardd	Invalidating assertion 398-363-1489054 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	20:14:29.767808-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:14:29.768076-0500	Nexy	[0x778095040] Connection returned listener port: 0xe403
default	20:14:29.768464-0500	Nexy	BringForward: pid=23856 asn=0x0-0x188a889 bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	20:14:29.768889-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:14:29.770582-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:14:29.771385-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:14:29.798657-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:14:29.798803-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:14:29.803812-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	20:14:29.803822-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	20:14:29.803874-0500	Nexy	Initializing connection
default	20:14:29.803914-0500	Nexy	Removing all cached process handles
default	20:14:29.803941-0500	Nexy	Sending handshake request attempt #1 to server
default	20:14:29.803951-0500	Nexy	Creating connection to com.apple.runningboard
default	20:14:29.803958-0500	Nexy	[0x7780952c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	20:14:29.804339-0500	Nexy	[0x778095040] Connection returned listener port: 0xe403
default	20:14:29.804353-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] as ready
default	20:14:29.804989-0500	Nexy	Handshake succeeded
default	20:14:29.805006-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.20753384.20753390(501)>
default	20:14:29.805181-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 200000001b pid: 23856
default	20:14:29.807887-0500	Nexy	[0x778095040] Connection returned listener port: 0xe403
default	20:14:29.809178-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	20:14:29.809195-0500	Nexy	[0x778095400] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	20:14:29.809262-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	20:14:29.809309-0500	Nexy	[0x778095680] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:14:29.811621-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "frontmost:23856" ID:398-363-1489056 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractiveFocal" sourceEnvironment:"(null)">
	]>
default	20:14:29.811692-0500	runningboardd	Assertion 398-363-1489056 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:29.811963-0500	WindowServer	19dfd3[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x188a889 (Nexy) mainConnectionID: 19DFD3;
} for reason: updated frontmost process
default	20:14:29.812036-0500	WindowServer	19dfd3[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x188a889 (Nexy) -> <pid: 23856>
default	20:14:29.812171-0500	WindowServer	new deferring rules for pid:393: [
    [393-DB08]; <keyboardFocus; Nexy:0x0-0x188a889>; () -> <pid: 23856>; reason: frontmost PSN --> outbound target,
    [393-DB07]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x188a889; pid: 393>; reason: frontmost PSN,
    [393-DB06]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	20:14:29.812252-0500	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-DB08]; <keyboardFocus; Nexy:0x0-0x188a889>; () -> <pid: 23856>; reason: frontmost PSN --> outbound target,
    [393-DB07]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x188a889; pid: 393>; reason: frontmost PSN,
    [393-DB06]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	20:14:29.812275-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:29.812308-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:29.812365-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Set darwin role to: UserInteractiveFocal
default	20:14:29.812406-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:29.812516-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:29.812911-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "notification:23856" ID:398-363-1489057 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	20:14:29.813030-0500	runningboardd	Assertion 398-363-1489057 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:29.813335-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x188a889; pid: 393>,
    <pid: 23856>
]
default	20:14:29.813922-0500	Nexy	[0x778095680] Connection returned listener port: 0x14803
default	20:14:29.814404-0500	Nexy	Registered process with identifier 23856-2429108
default	20:14:29.816807-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	20:14:29.817087-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:29.817101-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:29.817112-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:29.817131-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:29.817866-0500	Nexy	[0x778095900] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	20:14:29.822809-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	20:14:29.827903-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	20:14:29.830760-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2400000020 pid: 23856
default	20:14:29.840966-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x7792c5360
 (
    "<NSDarkAquaAppearance: 0x7792c5400>",
    "<NSSystemAppearance: 0x7792c4fa0>"
)>
default	20:14:29.848228-0500	Nexy	[0x778095e00] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	20:14:29.850409-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	20:14:29.850652-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	20:14:29.850662-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	20:14:29.850684-0500	Nexy	[0x778095f40] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	20:14:29.851366-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	20:14:29.854475-0500	Nexy	[0x778096080] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	20:14:29.854696-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	20:14:29.854741-0500	Nexy	[0x7780961c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:14:29.854803-0500	Nexy	FBSWorkspace registering source: <private>
default	20:14:29.855468-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:14:29.855854-0500	Nexy	<FBSWorkspaceScenesClient:0x7792c64e0 <private>> attempting immediate handshake from activate
default	20:14:29.855897-0500	Nexy	<FBSWorkspaceScenesClient:0x7792c64e0 <private>> sent handshake
default	20:14:29.855987-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	20:14:29.856425-0500	Nexy	<FBSWorkspaceScenesClient:0x7792c64e0 <private>> was invalidated
default	20:14:29.856468-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:14:29.856631-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	20:14:29.857939-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	20:14:29.858709-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	20:14:29.859163-0500	Nexy	Requesting scene <FBSScene: 0x7792c6760; com.apple.controlcenter:8A20941E-0FC9-4C6A-956B-53447BB8F2DB> from com.apple.controlcenter.statusitems
error	20:14:29.859347-0500	Nexy	Error creating <FBSScene: 0x7792c6760; com.apple.controlcenter:8A20941E-0FC9-4C6A-956B-53447BB8F2DB>: <NSError: 0x77a2332a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	20:14:29.859401-0500	Nexy	Request for <FBSScene: 0x7792c6760; com.apple.controlcenter:8A20941E-0FC9-4C6A-956B-53447BB8F2DB> complete!
default	20:14:29.867197-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	20:14:29.874259-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:14:29.882162-0500	Nexy	Registering for test daemon availability notify post.
default	20:14:29.882313-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:14:29.882405-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:14:29.882494-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:14:29.884088-0500	Nexy	[0x778096580] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	20:14:29.884574-0500	Nexy	[0x778095040] Connection returned listener port: 0xe403
default	20:14:29.884870-0500	Nexy	SignalReady: pid=23856 asn=0x0-0x188a889
default	20:14:29.885137-0500	Nexy	SIGNAL: pid=23856 asn=0x0x-0x188a889
default	20:14:29.885632-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:14:29.887377-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
error	20:14:29.892040-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
default	20:14:29.895226-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:14:29.895231-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	20:14:29.895243-0500	Nexy	[0x778094dc0] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	20:14:29.895318-0500	Nexy	[0x778094dc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:14:29.896672-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:14:29.900851-0500	Nexy	[C:2] Alloc <private>
default	20:14:29.900888-0500	Nexy	[0x778094dc0] activating connection: mach=false listener=false peer=false name=(anonymous)
error	20:14:29.901040-0500	kernel	Sandbox: WindowManager(584) deny(1) mach-task-name others [Nexy(23856)]
default	20:14:29.901262-0500	Nexy	[0x778096800] activating connection: mach=false listener=false peer=false name=com.apple.ViewBridgeAuxiliary
default	20:14:29.902446-0500	WindowManager	Connection activated | (23856) Nexy
default	20:14:29.909521-0500	Nexy	[0x7780966c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:14:29.909950-0500	Nexy	[0x778096940] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:14:29.909964-0500	Nexy	[0x778096940] Connection returned listener port: 0x15c03
default	20:14:29.916414-0500	Nexy	[0x778096800] invalidated after the last release of the connection object
default	20:14:29.917011-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-23856-1489058 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:14:29.917067-0500	runningboardd	Assertion 398-23856-1489058 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:29.920778-0500	runningboardd	Invalidating assertion 398-23856-1489058 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856]
default	20:14:29.920804-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:29.920819-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:29.920897-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:29.920949-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-23856-1489059 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:14:29.920959-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:29.921022-0500	runningboardd	Assertion 398-23856-1489059 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:29.924200-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	20:14:29.924391-0500	runningboardd	Invalidating assertion 398-23856-1489059 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856]
default	20:14:29.924523-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-23856-1489060 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:14:29.924580-0500	runningboardd	Assertion 398-23856-1489060 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:29.924598-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:14:29.924782-0500	runningboardd	Invalidating assertion 398-23856-1489060 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856]
default	20:14:29.924880-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-23856-1489061 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:14:29.924921-0500	runningboardd	Assertion 398-23856-1489061 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:29.925115-0500	runningboardd	Invalidating assertion 398-23856-1489061 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856]
default	20:14:29.925203-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-23856-1489062 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:14:29.925235-0500	runningboardd	Assertion 398-23856-1489062 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:29.925437-0500	runningboardd	Invalidating assertion 398-23856-1489062 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856]
default	20:14:30.020349-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	20:14:30.024853-0500	Nexy	Start service name com.apple.spotlightknowledged
default	20:14:30.025639-0500	Nexy	[GMS] availability notification token 75
default	20:14:30.027915-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:30.027926-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:30.027937-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:30.027966-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:30.031481-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	20:14:30.031924-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:14:30.095168-0500	kernel	udp connect: [<IPv4-redacted>:52924<-><IPv4-redacted>:443] interface:  (skipped: 1081)
so_gencnt: 5762908 so_state: 0x0002 process: Nexy:23856 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x841f33a6
default	20:14:30.095189-0500	kernel	udp_connection_summary [<IPv4-redacted>:52924<-><IPv4-redacted>:443] interface:  (skipped: 1081)
so_gencnt: 5762908 so_state: 0x0002 process: Nexy:23856 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x841f33a6 flowctl: 0us (0x)
default	20:14:30.097516-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid C472A8D5-C785-498D-A97F-B426A5608355 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.50524,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x4958e3fe tp_proto=0x06"
default	20:14:30.097628-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:50524<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 5762910 t_state: SYN_SENT process: Nexy:23856 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 21 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x894149fe
default	20:14:30.119575-0500	kernel	tcp connected: [<IPv4-redacted>:50524<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 5762910 t_state: ESTABLISHED process: Nexy:23856 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 21 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x894149fe
default	20:14:30.146557-0500	Nexy	[0x778094a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:14:30.147254-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23856.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:14:30.148420-0500	tccd	AUTHREQ_SUBJECT: msgID=23856.6, subject=com.nexy.assistant,
default	20:14:30.149040-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	20:14:30.152415-0500	Nexy	[0x778096800] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	20:14:30.156133-0500	Nexy	+[IMKClient subclass]: chose IMKClient_Modern
default	20:14:30.156164-0500	Nexy	+[IMKInputSession subclass]: chose IMKInputSession_Modern
default	20:14:30.158179-0500	Nexy	[0x778096a80] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	20:14:30.159060-0500	Nexy	[0x778096bc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:14:30.162344-0500	Nexy	[0x778094a00] invalidated after the last release of the connection object
default	20:14:30.162373-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:14:30.162723-0500	Nexy	[0x778094a00] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	20:14:30.162812-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	20:14:30.162868-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	20:14:30.164705-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=87854.12, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=87854, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:14:30.164731-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=87854, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:14:30.165599-0500	tccd	AUTHREQ_SUBJECT: msgID=87854.12, subject=com.nexy.assistant,
default	20:14:30.166184-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	20:14:30.175230-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23913.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=23913, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:14:30.176403-0500	tccd	AUTHREQ_SUBJECT: msgID=23913.1, subject=com.nexy.assistant,
default	20:14:30.176943-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	20:14:30.183734-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16209, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:14:30.183759-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:14:30.184590-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16209, subject=com.nexy.assistant,
default	20:14:30.185162-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d1db300 at /Applications/Nexy.app
default	20:14:30.209134-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	20:14:30.213850-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16210, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=23913, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:14:30.214760-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16210, subject=com.nexy.assistant,
default	20:14:30.215349-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	20:14:30.243973-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	20:14:30.260265-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 23863: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 cb102500 };
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
default	20:14:30.270703-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:14:30.293083-0500	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x188a889 (Nexy) mainConnectionID: 19DFD3;
} for reason: deferringPolicyEvaluationSuppression
default	20:14:30.293145-0500	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x188a889 (Nexy) -> <pid: 23856>
default	20:14:30.293231-0500	WindowServer	new deferring rules for pid:393: [
    [393-DB0B]; <keyboardFocus; Nexy:0x0-0x188a889>; () -> <pid: 23856>; reason: frontmost PSN --> outbound target,
    [393-DB0A]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x188a889; pid: 393>; reason: frontmost PSN,
    [393-DB09]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	20:14:30.293267-0500	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-DB0B]; <keyboardFocus; Nexy:0x0-0x188a889>; () -> <pid: 23856>; reason: frontmost PSN --> outbound target,
    [393-DB0A]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x188a889; pid: 393>; reason: frontmost PSN,
    [393-DB09]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	20:14:30.293827-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x188a889; pid: 393>,
    <pid: 23856>
]
default	20:14:30.474443-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60346)
default	20:14:30.474519-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:60346 called from <private>
default	20:14:30.474528-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60346 called from <private>
default	20:14:30.475444-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60347)
default	20:14:30.475486-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:60347 called from <private>
default	20:14:30.475493-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60347 called from <private>
default	20:14:30.489237-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60346 called from <private>
default	20:14:30.489269-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60346 called from <private>
default	20:14:30.490217-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60346)
default	20:14:30.490250-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:60346 called from <private>
default	20:14:30.490257-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:60346 called from <private>
default	20:14:30.495280-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60346)
default	20:14:30.495332-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:60346 called from <private>
default	20:14:30.495342-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:60346 called from <private>
default	20:14:30.495492-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60346)
default	20:14:30.495754-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60346)
default	20:14:30.500246-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60346 called from <private>
default	20:14:30.500277-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60346 called from <private>
default	20:14:30.500313-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60346 called from <private>
default	20:14:30.500324-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:60346 called from <private>
default	20:14:30.500330-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:60346 called from <private>
default	20:14:30.500336-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60346 called from <private>
default	20:14:30.502141-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60346)
default	20:14:30.504503-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60347)
default	20:14:30.504542-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60347 called from <private>
default	20:14:30.504549-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:60347 called from <private>
default	20:14:30.504925-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:60346 called from <private>
default	20:14:30.504936-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:60346 called from <private>
default	20:14:30.518498-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:60346 called from <private>
default	20:14:30.518528-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:60346 called from <private>
default	20:14:30.518611-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60346)
default	20:14:30.531192-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60346)
default	20:14:30.531579-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:60346 called from <private>
default	20:14:30.531593-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:60346 called from <private>
default	20:14:30.531713-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(60346)
default	20:14:30.537060-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(60346)
default	20:14:30.537388-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:60346 called from <private>
default	20:14:30.537398-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:60346 called from <private>
default	20:14:30.537451-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60346 called from <private>
default	20:14:30.537467-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:60346 called from <private>
default	20:14:30.537482-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:60346 called from <private>
default	20:14:30.537487-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60346 called from <private>
default	20:14:30.537494-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60346 called from <private>
default	20:14:30.537967-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:60346 called from <private>
default	20:14:30.538091-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:60346 called from <private>
default	20:14:30.538183-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:60346 called from <private>
default	20:14:30.538268-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:60346 called from <private>
default	20:14:30.538355-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:60346 called from <private>
default	20:14:30.677324-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7790f5540) Selecting device 85 from constructor
default	20:14:30.677347-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7790f5540)
default	20:14:30.677356-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7790f5540) not already running
default	20:14:30.677361-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7790f5540) nothing to teardown
default	20:14:30.677366-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7790f5540) connecting device 85
default	20:14:30.677480-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7790f5540) Device ID: 85 (Input:No | Output:Yes): true
default	20:14:30.677630-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7790f5540) created ioproc 0xb for device 85
default	20:14:30.677773-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f5540) adding 7 device listeners to device 85
default	20:14:30.677983-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f5540) adding 0 device delegate listeners to device 85
default	20:14:30.677997-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7790f5540)
default	20:14:30.678090-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:14:30.678098-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	20:14:30.678106-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:14:30.678113-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	20:14:30.678122-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:14:30.678251-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7790f5540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:14:30.678267-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7790f5540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:14:30.678276-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:14:30.678282-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f5540) removing 0 device listeners from device 0
default	20:14:30.678287-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f5540) removing 0 device delegate listeners from device 0
default	20:14:30.678293-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7790f5540)
default	20:14:30.678311-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7790f5540) caller requesting device change from 85 to 85
default	20:14:30.678316-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7790f5540)
default	20:14:30.678320-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x7790f5540) exiting with nothing to do
default	20:14:30.678836-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:14:30.679157-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:14:30.680212-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:14:30.681747-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7790f5540) Selecting device 0 from destructor
default	20:14:30.681760-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7790f5540)
default	20:14:30.681767-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7790f5540) not already running
default	20:14:30.681788-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7790f5540) disconnecting device 85
default	20:14:30.681793-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7790f5540) destroying ioproc 0xb for device 85
default	20:14:30.681830-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:14:30.681906-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:14:30.682066-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x7790f5540) nothing to setup
default	20:14:30.682080-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f5540) adding 0 device listeners to device 0
default	20:14:30.682086-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f5540) adding 0 device delegate listeners to device 0
default	20:14:30.682092-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f5540) removing 7 device listeners from device 85
default	20:14:30.682285-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f5540) removing 0 device delegate listeners from device 85
default	20:14:30.682301-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7790f5540)
default	20:14:30.683525-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7790f5540) Selecting device 85 from constructor
default	20:14:30.683540-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7790f5540)
default	20:14:30.683548-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7790f5540) not already running
default	20:14:30.683554-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7790f5540) nothing to teardown
default	20:14:30.683559-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7790f5540) connecting device 85
default	20:14:30.683672-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7790f5540) Device ID: 85 (Input:No | Output:Yes): true
default	20:14:30.683852-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7790f5540) created ioproc 0xc for device 85
default	20:14:30.684020-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f5540) adding 7 device listeners to device 85
default	20:14:30.684263-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7790f5540) adding 0 device delegate listeners to device 85
default	20:14:30.684276-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7790f5540)
default	20:14:30.684386-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:14:30.684398-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	20:14:30.684406-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:14:30.684417-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	20:14:30.684427-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:14:30.684547-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7790f5540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:14:30.684564-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7790f5540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:14:30.684571-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:14:30.684576-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f5540) removing 0 device listeners from device 0
default	20:14:30.684581-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7790f5540) removing 0 device delegate listeners from device 0
default	20:14:30.684587-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7790f5540)
default	20:14:30.684627-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7790f5540) caller requesting device change from 85 to 85
default	20:14:30.684636-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7790f5540)
default	20:14:30.684640-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x7790f5540) exiting with nothing to do
default	20:14:30.684673-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	20:14:30.685156-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:14:30.685512-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:14:30.688560-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-23856-1489065 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:14:30.688679-0500	runningboardd	Assertion 398-23856-1489065 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:30.689836-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:30.689976-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:30.690124-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:30.690318-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:30.689857-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20753384.20753390(501)>:23856] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1489066 target:23856 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:14:30.690498-0500	runningboardd	Assertion 398-334-1489066 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) will be created as active
default	20:14:30.694832-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	20:14:30.695137-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:30.695148-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:30.695166-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:30.695225-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:30.695542-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:14:30.698574-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	20:14:30.699048-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:14:30.893481-0500	Nexy	FBSWorkspace registering source: <private>
default	20:14:30.893532-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:14:30.893624-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a4f00 <private>> attempting immediate handshake from activate
default	20:14:30.893662-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a4f00 <private>> sent handshake
default	20:14:30.894078-0500	Nexy	Requesting scene <FBSScene: 0x77a3a54a0; com.apple.controlcenter:7D1DA87D-9EB4-44D3-BE83-0136C8464FC8> from com.apple.controlcenter.statusitems
default	20:14:30.894515-0500	Nexy	Request for <FBSScene: 0x77a3a54a0; com.apple.controlcenter:7D1DA87D-9EB4-44D3-BE83-0136C8464FC8> complete!
default	20:14:30.894599-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a4f00 <private>> was invalidated
default	20:14:30.894675-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:14:30.894689-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
error	20:14:30.894789-0500	Nexy	Error creating <FBSScene: 0x77a3a54a0; com.apple.controlcenter:7D1DA87D-9EB4-44D3-BE83-0136C8464FC8>: <NSError: 0x77a4d0600; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:14:30.894836-0500	Nexy	No scene exists for identity: com.apple.controlcenter:7D1DA87D-9EB4-44D3-BE83-0136C8464FC8
default	20:14:30.896358-0500	Nexy	FBSWorkspace registering source: <private>
default	20:14:30.896373-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:14:30.896423-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> attempting immediate handshake from activate
default	20:14:30.896441-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> sent handshake
default	20:14:30.896516-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	20:14:30.896872-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	20:14:30.896944-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> was invalidated
default	20:14:30.896961-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:14:30.897238-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	20:14:30.897279-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	20:14:30.897656-0500	Nexy	Requesting scene <FBSScene: 0x77a3a5400; com.apple.controlcenter:7D1DA87D-9EB4-44D3-BE83-0136C8464FC8-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	20:14:30.897840-0500	Nexy	Error creating <FBSScene: 0x77a3a5400; com.apple.controlcenter:7D1DA87D-9EB4-44D3-BE83-0136C8464FC8-Aux[1]-NSStatusItemView>: <NSError: 0x77a4d03f0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	20:14:30.897885-0500	Nexy	Request for <FBSScene: 0x77a3a5400; com.apple.controlcenter:7D1DA87D-9EB4-44D3-BE83-0136C8464FC8-Aux[1]-NSStatusItemView> complete!
error	20:14:30.898267-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:30.898288-0500	Nexy	[com.apple.controlcenter:7D1DA87D-9EB4-44D3-BE83-0136C8464FC8] No matching scene to invalidate for this identity.
error	20:14:30.898315-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:30.898371-0500	Nexy	Unhandled disconnected scene <private>
error	20:14:30.898467-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:14:31.247648-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	20:14:31.248660-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef287","name":"Nexy(23856)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:14:31.248820-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:14:31.248853-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef287, Nexy(23856), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:14:31.248886-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:14:31.248931-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef287, Nexy(23856), 'prim'', AudioCategory changed to 'MediaPlayback'
default	20:14:31.248953-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:31.248996-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:14:31.249008-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 648 starting playing
default	20:14:31.249105-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:14:31.249138-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:14:31.249176-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef287, Nexy(23856), 'prim'', displayID:'com.nexy.assistant'}
default	20:14:31.249200-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	20:14:31.249130-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:31.249255-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:31.249269-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef287 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":23856}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef287, sessionType: 'prim', isRecording: false }, 
]
default	20:14:31.249491-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:14:31.249597-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	20:14:31.249332-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:14:31.249505-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:14:31.251296-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:14:31.251418-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:14:31.251446-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:14:31.251457-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	20:14:31.251467-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	20:14:31.251480-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	20:14:31.251547-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	20:14:31.899761-0500	Nexy	FBSWorkspace registering source: <private>
default	20:14:31.899801-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:14:31.899894-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> attempting immediate handshake from activate
default	20:14:31.899926-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> sent handshake
default	20:14:31.900249-0500	Nexy	Requesting scene <FBSScene: 0x77a3a5400; com.apple.controlcenter:FCAB7492-D68D-4178-9684-3853D37F7155> from com.apple.controlcenter.statusitems
default	20:14:31.900518-0500	Nexy	Request for <FBSScene: 0x77a3a5400; com.apple.controlcenter:FCAB7492-D68D-4178-9684-3853D37F7155> complete!
default	20:14:31.900890-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> was invalidated
default	20:14:31.900929-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:14:31.901040-0500	Nexy	Error creating <FBSScene: 0x77a3a5400; com.apple.controlcenter:FCAB7492-D68D-4178-9684-3853D37F7155>: <NSError: 0x77a4d0900; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:14:31.901060-0500	Nexy	No scene exists for identity: com.apple.controlcenter:FCAB7492-D68D-4178-9684-3853D37F7155
default	20:14:31.901094-0500	Nexy	Requesting scene <FBSScene: 0x77a3a54a0; com.apple.controlcenter:FCAB7492-D68D-4178-9684-3853D37F7155-Aux[2]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	20:14:31.901212-0500	Nexy	Error creating <FBSScene: 0x77a3a54a0; com.apple.controlcenter:FCAB7492-D68D-4178-9684-3853D37F7155-Aux[2]-NSStatusItemView>: <NSError: 0x77a4d0120; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	20:14:31.901258-0500	Nexy	Request for <FBSScene: 0x77a3a54a0; com.apple.controlcenter:FCAB7492-D68D-4178-9684-3853D37F7155-Aux[2]-NSStatusItemView> complete!
error	20:14:31.901448-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:31.901467-0500	Nexy	[com.apple.controlcenter:FCAB7492-D68D-4178-9684-3853D37F7155] No matching scene to invalidate for this identity.
error	20:14:31.901493-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:31.901532-0500	Nexy	Unhandled disconnected scene <private>
error	20:14:31.901604-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:14:32.902672-0500	Nexy	FBSWorkspace registering source: <private>
default	20:14:32.902729-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:14:32.902861-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a54a0 <private>> attempting immediate handshake from activate
default	20:14:32.902909-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a54a0 <private>> sent handshake
default	20:14:32.903342-0500	Nexy	Requesting scene <FBSScene: 0x77a3a5400; com.apple.controlcenter:F58E860B-F1EF-4B4F-9523-06FF73730FEE> from com.apple.controlcenter.statusitems
default	20:14:32.903708-0500	Nexy	Request for <FBSScene: 0x77a3a5400; com.apple.controlcenter:F58E860B-F1EF-4B4F-9523-06FF73730FEE> complete!
default	20:14:32.904146-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a54a0 <private>> was invalidated
default	20:14:32.904182-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:14:32.904301-0500	Nexy	Error creating <FBSScene: 0x77a3a5400; com.apple.controlcenter:F58E860B-F1EF-4B4F-9523-06FF73730FEE>: <NSError: 0x77a4d0690; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:14:32.904328-0500	Nexy	No scene exists for identity: com.apple.controlcenter:F58E860B-F1EF-4B4F-9523-06FF73730FEE
default	20:14:32.904376-0500	Nexy	Requesting scene <FBSScene: 0x77a3a55e0; com.apple.controlcenter:F58E860B-F1EF-4B4F-9523-06FF73730FEE-Aux[3]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	20:14:32.904520-0500	Nexy	Error creating <FBSScene: 0x77a3a55e0; com.apple.controlcenter:F58E860B-F1EF-4B4F-9523-06FF73730FEE-Aux[3]-NSStatusItemView>: <NSError: 0x77a4d05a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	20:14:32.904576-0500	Nexy	Request for <FBSScene: 0x77a3a55e0; com.apple.controlcenter:F58E860B-F1EF-4B4F-9523-06FF73730FEE-Aux[3]-NSStatusItemView> complete!
error	20:14:32.904807-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:32.904830-0500	Nexy	[com.apple.controlcenter:F58E860B-F1EF-4B4F-9523-06FF73730FEE] No matching scene to invalidate for this identity.
error	20:14:32.904866-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:32.904925-0500	Nexy	Unhandled disconnected scene <private>
error	20:14:32.905019-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:14:33.105937-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	20:14:33.906440-0500	Nexy	FBSWorkspace registering source: <private>
default	20:14:33.906503-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:14:33.906640-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> attempting immediate handshake from activate
default	20:14:33.906689-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> sent handshake
default	20:14:33.907139-0500	Nexy	Requesting scene <FBSScene: 0x77a3a5400; com.apple.controlcenter:EC594D8C-64CA-45E1-A865-D6B756139AA7> from com.apple.controlcenter.statusitems
default	20:14:33.907557-0500	Nexy	Request for <FBSScene: 0x77a3a5400; com.apple.controlcenter:EC594D8C-64CA-45E1-A865-D6B756139AA7> complete!
default	20:14:33.908062-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> was invalidated
default	20:14:33.908102-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:14:33.908162-0500	Nexy	FBSWorkspace registering source: <private>
default	20:14:33.908185-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:14:33.908241-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a54a0 <private>> attempting immediate handshake from activate
default	20:14:33.908267-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a54a0 <private>> sent handshake
error	20:14:33.908343-0500	Nexy	Error creating <FBSScene: 0x77a3a5400; com.apple.controlcenter:EC594D8C-64CA-45E1-A865-D6B756139AA7>: <NSError: 0x77a4d0480; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:14:33.908368-0500	Nexy	No scene exists for identity: com.apple.controlcenter:EC594D8C-64CA-45E1-A865-D6B756139AA7
default	20:14:33.908442-0500	Nexy	Requesting scene <FBSScene: 0x77a3a4f00; com.apple.controlcenter:EC594D8C-64CA-45E1-A865-D6B756139AA7-Aux[4]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:14:33.908771-0500	Nexy	Request for <FBSScene: 0x77a3a4f00; com.apple.controlcenter:EC594D8C-64CA-45E1-A865-D6B756139AA7-Aux[4]-NSStatusItemView> complete!
default	20:14:33.908780-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a54a0 <private>> was invalidated
default	20:14:33.908808-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:14:33.908874-0500	Nexy	Error creating <FBSScene: 0x77a3a4f00; com.apple.controlcenter:EC594D8C-64CA-45E1-A865-D6B756139AA7-Aux[4]-NSStatusItemView>: <NSError: 0x77a4d08a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:14:33.908895-0500	Nexy	No scene exists for identity: com.apple.controlcenter:EC594D8C-64CA-45E1-A865-D6B756139AA7-Aux[4]-NSStatusItemView
default	20:14:33.909714-0500	Nexy	[com.apple.controlcenter:EC594D8C-64CA-45E1-A865-D6B756139AA7-Aux[4]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	20:14:33.909991-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:33.910007-0500	Nexy	[com.apple.controlcenter:EC594D8C-64CA-45E1-A865-D6B756139AA7] No matching scene to invalidate for this identity.
error	20:14:33.910028-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:33.910041-0500	Nexy	[com.apple.controlcenter:EC594D8C-64CA-45E1-A865-D6B756139AA7-Aux[4]-NSStatusItemView] No matching scene to invalidate for this identity.
error	20:14:33.910429-0500	Nexy	Unhandled disconnected scene <private>
error	20:14:33.910501-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	20:14:33.910576-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	20:14:33.910617-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:14:34.832745-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=0
default	20:14:34.839632-0500	runningboardd	Assertion did invalidate due to timeout: 398-363-1489057 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856])
default	20:14:34.911087-0500	Nexy	FBSWorkspace registering source: <private>
default	20:14:34.911145-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:14:34.911266-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a4f00 <private>> attempting immediate handshake from activate
default	20:14:34.911308-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a4f00 <private>> sent handshake
default	20:14:34.911701-0500	Nexy	Requesting scene <FBSScene: 0x77a3a5400; com.apple.controlcenter:36F8D684-7D74-49DE-A088-E01B93EABD5F> from com.apple.controlcenter.statusitems
default	20:14:34.912045-0500	Nexy	Request for <FBSScene: 0x77a3a5400; com.apple.controlcenter:36F8D684-7D74-49DE-A088-E01B93EABD5F> complete!
default	20:14:34.912559-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a4f00 <private>> was invalidated
default	20:14:34.912602-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:14:34.912729-0500	Nexy	Error creating <FBSScene: 0x77a3a5400; com.apple.controlcenter:36F8D684-7D74-49DE-A088-E01B93EABD5F>: <NSError: 0x77a4d0900; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:14:34.912760-0500	Nexy	No scene exists for identity: com.apple.controlcenter:36F8D684-7D74-49DE-A088-E01B93EABD5F
default	20:14:34.912830-0500	Nexy	Requesting scene <FBSScene: 0x77a3a54a0; com.apple.controlcenter:36F8D684-7D74-49DE-A088-E01B93EABD5F-Aux[5]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	20:14:34.913013-0500	Nexy	Error creating <FBSScene: 0x77a3a54a0; com.apple.controlcenter:36F8D684-7D74-49DE-A088-E01B93EABD5F-Aux[5]-NSStatusItemView>: <NSError: 0x77a4d0b40; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	20:14:34.913089-0500	Nexy	Request for <FBSScene: 0x77a3a54a0; com.apple.controlcenter:36F8D684-7D74-49DE-A088-E01B93EABD5F-Aux[5]-NSStatusItemView> complete!
error	20:14:34.913321-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:34.913348-0500	Nexy	[com.apple.controlcenter:36F8D684-7D74-49DE-A088-E01B93EABD5F] No matching scene to invalidate for this identity.
error	20:14:34.913391-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:34.913431-0500	Nexy	Unhandled disconnected scene <private>
error	20:14:34.913516-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:14:35.035803-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:35.035834-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:35.035854-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:35.035902-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:35.040586-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	20:14:35.041305-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:14:35.690623-0500	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x188a889 (Nexy) mainConnectionID: 19DFD3;
} for reason: deferringPolicyEvaluationSuppression
default	20:14:35.690745-0500	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x188a889 (Nexy) -> <pid: 23856>
default	20:14:35.690906-0500	WindowServer	new deferring rules for pid:393: [
    [393-DB0E]; <keyboardFocus; Nexy:0x0-0x188a889>; () -> <pid: 23856>; reason: frontmost PSN --> outbound target,
    [393-DB0D]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x188a889; pid: 393>; reason: frontmost PSN,
    [393-DB0C]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	20:14:35.690960-0500	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-DB0E]; <keyboardFocus; Nexy:0x0-0x188a889>; () -> <pid: 23856>; reason: frontmost PSN --> outbound target,
    [393-DB0D]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x188a889; pid: 393>; reason: frontmost PSN,
    [393-DB0C]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	20:14:35.691837-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x188a889; pid: 393>,
    <pid: 23856>
]
default	20:14:35.867279-0500	runningboardd	Invalidating assertion 398-363-1489056 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	20:14:35.875786-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	20:14:35.914545-0500	Nexy	FBSWorkspace registering source: <private>
default	20:14:35.914570-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:14:35.914623-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a54a0 <private>> attempting immediate handshake from activate
default	20:14:35.914642-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a54a0 <private>> sent handshake
default	20:14:35.914815-0500	Nexy	Requesting scene <FBSScene: 0x77a3a4f00; com.apple.controlcenter:0A930043-1166-46C2-9ACC-0B711B215372> from com.apple.controlcenter.statusitems
default	20:14:35.914972-0500	Nexy	Request for <FBSScene: 0x77a3a4f00; com.apple.controlcenter:0A930043-1166-46C2-9ACC-0B711B215372> complete!
default	20:14:35.915199-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a54a0 <private>> was invalidated
default	20:14:35.915221-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:14:35.915267-0500	Nexy	Error creating <FBSScene: 0x77a3a4f00; com.apple.controlcenter:0A930043-1166-46C2-9ACC-0B711B215372>: <NSError: 0x77a4d0420; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:14:35.915282-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0A930043-1166-46C2-9ACC-0B711B215372
default	20:14:35.915333-0500	Nexy	Requesting scene <FBSScene: 0x77a3a55e0; com.apple.controlcenter:0A930043-1166-46C2-9ACC-0B711B215372-Aux[6]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	20:14:35.915425-0500	Nexy	Error creating <FBSScene: 0x77a3a55e0; com.apple.controlcenter:0A930043-1166-46C2-9ACC-0B711B215372-Aux[6]-NSStatusItemView>: <NSError: 0x77a4d0a50; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	20:14:35.915462-0500	Nexy	Request for <FBSScene: 0x77a3a55e0; com.apple.controlcenter:0A930043-1166-46C2-9ACC-0B711B215372-Aux[6]-NSStatusItemView> complete!
error	20:14:35.915574-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:35.915589-0500	Nexy	[com.apple.controlcenter:0A930043-1166-46C2-9ACC-0B711B215372] No matching scene to invalidate for this identity.
error	20:14:35.915611-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:35.915635-0500	Nexy	Unhandled disconnected scene <private>
error	20:14:35.915674-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:14:35.973232-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:35.973243-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:35.973282-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Set darwin role to: UserInteractive
default	20:14:35.973299-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:35.973318-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:35.976809-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:14:35.977217-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:14:36.105952-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	20:14:36.649990-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	20:14:36.650367-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef287","name":"Nexy(23856)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:14:36.650475-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 648 stopping playing
default	20:14:36.650530-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:14:36.650573-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:14:36.650645-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 648, PID = 23856, Name = sid:0x1ef287, Nexy(23856), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:14:36.650743-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:36.650798-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef287 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":23856}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef287, sessionType: 'prim', isRecording: false }, 
]
default	20:14:36.650871-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:14:36.650883-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:14:36.650938-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:36.651002-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:14:36.651026-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:14:36.655179-0500	runningboardd	Invalidating assertion 398-23856-1489065 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [app<application.com.nexy.assistant.20753384.20753390(501)>:23856]
default	20:14:36.655299-0500	runningboardd	Invalidating assertion 398-334-1489066 (target:[app<application.com.nexy.assistant.20753384.20753390(501)>:23856]) from originator [osservice<com.apple.powerd>:334]
default	20:14:36.662491-0500	coreaudiod	Sending message. { reporterID=102460739813380, category=IO, type=error, message=["anchor_sample_time": Optional(2692), "num_continuous_nonzero_io_cycles": Optional(0), "wg_user_time_mach": Optional(13715), "is_recovering": Optional(0), "smallest_buffer_frame_size": Optional(2147483647), "output_device_source_list": Optional(Unknown), "HostApplicationDisplayID": Optional(com.nexy.assistant), "scheduler_latency": Optional(15000), "overload_type": Optional(Overload), "cause_set": Optional(12), "HAL_client_IO_duration": Optional(26216083), "wg_external_wakeups": Optional(3), "other_page_faults": Optional(0), "deadline": Optional(261284), "wg_cycles": Optional(1302924), "start_time": Optional(12521820219726), "sample_rate": Optional(48000), "careporting_timestamp": 1762305276.662235, "io_page_faults": Optional(0), "io_buffer_size": Optional(512), "multi_cycle_io_page_faults": Optional(0), "wg_instructions": Optional(860276), "output_device_transport_list": Optional(Bluetooth), "multi_cycle_io_page_faults_duration": Optional(0), "safety_violation": Optio<…> }
default	20:14:36.762790-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring jetsam update because this process is not memory-managed
default	20:14:36.762815-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring suspend because this process is not lifecycle managed
default	20:14:36.762834-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring GPU update because this process is not GPU managed
default	20:14:36.762861-0500	runningboardd	[app<application.com.nexy.assistant.20753384.20753390(501)>:23856] Ignoring memory limit update because this process is not memory-managed
default	20:14:36.767373-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20753384.20753390(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:14:36.768095-0500	gamepolicyd	Received state update for 23856 (app<application.com.nexy.assistant.20753384.20753390(501)>, running-active-NotVisible
default	20:14:36.843019-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23915.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=23915, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:14:36.844383-0500	tccd	AUTHREQ_SUBJECT: msgID=23915.1, subject=com.nexy.assistant,
default	20:14:36.844975-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	20:14:36.859258-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16213, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=23856, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=23915, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:14:36.860162-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16213, subject=com.nexy.assistant,
default	20:14:36.860755-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	20:14:36.893831-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	20:14:36.914717-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 23863: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 d0102500 };
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
default	20:14:36.916029-0500	Nexy	FBSWorkspace registering source: <private>
default	20:14:36.916054-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:14:36.916110-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> attempting immediate handshake from activate
default	20:14:36.916134-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> sent handshake
default	20:14:36.916332-0500	Nexy	Requesting scene <FBSScene: 0x77a3a5400; com.apple.controlcenter:0D7621AD-37BF-4B04-9ED6-E1E294758CB0> from com.apple.controlcenter.statusitems
default	20:14:36.916515-0500	Nexy	Request for <FBSScene: 0x77a3a5400; com.apple.controlcenter:0D7621AD-37BF-4B04-9ED6-E1E294758CB0> complete!
default	20:14:36.916806-0500	Nexy	Requesting scene <FBSScene: 0x77a3a5680; com.apple.controlcenter:0D7621AD-37BF-4B04-9ED6-E1E294758CB0-Aux[7]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:14:36.916857-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a55e0 <private>> was invalidated
default	20:14:36.916886-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:14:36.916929-0500	Nexy	Request for <FBSScene: 0x77a3a5680; com.apple.controlcenter:0D7621AD-37BF-4B04-9ED6-E1E294758CB0-Aux[7]-NSStatusItemView> complete!
error	20:14:36.916944-0500	Nexy	Error creating <FBSScene: 0x77a3a5400; com.apple.controlcenter:0D7621AD-37BF-4B04-9ED6-E1E294758CB0>: <NSError: 0x77a22d440; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:14:36.916956-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0D7621AD-37BF-4B04-9ED6-E1E294758CB0
error	20:14:36.916982-0500	Nexy	Error creating <FBSScene: 0x77a3a5680; com.apple.controlcenter:0D7621AD-37BF-4B04-9ED6-E1E294758CB0-Aux[7]-NSStatusItemView>: <NSError: 0x77a22d320; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:14:36.916991-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0D7621AD-37BF-4B04-9ED6-E1E294758CB0-Aux[7]-NSStatusItemView
error	20:14:36.917067-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:36.917078-0500	Nexy	[com.apple.controlcenter:0D7621AD-37BF-4B04-9ED6-E1E294758CB0] No matching scene to invalidate for this identity.
error	20:14:36.917095-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:36.917162-0500	Nexy	Unhandled disconnected scene <private>
error	20:14:36.917208-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:14:36.926168-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:14:37.918625-0500	Nexy	FBSWorkspace registering source: <private>
default	20:14:37.918674-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:14:37.918791-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a5400 <private>> attempting immediate handshake from activate
default	20:14:37.918832-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a5400 <private>> sent handshake
default	20:14:37.919226-0500	Nexy	Requesting scene <FBSScene: 0x77a3a5680; com.apple.controlcenter:99F8C44E-8175-4078-B7D3-CB5718F867F5> from com.apple.controlcenter.statusitems
default	20:14:37.919567-0500	Nexy	Request for <FBSScene: 0x77a3a5680; com.apple.controlcenter:99F8C44E-8175-4078-B7D3-CB5718F867F5> complete!
default	20:14:37.920027-0500	Nexy	<FBSWorkspaceScenesClient:0x77a3a5400 <private>> was invalidated
default	20:14:37.920073-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:14:37.920211-0500	Nexy	Error creating <FBSScene: 0x77a3a5680; com.apple.controlcenter:99F8C44E-8175-4078-B7D3-CB5718F867F5>: <NSError: 0x77a4d0690; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:14:37.920239-0500	Nexy	No scene exists for identity: com.apple.controlcenter:99F8C44E-8175-4078-B7D3-CB5718F867F5
default	20:14:37.920291-0500	Nexy	Requesting scene <FBSScene: 0x77a3a55e0; com.apple.controlcenter:99F8C44E-8175-4078-B7D3-CB5718F867F5-Aux[8]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	20:14:37.920458-0500	Nexy	Error creating <FBSScene: 0x77a3a55e0; com.apple.controlcenter:99F8C44E-8175-4078-B7D3-CB5718F867F5-Aux[8]-NSStatusItemView>: <NSError: 0x77a4d0a20; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	20:14:37.920546-0500	Nexy	Request for <FBSScene: 0x77a3a55e0; com.apple.controlcenter:99F8C44E-8175-4078-B7D3-CB5718F867F5-Aux[8]-NSStatusItemView> complete!
error	20:14:37.920777-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:37.920806-0500	Nexy	[com.apple.controlcenter:99F8C44E-8175-4078-B7D3-CB5718F867F5] No matching scene to invalidate for this identity.
error	20:14:37.920850-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:14:37.920888-0500	Nexy	Unhandled disconnected scene <private>
error	20:14:37.920977-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
