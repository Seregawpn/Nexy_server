default	23:25:54.882442-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	23:25:54.882587-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	23:25:54.884073-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:25:54.886547-0400	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	23:25:54.890747-0400	runningboardd	Launch request for app<application.com.nexy.assistant.18912707.18912713(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	23:25:54.890825-0400	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.18912707.18912713(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:17058] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-17058-449177 target:app<application.com.nexy.assistant.18912707.18912713(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	23:25:54.890908-0400	runningboardd	Assertion 398-17058-449177 (target:app<application.com.nexy.assistant.18912707.18912713(501)>) will be created as active
default	23:25:54.893841-0400	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	23:25:54.893873-0400	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.18912707.18912713(501)>
default	23:25:54.893886-0400	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	23:25:54.893940-0400	runningboardd	app<application.com.nexy.assistant.18912707.18912713(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000954 ms (wallclock); resolved to {4294967295, (null)}
default	23:25:54.928108-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] is not RunningBoard jetsam managed.
default	23:25:54.928123-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] This process will not be managed.
default	23:25:54.928137-0400	runningboardd	Now tracking process: [app<application.com.nexy.assistant.18912707.18912713(501)>:45569]
default	23:25:54.928277-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:25:54.929189-0400	gamepolicyd	Hit the server for a process handle 74fd9420000b201 that resolved to: [app<application.com.nexy.assistant.18912707.18912713(501)>:45569]
default	23:25:54.929233-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-active-NotVisible
default	23:25:54.931756-0400	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.18912707.18912713(501)>:45569]
default	23:25:54.931828-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18912707.18912713(501)>:45569] from originator [app<application.com.nexy.assistant.18912707.18912713(501)>:45569] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-449179 target:45569 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:25:54.932029-0400	runningboardd	Assertion 398-398-449179 (target:[app<application.com.nexy.assistant.18912707.18912713(501)>:45569]) will be created as active
default	23:25:54.932213-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring jetsam update because this process is not memory-managed
default	23:25:54.932229-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring suspend because this process is not lifecycle managed
default	23:25:54.932260-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Set darwin role to: UserInteractive
default	23:25:54.932269-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:25:54.932286-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:25:54.932333-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] reported to RB as running
default	23:25:54.933958-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18912707.18912713(501)>:45569] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:45569" ID:398-363-449180 target:45569 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	23:25:54.934211-0400	runningboardd	Assertion 398-363-449180 (target:[app<application.com.nexy.assistant.18912707.18912713(501)>:45569]) will be created as active
default	23:25:54.934139-0400	CoreServicesUIAgent	LAUNCH: 0x0-0x987987 com.nexy.assistant starting stopped process.
default	23:25:54.935153-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	23:25:54.935305-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	23:25:54.937295-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring jetsam update because this process is not memory-managed
default	23:25:54.937356-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring suspend because this process is not lifecycle managed
default	23:25:54.937392-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:25:54.937438-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:25:54.937609-0400	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.18912707.18912713(501)>:45569]
default	23:25:54.938915-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:25:54.939354-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:25:54.939548-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:25:54.939696-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-active-NotVisible
default	23:25:54.942908-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:25:55.045268-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring jetsam update because this process is not memory-managed
default	23:25:55.045279-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring suspend because this process is not lifecycle managed
default	23:25:55.045289-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:25:55.045309-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:25:55.045675-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-active-NotVisible
default	23:25:55.048239-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:25:55.048973-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-active-NotVisible
default	23:25:55.141588-0400	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	23:25:55.143722-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=511.69, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	23:25:55.154025-0400	tccd	AUTHREQ_SUBJECT: msgID=511.69, subject=com.nexy.assistant,
default	23:25:55.155452-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	23:25:55.175673-0400	kernel	Nexy[45569] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x34951bf8d8b82587. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	23:25:55.175704-0400	kernel	Nexy[45569] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0x34951bf8d8b82587. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	23:25:55.537507-0400	Nexy	[0x103a158f0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	23:25:55.537575-0400	Nexy	[0x103a15e30] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	23:25:55.678339-0400	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x103a19390 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	23:25:55.678575-0400	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x103a19390 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	23:25:55.678798-0400	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x103a19390 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	23:25:55.679009-0400	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x103a19390 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	23:25:55.789813-0400	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	23:25:55.793932-0400	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	23:25:55.795553-0400	Nexy	[0x103a1e6e0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	23:25:55.799098-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.18912707.18912713 AUID=501> and <type=Application identifier=application.com.nexy.assistant.18912707.18912713>
default	23:25:55.803888-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	23:25:55.805854-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	23:25:55.806041-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	23:25:55.806193-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	23:25:55.806205-0400	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	23:25:55.806241-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	23:25:55.806440-0400	Nexy	[0xbafae8000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	23:25:55.806593-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	23:25:55.807254-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45569.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:25:55.813934-0400	tccd	AUTHREQ_SUBJECT: msgID=45569.1, subject=com.nexy.assistant,
default	23:25:55.814560-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108f00 at /Applications/Nexy.app
default	23:25:55.827790-0400	Nexy	[0xbafae8000] invalidated after the last release of the connection object
default	23:25:55.827847-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	23:25:55.830543-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	23:25:55.832365-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3674, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:25:55.833214-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3674, subject=com.nexy.assistant,
default	23:25:55.833765-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108f00 at /Applications/Nexy.app
error	23:25:55.849137-0400	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	23:25:55.850052-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3676, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:25:55.850903-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3676, subject=com.nexy.assistant,
default	23:25:55.851460-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108f00 at /Applications/Nexy.app
default	23:25:55.865858-0400	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	23:25:55.865889-0400	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xbae404180> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	23:25:55.881185-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	23:25:58.321345-0400	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid F0572AC5-7CB0-42D8-85B7-B57021ADF075 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65231,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x32b880fe tp_proto=0x06"
default	23:25:58.321405-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65231<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296411 t_state: SYN_SENT process: Nexy:45569 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x835b2ea3
default	23:25:58.341747-0400	kernel	tcp connected: [<IPv4-redacted>:65231<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296411 t_state: ESTABLISHED process: Nexy:45569 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x835b2ea3
default	23:25:58.342191-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65231<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296411 t_state: FIN_WAIT_1 process: Nexy:45569 Duration: 0.021 sec Conn_Time: 0.021 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 21.000 ms rttvar: 10.500 ms base rtt: 21 ms so_error: 0 svc/tc: 0 flow: 0x835b2ea3
default	23:25:58.342200-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65231<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296411 t_state: FIN_WAIT_1 process: Nexy:45569 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:25:58.372051-0400	Nexy	[0xbafae8000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	23:25:58.389640-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xbad584040) Selecting device 71 from constructor
default	23:25:58.389651-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbad584040)
default	23:25:58.389657-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbad584040) not already running
default	23:25:58.389661-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xbad584040) nothing to teardown
default	23:25:58.389664-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbad584040) connecting device 71
default	23:25:58.389991-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xbad584040) Device ID: 71 (Input:No | Output:Yes): true
default	23:25:58.390280-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xbad584040) created ioproc 0xa for device 71
default	23:25:58.390933-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 7 device listeners to device 71
default	23:25:58.391105-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 0 device delegate listeners to device 71
default	23:25:58.391113-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xbad584040)
default	23:25:58.391185-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:25:58.391196-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:25:58.391211-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:25:58.391225-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:25:58.391233-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:25:58.391330-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xbad584040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:25:58.391341-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xbad584040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:25:58.391347-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:25:58.391352-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 0 device listeners from device 0
default	23:25:58.391357-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 0 device delegate listeners from device 0
default	23:25:58.391361-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbad584040)
default	23:25:58.391377-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	23:25:58.391786-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xbad584040) caller requesting device change from 71 to 78
default	23:25:58.391792-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbad584040)
default	23:25:58.391797-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbad584040) not already running
default	23:25:58.391799-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xbad584040) disconnecting device 71
default	23:25:58.391803-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xbad584040) destroying ioproc 0xa for device 71
default	23:25:58.392312-0400	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	23:25:58.393238-0400	Nexy	[0xbafae8280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	23:25:58.395423-0400	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef0ac","name":"Nexy(45569)"}, "details":{"PID":45569,"session_type":"Primary"} }
default	23:25:58.395514-0400	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":45569}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ac, sessionType: 'prim', isRecording: false }, 
]
default	23:25:58.396322-0400	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 45569, name = Nexy
default	23:25:58.396598-0400	Nexy	    SessionCore_Create.mm:99    Created session 0xbaf8d25c0 with ID: 0x1ef0ac
default	23:25:58.398061-0400	Nexy	[0xbafae83c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	23:25:58.398488-0400	Nexy	No persisted cache on this platform.
error	23:25:58.399542-0400	Nexy	Reporter disconnected. { function=sendMessage, reporterID=195717364711425 }
default	23:25:58.399558-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xa}
default	23:25:58.399612-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:25:58.399723-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbad584040) connecting device 78
default	23:25:58.399808-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xbad584040) Device ID: 78 (Input:Yes | Output:No): true
default	23:25:58.401539-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3677, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:25:58.402944-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3677, subject=com.nexy.assistant,
default	23:25:58.403795-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108f00 at /Applications/Nexy.app
default	23:25:58.418315-0400	tccd	AUTHREQ_PROMPTING: msgID=401.3677, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	23:26:00.543534-0400	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	23:26:00.543989-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xbad584040) created ioproc 0xa for device 78
default	23:26:00.544228-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 7 device listeners to device 78
default	23:26:00.544548-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 0 device delegate listeners to device 78
default	23:26:00.544564-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xbad584040)
default	23:26:00.544580-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	23:26:00.544608-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:26:00.544842-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	23:26:00.544855-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	23:26:00.544862-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	23:26:00.545011-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xbad584040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:26:00.545037-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xbad584040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:26:00.545047-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:26:00.545054-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 7 device listeners from device 71
default	23:26:00.544730-0400	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	23:26:00.545326-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 0 device delegate listeners from device 71
default	23:26:00.545341-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbad584040)
default	23:26:00.546838-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:26:00.548650-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3678, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:26:00.549978-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3678, subject=com.nexy.assistant,
default	23:26:00.551095-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108f00 at /Applications/Nexy.app
default	23:26:00.568978-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:26:00.570349-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3679, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:26:00.571340-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3679, subject=com.nexy.assistant,
default	23:26:00.572369-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108f00 at /Applications/Nexy.app
default	23:26:00.596848-0400	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	23:26:00.598217-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:26:00.599426-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3680, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:26:00.600677-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3680, subject=com.nexy.assistant,
default	23:26:00.601764-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108f00 at /Applications/Nexy.app
default	23:26:00.619076-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3681, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:26:00.620213-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3681, subject=com.nexy.assistant,
default	23:26:00.620857-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108c00 at /Applications/Nexy.app
default	23:26:00.637556-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	23:26:00.637991-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	23:26:00.640516-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18912707.18912713(501)>:45569] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449207 target:45569 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:26:00.640625-0400	runningboardd	Assertion 398-334-449207 (target:[app<application.com.nexy.assistant.18912707.18912713(501)>:45569]) will be created as active
default	23:26:00.641033-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring jetsam update because this process is not memory-managed
default	23:26:00.641074-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring suspend because this process is not lifecycle managed
default	23:26:00.641110-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:26:00.641158-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:26:00.641226-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	23:26:00.647763-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:26:00.653353-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-active-NotVisible
default	23:26:00.664307-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xa}
default	23:26:00.665863-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ac","name":"Nexy(45569)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	23:26:00.665630-0400	runningboardd	Assertion did invalidate due to timeout: 398-398-449179 (target:[app<application.com.nexy.assistant.18912707.18912713(501)>:45569])
default	23:26:00.665967-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:26:00.666337-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:26:00.666415-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ac, Nexy(45569), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	23:26:00.666531-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:26:00.666475-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:00.666829-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:00.666613-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:26:00.666908-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:00.666847-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	23:26:00.666872-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ac, Nexy(45569), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 173 starting recording
fault	23:26:00.667027-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.18912707.18912713 AUID=501> and <type=Application identifier=application.com.nexy.assistant.18912707.18912713>
default	23:26:00.666825-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:00.667263-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:00.667639-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:26:00.668064-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	23:26:00.667785-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:26:00.668076-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:26:00.667290-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:00.667870-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ac, Nexy(45569), 'prim'', displayID:'com.nexy.assistant'}
default	23:26:00.668191-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:00.668217-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:00.668062-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:00.668230-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	23:26:00.668237-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	23:26:00.668247-0400	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	23:26:00.668378-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
fault	23:26:00.669333-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.18912707.18912713 AUID=501> and <type=Application identifier=application.com.nexy.assistant.18912707.18912713>
default	23:26:00.685220-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:26:00.685373-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	23:26:00.685422-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	23:26:00.687534-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring jetsam update because this process is not memory-managed
default	23:26:00.687555-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring suspend because this process is not lifecycle managed
default	23:26:00.687567-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:26:00.687587-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:26:00.689174-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:00.689197-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:00.689490-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:00.689507-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:00.689516-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:00.689523-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:26:00.689686-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:26:00.692831-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-active-NotVisible
default	23:26:00.696515-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	23:26:01.650270-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	23:26:01.658652-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	23:26:01.659027-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ac","name":"Nexy(45569)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:26:01.659068-0400	runningboardd	Invalidating assertion 398-334-449207 (target:[app<application.com.nexy.assistant.18912707.18912713(501)>:45569]) from originator [osservice<com.apple.powerd>:334]
default	23:26:01.659188-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:26:01.659264-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:26:01.659310-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ac, Nexy(45569), 'prim'', displayID:'com.nexy.assistant'}
default	23:26:01.659389-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ac, Nexy(45569), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 173 stopping recording
default	23:26:01.659398-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:01.659424-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:26:01.659496-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:26:01.659571-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:26:01.659590-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:01.659651-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:01.659763-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:26:01.659677-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:26:01.659784-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:26:01.659652-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:01.659758-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:26:01.659831-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:01.659884-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:01.659946-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	23:26:01.662404-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	23:26:01.663662-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:01.663678-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:01.663706-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:01.663717-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:01.663727-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:01.663734-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:26:01.663845-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:26:01.762017-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbad584040) Selecting device 0 from destructor
default	23:26:01.762038-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbad584040)
default	23:26:01.762048-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbad584040) not already running
default	23:26:01.762053-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xbad584040) disconnecting device 78
default	23:26:01.762062-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xbad584040) destroying ioproc 0xa for device 78
default	23:26:01.762105-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	23:26:01.762144-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:26:01.762360-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xbad584040) nothing to setup
default	23:26:01.762373-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 0 device listeners to device 0
default	23:26:01.762381-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 0 device delegate listeners to device 0
default	23:26:01.762389-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 7 device listeners from device 78
default	23:26:01.762567-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring jetsam update because this process is not memory-managed
default	23:26:01.762583-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring suspend because this process is not lifecycle managed
default	23:26:01.762635-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 0 device delegate listeners from device 78
default	23:26:01.762651-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbad584040)
default	23:26:01.762594-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:26:01.762625-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:26:01.765957-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:26:01.766657-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-active-NotVisible
default	23:26:01.901427-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45577.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=45577, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	23:26:01.903157-0400	tccd	AUTHREQ_SUBJECT: msgID=45577.1, subject=com.nexy.assistant,
default	23:26:01.903861-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	23:26:01.919558-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6029, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=45577, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:26:01.920567-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6029, subject=com.nexy.assistant,
default	23:26:01.921262-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	23:26:01.952399-0400	launchservicesd	CHECKIN:0x0-0x987987 45577 com.nexy.assistant
default	23:26:01.953459-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	23:26:01.953572-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	23:26:01.954529-0400	runningboardd	Invalidating assertion 398-363-449180 (target:[app<application.com.nexy.assistant.18912707.18912713(501)>:45569]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	23:26:01.955874-0400	WindowServer	afbb3[CreateApplication]: Process creation: 0x0-0x987987 (Nexy) connectionID: AFBB3 pid: 45577 in session 0x101
default	23:26:01.962811-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	23:26:01.966557-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	23:26:01.985650-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 45029: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 0a4d0d00 };
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
default	23:26:02.999629-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	23:26:02.029733-0400	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x987987} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	23:26:02.029767-0400	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 9992583
default	23:26:02.029866-0400	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	23:26:02.031038-0400	WindowServer	0[outside of RPC]: Process death: 0x0-0x987987 (Nexy) connectionID: AFBB3 pid: 45577 in session 0x101
default	23:26:02.031079-0400	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x987987 (Nexy) acq:0x800bd3c60 count:1
default	23:26:02.031456-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x987987 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x987987 (Nexy)"
)}
default	23:26:02.031681-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xb209 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x987987 (Nexy)"
)}
default	23:26:02.061880-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring jetsam update because this process is not memory-managed
default	23:26:02.061898-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring suspend because this process is not lifecycle managed
default	23:26:02.061952-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Set darwin role to: None
default	23:26:02.062007-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:26:02.062068-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:26:02.065279-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: running-suspended (role: None) (endowments: (null))
default	23:26:02.065680-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-suspended-NotVisible
default	23:26:02.213840-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xbad584040) Selecting device 71 from constructor
default	23:26:02.213848-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbad584040)
default	23:26:02.213854-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbad584040) not already running
default	23:26:02.213857-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xbad584040) nothing to teardown
default	23:26:02.213860-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbad584040) connecting device 71
default	23:26:02.213974-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xbad584040) Device ID: 71 (Input:No | Output:Yes): true
default	23:26:02.214107-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xbad584040) created ioproc 0xb for device 71
default	23:26:02.214241-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 7 device listeners to device 71
default	23:26:02.214437-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 0 device delegate listeners to device 71
default	23:26:02.214447-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xbad584040)
default	23:26:02.214519-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:26:02.214526-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:26:02.214531-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:26:02.214538-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:26:02.214545-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:26:02.214637-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xbad584040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:26:02.214648-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xbad584040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:26:02.214657-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:26:02.214660-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 0 device listeners from device 0
default	23:26:02.214664-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 0 device delegate listeners from device 0
default	23:26:02.214668-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbad584040)
default	23:26:02.214683-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	23:26:02.214761-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xbad584040) caller requesting device change from 71 to 78
default	23:26:02.214767-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbad584040)
default	23:26:02.214771-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbad584040) not already running
default	23:26:02.214776-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xbad584040) disconnecting device 71
default	23:26:02.214780-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xbad584040) destroying ioproc 0xb for device 71
default	23:26:02.214799-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xb}
default	23:26:02.214832-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:26:02.214907-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbad584040) connecting device 78
default	23:26:02.214986-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xbad584040) Device ID: 78 (Input:Yes | Output:No): true
default	23:26:02.216384-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3682, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:26:02.217509-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3682, subject=com.nexy.assistant,
default	23:26:02.218126-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:26:02.231096-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xbad584040) created ioproc 0xb for device 78
default	23:26:02.231235-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 7 device listeners to device 78
default	23:26:02.231414-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 0 device delegate listeners to device 78
default	23:26:02.231420-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xbad584040)
default	23:26:02.231426-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	23:26:02.231434-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:26:02.231551-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	23:26:02.231563-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	23:26:02.231568-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	23:26:02.231686-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xbad584040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:26:02.231699-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xbad584040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:26:02.231704-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:26:02.231709-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 7 device listeners from device 71
default	23:26:02.231879-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 0 device delegate listeners from device 71
default	23:26:02.231894-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbad584040)
default	23:26:02.232290-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:26:02.233350-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3683, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:26:02.234174-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3683, subject=com.nexy.assistant,
default	23:26:02.234746-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:26:02.247422-0400	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	23:26:02.247489-0400	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0xbaf89dfb0, from  1 ch,  48000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	23:26:02.247690-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:26:02.248645-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3684, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:26:02.249418-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3684, subject=com.nexy.assistant,
default	23:26:02.249939-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:26:02.267877-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3685, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:26:02.268655-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3685, subject=com.nexy.assistant,
default	23:26:02.269176-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:26:02.281996-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18912707.18912713(501)>:45569] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449230 target:45569 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:26:02.282061-0400	runningboardd	Assertion 398-334-449230 (target:[app<application.com.nexy.assistant.18912707.18912713(501)>:45569]) will be created as active
default	23:26:02.282311-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring jetsam update because this process is not memory-managed
default	23:26:02.282325-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring suspend because this process is not lifecycle managed
default	23:26:02.282363-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Set darwin role to: Background
default	23:26:02.282418-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:26:02.282516-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:26:02.285366-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: running-active (role: Background) (endowments: (null))
default	23:26:02.285712-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-active-NotVisible
default	23:26:02.306318-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xb}
default	23:26:02.307332-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ac","name":"Nexy(45569)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	23:26:02.307399-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:26:02.307426-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ac, Nexy(45569), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:26:02.307452-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:26:02.307498-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ac, Nexy(45569), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	23:26:02.307528-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:02.307542-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:26:02.307571-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:26:02.307650-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:02.307615-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	23:26:02.307634-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:02.307657-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ac, Nexy(45569), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 173 starting recording
default	23:26:02.307679-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:02.307769-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:26:02.307744-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:02.307768-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:02.307804-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:26:02.307827-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ac, Nexy(45569), 'prim'', displayID:'com.nexy.assistant'}
default	23:26:02.308001-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:02.307903-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:02.308022-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:02.308032-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	23:26:02.308041-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	23:26:02.308051-0400	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	23:26:02.308077-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:26:02.308088-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	23:26:02.308104-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:26:02.312758-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:26:02.312817-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	23:26:02.312858-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	23:26:02.313260-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:02.313271-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:02.313282-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:02.313288-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:02.313296-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:02.313302-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:26:02.313322-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:02.313344-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:02.313369-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:02.313378-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:02.313400-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:02.313431-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:26:02.313544-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:26:02.314635-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	23:26:02.314754-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:02.314766-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:02.314776-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:02.314784-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:02.314790-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:02.314795-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:26:03.500099-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
default	23:26:06.500128-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
default	23:26:09.316319-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	23:26:09.324086-0400	runningboardd	Invalidating assertion 398-334-449230 (target:[app<application.com.nexy.assistant.18912707.18912713(501)>:45569]) from originator [osservice<com.apple.powerd>:334]
default	23:26:09.324459-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	23:26:09.324809-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ac","name":"Nexy(45569)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:26:09.324966-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:26:09.325052-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:26:09.325093-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ac, Nexy(45569), 'prim'', displayID:'com.nexy.assistant'}
default	23:26:09.325162-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ac, Nexy(45569), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 173 stopping recording
default	23:26:09.325170-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:09.325225-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:26:09.325265-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:26:09.325308-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:26:09.325361-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:09.325400-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:09.325464-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:26:09.325484-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:09.325515-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:26:09.325583-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:26:09.325601-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:09.325615-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	23:26:09.326183-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:26:09.326215-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:26:09.327837-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	23:26:09.342761-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:09.342780-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:09.342794-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:09.342803-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:26:09.342812-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:26:09.342819-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:26:09.342940-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:26:09.426253-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring jetsam update because this process is not memory-managed
default	23:26:09.426274-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring suspend because this process is not lifecycle managed
default	23:26:09.426332-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Set darwin role to: None
default	23:26:09.426348-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:26:09.426377-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:26:09.430064-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: running-suspended (role: None) (endowments: (null))
default	23:26:09.430838-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-suspended-NotVisible
default	23:26:09.517246-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbad584040) Selecting device 0 from destructor
default	23:26:09.517267-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbad584040)
default	23:26:09.517277-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbad584040) not already running
default	23:26:09.517285-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xbad584040) disconnecting device 78
default	23:26:09.517293-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xbad584040) destroying ioproc 0xb for device 78
default	23:26:09.517334-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	23:26:09.517381-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:26:09.517687-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xbad584040) nothing to setup
default	23:26:09.517719-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 0 device listeners to device 0
default	23:26:09.517735-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad584040) adding 0 device delegate listeners to device 0
default	23:26:09.517750-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 7 device listeners from device 78
default	23:26:09.518285-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad584040) removing 0 device delegate listeners from device 78
default	23:26:09.518312-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbad584040)
default	23:26:09.580935-0400	Nexy	[0xbafae8640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	23:26:09.581731-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45569.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:26:09.583504-0400	tccd	AUTHREQ_SUBJECT: msgID=45569.2, subject=com.nexy.assistant,
default	23:26:09.584285-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	23:26:09.598543-0400	Nexy	[0xbafae8640] invalidated after the last release of the connection object
default	23:26:09.599622-0400	Nexy	[0xbafae8640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	23:26:09.600132-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45569.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:26:09.601074-0400	tccd	AUTHREQ_SUBJECT: msgID=45569.3, subject=com.nexy.assistant,
default	23:26:09.601684-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	23:26:09.614116-0400	Nexy	[0xbafae8640] invalidated after the last release of the connection object
default	23:26:09.614295-0400	Nexy	[0xbafae8640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	23:26:09.614729-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45569.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:26:09.615561-0400	tccd	AUTHREQ_SUBJECT: msgID=45569.4, subject=com.nexy.assistant,
default	23:26:09.616132-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	23:26:09.628693-0400	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[45569], responsiblePID[45569], responsiblePath: /Applications/Nexy.app to UID: 501
default	23:26:09.628941-0400	Nexy	[0xbafae8640] invalidated after the last release of the connection object
default	23:26:09.719150-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	23:26:09.738550-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	23:26:09.744415-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	23:26:16.779130-0400	Nexy	[0xbafae8640] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	23:26:16.780169-0400	Nexy	[0xbafae88c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	23:26:16.781157-0400	Nexy	Received configuration update from daemon (initial)
default	23:26:16.830928-0400	Nexy	[0xbafae8a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	23:26:16.831542-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	23:26:16.831728-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45569.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:26:16.833039-0400	tccd	AUTHREQ_SUBJECT: msgID=45569.5, subject=com.nexy.assistant,
default	23:26:16.833786-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:26:16.848232-0400	Nexy	[0xbafae8a00] invalidated after the last release of the connection object
default	23:26:16.849051-0400	Nexy	[0xbafae8a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	23:26:16.849452-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	23:26:16.849615-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45569.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:26:16.850519-0400	tccd	AUTHREQ_SUBJECT: msgID=45569.6, subject=com.nexy.assistant,
default	23:26:16.851238-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:26:16.863857-0400	Nexy	[0xbafae8a00] invalidated after the last release of the connection object
default	23:26:16.863920-0400	Nexy	[0xbafae8a00] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	23:26:16.864011-0400	Nexy	[0xbafae8a00] invalidated after the last release of the connection object
default	23:26:16.864322-0400	Nexy	[0xbafae8b40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	23:26:16.864759-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45569.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:26:16.865612-0400	tccd	AUTHREQ_SUBJECT: msgID=45569.7, subject=com.nexy.assistant,
default	23:26:16.866281-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:26:16.879123-0400	tccd	Notifying for access  kTCCServiceListenEvent for target PID[45569], responsiblePID[45569], responsiblePath: /Applications/Nexy.app to UID: 501
default	23:26:16.879390-0400	Nexy	[0xbafae8b40] invalidated after the last release of the connection object
default	23:26:16.879710-0400	Nexy	server port 0x0000b113, session port 0x0000b00b
default	23:26:16.880686-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6047, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:26:16.880713-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	23:26:16.883089-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6047, subject=com.nexy.assistant,
default	23:26:16.883812-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:26:16.884505-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	23:26:16.903059-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	23:26:16.907785-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	23:26:16.934767-0400	Nexy	server port 0x0000b00b, session port 0x0000b00b
default	23:26:16.936275-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6048, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:26:16.936301-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=45569, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	23:26:16.937822-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6048, subject=com.nexy.assistant,
default	23:26:16.939632-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	23:26:16.945475-0400	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4B3756D0-662D-4237-9BF4-009E4990BC85 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65234,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x75a29e45 tp_proto=0x06"
default	23:26:16.945673-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65234<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296461 t_state: SYN_SENT process: Nexy:45569 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 17 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbca090a8
default	23:26:16.955210-0400	Nexy	[0xbafae8c80] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	23:26:16.957473-0400	Nexy	New connection 0x1063ff main
default	23:26:16.957743-0400	Nexy	[0xbafae8b40] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	23:26:16.959891-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	23:26:16.960089-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	23:26:16.960582-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	23:26:16.960966-0400	Nexy	nw_path_libinfo_path_check [C3884D05-C603-4976-9142-E7E8428908C7 IPv4#f5fd5778:8081 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	23:26:16.961414-0400	Nexy	[0xbafae8f00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	23:26:16.962533-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 022F38FC-9F3A-4555-A10D-A18152791C27 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65235,dst=<IPv4-redacted>.8081,proto=0x06 mask=0x0000003f,hash=0x5c4dc433 tp_proto=0x06"
default	23:26:16.962594-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65235<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2296462 t_state: SYN_SENT process: Nexy:45569 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8303fb29
default	23:26:16.964556-0400	kernel	tcp connected: [<IPv4-redacted>:65234<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296461 t_state: ESTABLISHED process: Nexy:45569 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 17 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbca090a8
default	23:26:16.964967-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65234<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296461 t_state: FIN_WAIT_1 process: Nexy:45569 Duration: 0.020 sec Conn_Time: 0.020 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 20.000 ms rttvar: 10.000 ms base rtt: 17 ms so_error: 0 svc/tc: 0 flow: 0xbca090a8
default	23:26:16.964977-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65234<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296461 t_state: FIN_WAIT_1 process: Nexy:45569 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:26:16.965440-0400	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid E84F6871-6E7C-4017-AEFB-FC73F248F12C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65236,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xae144064 tp_proto=0x06"
default	23:26:16.965481-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65236<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296463 t_state: SYN_SENT process: Nexy:45569 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 17 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8e6a11e2
default	23:26:16.974642-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	23:26:16.978101-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	23:26:16.986872-0400	kernel	tcp connected: [<IPv4-redacted>:65236<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296463 t_state: ESTABLISHED process: Nexy:45569 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 17 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8e6a11e2
default	23:26:16.988197-0400	kernel	tcp connected: [<IPv4-redacted>:65235<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2296462 t_state: ESTABLISHED process: Nexy:45569 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8303fb29
default	23:26:16.991254-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65236<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296463 t_state: FIN_WAIT_1 process: Nexy:45569 Duration: 0.026 sec Conn_Time: 0.022 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 22.000 ms rttvar: 11.000 ms base rtt: 17 ms so_error: 0 svc/tc: 0 flow: 0x8e6a11e2
default	23:26:16.991270-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65236<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296463 t_state: FIN_WAIT_1 process: Nexy:45569 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:26:17.020287-0400	Nexy	nw_path_libinfo_path_check [118F1C27-9018-4316-804C-5F83AA48EB29 Hostname#dafa74fb:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	23:26:17.020427-0400	mDNSResponder	[R279438] DNSServiceCreateConnection START PID[45569](Nexy)
default	23:26:17.020493-0400	mDNSResponder	[R279439] DNSServiceQueryRecord START -- qname: <mask.hash: 'fzWYXTe2YMapr48UvSyQLQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 45569 (Nexy), name hash: 93389144
default	23:26:17.021059-0400	mDNSResponder	[R279440] DNSServiceQueryRecord START -- qname: <mask.hash: 'fzWYXTe2YMapr48UvSyQLQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 45569 (Nexy), name hash: 93389144
default	23:26:17.041886-0400	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 65D30757-2643-4390-AAD0-BB1560B42736 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65237,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x613daa5d tp_proto=0x06"
default	23:26:17.041940-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65237<-><IPv4-redacted>:443] interface: en0 (skipped: 871)
so_gencnt: 2296476 t_state: SYN_SENT process: Nexy:45569 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d1f655a
default	23:26:17.079472-0400	kernel	tcp connected: [<IPv4-redacted>:65237<-><IPv4-redacted>:443] interface: en0 (skipped: 871)
so_gencnt: 2296476 t_state: ESTABLISHED process: Nexy:45569 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d1f655a
default	23:26:17.279041-0400	Nexy	nw_path_libinfo_path_check [BE0B792F-5430-4349-AE46-44A499678A75 Hostname#11e25496:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	23:26:17.279139-0400	mDNSResponder	[R279443] DNSServiceQueryRecord START -- qname: <mask.hash: '2M6q9I8vyy1ql8eChmIyow=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 45569 (Nexy), name hash: c6742fa2
default	23:26:17.279604-0400	mDNSResponder	[R279444] DNSServiceQueryRecord START -- qname: <mask.hash: '2M6q9I8vyy1ql8eChmIyow=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 45569 (Nexy), name hash: c6742fa2
default	23:26:17.308099-0400	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 90C17F40-AE0B-488C-B403-E94A88E30A86 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65238,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x57fba84f tp_proto=0x06"
default	23:26:17.308157-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65238<-><IPv4-redacted>:443] interface: en0 (skipped: 871)
so_gencnt: 2296488 t_state: SYN_SENT process: Nexy:45569 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa59e1603
default	23:26:17.324353-0400	kernel	tcp connected: [<IPv4-redacted>:65238<-><IPv4-redacted>:443] interface: en0 (skipped: 871)
so_gencnt: 2296488 t_state: ESTABLISHED process: Nexy:45569 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa59e1603
default	23:26:17.477752-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	23:26:17.493845-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	23:26:17.504832-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	23:26:18.457092-0400	kernel	udp connect: [<IPv4-redacted>:51867<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2296502 so_state: 0x0002 process: Nexy:45569 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x9c592a99
default	23:26:18.457125-0400	kernel	udp_connection_summary [<IPv4-redacted>:51867<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2296502 so_state: 0x0002 process: Nexy:45569 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x9c592a99 flowctl: 0us (0x)
default	23:26:18.458092-0400	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid E8BECF07-E66F-484F-8EDC-C7B33F875B8A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65241,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0x46180805 tp_proto=0x06"
default	23:26:18.458180-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65241<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2296504 t_state: SYN_SENT process: Nexy:45569 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 24 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa1f19d1e
default	23:26:18.494569-0400	kernel	tcp connected: [<IPv4-redacted>:65241<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2296504 t_state: ESTABLISHED process: Nexy:45569 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 24 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa1f19d1e
default	23:26:19.868998-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xbad585c40) Selecting device 71 from constructor
default	23:26:19.869019-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbad585c40)
default	23:26:19.869026-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbad585c40) not already running
default	23:26:19.869033-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xbad585c40) nothing to teardown
default	23:26:19.869038-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbad585c40) connecting device 71
default	23:26:19.869153-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xbad585c40) Device ID: 71 (Input:No | Output:Yes): true
default	23:26:19.869298-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xbad585c40) created ioproc 0xc for device 71
default	23:26:19.869455-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad585c40) adding 7 device listeners to device 71
default	23:26:19.869699-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad585c40) adding 0 device delegate listeners to device 71
default	23:26:19.869710-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xbad585c40)
default	23:26:19.869812-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:26:19.869822-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:26:19.869829-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:26:19.869838-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:26:19.869848-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:26:19.869972-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xbad585c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:26:19.869986-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xbad585c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:26:19.869992-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:26:19.870001-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad585c40) removing 0 device listeners from device 0
default	23:26:19.870007-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad585c40) removing 0 device delegate listeners from device 0
default	23:26:19.870012-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbad585c40)
default	23:26:19.870026-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xbad585c40) caller requesting device change from 71 to 71
default	23:26:19.870037-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbad585c40)
default	23:26:19.870045-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xbad585c40) exiting with nothing to do
default	23:26:19.870507-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	23:26:19.870841-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	23:26:19.873274-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbad585c40) Selecting device 0 from destructor
default	23:26:19.873289-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbad585c40)
default	23:26:19.873296-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbad585c40) not already running
default	23:26:19.873302-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xbad585c40) disconnecting device 71
default	23:26:19.873308-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xbad585c40) destroying ioproc 0xc for device 71
default	23:26:19.873354-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xc}
default	23:26:19.873392-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:26:19.873531-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xbad585c40) nothing to setup
default	23:26:19.873544-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad585c40) adding 0 device listeners to device 0
default	23:26:19.873549-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad585c40) adding 0 device delegate listeners to device 0
default	23:26:19.873557-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad585c40) removing 7 device listeners from device 71
default	23:26:19.873776-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad585c40) removing 0 device delegate listeners from device 71
default	23:26:19.873791-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbad585c40)
default	23:26:19.874876-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xbad585c40) Selecting device 71 from constructor
default	23:26:19.874891-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbad585c40)
default	23:26:19.874898-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xbad585c40) not already running
default	23:26:19.874903-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xbad585c40) nothing to teardown
default	23:26:19.874908-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbad585c40) connecting device 71
default	23:26:19.875016-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xbad585c40) Device ID: 71 (Input:No | Output:Yes): true
default	23:26:19.875138-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xbad585c40) created ioproc 0xd for device 71
default	23:26:19.875283-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad585c40) adding 7 device listeners to device 71
default	23:26:19.875524-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xbad585c40) adding 0 device delegate listeners to device 71
default	23:26:19.875538-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xbad585c40)
default	23:26:19.875641-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:26:19.875653-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:26:19.875659-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:26:19.875669-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:26:19.875677-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:26:19.875793-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xbad585c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:26:19.875809-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xbad585c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:26:19.875818-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:26:19.875823-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad585c40) removing 0 device listeners from device 0
default	23:26:19.875828-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xbad585c40) removing 0 device delegate listeners from device 0
default	23:26:19.875833-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xbad585c40)
default	23:26:19.875855-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xbad585c40) caller requesting device change from 71 to 71
default	23:26:19.875861-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xbad585c40)
default	23:26:19.875865-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xbad585c40) exiting with nothing to do
default	23:26:19.875874-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	23:26:19.876714-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	23:26:19.877028-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	23:26:19.880578-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18912707.18912713(501)>:45569] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449310 target:45569 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:26:19.880661-0400	runningboardd	Assertion 398-334-449310 (target:[app<application.com.nexy.assistant.18912707.18912713(501)>:45569]) will be created as active
default	23:26:19.882081-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring jetsam update because this process is not memory-managed
default	23:26:19.882092-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring suspend because this process is not lifecycle managed
default	23:26:19.882167-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Set darwin role to: Background
default	23:26:19.882193-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:26:19.882246-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:26:19.885248-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: running-active (role: Background) (endowments: (null))
default	23:26:19.885799-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-active-NotVisible
default	23:26:19.906779-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0xd}
default	23:26:19.907876-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ac","name":"Nexy(45569)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	23:26:19.908004-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:26:19.908044-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ac, Nexy(45569), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:26:19.908080-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:26:19.908126-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ac, Nexy(45569), 'prim'', AudioCategory changed to 'MediaPlayback'
default	23:26:19.908152-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:19.908185-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	23:26:19.908198-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 173 starting playing
default	23:26:19.908318-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:19.908365-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:19.908272-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:26:19.908313-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:26:19.908340-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ac, Nexy(45569), 'prim'', displayID:'com.nexy.assistant'}
default	23:26:19.908425-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	23:26:19.908544-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ac to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45569}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ac, sessionType: 'prim', isRecording: false }, 
]
default	23:26:19.908566-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	23:26:19.908746-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	23:26:19.908762-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:26:19.909585-0400	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	23:26:19.909816-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:26:19.909929-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:26:19.909960-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:26:19.909976-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	23:26:19.909985-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	23:26:19.910008-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	23:26:19.910056-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
error	23:26:20.411184-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:20.423428-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["multi_cycle_io_page_faults_duration": Optional(0), "anchor_sample_time": Optional(68), "other_page_faults": Optional(0), "issue_type": Optional(overload), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_total_wakeups": Optional(5), "io_frame_counter": Optional(23552), "is_recovering": Optional(0), "wg_system_time_mach": Optional(2263), "io_cycle_budget": Optional(11354166), "smallest_buffer_frame_size": Optional(512), "io_cycle": Optional(46), "io_cycle_usage": Optional(1), "reporting_latency": Optional(14140041), "io_page_faults_duration": Optional(0), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "wg_user_time_mach": Optional(23296), "output_device_transport_list": Optional(BuiltIn), "wg_cycles": Optional(2482705), "input_device_uid_list": Optional(), "start_time": Optional(4839100005182), "careporting_timestamp": 1761708380.423151, "input_device_source_list": Optional(), "is_prewarming": Optional(0), "HAL_client_IO_duration": Optional(1301<…> }
error	23:26:21.266735-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:21.282871-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["cause_set": Optional(12), "io_frame_counter": Optional(40448), "safety_violation": Optional(1), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "careporting_timestamp": 1761708381.282143, "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(89), "multi_cycle_io_page_faults_duration": Optional(0), "input_device_source_list": Optional(), "wg_cycles": Optional(2154293), "HAL_client_IO_duration": Optional(11906750), "num_continuous_silent_io_cycles": Optional(0), "scheduler_latency": Optional(15958), "smallest_buffer_frame_size": Optional(512), "input_device_transport_list": Optional(), "reporting_latency": Optional(15693875), "wg_external_wakeups": Optional(0), "input_device_uid_list": Optional(), "multi_cycle_io_page_faults": Optional(0), "io_cycle_budget": Optional(11354125), "anchor_sample_time": Optional(24280), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "io_cycle": Optional(79), "wg_instructio<…> }
error	23:26:21.321239-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:21.333117-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["multi_cycle_io_page_faults_duration": Optional(0), "anchor_sample_time": Optional(65344), "other_page_faults": Optional(0), "issue_type": Optional(overload), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_total_wakeups": Optional(6), "io_frame_counter": Optional(2048), "is_recovering": Optional(0), "wg_system_time_mach": Optional(2658), "io_cycle_budget": Optional(11354125), "smallest_buffer_frame_size": Optional(512), "io_cycle": Optional(4), "io_cycle_usage": Optional(1), "reporting_latency": Optional(11787666), "io_page_faults_duration": Optional(0), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "wg_user_time_mach": Optional(24526), "output_device_transport_list": Optional(BuiltIn), "wg_cycles": Optional(1917372), "input_device_uid_list": Optional(), "start_time": Optional(4839121891045), "careporting_timestamp": 1761708381.332767, "input_device_source_list": Optional(), "is_prewarming": Optional(0), "HAL_client_IO_duration": Optional(110<…> }
default	23:26:21.499913-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	23:26:22.531147-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["cause_set": Optional(12), "io_frame_counter": Optional(8704), "safety_violation": Optional(1), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "careporting_timestamp": 1761708382.517531, "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(8336), "multi_cycle_io_page_faults_duration": Optional(0), "input_device_source_list": Optional(), "wg_cycles": Optional(2876061), "HAL_client_IO_duration": Optional(183597916), "num_continuous_silent_io_cycles": Optional(0), "scheduler_latency": Optional(10375), "smallest_buffer_frame_size": Optional(512), "input_device_transport_list": Optional(), "reporting_latency": Optional(1000807875), "wg_external_wakeups": Optional(0), "input_device_uid_list": Optional(), "multi_cycle_io_page_faults": Optional(0), "io_cycle_budget": Optional(11354125), "anchor_sample_time": Optional(67968), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "io_cycle": Optional(17), "wg_instru<…> }
default	23:26:23.154501-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["multi_cycle_io_page_faults_duration": Optional(0), "anchor_sample_time": Optional(92740), "other_page_faults": Optional(0), "issue_type": Optional(overload), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_total_wakeups": Optional(6), "io_frame_counter": Optional(512), "is_recovering": Optional(0), "wg_system_time_mach": Optional(13280), "io_cycle_budget": Optional(11354125), "smallest_buffer_frame_size": Optional(512), "io_cycle": Optional(1), "io_cycle_usage": Optional(1), "reporting_latency": Optional(1292745041), "io_page_faults_duration": Optional(0), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "wg_user_time_mach": Optional(67765), "output_device_transport_list": Optional(BuiltIn), "wg_cycles": Optional(7304141), "input_device_uid_list": Optional(), "start_time": Optional(4839134821013), "careporting_timestamp": 1761708383.153197, "input_device_source_list": Optional(), "is_prewarming": Optional(0), "HAL_client_IO_duration": Optional(1<…> }
default	23:26:23.223404-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["cause_set": Optional(12), "io_frame_counter": Optional(512), "safety_violation": Optional(1), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "careporting_timestamp": 1761708383.2215738, "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(1795), "multi_cycle_io_page_faults_duration": Optional(0), "input_device_source_list": Optional(), "wg_cycles": Optional(4825520), "HAL_client_IO_duration": Optional(46902875), "num_continuous_silent_io_cycles": Optional(0), "scheduler_latency": Optional(38416), "smallest_buffer_frame_size": Optional(512), "input_device_transport_list": Optional(), "reporting_latency": Optional(57317666), "wg_external_wakeups": Optional(1), "input_device_uid_list": Optional(), "multi_cycle_io_page_faults": Optional(0), "io_cycle_budget": Optional(11354166), "anchor_sample_time": Optional(155244), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "io_cycle": Optional(1), "wg_instructi<…> }
default	23:26:23.250688-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["multi_cycle_io_page_faults_duration": Optional(0), "anchor_sample_time": Optional(158208), "other_page_faults": Optional(0), "issue_type": Optional(overload), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_total_wakeups": Optional(5), "io_frame_counter": Optional(512), "is_recovering": Optional(0), "wg_system_time_mach": Optional(5131), "io_cycle_budget": Optional(11354166), "smallest_buffer_frame_size": Optional(512), "io_cycle": Optional(1), "io_cycle_usage": Optional(1), "reporting_latency": Optional(26302083), "io_page_faults_duration": Optional(0), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "wg_user_time_mach": Optional(55272), "output_device_transport_list": Optional(BuiltIn), "wg_cycles": Optional(4740683), "input_device_uid_list": Optional(), "start_time": Optional(4839167554908), "careporting_timestamp": 1761708383.250074, "input_device_source_list": Optional(), "is_prewarming": Optional(0), "HAL_client_IO_duration": Optional(207<…> }
error	23:26:23.265494-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
error	23:26:23.266740-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
error	23:26:23.266762-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
error	23:26:23.266771-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:23.317269-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["cause_set": Optional(12), "io_frame_counter": Optional(2560), "safety_violation": Optional(1), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "careporting_timestamp": 1761708383.316663, "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(83), "multi_cycle_io_page_faults_duration": Optional(0), "input_device_source_list": Optional(), "wg_cycles": Optional(2914777), "HAL_client_IO_duration": Optional(11577083), "num_continuous_silent_io_cycles": Optional(0), "scheduler_latency": Optional(22916), "smallest_buffer_frame_size": Optional(512), "input_device_transport_list": Optional(), "reporting_latency": Optional(13293541), "wg_external_wakeups": Optional(2), "input_device_uid_list": Optional(), "multi_cycle_io_page_faults": Optional(0), "io_cycle_budget": Optional(11354166), "anchor_sample_time": Optional(159980), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "io_cycle": Optional(5), "wg_instruction<…> }
error	23:26:23.318594-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:24.506964-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	23:26:25.793864-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	23:26:25.810555-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:26:25.819567-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	23:26:27.499926-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
error	23:26:28.175157-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:28.185667-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["cause_set": Optional(12), "io_frame_counter": Optional(209408), "safety_violation": Optional(1), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "careporting_timestamp": 1761708388.177619, "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(1886), "multi_cycle_io_page_faults_duration": Optional(0), "input_device_source_list": Optional(), "wg_cycles": Optional(2632000), "HAL_client_IO_duration": Optional(49415125), "num_continuous_silent_io_cycles": Optional(64), "scheduler_latency": Optional(12000), "smallest_buffer_frame_size": Optional(512), "input_device_transport_list": Optional(), "reporting_latency": Optional(51844541), "wg_external_wakeups": Optional(0), "input_device_uid_list": Optional(), "multi_cycle_io_page_faults": Optional(0), "io_cycle_budget": Optional(11354125), "anchor_sample_time": Optional(184620), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "io_cycle": Optional(409), "wg_inst<…> }
default	23:26:30.486479-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
error	23:26:32.273629-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:32.286555-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["cause_set": Optional(12), "io_frame_counter": Optional(194560), "safety_violation": Optional(1), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "careporting_timestamp": 1761708392.2858648, "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(105), "multi_cycle_io_page_faults_duration": Optional(0), "input_device_source_list": Optional(), "wg_cycles": Optional(3639827), "HAL_client_IO_duration": Optional(11927041), "num_continuous_silent_io_cycles": Optional(35), "scheduler_latency": Optional(32625), "smallest_buffer_frame_size": Optional(512), "input_device_transport_list": Optional(), "reporting_latency": Optional(13298875), "wg_external_wakeups": Optional(0), "input_device_uid_list": Optional(), "multi_cycle_io_page_faults": Optional(0), "io_cycle_budget": Optional(11354125), "anchor_sample_time": Optional(398500), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "io_cycle": Optional(380), "wg_inst<…> }
default	23:26:33.499864-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
error	23:26:35.285326-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:35.297957-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["multi_cycle_io_page_faults_duration": Optional(0), "anchor_sample_time": Optional(593684), "other_page_faults": Optional(0), "issue_type": Optional(overload), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_total_wakeups": Optional(5), "io_frame_counter": Optional(143872), "is_recovering": Optional(0), "wg_system_time_mach": Optional(1905), "io_cycle_budget": Optional(11354125), "smallest_buffer_frame_size": Optional(512), "io_cycle": Optional(281), "io_cycle_usage": Optional(1), "reporting_latency": Optional(14521125), "io_page_faults_duration": Optional(0), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "wg_user_time_mach": Optional(21293), "output_device_transport_list": Optional(BuiltIn), "wg_cycles": Optional(2110690), "input_device_uid_list": Optional(), "start_time": Optional(4839456971760), "careporting_timestamp": 1761708395.297313, "input_device_source_list": Optional(), "is_prewarming": Optional(0), "HAL_client_IO_duration": Optiona<…> }
default	23:26:36.505723-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	23:26:39.136396-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:26:39.136490-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:26:39.136631-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:26:39.136763-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:26:39.451759-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:26:39.451857-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:26:39.451891-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:26:39.451935-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:26:39.452353-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:26:39.452413-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:26:39.499885-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
error	23:26:40.279498-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:40.292172-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["cause_set": Optional(8), "io_frame_counter": Optional(239104), "safety_violation": Optional(1), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "careporting_timestamp": 1761708400.291558, "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(59), "multi_cycle_io_page_faults_duration": Optional(0), "input_device_source_list": Optional(), "wg_cycles": Optional(3580187), "HAL_client_IO_duration": Optional(11040166), "num_continuous_silent_io_cycles": Optional(26), "scheduler_latency": Optional(19416), "smallest_buffer_frame_size": Optional(512), "input_device_transport_list": Optional(), "reporting_latency": Optional(13049166), "wg_external_wakeups": Optional(0), "input_device_uid_list": Optional(), "multi_cycle_io_page_faults": Optional(0), "io_cycle_budget": Optional(11354083), "anchor_sample_time": Optional(738248), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "io_cycle": Optional(467), "wg_instruc<…> }
default	23:26:42.486304-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
error	23:26:43.452214-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:43.464349-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["multi_cycle_io_page_faults_duration": Optional(0), "anchor_sample_time": Optional(977972), "other_page_faults": Optional(0), "issue_type": Optional(overload), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_total_wakeups": Optional(9), "io_frame_counter": Optional(151552), "is_recovering": Optional(0), "wg_system_time_mach": Optional(36949), "io_cycle_budget": Optional(11354125), "smallest_buffer_frame_size": Optional(512), "io_cycle": Optional(296), "io_cycle_usage": Optional(1), "reporting_latency": Optional(15304375), "io_page_faults_duration": Optional(0), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "wg_user_time_mach": Optional(26111), "output_device_transport_list": Optional(BuiltIn), "wg_cycles": Optional(3467931), "input_device_uid_list": Optional(), "start_time": Optional(4839652954950), "careporting_timestamp": 1761708403.463942, "input_device_source_list": Optional(), "is_prewarming": Optional(0), "HAL_client_IO_duration": Option<…> }
error	23:26:44.278038-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:44.290873-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["cause_set": Optional(12), "io_frame_counter": Optional(38912), "safety_violation": Optional(1), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "careporting_timestamp": 1761708404.290189, "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(205), "multi_cycle_io_page_faults_duration": Optional(0), "input_device_source_list": Optional(), "wg_cycles": Optional(3116960), "HAL_client_IO_duration": Optional(14149833), "num_continuous_silent_io_cycles": Optional(0), "scheduler_latency": Optional(21958), "smallest_buffer_frame_size": Optional(512), "input_device_transport_list": Optional(), "reporting_latency": Optional(15385291), "wg_external_wakeups": Optional(0), "input_device_uid_list": Optional(), "multi_cycle_io_page_faults": Optional(0), "io_cycle_budget": Optional(11354083), "anchor_sample_time": Optional(1130260), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "io_cycle": Optional(76), "wg_instruc<…> }
error	23:26:45.284542-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:45.297478-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["multi_cycle_io_page_faults_duration": Optional(0), "anchor_sample_time": Optional(1169900), "other_page_faults": Optional(0), "issue_type": Optional(overload), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_total_wakeups": Optional(6), "io_frame_counter": Optional(47616), "is_recovering": Optional(0), "wg_system_time_mach": Optional(1998), "io_cycle_budget": Optional(11354083), "smallest_buffer_frame_size": Optional(512), "io_cycle": Optional(93), "io_cycle_usage": Optional(1), "reporting_latency": Optional(14903750), "io_page_faults_duration": Optional(0), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "wg_user_time_mach": Optional(21361), "output_device_transport_list": Optional(BuiltIn), "wg_cycles": Optional(2220116), "input_device_uid_list": Optional(), "start_time": Optional(4839696950764), "careporting_timestamp": 1761708405.296852, "input_device_source_list": Optional(), "is_prewarming": Optional(0), "HAL_client_IO_duration": Optional<…> }
default	23:26:45.496881-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	23:26:46.993783-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 85B12F3B-4978-48B7-AE00-C038D5C787E1 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65257,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x616e3884 tp_proto=0x06"
default	23:26:46.993947-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65257<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296650 t_state: SYN_SENT process: Nexy:45569 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 17 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x96dc7af6
default	23:26:47.012480-0400	kernel	tcp connected: [<IPv4-redacted>:65257<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296650 t_state: ESTABLISHED process: Nexy:45569 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 17 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x96dc7af6
default	23:26:47.013456-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65257<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296650 t_state: FIN_WAIT_1 process: Nexy:45569 Duration: 0.020 sec Conn_Time: 0.019 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 19.000 ms rttvar: 9.500 ms base rtt: 17 ms so_error: 0 svc/tc: 0 flow: 0x96dc7af6
default	23:26:47.013482-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65257<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296650 t_state: FIN_WAIT_1 process: Nexy:45569 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:26:47.014189-0400	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D769F7FB-087D-49FD-87FA-8C3A337D0C2D flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65258,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xe0a5e1a1 tp_proto=0x06"
default	23:26:47.014261-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65258<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296651 t_state: SYN_SENT process: Nexy:45569 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 17 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb1adb55e
default	23:26:47.029098-0400	kernel	tcp connected: [<IPv4-redacted>:65258<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296651 t_state: ESTABLISHED process: Nexy:45569 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb1adb55e
default	23:26:47.029691-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65258<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296651 t_state: FIN_WAIT_1 process: Nexy:45569 Duration: 0.016 sec Conn_Time: 0.015 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 15.000 ms rttvar: 7.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xb1adb55e
default	23:26:47.029716-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65258<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2296651 t_state: FIN_WAIT_1 process: Nexy:45569 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:26:47.230156-0400	kernel	hfs: mounted Nexy on device disk4s1
error	23:26:47.271226-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:26:47.281709-0400	com.apple.appkit.xpc.openAndSavePanelService	CacheDeleteCopyPurgeableSpaceWithInfo result for unknown!! : {
    "CACHE_DELETE_ERROR" = "Bad volume: /private/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_update_5oheeexm";
}
default	23:26:47.283265-0400	coreaudiod	Sending message. { reporterID=195717364711429, category=IO, type=error, message=["cause_set": Optional(12), "io_frame_counter": Optional(94720), "safety_violation": Optional(1), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "careporting_timestamp": 1761708407.282939, "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(114), "multi_cycle_io_page_faults_duration": Optional(0), "input_device_source_list": Optional(), "wg_cycles": Optional(8517984), "HAL_client_IO_duration": Optional(12335250), "num_continuous_silent_io_cycles": Optional(14), "scheduler_latency": Optional(19708), "smallest_buffer_frame_size": Optional(512), "input_device_transport_list": Optional(), "reporting_latency": Optional(13281500), "wg_external_wakeups": Optional(4), "input_device_uid_list": Optional(), "multi_cycle_io_page_faults": Optional(0), "io_cycle_budget": Optional(11354083), "anchor_sample_time": Optional(1218216), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "io_cycle": Optional(185), "wg_instr<…> }
default	23:26:47.315006-0400	storagekitd	CacheDeleteCopyPurgeableSpaceWithInfo result for unknown!! : {
    "CACHE_DELETE_ERROR" = "Bad volume: /private/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_update_5oheeexm";
}
default	23:26:48.025469-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xd}
default	23:26:48.025893-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ac","name":"Nexy(45569)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:26:48.025979-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 173 stopping playing
default	23:26:48.026026-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:26:48.026068-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:26:48.026122-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:26:48.026241-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:48.026249-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ac to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45569}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ac, sessionType: 'prim', isRecording: false }, 
]
default	23:26:48.026346-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:26:48.026357-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:26:48.026408-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:48.026453-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:48.026472-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	23:26:48.065495-0400	runningboardd	Invalidating assertion 398-334-449310 (target:[app<application.com.nexy.assistant.18912707.18912713(501)>:45569]) from originator [osservice<com.apple.powerd>:334]
default	23:26:48.166872-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring jetsam update because this process is not memory-managed
default	23:26:48.166891-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring suspend because this process is not lifecycle managed
default	23:26:48.166989-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Set darwin role to: None
default	23:26:48.167005-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring GPU update because this process is not GPU managed
default	23:26:48.167069-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] Ignoring memory limit update because this process is not memory-managed
default	23:26:48.171590-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: running-suspended (role: None) (endowments: (null))
default	23:26:48.172204-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, running-suspended-NotVisible
default	23:26:51.913383-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:51.913726-0400	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	23:26:51.926697-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:51.940660-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:51.957443-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:51.977474-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
error	23:26:51.983051-0400	managedappdistributionagent	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
default	23:26:51.994904-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.010222-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.011409-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.024863-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
error	23:26:52.026583-0400	managedappdistributionagent	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
error	23:26:52.034995-0400	managedappdistributiond	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
default	23:26:52.036389-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.050163-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.062446-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.066692-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
error	23:26:52.068881-0400	managedappdistributiond	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
default	23:26:52.075777-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.087886-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.505568-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	23:26:52.505825-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	23:26:52.508846-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.526418-0400	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	23:26:52.539446-0400	kernel	hfs: unmount initiated on Nexy on device disk4s1
default	23:26:52.574917-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	23:26:52.575079-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	23:26:52.577387-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.583101-0400	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	23:26:52.602766-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	23:26:52.602916-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	23:26:52.603615-0400	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef0ac","name":"Nexy(45569)"}, "details":null }
default	23:26:52.603640-0400	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef0ac from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":45569})
default	23:26:52.603650-0400	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":45569})
default	23:26:52.603872-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:26:52.603950-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 173, PID = 45569, Name = sid:0x1ef0ac, Nexy(45569), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:26:52.604011-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:52.604120-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:52.604154-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:52.604070-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:52.604168-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:52.604232-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:26:52.612221-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65241<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2296504 t_state: FIN_WAIT_1 process: Nexy:45569 Duration: 34.154 sec Conn_Time: 0.037 sec bytes in/out: 2462548/964 pkts in/out: 375/14 pkt rxmit: 0 ooo pkts: 45 dup bytes in: 0 ACKs delayed: 25 delayed ACKs sent: 0
rtt: 48.125 ms rttvar: 17.937 ms base rtt: 23 ms so_error: 0 svc/tc: 0 flow: 0xa1f19d1e
default	23:26:52.612236-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65241<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2296504 t_state: FIN_WAIT_1 process: Nexy:45569 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:26:52.612332-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65238<-><IPv4-redacted>:443] interface: en0 (skipped: 871)
so_gencnt: 2296488 t_state: FIN_WAIT_1 process: Nexy:45569 Duration: 35.304 sec Conn_Time: 0.016 sec bytes in/out: 97545075/2617 pkts in/out: 11156/4 pkt rxmit: 0 ooo pkts: 284 dup bytes in: 0 ACKs delayed: 6400 delayed ACKs sent: 1
rtt: 18.406 ms rttvar: 7.250 ms base rtt: 8 ms so_error: 0 svc/tc: 0 flow: 0xa59e1603
default	23:26:52.612344-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65238<-><IPv4-redacted>:443] interface: en0 (skipped: 871)
so_gencnt: 2296488 t_state: FIN_WAIT_1 process: Nexy:45569 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:26:52.612363-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65235<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2296462 t_state: FIN_WAIT_1 process: Nexy:45569 Duration: 35.650 sec Conn_Time: 0.026 sec bytes in/out: 1369/116 pkts in/out: 1/1 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 25.750 ms rttvar: 10.250 ms base rtt: 23 ms so_error: 0 svc/tc: 0 flow: 0x8303fb29
default	23:26:52.612375-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65235<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2296462 t_state: FIN_WAIT_1 process: Nexy:45569 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:26:52.612399-0400	kernel	tcp_connection_summary (tcp_drop:1348)[<IPv4-redacted>:65237<-><IPv4-redacted>:443] interface: en0 (skipped: 871)
so_gencnt: 2296476 t_state: CLOSED process: Nexy:45569 Duration: 35.571 sec Conn_Time: 0.037 sec bytes in/out: 8745/1774 pkts in/out: 8/4 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 43.312 ms rttvar: 19.187 ms base rtt: 37 ms so_error: 0 svc/tc: 0 flow: 0x9d1f655a
default	23:26:52.612406-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65237<-><IPv4-redacted>:443] interface: en0 (skipped: 871)
so_gencnt: 2296476 t_state: CLOSED process: Nexy:45569 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/1 AccECN (client/server): Disabled/Disabled
default	23:26:52.612442-0400	mDNSResponder	[R279438] DNSServiceCreateConnection STOP PID[45569](Nexy)
default	23:26:52.613504-0400	runningboardd	[app<application.com.nexy.assistant.18912707.18912713(501)>:45569] termination reported by launchd (0, 0, 0)
default	23:26:52.613610-0400	runningboardd	Removing process: [app<application.com.nexy.assistant.18912707.18912713(501)>:45569]
default	23:26:52.613807-0400	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.18912707.18912713(501)>:45569]
default	23:26:52.613962-0400	runningboardd	Removed job for [app<application.com.nexy.assistant.18912707.18912713(501)>:45569]
default	23:26:52.613979-0400	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.18912707.18912713(501)>:45569]
default	23:26:52.614279-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18912707.18912713(501)>: none (role: None) (endowments: (null))
default	23:26:52.614342-0400	audiomxd	  ServerSessionManager.mm:1322  Monitored process died, pid = 45569, name = Nexy
default	23:26:52.615511-0400	launchservicesd	Hit the server for a process handle 74fd9420000b201 that resolved to: [app<application.com.nexy.assistant.18912707.18912713(501)>:45569]
default	23:26:52.615520-0400	gamepolicyd	Received state update for 45569 (app<application.com.nexy.assistant.18912707.18912713(501)>, none-NotVisible
error	23:26:52.616436-0400	managedappdistributionagent	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
default	23:26:52.617566-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	23:26:52.617707-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	23:26:52.619219-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.626085-0400	runningboardd	Launch request for app<application.com.nexy.assistant.18914053.18914413(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	23:26:52.626164-0400	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.18914053.18914413(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:17058] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-17058-449374 target:app<application.com.nexy.assistant.18914053.18914413(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	23:26:52.626241-0400	runningboardd	Assertion 398-17058-449374 (target:app<application.com.nexy.assistant.18914053.18914413(501)>) will be created as active
default	23:26:52.631750-0400	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	23:26:52.631776-0400	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.18914053.18914413(501)>
default	23:26:52.631820-0400	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	23:26:52.631911-0400	runningboardd	app<application.com.nexy.assistant.18914053.18914413(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	23:26:52.659476-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] is not RunningBoard jetsam managed.
default	23:26:52.659514-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] This process will not be managed.
default	23:26:52.659549-0400	runningboardd	Now tracking process: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:26:52.659673-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:26:52.663747-0400	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:26:52.663841-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-449375 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:26:52.664005-0400	runningboardd	Assertion 398-398-449375 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:26:52.664252-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:26:52.664263-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:26:52.664288-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Set darwin role to: UserInteractive
default	23:26:52.664314-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:26:52.664386-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:26:52.664398-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] reported to RB as running
default	23:26:52.666243-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:45671" ID:398-363-449376 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	23:26:52.666337-0400	runningboardd	Assertion 398-363-449376 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:26:52.667063-0400	CoreServicesUIAgent	LAUNCH: 0x0-0x99a99a com.nexy.assistant starting stopped process.
default	23:26:52.671799-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:26:52.671812-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:26:52.671823-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:26:52.671864-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:26:52.671943-0400	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:26:52.672082-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:26:52.672425-0400	runningboardd	Invalidating assertion 398-17058-449374 (target:app<application.com.nexy.assistant.18914053.18914413(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:17058]
default	23:26:52.672455-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:26:52.672513-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:26:52.672550-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:26:52.672610-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:26:52.676481-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:26:52.666152-0400	gamepolicyd	Hit the server for a process handle 47ea5700000b267 that resolved to: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:26:52.666188-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:26:52.667135-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	23:26:52.667296-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	23:26:52.668107-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	23:26:52.705069-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:26:52.712587-0400	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	23:26:52.731743-0400	nehelper	Received an apps installed notification with bundle IDs (
    "com.nexy.assistant"
)
error	23:26:52.740299-0400	managedappdistributiond	Error occurred during transaction: The provided identifier "com.nexy.assistant" is invalid
default	23:26:53.334577-0400	nehelper	Handling an apps installed notification with bundle IDs (
    "com.nexy.assistant"
)
default	23:26:53.504961-0400	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: com.nexy.assistant), 0, 0, 1, 0, 4, 4, 1
default	23:26:53.505886-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=511.70, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	23:26:53.512476-0400	tccd	AUTHREQ_SUBJECT: msgID=511.70, subject=com.nexy.assistant,
default	23:26:53.527059-0400	syspolicyd	Found provenance data on target: TA(c1427ed62e916d1d, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: com.nexy.assistant)
default	23:26:54.584171-0400	Nexy	[0x1018fd130] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	23:26:54.584247-0400	Nexy	[0x1018fd270] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	23:26:54.823590-0400	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x1018edf70 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	23:26:54.823843-0400	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x1018edf70 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	23:26:54.824058-0400	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x1018edf70 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	23:26:54.824265-0400	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x1018edf70 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	23:26:55.046142-0400	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	23:26:55.051811-0400	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	23:26:55.053580-0400	Nexy	[0x101905120] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	23:26:55.057180-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.18914053.18914413 AUID=501> and <type=Application identifier=application.com.nexy.assistant.18914053.18914413>
default	23:26:55.062542-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	23:26:55.064699-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	23:26:55.064951-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	23:26:55.065124-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	23:26:55.065140-0400	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	23:26:55.065175-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	23:26:55.065367-0400	Nexy	[0x93d688000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	23:26:55.065481-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	23:26:55.065821-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45671.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:26:55.073299-0400	tccd	AUTHREQ_SUBJECT: msgID=45671.1, subject=com.nexy.assistant,
default	23:26:55.073935-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:26:55.086380-0400	Nexy	[0x93d688000] invalidated after the last release of the connection object
default	23:26:55.086539-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	23:26:55.086577-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	23:26:55.086838-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	23:26:55.088196-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3686, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:26:55.089059-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3686, subject=com.nexy.assistant,
default	23:26:55.089617-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
error	23:26:55.102230-0400	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	23:26:55.103137-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3688, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:26:55.103923-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3688, subject=com.nexy.assistant,
default	23:26:55.104448-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:26:55.120174-0400	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	23:26:55.120201-0400	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x93d565780> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	23:26:55.138258-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	23:26:58.625219-0400	runningboardd	Assertion did invalidate due to timeout: 398-398-449375 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671])
default	23:26:58.825762-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:26:58.825776-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:26:58.825783-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:26:58.825798-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:26:58.829231-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:26:58.829857-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:01.169459-0400	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid DCDA9753-B0ED-4855-8AFC-7822E1283489 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65274,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x79275805 tp_proto=0x06"
default	23:27:01.169553-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65274<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2297026 t_state: SYN_SENT process: Nexy:45671 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbdbbc00b
default	23:27:01.193605-0400	kernel	tcp connected: [<IPv4-redacted>:65274<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2297026 t_state: ESTABLISHED process: Nexy:45671 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbdbbc00b
default	23:27:01.194238-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65274<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2297026 t_state: FIN_WAIT_1 process: Nexy:45671 Duration: 0.024 sec Conn_Time: 0.024 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 24.000 ms rttvar: 12.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xbdbbc00b
default	23:27:01.194262-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65274<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2297026 t_state: FIN_WAIT_1 process: Nexy:45671 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:27:01.276520-0400	Nexy	[0x93d688000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	23:27:01.288168-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x93d71b840) Selecting device 71 from constructor
default	23:27:01.288182-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93d71b840)
default	23:27:01.288187-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93d71b840) not already running
default	23:27:01.288191-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x93d71b840) nothing to teardown
default	23:27:01.288193-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93d71b840) connecting device 71
default	23:27:01.288288-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93d71b840) Device ID: 71 (Input:No | Output:Yes): true
default	23:27:01.288393-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93d71b840) created ioproc 0xa for device 71
default	23:27:01.288491-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93d71b840) adding 7 device listeners to device 71
default	23:27:01.288662-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93d71b840) adding 0 device delegate listeners to device 71
default	23:27:01.288671-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93d71b840)
default	23:27:01.288734-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:01.288743-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:27:01.288753-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:01.288758-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:27:01.288765-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:01.288852-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93d71b840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:01.288862-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93d71b840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:01.288868-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:01.288872-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93d71b840) removing 0 device listeners from device 0
default	23:27:01.288876-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93d71b840) removing 0 device delegate listeners from device 0
default	23:27:01.288880-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93d71b840)
default	23:27:01.288891-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	23:27:01.288970-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x93d71b840) caller requesting device change from 71 to 78
default	23:27:01.288978-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93d71b840)
default	23:27:01.288983-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93d71b840) not already running
default	23:27:01.288986-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93d71b840) disconnecting device 71
default	23:27:01.288991-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93d71b840) destroying ioproc 0xa for device 71
default	23:27:01.289041-0400	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	23:27:01.289474-0400	Nexy	[0x93d688280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	23:27:01.290303-0400	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"PID":45671,"session_type":"Primary"} }
default	23:27:01.290381-0400	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: false }, 
]
default	23:27:01.290968-0400	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 45671, name = Nexy
default	23:27:01.291218-0400	Nexy	    SessionCore_Create.mm:99    Created session 0x93d56a5c0 with ID: 0x1ef0ad
default	23:27:01.292696-0400	Nexy	[0x93d6883c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	23:27:01.292819-0400	Nexy	No persisted cache on this platform.
error	23:27:01.293097-0400	Nexy	Reporter disconnected. { function=sendMessage, reporterID=196155451375617 }
default	23:27:01.293111-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xa}
default	23:27:01.293164-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:01.293255-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93d71b840) connecting device 78
default	23:27:01.293337-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93d71b840) Device ID: 78 (Input:Yes | Output:No): true
default	23:27:01.294528-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3689, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:01.295768-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3689, subject=com.nexy.assistant,
default	23:27:01.296407-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108600 at /Applications/Nexy.app
default	23:27:01.314311-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93d71b840) created ioproc 0xa for device 78
default	23:27:01.314470-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93d71b840) adding 7 device listeners to device 78
default	23:27:01.314702-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93d71b840) adding 0 device delegate listeners to device 78
default	23:27:01.314713-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93d71b840)
default	23:27:01.314722-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	23:27:01.314733-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:01.314896-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	23:27:01.314910-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	23:27:01.314919-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	23:27:01.315032-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93d71b840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:01.315046-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93d71b840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:01.315052-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:01.315067-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93d71b840) removing 7 device listeners from device 71
default	23:27:01.315274-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93d71b840) removing 0 device delegate listeners from device 71
default	23:27:01.315285-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93d71b840)
default	23:27:01.315803-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:01.317225-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3690, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:01.318312-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3690, subject=com.nexy.assistant,
default	23:27:01.318995-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108600 at /Applications/Nexy.app
default	23:27:01.334093-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:01.335365-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3691, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:01.336427-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3691, subject=com.nexy.assistant,
default	23:27:01.337171-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108600 at /Applications/Nexy.app
default	23:27:01.352765-0400	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	23:27:01.354517-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3692, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:01.355679-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3692, subject=com.nexy.assistant,
default	23:27:01.356359-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108600 at /Applications/Nexy.app
default	23:27:01.374814-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449412 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:27:01.374911-0400	runningboardd	Assertion 398-334-449412 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:01.375264-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:01.375279-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:01.375343-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:01.375403-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:01.378773-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:01.379252-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:01.399900-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xa}
default	23:27:01.400954-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	23:27:01.401060-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:01.401134-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:01.401242-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	23:27:01.401298-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:01.401328-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:01.401365-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:01.401434-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:01.401438-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
fault	23:27:01.401397-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.18914053.18914413 AUID=501> and <type=Application identifier=application.com.nexy.assistant.18914053.18914413>
default	23:27:01.401465-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ad, Nexy(45671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 starting recording
default	23:27:01.401501-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:01.401555-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:01.401597-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:01.401628-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:27:01.401655-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:01.401655-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:01.401711-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:01.401729-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:01.401773-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	23:27:01.401859-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:01.401784-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:01.401895-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:01.401911-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	23:27:01.401925-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	23:27:01.401940-0400	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	23:27:01.401993-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
fault	23:27:01.402997-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.18914053.18914413 AUID=501> and <type=Application identifier=application.com.nexy.assistant.18914053.18914413>
default	23:27:01.425561-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:01.425654-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	23:27:01.425698-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	23:27:01.428122-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:01.428136-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:01.428150-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:01.428158-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:01.428168-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:01.428174-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:01.428323-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:01.432168-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:01.432199-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:01.432225-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:01.432245-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:01.432256-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:01.432266-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:01.432481-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:01.432665-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:01.432688-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:01.432698-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:01.432707-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:01.432714-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:01.432723-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:01.434699-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	23:27:02.030752-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _appQuitTimer:] | _appQuitTimer fired for: ASN: 9992583, name: Nexy with url: file:///Applications/Nexy.app/
default	23:27:02.031131-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | There are other instances of Nexy at /Applications/Nexy.app.  Done with this instance.
default	23:27:02.386847-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	23:27:02.394515-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	23:27:02.395108-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:27:02.395155-0400	runningboardd	Invalidating assertion 398-334-449412 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.powerd>:334]
default	23:27:02.395277-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:02.395351-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:27:02.395392-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:02.395603-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ad, Nexy(45671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 stopping recording
default	23:27:02.395670-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:27:02.395709-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:02.395724-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:02.395771-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:02.395915-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:02.395975-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:02.396011-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:02.396033-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:02.396013-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:27:02.395908-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:02.396028-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:02.396107-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:02.396126-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:02.396167-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	23:27:02.399203-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	23:27:02.400707-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:02.400729-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:02.400751-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:02.400763-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:02.400777-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:02.400789-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:02.400950-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:02.498215-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x93d71b840) Selecting device 0 from destructor
default	23:27:02.498239-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93d71b840)
default	23:27:02.498245-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93d71b840) not already running
default	23:27:02.498251-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93d71b840) disconnecting device 78
default	23:27:02.498260-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93d71b840) destroying ioproc 0xa for device 78
default	23:27:02.498302-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	23:27:02.498344-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:02.498543-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x93d71b840) nothing to setup
default	23:27:02.498558-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93d71b840) adding 0 device listeners to device 0
default	23:27:02.498565-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93d71b840) adding 0 device delegate listeners to device 0
default	23:27:02.498574-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93d71b840) removing 7 device listeners from device 78
default	23:27:02.499073-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93d71b840) removing 0 device delegate listeners from device 78
default	23:27:02.499102-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93d71b840)
default	23:27:02.500055-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:02.500068-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:02.500099-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:02.500128-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:02.505297-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:02.506005-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:02.640546-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45694.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=45694, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	23:27:02.642360-0400	tccd	AUTHREQ_SUBJECT: msgID=45694.1, subject=com.nexy.assistant,
default	23:27:02.643140-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:02.663461-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6084, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=45694, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:27:02.664716-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6084, subject=com.nexy.assistant,
default	23:27:02.665426-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:02.693526-0400	launchservicesd	CHECKIN:0x0-0x99a99a 45694 com.nexy.assistant
default	23:27:02.694394-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	23:27:02.694525-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	23:27:02.696768-0400	WindowServer	afc5f[CreateApplication]: Process creation: 0x0-0x99a99a (Nexy) connectionID: AFC5F pid: 45694 in session 0x101
default	23:27:02.700037-0400	runningboardd	Invalidating assertion 398-363-449376 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	23:27:02.701792-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:02.703037-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	23:27:02.723449-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 45029: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 4d4e0d00 };
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
default	23:27:02.737873-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:02.765542-0400	WindowServer	0[outside of RPC]: Process death: 0x0-0x99a99a (Nexy) connectionID: AFC5F pid: 45694 in session 0x101
default	23:27:02.765599-0400	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x99a99a (Nexy) acq:0x800bd1a80 count:1
default	23:27:02.767463-0400	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x99a99a} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	23:27:02.767489-0400	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 10070426
default	23:27:02.767564-0400	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	23:27:02.768480-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x99a99a removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x99a99a (Nexy)"
)}
default	23:27:02.768836-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xb27e removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x99a99a (Nexy)"
)}
default	23:27:02.809029-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:02.809065-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:02.809302-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Set darwin role to: None
default	23:27:02.809312-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:02.809362-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:02.812701-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-suspended (role: None) (endowments: (null))
default	23:27:02.813147-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-suspended-NotVisible
default	23:27:03.382930-0400	Nexy	[0x93d688640] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	23:27:03.384004-0400	Nexy	[0x93d6888c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	23:27:03.495934-0400	Nexy	Received configuration update from daemon (initial)
default	23:27:03.558037-0400	Nexy	[0x93d688a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	23:27:03.559218-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	23:27:03.559474-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45671.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:27:03.562133-0400	tccd	AUTHREQ_SUBJECT: msgID=45671.2, subject=com.nexy.assistant,
default	23:27:03.562874-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:03.578521-0400	Nexy	[0x93d688a00] invalidated after the last release of the connection object
default	23:27:03.579364-0400	Nexy	[0x93d688a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	23:27:03.579843-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	23:27:03.580002-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45671.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:27:03.581219-0400	tccd	AUTHREQ_SUBJECT: msgID=45671.3, subject=com.nexy.assistant,
default	23:27:03.581939-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:03.599692-0400	Nexy	[0x93d688a00] invalidated after the last release of the connection object
default	23:27:03.599786-0400	Nexy	[0x93d688a00] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	23:27:03.599977-0400	Nexy	[0x93d688a00] invalidated after the last release of the connection object
default	23:27:03.600487-0400	Nexy	[0x93d688b40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	23:27:03.601109-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45671.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:27:03.602771-0400	tccd	AUTHREQ_SUBJECT: msgID=45671.4, subject=com.nexy.assistant,
default	23:27:03.604662-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:03.620620-0400	Nexy	[0x93d688b40] invalidated after the last release of the connection object
default	23:27:03.621143-0400	Nexy	server port 0x0000b00f, session port 0x0000f513
default	23:27:03.622363-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6085, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:27:03.622389-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:03.623938-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6085, subject=com.nexy.assistant,
default	23:27:03.625346-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:03.669639-0400	kernel	tcp connected: [<IPv4-redacted>:65276<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2297033 t_state: ESTABLISHED process: Nexy:45671 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x917fcaad
default	23:27:03.707629-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65276<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2297033 t_state: FIN_WAIT_1 process: Nexy:45671 Duration: 0.059 sec Conn_Time: 0.021 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 21.000 ms rttvar: 10.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x917fcaad
default	23:27:03.707653-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65276<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2297033 t_state: FIN_WAIT_1 process: Nexy:45671 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:27:03.707875-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	23:27:03.708122-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	23:27:03.708575-0400	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 24B01C85-827E-4AC5-9B77-EC4BCD66D962 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65277,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x5490efda tp_proto=0x06"
default	23:27:03.708704-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65277<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2297034 t_state: SYN_SENT process: Nexy:45671 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x89c5314f
default	23:27:03.709337-0400	Nexy	nw_path_libinfo_path_check [9034599A-8983-4579-98B2-C120ACB434B8 IPv4#97fd4da3:8081 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	23:27:03.709853-0400	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 025DBCB3-D76B-49F9-834E-6157BDB53BC8 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65278,dst=<IPv4-redacted>.8081,proto=0x06 mask=0x0000003f,hash=0xb4342c0a tp_proto=0x06"
default	23:27:03.709887-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65278<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2297035 t_state: SYN_SENT process: Nexy:45671 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 23 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x93132625
default	23:27:03.728207-0400	kernel	tcp connected: [<IPv4-redacted>:65277<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2297034 t_state: ESTABLISHED process: Nexy:45671 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x89c5314f
default	23:27:03.728558-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65277<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2297034 t_state: FIN_WAIT_1 process: Nexy:45671 Duration: 0.020 sec Conn_Time: 0.019 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 19.000 ms rttvar: 9.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x89c5314f
default	23:27:03.728566-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65277<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2297034 t_state: FIN_WAIT_1 process: Nexy:45671 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:27:03.736119-0400	kernel	tcp connected: [<IPv4-redacted>:65278<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2297035 t_state: ESTABLISHED process: Nexy:45671 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 23 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x93132625
default	23:27:03.791846-0400	Nexy	[0x93d688c80] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	23:27:03.792867-0400	Nexy	[0x93d688b40] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	23:27:03.795527-0400	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	23:27:03.796127-0400	Nexy	server port 0x0000f513, session port 0x0000f513
default	23:27:03.798151-0400	Nexy	New connection 0xefc1b main
default	23:27:03.800209-0400	Nexy	CHECKIN: pid=45671
default	23:27:03.806404-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:45671" ID:398-363-449416 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	23:27:03.806478-0400	runningboardd	Assertion 398-363-449416 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:03.806487-0400	launchservicesd	CHECKIN:0x0-0x99b99b 45671 com.nexy.assistant
default	23:27:03.806773-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:45671" ID:398-363-449417 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	23:27:03.806792-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:03.806847-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:03.806967-0400	Nexy	CHECKEDIN: pid=45671 asn=0x0-0x99b99b foreground=0
default	23:27:03.806916-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Set darwin role to: UserInteractive
default	23:27:03.806977-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:03.806863-0400	runningboardd	Assertion 398-363-449417 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:03.807084-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:03.807281-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	23:27:03.807346-0400	Nexy	[0x93d688dc0] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	23:27:03.807430-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	23:27:03.807663-0400	Nexy	[0x93d688f00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	23:27:03.807672-0400	Nexy	[0x93d688f00] Connection returned listener port: 0xc103
default	23:27:03.807801-0400	Nexy	[0x93df28780] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x93d688f00.peer[363].0x93df28780
default	23:27:03.810542-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:03.810786-0400	runningboardd	Invalidating assertion 398-363-449416 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	23:27:03.811094-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:03.811235-0400	Nexy	FRONTLOGGING: version 1
default	23:27:03.811243-0400	Nexy	Registered, pid=45671 ASN=0x0,0x99b99b
default	23:27:03.811444-0400	WindowServer	efc1b[CreateApplication]: Process creation: 0x0-0x99b99b (Nexy) connectionID: EFC1B pid: 45671 in session 0x101
default	23:27:03.811784-0400	Nexy	[0x93d689040] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	23:27:03.812256-0400	Nexy	[0x93d688f00] Connection returned listener port: 0xc103
default	23:27:03.812676-0400	Nexy	BringForward: pid=45671 asn=0x0-0x99b99b bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	23:27:03.813141-0400	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	23:27:03.815310-0400	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	23:27:03.816090-0400	Nexy	Post-registration system appearance: (HLTB: 2)
default	23:27:03.824150-0400	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	23:27:03.824160-0400	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	23:27:03.824209-0400	Nexy	Initializing connection
default	23:27:03.824249-0400	Nexy	Removing all cached process handles
default	23:27:03.824269-0400	Nexy	Sending handshake request attempt #1 to server
default	23:27:03.824278-0400	Nexy	Creating connection to com.apple.runningboard
default	23:27:03.824285-0400	Nexy	[0x93d6892c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	23:27:03.824616-0400	Nexy	[0x93d688f00] Connection returned listener port: 0xc103
default	23:27:03.824626-0400	runningboardd	Setting client for [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] as ready
default	23:27:03.825192-0400	Nexy	Handshake succeeded
default	23:27:03.825210-0400	Nexy	Identity resolved as app<application.com.nexy.assistant.18914053.18914413(501)>
default	23:27:03.827440-0400	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 200000001b pid: 45671
default	23:27:03.829984-0400	Nexy	[0x93d688f00] Connection returned listener port: 0xc103
default	23:27:03.831516-0400	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	23:27:03.831554-0400	Nexy	[0x93d689540] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	23:27:03.831661-0400	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	23:27:03.831717-0400	Nexy	[0x93d689680] activating connection: mach=false listener=true peer=false name=(anonymous)
default	23:27:03.834352-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "frontmost:45671" ID:398-363-449418 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractiveFocal" sourceEnvironment:"(null)">
	]>
default	23:27:03.834427-0400	runningboardd	Assertion 398-363-449418 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:03.834522-0400	WindowServer	efc1b[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x99b99b (Nexy) mainConnectionID: EFC1B;
} for reason: updated frontmost process
default	23:27:03.834594-0400	WindowServer	efc1b[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x99b99b (Nexy) -> <pid: 45671>
default	23:27:03.834688-0400	WindowServer	new deferring rules for pid:393: [
    [393-5EA5]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EA4]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EA3]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:03.834758-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-5EA5]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EA4]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EA3]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:03.834706-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:03.834736-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:03.834826-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Set darwin role to: UserInteractiveFocal
default	23:27:03.834888-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:03.834995-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:03.835468-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "notification:45671" ID:398-363-449419 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	23:27:03.835578-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x99b99b; pid: 393>,
    <pid: 45671>
]
default	23:27:03.835566-0400	runningboardd	Assertion 398-363-449419 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:03.840209-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:03.840470-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:03.840490-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:03.840498-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:03.840548-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:03.844574-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:03.857163-0400	Nexy	[0x93d689900] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	23:27:03.871927-0400	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2400000020 pid: 45671
default	23:27:03.878103-0400	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	23:27:03.886146-0400	Nexy	[0x93d689680] Connection returned listener port: 0x10303
default	23:27:03.889002-0400	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x93c641400
 (
    "<NSDarkAquaAppearance: 0x93c641360>",
    "<NSSystemAppearance: 0x93c6412c0>"
)>
default	23:27:03.896759-0400	Nexy	[0x93d689e00] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	23:27:03.900719-0400	Nexy	[0x93d689f40] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	23:27:03.903162-0400	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	23:27:03.903440-0400	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	23:27:03.903455-0400	Nexy	Start service name com.apple.spotlight.IndexAgent
default	23:27:03.903479-0400	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	23:27:03.903485-0400	Nexy	[0x93d68a080] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	23:27:03.903525-0400	Nexy	[0x93d68a300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	23:27:03.903587-0400	Nexy	FBSWorkspace registering source: <private>
default	23:27:03.904244-0400	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	23:27:03.905286-0400	Nexy	FBSWorkspace connected to endpoint : <private>
default	23:27:03.905350-0400	Nexy	<FBSWorkspaceScenesClient:0x93c642760 <private>> attempting immediate handshake from activate
default	23:27:03.905397-0400	Nexy	<FBSWorkspaceScenesClient:0x93c642760 <private>> sent handshake
default	23:27:03.905487-0400	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	23:27:03.905819-0400	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:03.905843-0400	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:03.905919-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Registering event dispatcher at init
default	23:27:03.912280-0400	ControlCenter	Created <FBWorkspace: 0xaf8b16120; <FBApplicationProcess: 0xaf8cfca80; app<application.com.nexy.assistant.18914053.18914413>:45671(vD4E14)>>
default	23:27:03.912321-0400	ControlCenter	Bootstrapping app<application.com.nexy.assistant.18914053.18914413> with intent background
default	23:27:03.912667-0400	runningboardd	Launch request for app<application.com.nexy.assistant.18914053.18914413(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	23:27:03.912784-0400	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.18914053.18914413(501)> from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:398-632-449420 target:app<application.com.nexy.assistant.18914053.18914413(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	23:27:03.912914-0400	runningboardd	Assertion 398-632-449420 (target:app<application.com.nexy.assistant.18914053.18914413(501)>) will be created as active
default	23:27:03.912944-0400	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:398-632-449420 target:app<application.com.nexy.assistant.18914053.18914413(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:03.913256-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:03.913269-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:03.913279-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:03.913296-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:03.915664-0400	Nexy	Registered process with identifier 45671-871956
default	23:27:03.915879-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:03.915983-0400	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	23:27:03.917506-0400	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	23:27:03.918267-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:03.919375-0400	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	23:27:03.919899-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Bootstrap success!
default	23:27:03.920181-0400	Nexy	Requesting scene <FBSScene: 0x93c640dc0; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292> from com.apple.controlcenter.statusitems
default	23:27:03.920281-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Setting process visibility to: Background
default	23:27:03.920325-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] No launch watchdog for this process, dropping initial assertion in 2.0s
default	23:27:03.920536-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:398-632-449421 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	23:27:03.920584-0400	runningboardd	Assertion 398-632-449421 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:03.920984-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:03.920994-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:03.921015-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:03.921075-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:03.922944-0400	Nexy	Request for <FBSScene: 0x93c640dc0; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292> complete!
default	23:27:03.923041-0400	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	23:27:03.923404-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:03.923716-0400	ControlCenter	Adding: <FBApplicationProcess: 0xaf8cfca80; app<application.com.nexy.assistant.18914053.18914413>:45671(vD4E14)>
default	23:27:03.923860-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:03.924062-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Connection established.
default	23:27:03.924115-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xaf8ce4cb0>
default	23:27:03.924134-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Connection to remote process established!
default	23:27:03.924145-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:03.924834-0400	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	23:27:03.925066-0400	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	23:27:03.925280-0400	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	23:27:03.925314-0400	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	23:27:03.925581-0400	Nexy	Requesting scene <FBSScene: 0x93c642bc0; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	23:27:03.925764-0400	Nexy	Request for <FBSScene: 0x93c642bc0; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView> complete!
default	23:27:03.928644-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	23:27:03.928659-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	23:27:03.935988-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	23:27:03.936008-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	23:27:03.936100-0400	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	23:27:03.936638-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	23:27:03.936654-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	23:27:03.937661-0400	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:03.937676-0400	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xaf8cfca80; app<application.com.nexy.assistant.18914053.18914413>:45671(vD4E14)>
default	23:27:03.937743-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Registered new scene: <FBWorkspaceScene: 0xaf5dc4c00; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292> (fromRemnant = 0)
default	23:27:03.937777-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace interruption policy did change: reconnect
default	23:27:03.937896-0400	ControlCenter	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Client process connected: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:03.937906-0400	Nexy	Request for <FBSScene: 0x93c640dc0; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292> complete!
default	23:27:03.938040-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:398-632-449422 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	23:27:03.938119-0400	runningboardd	Assertion 398-632-449422 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as inactive as originator process has not exited
default	23:27:03.938446-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-449423 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	23:27:03.938543-0400	runningboardd	Assertion 398-632-449423 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:03.938631-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	23:27:03.938723-0400	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:03.938736-0400	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xaf8cfca80; app<application.com.nexy.assistant.18914053.18914413>:45671(vD4E14)>
default	23:27:03.938797-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Registered new scene: <FBWorkspaceScene: 0xaf5dc4000; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	23:27:03.938811-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:03.938822-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:03.938832-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:03.938924-0400	ControlCenter	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:03.938853-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:03.939173-0400	Nexy	<FBSWorkspaceScenesClient:0x93c642760 <private>> Reconnecting scene com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292
default	23:27:03.939474-0400	Nexy	<FBSWorkspaceScenesClient:0x93c642760 <private>> Reconnecting scene com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView
default	23:27:03.939588-0400	Nexy	Request for <FBSScene: 0x93c642bc0; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView> complete!
default	23:27:03.941436-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:03.941884-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:03.942156-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:03.961436-0400	Nexy	Registering for test daemon availability notify post.
default	23:27:03.961615-0400	Nexy	notify_get_state check indicated test daemon not ready.
default	23:27:03.961720-0400	Nexy	notify_get_state check indicated test daemon not ready.
default	23:27:03.961819-0400	Nexy	notify_get_state check indicated test daemon not ready.
default	23:27:03.963205-0400	Nexy	[0x93d68a580] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	23:27:03.963753-0400	Nexy	[0x93d688f00] Connection returned listener port: 0xc103
default	23:27:03.964104-0400	Nexy	SignalReady: pid=45671 asn=0x0-0x99b99b
default	23:27:03.964368-0400	Nexy	SIGNAL: pid=45671 asn=0x0x-0x99b99b
default	23:27:03.964886-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	23:27:03.966861-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:03.975948-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	23:27:03.978270-0400	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	23:27:03.978276-0400	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	23:27:03.978300-0400	Nexy	[0x93d689180] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	23:27:03.978398-0400	Nexy	[0x93d689180] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	23:27:03.979624-0400	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	23:27:03.981772-0400	Nexy	[C:2] Alloc <private>
default	23:27:03.981803-0400	Nexy	[0x93d689180] activating connection: mach=false listener=false peer=false name=(anonymous)
error	23:27:03.981982-0400	kernel	Sandbox: WindowManager(584) deny(1) mach-task-name others [Nexy(45671)]
default	23:27:03.982263-0400	Nexy	[0x93d68a6c0] activating connection: mach=false listener=false peer=false name=com.apple.ViewBridgeAuxiliary
default	23:27:03.982441-0400	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-45671). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	23:27:03.983597-0400	WindowManager	Connection activated | (45671) Nexy
default	23:27:03.984715-0400	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-45671)
default	23:27:03.985210-0400	ControlCenter	Created new displayable type DisplayableAppStatusItemType(0BE10715, (bid:com.nexy.assistant-Item-0-45671)) for (bid:com.nexy.assistant-Item-0-45671)
default	23:27:03.985815-0400	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-45671)]
default	23:27:03.986301-0400	ControlCenter	Created instance DisplayableId(F40DD33B) in .menuBar for DisplayableAppStatusItemType(0BE10715, (bid:com.nexy.assistant-Item-0-45671)) .menuBar
default	23:27:03.990670-0400	Nexy	[0x93d68a940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	23:27:03.991168-0400	Nexy	[0x93d68aa80] activating connection: mach=false listener=true peer=false name=(anonymous)
default	23:27:03.991178-0400	Nexy	[0x93d68aa80] Connection returned listener port: 0x1fa03
default	23:27:03.994663-0400	Nexy	[0x93d68a6c0] invalidated after the last release of the connection object
default	23:27:03.995249-0400	ControlCenter	Created ephemaral instance DisplayableId(F40DD33B) for (bid:com.nexy.assistant-Item-0-45671) with positioning .ephemeral
default	23:27:03.997229-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-45671-449424 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	23:27:03.997288-0400	runningboardd	Assertion 398-45671-449424 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:03.997597-0400	runningboardd	Invalidating assertion 398-45671-449424 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:03.997627-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:03.997657-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:03.997704-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:03.997843-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Received action(s): NSStatusItemChangeVisibilityAction
default	23:27:03.997798-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:04.000385-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:04.000833-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:04.000868-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Observer <NSSceneStatusItem: 0x93d68e760> handled action(s): <private>
default	23:27:04.000977-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:04.001312-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	23:27:04.002613-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	23:27:04.003192-0400	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	23:27:04.003305-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	23:27:04.015289-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:04.103741-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:04.103759-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:04.103770-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:04.103789-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:04.106870-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:04.107302-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:04.107441-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:04.134176-0400	kernel	udp connect: [<IPv4-redacted>:63428<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2297038 so_state: 0x0002 process: Nexy:45671 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xa125311c
default	23:27:04.134193-0400	kernel	udp_connection_summary [<IPv4-redacted>:63428<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2297038 so_state: 0x0002 process: Nexy:45671 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xa125311c flowctl: 0us (0x)
default	23:27:04.134577-0400	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3AB7AD64-DDF0-4850-B19D-868D4B3E5286 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.65280,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0x2d0f09ed tp_proto=0x06"
default	23:27:04.134669-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:65280<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2297040 t_state: SYN_SENT process: Nexy:45671 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 23 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xba27d84f
default	23:27:04.145368-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:04.163330-0400	kernel	tcp connected: [<IPv4-redacted>:65280<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2297040 t_state: ESTABLISHED process: Nexy:45671 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 23 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xba27d84f
default	23:27:04.187271-0400	Nexy	[0x93d68a800] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	23:27:04.188513-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45671.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:27:04.190078-0400	tccd	AUTHREQ_SUBJECT: msgID=45671.5, subject=com.nexy.assistant,
default	23:27:04.191008-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:04.205714-0400	Nexy	[0x93d68a800] invalidated after the last release of the connection object
default	23:27:04.205970-0400	Nexy	[0x93d68a800] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	23:27:04.206473-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45671.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	23:27:04.207406-0400	tccd	AUTHREQ_SUBJECT: msgID=45671.6, subject=com.nexy.assistant,
default	23:27:04.207992-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:04.216253-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	23:27:04.216365-0400	runningboardd	Invalidating assertion 398-632-449423 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	23:27:04.221273-0400	Nexy	[0x93d68a800] invalidated after the last release of the connection object
default	23:27:04.223546-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=45699.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=45699, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	23:27:04.224819-0400	tccd	AUTHREQ_SUBJECT: msgID=45699.1, subject=com.nexy.assistant,
default	23:27:04.225373-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:04.230926-0400	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	23:27:04.232498-0400	Nexy	[0x93d68a800] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	23:27:04.233863-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	23:27:04.236426-0400	Nexy	+[IMKClient subclass]: chose IMKClient_Modern
default	23:27:04.236449-0400	Nexy	+[IMKInputSession subclass]: chose IMKInputSession_Modern
default	23:27:04.237600-0400	Nexy	Start service name com.apple.spotlightknowledged
default	23:27:04.237968-0400	Nexy	[0x93d68a6c0] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	23:27:04.238147-0400	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	23:27:04.238270-0400	Nexy	[GMS] availability notification token 89
default	23:27:04.238544-0400	Nexy	[0x93d688a00] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	23:27:04.238878-0400	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	23:27:04.239664-0400	Nexy	[0x93d68abc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	23:27:04.240901-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6086, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=45699, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:27:04.241916-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6086, subject=com.nexy.assistant,
default	23:27:04.242506-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	23:27:04.253353-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=44004.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=44004, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	23:27:04.253386-0400	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=44004, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:04.254316-0400	tccd	AUTHREQ_SUBJECT: msgID=44004.4, subject=com.nexy.assistant,
default	23:27:04.254982-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:04.281521-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	23:27:04.299388-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 45029: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 574e0d00 };
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
default	23:27:04.307431-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6087, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:27:04.307465-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:04.308386-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6087, subject=com.nexy.assistant,
default	23:27:04.308993-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	23:27:04.311074-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:04.322169-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:04.322179-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:04.322187-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:04.322206-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:04.324799-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:04.325180-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:04.325546-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:04.332030-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	23:27:04.336098-0400	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x99b99b (Nexy) mainConnectionID: EFC1B;
} for reason: deferringPolicyEvaluationSuppression
default	23:27:04.336155-0400	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x99b99b (Nexy) -> <pid: 45671>
default	23:27:04.336236-0400	WindowServer	new deferring rules for pid:393: [
    [393-5EA8]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EA7]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EA6]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:04.336266-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-5EA8]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EA7]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EA6]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:04.336724-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x99b99b; pid: 393>,
    <pid: 45671>
]
default	23:27:04.348623-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:04.348684-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	23:27:04.348716-0400	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	23:27:04.352685-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:04.352699-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:04.352713-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:04.352719-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:04.352725-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:04.352731-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:04.352814-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:04.483481-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "AppDrawing" ID:398-393-449427 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:27:04.483601-0400	runningboardd	Assertion 398-393-449427 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:04.483990-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:04.484004-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:04.484014-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:04.484033-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:04.487471-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:04.488228-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:04.488379-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:04.512337-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x93dfd8040) Selecting device 71 from constructor
default	23:27:04.512365-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd8040)
default	23:27:04.512372-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd8040) not already running
default	23:27:04.512376-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x93dfd8040) nothing to teardown
default	23:27:04.512381-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd8040) connecting device 71
default	23:27:04.512574-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd8040) Device ID: 71 (Input:No | Output:Yes): true
default	23:27:04.512732-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd8040) created ioproc 0xb for device 71
default	23:27:04.512885-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd8040) adding 7 device listeners to device 71
default	23:27:04.513098-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd8040) adding 0 device delegate listeners to device 71
default	23:27:04.513107-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd8040)
default	23:27:04.513175-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:04.513183-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:27:04.513186-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:04.513194-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:27:04.513202-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:04.513313-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:04.513323-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:04.513328-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:04.513331-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd8040) removing 0 device listeners from device 0
default	23:27:04.513338-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd8040) removing 0 device delegate listeners from device 0
default	23:27:04.513343-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd8040)
default	23:27:04.513360-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x93dfd8040) caller requesting device change from 71 to 71
default	23:27:04.513365-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd8040)
default	23:27:04.513398-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x93dfd8040) exiting with nothing to do
default	23:27:04.513868-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	23:27:04.514120-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	23:27:04.516077-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x93dfd8040) Selecting device 0 from destructor
default	23:27:04.516084-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd8040)
default	23:27:04.516089-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd8040) not already running
default	23:27:04.516094-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd8040) disconnecting device 71
default	23:27:04.516098-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd8040) destroying ioproc 0xb for device 71
default	23:27:04.516129-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xb}
default	23:27:04.516182-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:04.516299-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x93dfd8040) nothing to setup
default	23:27:04.516310-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd8040) adding 0 device listeners to device 0
default	23:27:04.516319-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd8040) adding 0 device delegate listeners to device 0
default	23:27:04.516324-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd8040) removing 7 device listeners from device 71
default	23:27:04.516527-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd8040) removing 0 device delegate listeners from device 71
default	23:27:04.516544-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd8040)
default	23:27:04.517188-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x93dfd8040) Selecting device 71 from constructor
default	23:27:04.517198-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd8040)
default	23:27:04.517201-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd8040) not already running
default	23:27:04.517206-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x93dfd8040) nothing to teardown
default	23:27:04.517210-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd8040) connecting device 71
default	23:27:04.517285-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd8040) Device ID: 71 (Input:No | Output:Yes): true
default	23:27:04.517383-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd8040) created ioproc 0xc for device 71
default	23:27:04.517529-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd8040) adding 7 device listeners to device 71
default	23:27:04.517733-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd8040) adding 0 device delegate listeners to device 71
default	23:27:04.517741-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd8040)
default	23:27:04.517819-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:04.517827-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:27:04.517832-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:04.517838-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:27:04.517846-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:04.517950-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:04.517960-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:04.517965-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:04.517971-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd8040) removing 0 device listeners from device 0
default	23:27:04.517975-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd8040) removing 0 device delegate listeners from device 0
default	23:27:04.517978-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd8040)
default	23:27:04.517986-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x93dfd8040) caller requesting device change from 71 to 71
default	23:27:04.517991-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd8040)
default	23:27:04.518002-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x93dfd8040) exiting with nothing to do
default	23:27:04.518049-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	23:27:04.518378-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	23:27:04.518683-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	23:27:04.520247-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-45671-449428 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	23:27:04.520366-0400	runningboardd	Assertion 398-45671-449428 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:04.521516-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:04.521528-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:04.521548-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:04.521629-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:04.521861-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449429 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:27:04.521923-0400	runningboardd	Assertion 398-334-449429 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:04.525954-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:04.526464-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:04.526474-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:04.526484-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:04.526525-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:04.531718-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:04.548583-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0xc}
default	23:27:04.549452-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	23:27:04.549565-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:04.549602-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:27:04.549638-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:04.549690-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'MediaPlayback'
default	23:27:04.549747-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:04.549752-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	23:27:04.549794-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 174 starting playing
default	23:27:04.549881-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:04.549916-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:27:04.549940-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:04.549942-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:04.549962-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	23:27:04.549992-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:04.550091-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	23:27:04.550009-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	23:27:04.550101-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:04.550028-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: false }, 
]
default	23:27:04.550297-0400	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	23:27:04.550509-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:04.550585-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:04.550611-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:04.550623-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	23:27:04.550631-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	23:27:04.550642-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	23:27:04.550669-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:04.560982-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:04.561012-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:04.561219-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:04.561386-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:04.561708-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:04.561845-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:04.592587-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:04.592849-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:05.152214-0400	kernel	udp connect: [<IPv4-redacted>:56802<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2297049 so_state: 0x0002 process: Nexy:45671 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xb944b75e
default	23:27:05.152251-0400	kernel	udp_connection_summary [<IPv4-redacted>:56802<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2297049 so_state: 0x0002 process: Nexy:45671 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xb944b75e flowctl: 0us (0x)
default	23:27:05.869111-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:05.869190-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:05.869251-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:05.869335-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:06.018657-0400	runningboardd	Invalidating assertion 398-632-449420 (target:app<application.com.nexy.assistant.18914053.18914413(501)>) from originator [osservice<com.apple.controlcenter(501)>:632]
default	23:27:06.125093-0400	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.18914053.18914413(501)>
default	23:27:06.126012-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:06.126029-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:06.126043-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:06.126112-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:06.129390-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:06.134390-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:06.135833-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:06.171968-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:06.172014-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:06.172039-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:06.172059-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:06.172219-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:06.172280-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:06.501159-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	23:27:07.549595-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:07.549670-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:07.549727-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:07.549808-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:07.862865-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:07.862937-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:07.862962-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:07.863099-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:07.863281-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:07.863388-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:08.861493-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:08.861552-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:08.864602-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:08.864697-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:08.870616-0400	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x99b99b (Nexy) mainConnectionID: EFC1B;
} for reason: deferringPolicyEvaluationSuppression
default	23:27:08.870698-0400	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x99b99b (Nexy) -> <pid: 45671>
default	23:27:08.870805-0400	WindowServer	new deferring rules for pid:393: [
    [393-5EAB]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EAA]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EA9]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:08.870862-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-5EAB]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EAA]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EA9]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:08.872222-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x99b99b; pid: 393>,
    <pid: 45671>
]
default	23:27:08.873811-0400	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=0
default	23:27:08.878528-0400	runningboardd	Assertion did invalidate due to timeout: 398-363-449419 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671])
default	23:27:08.888839-0400	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x99b99b (Nexy) mainConnectionID: EFC1B;
} for reason: deferringPolicyEvaluationSuppression
default	23:27:08.888916-0400	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x99b99b (Nexy) -> <pid: 45671>
default	23:27:08.889033-0400	WindowServer	new deferring rules for pid:393: [
    [393-5EAE]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EAD]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EAC]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:08.889070-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-5EAE]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EAD]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EAC]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:08.890274-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x99b99b; pid: 393>,
    <pid: 45671>
]
default	23:27:08.912239-0400	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x99b99b (Nexy) mainConnectionID: EFC1B;
} for reason: deferringPolicyEvaluationSuppression
default	23:27:08.912333-0400	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x99b99b (Nexy) -> <pid: 45671>
default	23:27:08.912539-0400	WindowServer	new deferring rules for pid:393: [
    [393-5EB1]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EB0]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EAF]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:08.912605-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-5EB1]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EB0]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EAF]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:08.914038-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x99b99b; pid: 393>,
    <pid: 45671>
]
default	23:27:08.929018-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:08.978972-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:08.978986-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:08.978996-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:08.979021-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:09.506011-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	23:27:12.506783-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	23:27:14.417587-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:14.417610-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:14.417645-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:14.417680-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:14.417706-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:14.417735-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:14.417958-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:14.651213-0400	tccd	AUTHREQ_SUBJECT: msgID=45707.1, subject=com.nexy.assistant,
default	23:27:14.668356-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	23:27:14.704708-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	23:27:14.762546-0400	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x99b99b (Nexy) mainConnectionID: EFC1B;
} for reason: deferringPolicyEvaluationSuppression
default	23:27:14.762639-0400	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x99b99b (Nexy) -> <pid: 45671>
default	23:27:14.762763-0400	WindowServer	new deferring rules for pid:393: [
    [393-5EB4]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EB3]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EB2]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:14.762808-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-5EB4]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EB3]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EB2]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:15.492647-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	23:27:18.486289-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	23:27:21.492465-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	23:27:21.791701-0400	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	23:27:22.400111-0400	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	23:27:27.812947-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xc}
default	23:27:27.813451-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:27:27.813550-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 174 stopping playing
default	23:27:27.813611-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:27:27.813648-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:27.813707-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:27.813800-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:27.813818-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: false }, 
]
default	23:27:27.813889-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:27:27.813898-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:27.813986-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:27.814047-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:27.814069-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	23:27:27.852298-0400	runningboardd	Invalidating assertion 398-45671-449428 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:27.852421-0400	runningboardd	Invalidating assertion 398-334-449429 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.powerd>:334]
default	23:27:27.959400-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:27.959428-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:27.959451-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:27.959496-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:27.964344-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	23:27:27.964976-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:27.965204-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:30.526768-0400	WindowServer	e7227[ReleaseKeyFocusWithID]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x99b99b (Nexy) mainConnectionID: EFC1B;
} for reason: key thief updated 0
default	23:27:30.526854-0400	WindowServer	e7227[ReleaseKeyFocusWithID]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x99b99b (Nexy) -> <pid: 45671>
default	23:27:30.526954-0400	WindowServer	new deferring rules for pid:393: [
    [393-5EBB]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EBA]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EB9]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:30.526992-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-5EBB]; <keyboardFocus; Nexy:0x0-0x99b99b>; () -> <pid: 45671>; reason: frontmost PSN --> outbound target,
    [393-5EBA]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x99b99b; pid: 393>; reason: frontmost PSN,
    [393-5EB9]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	23:27:30.527565-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x99b99b; pid: 393>,
    <pid: 45671>
]
default	23:27:34.832942-0400	runningboardd	Invalidating assertion 398-363-449418 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	23:27:34.838526-0400	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	23:27:34.934171-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:34.934187-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:34.934226-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Set darwin role to: UserInteractive
default	23:27:34.934242-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:34.934278-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:34.937020-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:34.937386-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:34.937463-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:36.270071-0400	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:36.270087-0400	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xaf8cfca80; app<application.com.nexy.assistant.18914053.18914413>:45671(vD4E14)>
default	23:27:36.270143-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Registered new scene: <FBWorkspaceScene: 0xaf5086e80; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]> (fromRemnant = 0)
default	23:27:36.270251-0400	ControlCenter	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]] Client process connected: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:36.270585-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-449475 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	23:27:36.270694-0400	runningboardd	Assertion 398-632-449475 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:36.270783-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	23:27:36.271063-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:36.271105-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:36.271131-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:36.271207-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:36.275645-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:36.274607-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:36.275027-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:36.275718-0400	Nexy	Requesting scene <FBSScene: 0x93a859e00; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	23:27:36.275990-0400	Nexy	Request for <FBSScene: 0x93a859e00; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView> complete!
default	23:27:36.276582-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:36.276721-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	23:27:36.276740-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	23:27:36.278204-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	23:27:36.278235-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	23:27:36.278816-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:36.280369-0400	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:36.280380-0400	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xaf8cfca80; app<application.com.nexy.assistant.18914053.18914413>:45671(vD4E14)>
default	23:27:36.280433-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Registered new scene: <FBWorkspaceScene: 0xaf50879c0; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	23:27:36.280611-0400	ControlCenter	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:36.280643-0400	Nexy	Request for <FBSScene: 0x93a859e00; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView> complete!
default	23:27:36.281331-0400	Nexy	<FBSWorkspaceScenesClient:0x93c642760 <private>> Reconnecting scene com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView
default	23:27:36.281564-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:36.282443-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:36.283684-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	23:27:36.283915-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	23:27:36.285049-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:36.287172-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	23:27:36.293071-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:36.399143-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	23:27:36.399250-0400	runningboardd	Invalidating assertion 398-632-449475 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	23:27:36.409655-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:36.409666-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:36.409674-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:36.409725-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:36.412755-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:36.415153-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:36.415865-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:36.465055-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Unregistering scene: <FBWorkspaceScene: 0xaf50879c0; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView>
default	23:27:36.465449-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (FG-Active[90])" ID:398-632-449480 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Resume" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-ForegroundSupport" sourceEnvironment:"(null)">
	]>
default	23:27:36.465581-0400	runningboardd	Assertion 398-632-449480 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:36.465847-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Unregistering scene: <FBWorkspaceScene: 0xaf5086e80; com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]>
default	23:27:36.467294-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:36.467382-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:36.467468-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:36.467591-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:36.471065-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:36.471259-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace state did change: XX-None[0] --> FG-Active[90] (assertion acquired).
error	23:27:36.471560-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]-Aux[1]-NSStatusItemView] No matching scene to invalidate for this identity.
error	23:27:36.471710-0400	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	23:27:36.471818-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292-Replicant[1]] Sending action(s): NSStatusItemClearAutosaveStateAction
error	23:27:36.472974-0400	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	23:27:36.473278-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace state did change: FG-Active[90] --> XX-None[0] (assertion dropped).
default	23:27:36.473378-0400	runningboardd	Invalidating assertion 398-632-449480 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	23:27:36.497787-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-449481 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	23:27:36.497939-0400	runningboardd	Assertion 398-632-449481 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:36.498055-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	23:27:36.498311-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:36.498326-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:36.498337-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:36.498411-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:36.501869-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:36.516696-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:36.517148-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:36.581707-0400	suggestd	SGDSpotlightReceiver: deleting 1 unique identifiers (1 after de-duplication) for com.nexy.assistant: <private>
default	23:27:36.603194-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	23:27:36.603328-0400	runningboardd	Invalidating assertion 398-632-449481 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	23:27:36.610940-0400	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.18914053.18914413(501)>
default	23:27:36.615262-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:36.615274-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:36.615284-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:36.615300-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:36.619015-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:36.619398-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:36.619570-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:37.907423-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-449492 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	23:27:37.907552-0400	runningboardd	Assertion 398-632-449492 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:37.908684-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:37.908827-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:37.908878-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:37.909046-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:37.907692-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	23:27:37.912211-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:37.912705-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:37.913470-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:38.010238-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	23:27:38.010338-0400	runningboardd	Invalidating assertion 398-632-449492 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	23:27:38.113380-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:38.113401-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:38.113434-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:38.113554-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:38.118820-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:38.119118-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:38.119834-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:38.303587-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:50.323594-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=46073.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=46073, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	23:27:50.326934-0400	tccd	AUTHREQ_SUBJECT: msgID=46073.1, subject=com.nexy.assistant,
default	23:27:50.327924-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:50.354480-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6103, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=46073, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:27:50.355768-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6103, subject=com.nexy.assistant,
default	23:27:50.356549-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:50.424618-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:50.446877-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 45029: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 23510d00 };
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
default	23:27:50.460808-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:51.132322-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x93dfd9540) Selecting device 71 from constructor
default	23:27:51.132360-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:51.132379-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:51.132392-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x93dfd9540) nothing to teardown
default	23:27:51.132404-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 71
default	23:27:51.132647-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 71 (Input:No | Output:Yes): true
default	23:27:51.132929-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0xd for device 71
default	23:27:51.133218-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 71
default	23:27:51.133733-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 71
default	23:27:51.133759-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:51.133979-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:51.134004-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:27:51.134021-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:51.134042-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:27:51.134063-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:51.134332-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:51.134358-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:51.134387-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:51.134409-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device listeners from device 0
default	23:27:51.134422-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 0
default	23:27:51.134433-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:51.134469-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	23:27:51.134602-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x93dfd9540) caller requesting device change from 71 to 78
default	23:27:51.134633-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:51.134649-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:51.134661-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 71
default	23:27:51.134675-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0xd for device 71
default	23:27:51.134727-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xd}
default	23:27:51.134805-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:51.135004-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 78
default	23:27:51.135221-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 78 (Input:Yes | Output:No): true
default	23:27:51.138001-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3693, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:51.139971-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3693, subject=com.nexy.assistant,
default	23:27:51.140980-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:51.159135-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0xb for device 78
default	23:27:51.159310-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 78
default	23:27:51.159502-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 78
default	23:27:51.159514-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:51.159524-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	23:27:51.159535-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:51.159683-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	23:27:51.159691-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	23:27:51.159698-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	23:27:51.159802-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:51.159816-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:51.159821-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:51.159826-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 71
default	23:27:51.159980-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 71
default	23:27:51.159986-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:51.160335-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:51.161639-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3694, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:51.162681-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3694, subject=com.nexy.assistant,
default	23:27:51.163286-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:51.176377-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:51.177349-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3695, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:51.178148-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3695, subject=com.nexy.assistant,
default	23:27:51.178765-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:51.191623-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x93dfd9540) Selecting device 0 from destructor
default	23:27:51.191632-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:51.191639-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:51.191643-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 78
default	23:27:51.191649-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0xb for device 78
default	23:27:51.191673-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	23:27:51.191704-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:51.191796-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x93dfd9540) nothing to setup
default	23:27:51.191806-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device listeners to device 0
default	23:27:51.191812-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 0
default	23:27:51.191818-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 78
default	23:27:51.191972-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 78
default	23:27:51.191982-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:51.192950-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x93dfd9540) Selecting device 71 from constructor
default	23:27:51.192959-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:51.192964-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:51.192967-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x93dfd9540) nothing to teardown
default	23:27:51.192970-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 71
default	23:27:51.193053-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 71 (Input:No | Output:Yes): true
default	23:27:51.193142-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0xe for device 71
default	23:27:51.193243-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 71
default	23:27:51.193401-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 71
default	23:27:51.193407-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:51.193474-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:51.193484-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:27:51.193489-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:51.193495-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:27:51.193501-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:51.193587-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:51.193598-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:51.193614-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:51.193619-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device listeners from device 0
default	23:27:51.193623-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 0
default	23:27:51.193629-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:51.193640-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	23:27:51.193690-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x93dfd9540) caller requesting device change from 71 to 78
default	23:27:51.193696-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:51.193703-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:51.193707-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 71
default	23:27:51.193713-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0xe for device 71
default	23:27:51.193725-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xe}
default	23:27:51.193746-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:51.193819-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 78
default	23:27:51.193886-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 78 (Input:Yes | Output:No): true
default	23:27:51.194924-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3696, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:51.195827-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3696, subject=com.nexy.assistant,
default	23:27:51.196394-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:51.208260-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0xc for device 78
default	23:27:51.208369-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 78
default	23:27:51.208537-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 78
default	23:27:51.208544-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:51.208551-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	23:27:51.208559-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:51.208664-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	23:27:51.208673-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	23:27:51.208678-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	23:27:51.208760-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:51.208770-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:51.208775-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:51.208780-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 71
default	23:27:51.208970-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 71
default	23:27:51.208977-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:51.208986-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	23:27:51.209357-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:51.210294-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3697, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:51.211071-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3697, subject=com.nexy.assistant,
default	23:27:51.211611-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:51.224046-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:51.224996-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3698, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:51.225871-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3698, subject=com.nexy.assistant,
default	23:27:51.226500-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:51.241964-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-45671-449527 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	23:27:51.242064-0400	runningboardd	Assertion 398-45671-449527 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:51.243451-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:51.243465-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:51.243478-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:51.243520-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:51.243783-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3699, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:51.245793-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3699, subject=com.nexy.assistant,
default	23:27:51.248874-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:51.249969-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:51.250523-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:51.253071-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:51.272608-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449528 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:27:51.272682-0400	runningboardd	Assertion 398-334-449528 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:51.272958-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:51.272969-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:51.272978-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:51.273009-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:51.275501-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:51.275949-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:51.276170-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:51.298533-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xc}
default	23:27:51.313527-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:51.313605-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	23:27:51.313790-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	23:27:51.315279-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.315289-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.315303-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.315310-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.315318-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.315367-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:51.315547-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:51.318173-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.318203-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.318232-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.318254-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.318278-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.318356-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:51.318559-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:51.320816-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.320842-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.320936-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.320960-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.320990-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.321018-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:51.321228-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	23:27:51.321605-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	23:27:51.321695-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:51.321717-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:27:51.321742-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:51.321856-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	23:27:51.321893-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.321965-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:51.322060-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:51.322165-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	23:27:51.322165-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.322206-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ad, Nexy(45671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 starting recording
default	23:27:51.322370-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:51.322464-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.322511-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.322537-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.322634-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.322741-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.322782-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.322824-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	23:27:51.322851-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	23:27:51.322875-0400	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	23:27:51.322990-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:51.322432-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:27:51.322489-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:51.322593-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.324297-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	23:27:51.324608-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:51.446633-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xc}
default	23:27:51.446844-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:27:51.446933-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:51.446981-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:27:51.447007-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:51.447053-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ad, Nexy(45671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 stopping recording
default	23:27:51.447077-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:27:51.447078-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.447104-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:51.447130-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:51.447189-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.447247-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.447247-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:27:51.447288-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.447305-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:51.447263-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:51.447351-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:51.447376-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.447408-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.447423-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	23:27:51.451582-0400	runningboardd	Invalidating assertion 398-45671-449527 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:51.452007-0400	runningboardd	Invalidating assertion 398-334-449528 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.powerd>:334]
default	23:27:51.454746-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	23:27:51.455128-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.455141-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.455152-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.455180-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.455225-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.455248-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:51.455473-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:51.552540-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x93dfd9540) Selecting device 0 from destructor
default	23:27:51.552552-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:51.552561-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:51.552567-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 78
default	23:27:51.552573-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0xc for device 78
default	23:27:51.552597-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xc}
default	23:27:51.552624-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:51.552757-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x93dfd9540) nothing to setup
default	23:27:51.552772-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device listeners to device 0
default	23:27:51.552778-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 0
default	23:27:51.552784-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 78
default	23:27:51.553026-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 78
default	23:27:51.553041-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:51.554354-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x93dfd9540) Selecting device 71 from constructor
default	23:27:51.554373-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:51.554388-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:51.554394-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x93dfd9540) nothing to teardown
default	23:27:51.554399-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 71
default	23:27:51.554522-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 71 (Input:No | Output:Yes): true
default	23:27:51.554617-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0xf for device 71
default	23:27:51.554748-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 71
default	23:27:51.554964-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 71
default	23:27:51.554974-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:51.555062-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:51.555073-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:27:51.555080-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:51.555088-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:27:51.555098-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:51.555205-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:51.555217-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:51.555223-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:51.555228-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device listeners from device 0
default	23:27:51.555233-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 0
default	23:27:51.555238-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:51.555253-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	23:27:51.555311-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x93dfd9540) caller requesting device change from 71 to 78
default	23:27:51.555325-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:51.555332-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:51.555337-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 71
default	23:27:51.555341-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0xf for device 71
default	23:27:51.555367-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xf}
default	23:27:51.555417-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:51.555502-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 78
default	23:27:51.555603-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 78 (Input:Yes | Output:No): true
default	23:27:51.557020-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3700, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:51.558470-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:51.558481-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:51.558490-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:51.558532-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:51.558370-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3700, subject=com.nexy.assistant,
default	23:27:51.560048-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-45671-449529 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	23:27:51.560153-0400	runningboardd	Assertion 398-45671-449529 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:51.561810-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:51.564099-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:51.564457-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:51.564460-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449530 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:27:51.564469-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:51.564501-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:51.564505-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:51.564524-0400	runningboardd	Assertion 398-334-449530 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:51.564610-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:51.565234-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:51.570466-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:51.570907-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:51.570977-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:51.571036-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:51.571100-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:51.574337-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:51.581865-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0xd for device 78
default	23:27:51.582020-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 78
default	23:27:51.582254-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 78
default	23:27:51.582267-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:51.582277-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	23:27:51.582289-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:51.582464-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	23:27:51.582477-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	23:27:51.582483-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	23:27:51.582603-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:51.582622-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:51.582628-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:51.582634-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 71
default	23:27:51.582842-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 71
default	23:27:51.582854-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:51.582865-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	23:27:51.583287-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:51.584686-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3701, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:51.584851-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0xc}
default	23:27:51.585652-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	23:27:51.585741-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:51.585771-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:27:51.585799-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3701, subject=com.nexy.assistant,
default	23:27:51.585802-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:51.585844-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'MediaPlayback'
default	23:27:51.585864-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.585891-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	23:27:51.585902-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 174 starting playing
default	23:27:51.585954-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:51.585998-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.585983-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:27:51.586038-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.586013-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:51.586034-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	23:27:51.586077-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	23:27:51.586256-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	23:27:51.586126-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: false }, 
]
default	23:27:51.586270-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:51.586347-0400	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	23:27:51.586496-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.586582-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.586608-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.586622-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	23:27:51.586632-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	23:27:51.586648-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	23:27:51.586688-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:51.586802-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:51.603600-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:51.604774-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3702, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:51.606231-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3702, subject=com.nexy.assistant,
default	23:27:51.607207-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:51.619853-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:51.626255-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3703, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:51.627677-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3703, subject=com.nexy.assistant,
default	23:27:51.628535-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:51.667042-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:51.668366-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:51.671824-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xd}
default	23:27:51.685482-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:51.685563-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	23:27:51.685612-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	23:27:51.685791-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	23:27:51.685878-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:51.685902-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:27:51.685931-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:27:51.686011-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:51.686098-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	23:27:51.686223-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:51.686090-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.686152-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.686230-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.686273-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.686301-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:27:51.686311-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.686362-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:51.686331-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.686410-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.686383-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:51.686527-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.686460-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.686563-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.686577-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:51.686497-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.686542-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.686619-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:51.686579-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:51.686587-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.686558-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.686711-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.686666-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:27:51.686650-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:51.686739-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.686752-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:51.686794-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:51.686836-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.686860-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:51.686980-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	23:27:51.686964-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ad, Nexy(45671), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 174 starting recording
default	23:27:51.686937-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.687083-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	23:27:51.687199-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:51.687262-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:27:51.687366-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	23:27:51.687442-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:51.687776-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.687055-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.687530-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>. Old (201) and New (501) scores.
default	23:27:51.687812-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.687824-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:51.687695-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:51.687032-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:51.687954-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
)}
default	23:27:51.687968-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:51.687747-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	23:27:51.687868-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:51.687982-0400	audioaccessoryd	Routing request Wx NULL score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	23:27:51.688232-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	23:27:51.688256-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	23:27:51.688270-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 201 -> 501 count 2
default	23:27:51.688147-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	23:27:51.688278-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
error	23:27:51.688297-0400	audioaccessoryd	Updating local audio category 201 -> 501 app com.nexy.assistant
default	23:27:51.688365-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	23:27:51.687788-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:51.687741-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:51.689214-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:51.750588-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=46163.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=46163, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	23:27:51.753221-0400	tccd	AUTHREQ_SUBJECT: msgID=46163.1, subject=com.nexy.assistant,
default	23:27:51.754482-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:51.782191-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6104, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=46163, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:27:51.783660-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6104, subject=com.nexy.assistant,
default	23:27:51.784616-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:51.830629-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xc}
default	23:27:51.831841-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	23:27:51.831963-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:51.832003-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	23:27:51.832046-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	23:27:51.832082-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:51.832139-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	23:27:51.832179-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:51.832268-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	23:27:51.832282-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.832362-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:51.832537-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode Record_WithBluetooth/Default and coreSessionID = 174 stopping playing
default	23:27:51.832628-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:51.832607-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.832663-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.832555-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.832689-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 2
default	23:27:51.832707-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:27:51.832784-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:51.832701-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:51.833112-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
error	23:27:51.832974-0400	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	23:27:51.833132-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:51.833004-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.832964-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 1
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: true
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: true }, 
]
default	23:27:51.833097-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:51.833116-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.833153-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:51.833225-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.833282-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:51.833327-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.833369-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:51.833062-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:51.833497-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:51.843466-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:51.868427-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 45029: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 c7510d00 };
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
default	23:27:51.874782-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 2
default	23:27:51.889385-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:52.322838-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	23:27:52.322947-0400	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	23:27:52.326073-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=44004.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=44004, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	23:27:52.326149-0400	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=44004, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:52.328788-0400	tccd	AUTHREQ_SUBJECT: msgID=44004.5, subject=com.nexy.assistant,
default	23:27:52.330369-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:52.367100-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	23:27:52.386816-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:52.391267-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:52.391361-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant), [scr] Nexy (com.nexy.assistant)]
default	23:27:52.391401-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	23:27:52.393013-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.393035-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.393049-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:52.393057-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.393066-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:52.393074-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:52.393120-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.393155-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.393186-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:52.393193-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.393204-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:52.393220-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:52.393311-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.393327-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:52.393335-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.393363-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:52.393372-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.393393-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:52.393400-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:52.425000-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	23:27:52.429454-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:27:52.429198-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xd}
default	23:27:52.429541-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:52.429579-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:27:52.429930-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:52.429374-0400	runningboardd	Invalidating assertion 398-45671-449529 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:52.430233-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:52.430269-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:52.430074-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ad, Nexy(45671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 stopping recording
default	23:27:52.430282-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:52.430092-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:52.430125-0400	runningboardd	Invalidating assertion 398-334-449530 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.powerd>:334]
default	23:27:52.430134-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:27:52.430320-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:52.430222-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:52.430325-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:52.430512-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:27:52.430522-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:52.430615-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:52.430649-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:52.430670-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	23:27:52.430516-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:52.439132-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:52.439201-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	23:27:52.439248-0400	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	23:27:52.439264-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	23:27:52.439791-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.439804-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.439815-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:52.439821-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:52.439829-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:52.439836-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:52.439994-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:52.536075-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x93dfd9540) Selecting device 0 from destructor
default	23:27:52.536089-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:52.536097-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:52.536102-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 78
default	23:27:52.536108-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0xd for device 78
default	23:27:52.536133-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xd}
default	23:27:52.536161-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:52.536294-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x93dfd9540) nothing to setup
default	23:27:52.536309-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device listeners to device 0
default	23:27:52.536317-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 0
default	23:27:52.536324-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 78
default	23:27:52.536554-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 78
default	23:27:52.536570-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:52.601408-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:52.601425-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:52.601440-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:52.601464-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:52.607033-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:52.607551-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:52.607947-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:52.692420-0400	Nexy	nw_path_libinfo_path_check [BDF3E37D-A7E2-45BE-9EE0-8B80061C0AA9 Hostname#d680ec43:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	23:27:52.692558-0400	mDNSResponder	[R279575] DNSServiceCreateConnection START PID[45671](Nexy)
default	23:27:52.692632-0400	mDNSResponder	[R279576] DNSServiceQueryRecord START -- qname: <mask.hash: 'lETfDsfMRrhKUOGbaqIqQA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 45671 (Nexy), name hash: b360ab20
default	23:27:52.693240-0400	mDNSResponder	[R279577] DNSServiceQueryRecord START -- qname: <mask.hash: 'lETfDsfMRrhKUOGbaqIqQA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 45671 (Nexy), name hash: b360ab20
default	23:27:52.717458-0400	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 791D66A7-B8F2-44D8-87C4-7B9BC9E49E90 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=96,src=<IPv6-redacted>.65341,dst=<IPv6-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x3d551dca tp_proto=0x06"
default	23:27:52.717511-0400	kernel	tcp connect outgoing: [<IPv6-redacted>:65341<-><IPv6-redacted>:80] interface: en0 (skipped: 871)
so_gencnt: 2298476 t_state: SYN_SENT process: Nexy:45671 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 18 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x82c18171
default	23:27:52.731268-0400	kernel	tcp connected: [<IPv6-redacted>:65341<-><IPv6-redacted>:80] interface: en0 (skipped: 871)
so_gencnt: 2298476 t_state: ESTABLISHED process: Nexy:45671 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 18 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x82c18171
default	23:27:52.987243-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv6-redacted>:65341<-><IPv6-redacted>:80] interface: en0 (skipped: 871)
so_gencnt: 2298476 t_state: FIN_WAIT_1 process: Nexy:45671 Duration: 0.270 sec Conn_Time: 0.014 sec bytes in/out: 398/13845 pkts in/out: 2/3 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 20.375 ms rttvar: 4.312 ms base rtt: 14 ms so_error: 0 svc/tc: 0 flow: 0x82c18171
default	23:27:52.987272-0400	kernel	tcp_connection_summary [<IPv6-redacted>:65341<-><IPv6-redacted>:80] interface: en0 (skipped: 871)
so_gencnt: 2298476 t_state: FIN_WAIT_1 process: Nexy:45671 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:27:52.997436-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-45671-449536 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	23:27:52.997534-0400	runningboardd	Assertion 398-45671-449536 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:53.999631-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:53.999754-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:53.999815-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:53.999667-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449537 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:27:53.999946-0400	runningboardd	Assertion 398-334-449537 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:53.999959-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:53.003859-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:53.005182-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:53.005196-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:53.005204-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:53.005223-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:53.005433-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:53.013345-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:53.013876-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:53.014075-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:53.014283-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:53.024522-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0xc}
default	23:27:53.025408-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	23:27:53.025522-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:53.025554-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:27:53.025589-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:53.025631-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'MediaPlayback'
default	23:27:53.025652-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:53.025701-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	23:27:53.025713-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 174 starting playing
default	23:27:53.025785-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:53.025851-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:53.025811-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:53.025890-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:27:53.025991-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:53.026030-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	23:27:53.026072-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	23:27:53.026097-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: false }, 
]
default	23:27:53.026173-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	23:27:53.026256-0400	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	23:27:53.026295-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:53.026407-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:53.026492-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:53.026525-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:53.026544-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	23:27:53.026554-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	23:27:53.026576-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	23:27:53.026612-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
error	23:27:53.046571-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:27:53.049379-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:53.060108-0400	coreaudiod	Sending message. { reporterID=196155451375620, category=IO, type=error, message=["multi_cycle_io_page_faults_duration": Optional(7251), "anchor_sample_time": Optional(128), "other_page_faults": Optional(0), "issue_type": Optional(overload), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_total_wakeups": Optional(11), "io_frame_counter": Optional(512), "is_recovering": Optional(0), "wg_system_time_mach": Optional(24221), "io_cycle_budget": Optional(11354166), "smallest_buffer_frame_size": Optional(512), "io_cycle": Optional(1), "io_cycle_usage": Optional(1), "reporting_latency": Optional(12506541), "io_page_faults_duration": Optional(0), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "wg_user_time_mach": Optional(24656), "output_device_transport_list": Optional(BuiltIn), "wg_cycles": Optional(4232531), "input_device_uid_list": Optional(), "start_time": Optional(4841323316452), "careporting_timestamp": 1761708473.059211, "input_device_source_list": Optional(), "is_prewarming": Optional(0), "HAL_client_IO_duration": Optional(1<…> }
default	23:27:53.135133-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=46169.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=46169, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	23:27:53.137139-0400	tccd	AUTHREQ_SUBJECT: msgID=46169.1, subject=com.nexy.assistant,
default	23:27:53.137960-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:53.162564-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6105, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=46169, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:27:53.163999-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6105, subject=com.nexy.assistant,
default	23:27:53.164855-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:53.243726-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:53.267729-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 45029: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 d7510d00 };
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
default	23:27:53.286339-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:53.409490-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xc}
default	23:27:53.409780-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:27:53.409869-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 174 stopping playing
default	23:27:53.409919-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:27:53.409959-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:53.410016-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:53.410109-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:53.410150-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: false }, 
]
default	23:27:53.410250-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:27:53.410271-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:53.410320-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:53.410267-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:53.410339-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	23:27:53.448249-0400	runningboardd	Invalidating assertion 398-45671-449536 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:53.448908-0400	runningboardd	Invalidating assertion 398-334-449537 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.powerd>:334]
default	23:27:53.512906-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:53.512938-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:53.512970-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:53.513053-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:53.516912-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:53.517375-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:53.517661-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:54.321556-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=46171.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=46171, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	23:27:54.323390-0400	tccd	AUTHREQ_SUBJECT: msgID=46171.1, subject=com.nexy.assistant,
default	23:27:54.324167-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:54.343878-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6106, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=46171, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:27:54.345125-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6106, subject=com.nexy.assistant,
default	23:27:54.345918-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:54.382230-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:54.404361-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 45029: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 dc510d00 };
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
default	23:27:54.418606-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:54.642492-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:54.642590-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	23:27:55.115324-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x93dfd9540) Selecting device 71 from constructor
default	23:27:55.115365-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:55.115381-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:55.115395-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x93dfd9540) nothing to teardown
default	23:27:55.115407-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 71
default	23:27:55.115679-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 71 (Input:No | Output:Yes): true
default	23:27:55.115959-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0x10 for device 71
default	23:27:55.116305-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 71
default	23:27:55.116933-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 71
default	23:27:55.116971-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:55.117335-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:55.117381-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:27:55.117402-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:55.117424-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:27:55.117446-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:55.117741-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:55.117768-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:55.117783-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:55.117796-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device listeners from device 0
default	23:27:55.117811-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 0
default	23:27:55.117825-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:55.117867-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	23:27:55.118031-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x93dfd9540) caller requesting device change from 71 to 78
default	23:27:55.118055-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:55.118169-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:55.118186-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 71
default	23:27:55.118218-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0x10 for device 71
default	23:27:55.118308-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0x10}
default	23:27:55.118388-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:55.118602-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 78
default	23:27:55.118828-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 78 (Input:Yes | Output:No): true
default	23:27:55.121773-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3704, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.123927-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3704, subject=com.nexy.assistant,
default	23:27:55.125423-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.145427-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0xe for device 78
default	23:27:55.145638-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 78
default	23:27:55.145905-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 78
default	23:27:55.145916-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:55.145927-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	23:27:55.145941-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:55.146145-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	23:27:55.146158-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	23:27:55.146166-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	23:27:55.146313-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:55.146327-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:55.146337-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:55.146343-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 71
default	23:27:55.146578-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 71
default	23:27:55.146588-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:55.146605-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	23:27:55.146961-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:55.148379-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3705, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.149528-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3705, subject=com.nexy.assistant,
default	23:27:55.150199-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.163746-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:55.164668-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3706, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.165421-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3706, subject=com.nexy.assistant,
default	23:27:55.165956-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.178772-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x93dfd9540) Selecting device 0 from destructor
default	23:27:55.178781-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:55.178786-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:55.178790-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 78
default	23:27:55.178795-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0xe for device 78
default	23:27:55.178821-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xe}
default	23:27:55.178848-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:55.178947-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x93dfd9540) nothing to setup
default	23:27:55.178961-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device listeners to device 0
default	23:27:55.178966-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 0
default	23:27:55.178975-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 78
default	23:27:55.179162-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 78
default	23:27:55.179172-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:55.180047-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x93dfd9540) Selecting device 71 from constructor
default	23:27:55.180058-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:55.180064-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:55.180071-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x93dfd9540) nothing to teardown
default	23:27:55.180074-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 71
default	23:27:55.180166-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 71 (Input:No | Output:Yes): true
default	23:27:55.180253-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0x11 for device 71
default	23:27:55.180362-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 71
default	23:27:55.180517-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 71
default	23:27:55.180526-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:55.180593-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:55.180603-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:27:55.180608-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:55.180614-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:27:55.180623-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:55.180721-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:55.180732-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:55.180737-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:55.180742-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device listeners from device 0
default	23:27:55.180753-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 0
default	23:27:55.180757-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:55.180771-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	23:27:55.180816-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x93dfd9540) caller requesting device change from 71 to 78
default	23:27:55.180824-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:55.180830-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:55.180834-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 71
default	23:27:55.180838-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0x11 for device 71
default	23:27:55.180850-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0x11}
default	23:27:55.180871-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:55.180953-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 78
default	23:27:55.181034-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 78 (Input:Yes | Output:No): true
default	23:27:55.182111-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3707, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.182997-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3707, subject=com.nexy.assistant,
default	23:27:55.183592-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.196235-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0xf for device 78
default	23:27:55.196384-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 78
default	23:27:55.196660-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 78
default	23:27:55.196671-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:55.196680-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	23:27:55.196690-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:55.196835-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	23:27:55.196845-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	23:27:55.196850-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	23:27:55.196954-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:55.196970-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:55.196976-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:55.196980-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 71
default	23:27:55.197159-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 71
default	23:27:55.197165-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:55.197175-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	23:27:55.197566-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:55.198754-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3708, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.199986-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3708, subject=com.nexy.assistant,
default	23:27:55.200639-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.213651-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:55.214745-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3709, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.215657-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3709, subject=com.nexy.assistant,
default	23:27:55.216232-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.229059-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:55.230020-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3710, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.230858-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3710, subject=com.nexy.assistant,
default	23:27:55.231414-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.248143-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-45671-449549 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	23:27:55.248208-0400	runningboardd	Assertion 398-45671-449549 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:55.248548-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:55.248563-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:55.248577-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:55.248625-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:55.248872-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3711, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.249754-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3711, subject=com.nexy.assistant,
default	23:27:55.251267-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.252695-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:55.253134-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:55.253385-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:55.264955-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449550 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:27:55.265018-0400	runningboardd	Assertion 398-334-449550 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:55.265280-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:55.265291-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:55.265300-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:55.265320-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:55.267775-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:55.268498-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:55.268835-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:55.289588-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xf}
default	23:27:55.297275-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	23:27:55.297353-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:55.297374-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:27:55.297399-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:55.297501-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	23:27:55.297581-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.297651-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:55.297722-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:55.297836-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	23:27:55.297832-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.297735-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.297863-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ad, Nexy(45671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 starting recording
default	23:27:55.297776-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.298023-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:55.297954-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.297971-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.298382-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.298408-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.298422-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	23:27:55.298125-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:27:55.298446-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	23:27:55.298480-0400	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	23:27:55.298926-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	23:27:55.298194-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:55.298942-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:55.298553-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:55.298289-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.309432-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:55.313579-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:55.313646-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	23:27:55.313690-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	23:27:55.314934-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.314954-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.315006-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.315073-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.315083-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.315092-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:55.315104-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.315113-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.315119-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.315124-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.315138-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.315150-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:55.315186-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.315217-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.315283-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	23:27:55.315247-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.315325-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.315336-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.315342-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:55.315381-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:55.417835-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xf}
default	23:27:55.418040-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:27:55.418132-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:55.418174-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:27:55.418198-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:55.418248-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ad, Nexy(45671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 stopping recording
default	23:27:55.418270-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.418273-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:27:55.418302-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:55.418342-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:55.418409-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.418396-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.418450-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.418469-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:27:55.418490-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:55.418488-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:55.418538-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.418598-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:55.418612-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.418623-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	23:27:55.422780-0400	runningboardd	Invalidating assertion 398-45671-449549 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:55.423872-0400	runningboardd	Invalidating assertion 398-334-449550 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.powerd>:334]
default	23:27:55.432219-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:55.432292-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	23:27:55.432341-0400	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	23:27:55.432359-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	23:27:55.432918-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.432929-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.432940-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.432948-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.432955-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.432964-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:55.433051-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:55.452120-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:55.452136-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:55.452161-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:55.452215-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:55.455368-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:55.458674-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:55.459007-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:55.523962-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x93dfd9540) Selecting device 0 from destructor
default	23:27:55.523983-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:55.523993-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:55.523998-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 78
default	23:27:55.524005-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0xf for device 78
default	23:27:55.524041-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xf}
default	23:27:55.524080-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:55.524276-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x93dfd9540) nothing to setup
default	23:27:55.524288-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device listeners to device 0
default	23:27:55.524296-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 0
default	23:27:55.524302-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 78
default	23:27:55.524545-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 78
default	23:27:55.524561-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:55.526344-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x93dfd9540) Selecting device 71 from constructor
default	23:27:55.526360-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:55.526372-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:55.526379-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x93dfd9540) nothing to teardown
default	23:27:55.526384-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 71
default	23:27:55.526521-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 71 (Input:No | Output:Yes): true
default	23:27:55.526637-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0x12 for device 71
default	23:27:55.526768-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 71
default	23:27:55.526987-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 71
default	23:27:55.527002-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:55.527115-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:55.527127-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:27:55.527134-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:27:55.527143-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:27:55.527153-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:55.527267-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:55.527282-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:55.527290-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:55.527297-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device listeners from device 0
default	23:27:55.527301-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 0
default	23:27:55.527306-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:55.527324-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	23:27:55.527395-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x93dfd9540) caller requesting device change from 71 to 78
default	23:27:55.527421-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:55.527431-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:55.527437-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 71
default	23:27:55.527442-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0x12 for device 71
default	23:27:55.527471-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0x12}
default	23:27:55.527523-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:55.527632-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd9540) connecting device 78
default	23:27:55.527746-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd9540) Device ID: 78 (Input:Yes | Output:No): true
default	23:27:55.529800-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3712, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.531663-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-45671-449551 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	23:27:55.531779-0400	runningboardd	Assertion 398-45671-449551 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:55.533503-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:55.533520-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449552 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:27:55.533660-0400	runningboardd	Assertion 398-334-449552 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:55.533576-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:55.534018-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:55.534120-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:55.535084-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3712, subject=com.nexy.assistant,
default	23:27:55.536473-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.538085-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:55.538429-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:55.538440-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:55.538450-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:55.538477-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:55.545780-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:55.555788-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd9540) created ioproc 0x10 for device 78
default	23:27:55.555964-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 7 device listeners to device 78
default	23:27:55.556201-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 78
default	23:27:55.556211-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd9540)
default	23:27:55.556224-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	23:27:55.556238-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:27:55.556423-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	23:27:55.556436-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	23:27:55.556443-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	23:27:55.556567-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:27:55.556588-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:27:55.556595-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:27:55.556601-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 71
default	23:27:55.556807-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 71
default	23:27:55.556819-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:55.556834-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	23:27:55.557414-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0xc}
default	23:27:55.557588-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:55.558444-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	23:27:55.558563-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:55.558599-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:27:55.558645-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:55.558691-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'MediaPlayback'
default	23:27:55.558720-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.558743-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	23:27:55.558773-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 174 starting playing
default	23:27:55.558882-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.558928-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.558887-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:55.558921-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:27:55.558943-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:55.559020-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	23:27:55.559051-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	23:27:55.559138-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: false }, 
]
default	23:27:55.559339-0400	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	23:27:55.559226-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	23:27:55.559257-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:55.559499-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.559581-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.559609-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.559628-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	23:27:55.559638-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	23:27:55.559659-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	23:27:55.559700-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:55.559732-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3713, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.561167-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3713, subject=com.nexy.assistant,
default	23:27:55.561902-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.562046-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:55.562263-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	23:27:55.562315-0400	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	23:27:55.562352-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:55.564368-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=44004.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=44004, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	23:27:55.564397-0400	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=44004, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:55.565589-0400	tccd	AUTHREQ_SUBJECT: msgID=44004.6, subject=com.nexy.assistant,
default	23:27:55.566474-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:55.574940-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:55.576077-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:55.577131-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3714, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.577931-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3714, subject=com.nexy.assistant,
default	23:27:55.578500-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.591747-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	23:27:55.592761-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3715, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.593599-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3715, subject=com.nexy.assistant,
default	23:27:55.593637-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	23:27:55.594152-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.607399-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3716, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	23:27:55.608167-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3716, subject=com.nexy.assistant,
default	23:27:55.608704-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	23:27:55.640023-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=46172.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=46172, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	23:27:55.641273-0400	tccd	AUTHREQ_SUBJECT: msgID=46172.1, subject=com.nexy.assistant,
default	23:27:55.641829-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:55.645703-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0x10}
default	23:27:55.646707-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	23:27:55.646771-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:55.646792-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:27:55.646819-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:27:55.646840-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:55.646884-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	23:27:55.646909-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:55.646910-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.646939-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:27:55.646965-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:55.647017-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.647023-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:55.647023-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.647056-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.647051-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:27:55.647068-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:55.647073-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:55.647114-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ad, Nexy(45671), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 174 starting recording
default	23:27:55.647104-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.647129-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.647130-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:55.647144-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.647157-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	23:27:55.647151-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:55.647178-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:55.647191-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:27:55.647176-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:55.647212-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.647211-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	23:27:55.647229-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:55.647238-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	23:27:55.647236-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:55.647272-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:27:55.647254-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>. Old (201) and New (501) scores.
default	23:27:55.647300-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	23:27:55.647329-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
)}
default	23:27:55.647340-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:55.647439-0400	audioaccessoryd	Routing request Wx NULL score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	23:27:55.647574-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	23:27:55.647649-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	23:27:55.647674-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	23:27:55.647685-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 201 -> 501 count 2
default	23:27:55.647695-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
error	23:27:55.647710-0400	audioaccessoryd	Updating local audio category 201 -> 501 app com.nexy.assistant
default	23:27:55.647735-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	23:27:55.652601-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:55.655519-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6107, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=46172, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:27:55.655987-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:55.656055-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	23:27:55.656102-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	23:27:55.656380-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6107, subject=com.nexy.assistant,
default	23:27:55.656538-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.656553-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.656564-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.656573-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.656580-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.656589-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:55.656603-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.656665-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.656706-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.656788-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	23:27:55.656750-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.656819-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.656863-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:55.656932-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.657102-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:55.656970-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.657131-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.657180-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:55.657222-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:55.657316-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:55.657341-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:55.687645-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:55.705547-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 45029: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 de510d00 };
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
default	23:27:55.716020-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:55.803467-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xc}
default	23:27:55.804596-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	23:27:55.804682-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:55.804706-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	23:27:55.804732-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	23:27:55.804761-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:55.804811-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	23:27:55.804877-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:55.804887-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.804941-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	23:27:55.804969-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:55.805011-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.805026-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode Record_WithBluetooth/Default and coreSessionID = 174 stopping playing
default	23:27:55.805038-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.805053-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:55.805079-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:27:55.805100-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:55.805087-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.805126-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.805155-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 2
default	23:27:55.805171-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	23:27:55.805193-0400	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	23:27:55.805160-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.805181-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 1
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: true
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: true }, 
]
default	23:27:55.805238-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:55.805258-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.805263-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	23:27:55.805270-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:55.805280-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:55.805313-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:55.805330-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.805352-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:55.805366-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:55.805399-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:56.896068-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:56.896219-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:56.896301-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:56.896369-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:56.961436-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	23:27:56.961515-0400	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	23:27:56.964564-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=44004.7, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=44004, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	23:27:56.964607-0400	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=44004, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:56.966790-0400	tccd	AUTHREQ_SUBJECT: msgID=44004.7, subject=com.nexy.assistant,
default	23:27:56.967958-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:57.008723-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	23:27:57.130315-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	23:27:57.136049-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:27:57.136152-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:57.136199-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	23:27:57.136286-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:57.136451-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0ad, Nexy(45671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 stopping recording
default	23:27:57.136507-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:27:57.135684-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0x10}
default	23:27:57.136573-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:57.136574-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:57.136775-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:57.136657-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:57.136820-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	23:27:57.136356-0400	runningboardd	Invalidating assertion 398-45671-449551 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:27:57.136835-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	23:27:57.136914-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:57.136879-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	23:27:57.136910-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:27:57.136610-0400	runningboardd	Invalidating assertion 398-334-449552 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.powerd>:334]
default	23:27:57.137022-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:57.136920-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:57.137043-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:57.137053-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	23:27:57.147953-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:27:57.148046-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	23:27:57.148108-0400	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	23:27:57.148127-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	23:27:57.150572-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:57.150589-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:57.150604-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:57.150610-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:27:57.150618-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:27:57.150624-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:27:57.150799-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:27:57.242480-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x93dfd9540) Selecting device 0 from destructor
default	23:27:57.242491-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd9540)
default	23:27:57.242500-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd9540) not already running
default	23:27:57.242505-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd9540) disconnecting device 78
default	23:27:57.242511-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd9540) destroying ioproc 0x10 for device 78
default	23:27:57.242533-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0x10}
default	23:27:57.242559-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:27:57.242690-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x93dfd9540) nothing to setup
default	23:27:57.242702-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device listeners to device 0
default	23:27:57.242710-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd9540) adding 0 device delegate listeners to device 0
default	23:27:57.242714-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 7 device listeners from device 78
default	23:27:57.242918-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd9540) removing 0 device delegate listeners from device 78
default	23:27:57.242932-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd9540)
default	23:27:57.243539-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:57.243551-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:57.243561-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:57.243587-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:57.246092-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:57.246427-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:57.246541-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:57.268580-0400	Nexy	nw_path_libinfo_path_check [301B54E8-0401-472E-9396-4FE7AFFC27F4 Hostname#d680ec43:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	23:27:57.268677-0400	mDNSResponder	[R279620] DNSServiceQueryRecord START -- qname: <mask.hash: 'lETfDsfMRrhKUOGbaqIqQA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 45671 (Nexy), name hash: b360ab20
default	23:27:57.269121-0400	mDNSResponder	[R279621] DNSServiceQueryRecord START -- qname: <mask.hash: 'lETfDsfMRrhKUOGbaqIqQA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 45671 (Nexy), name hash: b360ab20
default	23:27:57.269759-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 883A41D3-AE27-4D2D-8419-99EA136E539F flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=96,src=<IPv6-redacted>.65350,dst=<IPv6-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x9fa1d0cc tp_proto=0x06"
default	23:27:57.269829-0400	kernel	tcp connect outgoing: [<IPv6-redacted>:65350<-><IPv6-redacted>:80] interface: en0 (skipped: 871)
so_gencnt: 2298758 t_state: SYN_SENT process: Nexy:45671 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 14 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa8e448bd
default	23:27:57.287727-0400	kernel	tcp connected: [<IPv6-redacted>:65350<-><IPv6-redacted>:80] interface: en0 (skipped: 871)
so_gencnt: 2298758 t_state: ESTABLISHED process: Nexy:45671 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 14 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa8e448bd
default	23:27:57.621479-0400	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv6-redacted>:65350<-><IPv6-redacted>:80] interface: en0 (skipped: 871)
so_gencnt: 2298758 t_state: LAST_ACK process: Nexy:45671 Duration: 0.352 sec Conn_Time: 0.018 sec bytes in/out: 571/23411 pkts in/out: 4/7 pkt rxmit: 0 ooo pkts: 1 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 19.375 ms rttvar: 2.937 ms base rtt: 14 ms so_error: 0 svc/tc: 0 flow: 0xa8e448bd
default	23:27:57.621511-0400	kernel	tcp_connection_summary [<IPv6-redacted>:65350<-><IPv6-redacted>:80] interface: en0 (skipped: 871)
so_gencnt: 2298758 t_state: LAST_ACK process: Nexy:45671 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:27:57.686265-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:27:57.755598-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=46176.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=46176, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	23:27:57.757132-0400	tccd	AUTHREQ_SUBJECT: msgID=46176.1, subject=com.nexy.assistant,
default	23:27:57.757761-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:57.772691-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6108, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=46176, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:27:57.773572-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6108, subject=com.nexy.assistant,
default	23:27:57.774157-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:57.806236-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:27:57.824563-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 45029: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 ea510d00 };
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
default	23:27:57.837042-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	23:27:59.507849-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-45671-449558 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	23:27:59.508040-0400	runningboardd	Assertion 398-45671-449558 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:59.511219-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:59.511266-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:59.511224-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449559 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:27:59.511292-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:59.511559-0400	runningboardd	Assertion 398-334-449559 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:27:59.511617-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:59.515412-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:59.515746-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:27:59.515757-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:27:59.515767-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:27:59.515841-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:27:59.516078-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:59.516922-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:59.521498-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:27:59.522249-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:59.523205-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:27:59.535451-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0xc}
default	23:27:59.536623-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	23:27:59.536750-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	23:27:59.536793-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0ad, Nexy(45671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	23:27:59.536830-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:27:59.536876-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0ad, Nexy(45671), 'prim'', AudioCategory changed to 'MediaPlayback'
default	23:27:59.536906-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:59.536940-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	23:27:59.536952-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 174 starting playing
default	23:27:59.537018-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:27:59.537053-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:27:59.537080-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:27:59.537106-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	23:27:59.537153-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	23:27:59.537089-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:59.537146-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:27:59.537189-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: false }, 
]
default	23:27:59.537278-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	23:27:59.537291-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:27:59.537334-0400	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	23:27:59.537512-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:59.537597-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:59.537626-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:27:59.537641-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	23:27:59.537650-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	23:27:59.537668-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	23:27:59.537708-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
error	23:28:00.628936-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:28:00.641236-0400	coreaudiod	Sending message. { reporterID=196155451375620, category=IO, type=error, message=["cause_set": Optional(12), "io_frame_counter": Optional(51200), "safety_violation": Optional(1), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "careporting_timestamp": 1761708480.640708, "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(759), "multi_cycle_io_page_faults_duration": Optional(0), "input_device_source_list": Optional(), "wg_cycles": Optional(5343952), "HAL_client_IO_duration": Optional(25654416), "num_continuous_silent_io_cycles": Optional(0), "scheduler_latency": Optional(16208), "smallest_buffer_frame_size": Optional(512), "input_device_transport_list": Optional(), "reporting_latency": Optional(26878000), "wg_external_wakeups": Optional(8), "input_device_uid_list": Optional(), "multi_cycle_io_page_faults": Optional(0), "io_cycle_budget": Optional(11354125), "anchor_sample_time": Optional(44), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "io_cycle": Optional(100), "wg_instruction<…> }
default	23:28:00.651639-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xc}
default	23:28:00.652070-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:28:00.652151-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 174 stopping playing
default	23:28:00.652195-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:28:00.652232-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:28:00.652287-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:28:00.652376-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:00.652415-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: false }, 
]
default	23:28:00.652509-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:28:00.652525-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:28:00.652626-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:00.652693-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:00.652723-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	23:28:00.690638-0400	runningboardd	Invalidating assertion 398-45671-449558 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:28:00.691673-0400	runningboardd	Invalidating assertion 398-334-449559 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.powerd>:334]
default	23:28:00.704161-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=46180.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=46180, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	23:28:00.705771-0400	tccd	AUTHREQ_SUBJECT: msgID=46180.1, subject=com.nexy.assistant,
default	23:28:00.706423-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:28:00.721869-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6110, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=46180, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:28:00.722912-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6110, subject=com.nexy.assistant,
default	23:28:00.723542-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:28:00.757201-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x93dfd8040) Selecting device 0 from destructor
default	23:28:00.757220-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd8040)
default	23:28:00.757227-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd8040) not already running
default	23:28:00.757232-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0x93dfd8040) disconnecting device 71
default	23:28:00.757242-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0x93dfd8040) destroying ioproc 0xc for device 71
default	23:28:00.757273-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xc}
default	23:28:00.757309-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	23:28:00.757450-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0x93dfd8040) nothing to setup
default	23:28:00.757458-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd8040) adding 0 device listeners to device 0
default	23:28:00.757464-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd8040) adding 0 device delegate listeners to device 0
default	23:28:00.757468-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd8040) removing 7 device listeners from device 71
default	23:28:00.757745-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd8040) removing 0 device delegate listeners from device 71
default	23:28:00.757760-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd8040)
default	23:28:00.759706-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:28:00.762051-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0x93dfd8040) Selecting device 71 from constructor
default	23:28:00.762062-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd8040)
default	23:28:00.762070-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0x93dfd8040) not already running
default	23:28:00.762074-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0x93dfd8040) nothing to teardown
default	23:28:00.762078-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0x93dfd8040) connecting device 71
default	23:28:00.762168-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x93dfd8040) Device ID: 71 (Input:No | Output:Yes): true
default	23:28:00.762254-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0x93dfd8040) created ioproc 0x13 for device 71
default	23:28:00.762403-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd8040) adding 7 device listeners to device 71
default	23:28:00.762563-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0x93dfd8040) adding 0 device delegate listeners to device 71
default	23:28:00.762574-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x93dfd8040)
default	23:28:00.762639-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	23:28:00.762648-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	23:28:00.762655-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	23:28:00.762661-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	23:28:00.762667-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	23:28:00.762761-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x93dfd8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	23:28:00.762773-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x93dfd8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	23:28:00.762778-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	23:28:00.762783-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd8040) removing 0 device listeners from device 0
default	23:28:00.762785-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0x93dfd8040) removing 0 device delegate listeners from device 0
default	23:28:00.762789-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x93dfd8040)
default	23:28:00.762800-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0x93dfd8040) caller requesting device change from 71 to 71
default	23:28:00.762804-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x93dfd8040)
default	23:28:00.762814-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x93dfd8040) exiting with nothing to do
default	23:28:00.762825-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	23:28:00.763128-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	23:28:00.763377-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	23:28:00.765062-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-45671-449564 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	23:28:00.765129-0400	runningboardd	Assertion 398-45671-449564 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:28:00.767374-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-449565 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:28:00.767472-0400	runningboardd	Assertion 398-334-449565 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:28:00.769949-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0x13}
default	23:28:00.771492-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	23:28:00.771616-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	23:28:00.771630-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 174 starting playing
default	23:28:00.771764-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:28:00.771852-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	23:28:00.771951-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0ad, Nexy(45671), 'prim'', displayID:'com.nexy.assistant'}
default	23:28:00.772234-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	23:28:00.772247-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:28:00.772371-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	23:28:00.772162-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: false }, 
]
default	23:28:00.772536-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:28:00.772212-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	23:28:00.772550-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	23:28:00.772558-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	23:28:00.772578-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	23:28:00.772622-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	23:28:00.782592-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 45029: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 f5510d00 };
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
default	23:28:00.795296-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
error	23:28:00.859756-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	23:28:00.864844-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:28:00.871438-0400	coreaudiod	Sending message. { reporterID=196155451375627, category=IO, type=error, message=["cause_set": Optional(12), "io_frame_counter": Optional(512), "safety_violation": Optional(1), "output_device_uid_list": Optional(BuiltInSpeakerDevice), "careporting_timestamp": 1761708480.871161, "io_page_faults": Optional(0), "safety_violation_sample_gap": Optional(3276), "multi_cycle_io_page_faults_duration": Optional(0), "input_device_source_list": Optional(), "wg_cycles": Optional(7685655), "HAL_client_IO_duration": Optional(78020916), "num_continuous_silent_io_cycles": Optional(0), "scheduler_latency": Optional(17333), "smallest_buffer_frame_size": Optional(512), "input_device_transport_list": Optional(), "reporting_latency": Optional(78967458), "wg_external_wakeups": Optional(24), "input_device_uid_list": Optional(), "multi_cycle_io_page_faults": Optional(0), "io_cycle_budget": Optional(11354166), "anchor_sample_time": Optional(59300), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "io_cycle": Optional(1), "wg_instructio<…> }
default	23:28:00.874448-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	23:28:00.935640-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=46182.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=46182, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	23:28:00.937505-0400	tccd	AUTHREQ_SUBJECT: msgID=46182.1, subject=com.nexy.assistant,
default	23:28:00.938158-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:28:00.953785-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6111, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=45671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=46182, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	23:28:00.954806-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6111, subject=com.nexy.assistant,
default	23:28:00.955373-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:28:00.986860-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	23:28:01.005364-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 45029: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 fa510d00 };
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
default	23:28:01.016993-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	23:28:01.095536-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0x13}
default	23:28:01.095885-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	23:28:01.095961-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 174 stopping playing
default	23:28:01.096004-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	23:28:01.096035-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:28:01.096100-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:28:01.096358-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:01.096406-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:01.096421-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	23:28:01.096342-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	23:28:01.096184-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:01.096359-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	23:28:01.096251-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0ad to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":45671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0ad, sessionType: 'prim', isRecording: false }, 
]
default	23:28:01.134035-0400	runningboardd	Invalidating assertion 398-45671-449564 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:28:01.135282-0400	runningboardd	Invalidating assertion 398-334-449565 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.powerd>:334]
default	23:28:01.241731-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:28:01.241745-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:28:01.241755-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:28:01.241775-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:28:01.244441-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:28:01.244801-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:28:01.244899-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:28:02.699012-0400	WindowServer	efc1b[StealKeyFocusReturningID]: [DeferringManager] Updating policy {
    advicePolicy: .keyThief;
    frontmostProcess: 0x0-0x19019 (Finder) mainConnectionID: 7B703;
    keyThiefConnectionID: EFC1B;
} for reason: key thief updated efc1b 0x0-0x99b99b (Nexy)
default	23:28:02.699067-0400	WindowServer	<BSCompoundAssertion:0x7fb015380> (com.apple.backboard.hid.delivery.localDelivery.preventFlushing) acquire for reason:key thief updated efc1b 0x0-0x99b99b (Nexy) <7998> acq:0x800bd38a0 count:1
default	23:28:02.753474-0400	Nexy	[com.apple.controlcenter:424BBAE1-5BFC-41B6-88D2-D83C3946D292] Sending action(s) in update: NSSceneFenceAction
default	23:28:02.768425-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _appQuitTimer:] | _appQuitTimer fired for: ASN: 10070426, name: Nexy with url: file:///Applications/Nexy.app/
default	23:28:02.768595-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | There are other instances of Nexy at /Applications/Nexy.app.  Done with this instance.
default	23:28:02.787301-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "AppVisible" ID:398-393-449568 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:28:02.787399-0400	runningboardd	Assertion 398-393-449568 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:28:02.787834-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:28:02.787853-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:28:02.787868-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:28:02.787919-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:28:02.790910-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:28:02.791518-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:28:02.791691-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:28:02.814013-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18914053.18914413(501)>:45671] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "FUSBProcessWindowState: visible" ID:398-393-449569 target:45671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.fuseboard" name:"Visible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	23:28:02.814131-0400	runningboardd	Assertion 398-393-449569 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) will be created as active
default	23:28:02.814506-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring jetsam update because this process is not memory-managed
default	23:28:02.814517-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring suspend because this process is not lifecycle managed
default	23:28:02.814527-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring GPU update because this process is not GPU managed
default	23:28:02.814549-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] Ignoring memory limit update because this process is not memory-managed
default	23:28:02.814578-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] visiblity is yes
default	23:28:02.817861-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	23:28:02.818367-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:28:02.818491-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, running-active-NotVisible
default	23:28:04.059649-0400	Nexy	[C:3] Alloc com.apple.backboard.hid-services.xpc
default	23:28:04.059736-0400	Nexy	[0x93d68b980] activating connection: mach=false listener=false peer=false name=(anonymous)
error	23:28:04.060396-0400	Nexy	Unable to obtain a task name port right for pid 393: (os/kern) failure (0x5)
default	23:28:04.060775-0400	Nexy	BKSHIDEventDeliveryManager - connection activation
default	23:28:04.063405-0400	Nexy	terminate:
default	23:28:04.063425-0400	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Terminating
default	23:28:04.063441-0400	Nexy	-[NSApplication _pushPersistentStateTerminationGeneration] sPersistentStateTerminateStackHeight -> 1
default	23:28:04.063553-0400	Nexy	Attempting sudden termination (1st attempt)
default	23:28:04.063570-0400	Nexy	Checking whether app should terminate
default	23:28:04.064440-0400	Nexy	Asking app delegate whether applicationShouldTerminate:
default	23:28:04.064465-0400	Nexy	replyToApplicationShouldTerminate:YES
default	23:28:04.064522-0400	Nexy	App termination approved
default	23:28:04.064533-0400	Nexy	Termination commencing
default	23:28:04.064542-0400	Nexy	Attempting sudden termination (2nd attempt)
default	23:28:04.065620-0400	Nexy	Termination complete. Exiting without sudden termination.
default	23:28:04.065989-0400	Nexy	[0x93d68bac0] activating connection: mach=true listener=false peer=false name=com.apple.powerlog.plxpclogger.xpc
default	23:28:04.066067-0400	Nexy	Entering exit handler.
default	23:28:04.066078-0400	Nexy	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	23:28:04.066123-0400	Nexy	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	23:28:04.066154-0400	Nexy	[0x93d6888c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	23:28:04.066179-0400	Nexy	Exiting exit handler.
default	23:28:04.067025-0400	Nexy	XPC connection invalidated (daemon unloaded/disabled)
default	23:28:04.072005-0400	WindowServer	0[outside of RPC]: Process death: 0x0-0x99b99b (Nexy) connectionID: EFC1B pid: 45671 in session 0x101
default	23:28:04.072043-0400	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x99b99b (Nexy) acq:0x800bd13a0 count:1
default	23:28:04.072351-0400	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef0ad","name":"Nexy(45671)"}, "details":null }
default	23:28:04.072423-0400	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef0ad from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":45671})
default	23:28:04.072443-0400	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":45671})
default	23:28:04.073030-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	23:28:04.073134-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 45671, Name = sid:0x1ef0ad, Nexy(45671), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	23:28:04.073826-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:04.073925-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:04.073987-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:04.078134-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:04.079575-0400	WindowManager	Connection invalidated | (45671) Nexy
default	23:28:04.073386-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:04.073637-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	23:28:04.084446-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x99b99b removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x99b99b (Nexy)"
)}
default	23:28:04.078671-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Workspace connection invalidated.
default	23:28:04.078697-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Now flagged as pending exit for reason: workspace client connection invalidated
default	23:28:04.085185-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xb267 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x99b99b (Nexy)"
)}
default	23:28:04.088227-0400	runningboardd	Invalidating assertion 398-393-449569 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.WindowServer(88)>:393]
default	23:28:04.088325-0400	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:28:04.088426-0400	runningboardd	Invalidating assertion 398-393-449568 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671]) from originator [osservice<com.apple.WindowServer(88)>:393]
default	23:28:04.103801-0400	mDNSResponder	[R279575] DNSServiceCreateConnection STOP PID[45671](Nexy)
default	23:28:04.103796-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65280<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2297040 t_state: FIN_WAIT_1 process: Nexy:45671 Duration: 59.969 sec Conn_Time: 0.028 sec bytes in/out: 2699062/475242 pkts in/out: 334/105 pkt rxmit: 1 ooo pkts: 36 dup bytes in: 0 ACKs delayed: 210 delayed ACKs sent: 0
rtt: 86.625 ms rttvar: 37.687 ms base rtt: 16 ms so_error: 0 svc/tc: 0 flow: 0xba27d84f
default	23:28:04.103817-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65280<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2297040 t_state: FIN_WAIT_1 process: Nexy:45671 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:28:04.103945-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:65278<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2297035 t_state: FIN_WAIT_1 process: Nexy:45671 Duration: 60.394 sec Conn_Time: 0.026 sec bytes in/out: 1369/116 pkts in/out: 1/1 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 25.625 ms rttvar: 10.500 ms base rtt: 16 ms so_error: 0 svc/tc: 0 flow: 0x93132625
default	23:28:04.103951-0400	kernel	tcp_connection_summary [<IPv4-redacted>:65278<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2297035 t_state: FIN_WAIT_1 process: Nexy:45671 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	23:28:04.105103-0400	runningboardd	[app<application.com.nexy.assistant.18914053.18914413(501)>:45671] termination reported by launchd (0, 0, 0)
default	23:28:04.105154-0400	runningboardd	Removing process: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:28:04.105562-0400	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:28:04.105747-0400	runningboardd	Removed job for [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:28:04.105798-0400	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:28:04.105844-0400	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.18914053.18914413(501)>
default	23:28:04.111274-0400	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x99b99b} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	23:28:04.111318-0400	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 10074523
default	23:28:04.111397-0400	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	23:28:04.113183-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: none (role: None) (endowments: (null))
default	23:28:04.113495-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18914053.18914413(501)>: none (role: None) (endowments: (null))
default	23:28:04.113564-0400	audiomxd	  ServerSessionManager.mm:1322  Monitored process died, pid = 45671, name = Nexy
default	23:28:04.113517-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Process exited: <RBSProcessExitContext| voluntary>.
default	23:28:04.113538-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Setting process task state to: Not Running
default	23:28:04.113549-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Setting process visibility to: Unknown
default	23:28:04.113553-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, none-NotVisible
default	23:28:04.113590-0400	ControlCenter	[app<application.com.nexy.assistant.18914053.18914413>:45671] Invalidating workspace.
default	23:28:04.113636-0400	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:28:04.113801-0400	ControlCenter	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, none-NotVisible
default	23:28:04.114062-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, none-NotVisible
default	23:28:04.114144-0400	ControlCenter	Removing: <FBApplicationProcess: 0xaf8cfca80; app<application.com.nexy.assistant.18914053.18914413>:45671(vD4E14)>
default	23:28:04.114947-0400	gamepolicyd	Received state update for 45671 (app<application.com.nexy.assistant.18914053.18914413(501)>, none-NotVisible
default	23:28:04.115070-0400	launchservicesd	Hit the server for a process handle 47ea5700000b267 that resolved to: [app<application.com.nexy.assistant.18914053.18914413(501)>:45671]
default	23:28:04.118453-0400	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-45671)
default	23:28:04.119779-0400	ControlCenter	Removing ephemeral displayable instance DisplayableId(F40DD33B) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-45671)
default	23:28:04.119832-0400	ControlCenter	Removing displayables [DisplayableAppStatusItem(F40DD33B, (bid:com.nexy.assistant-Item-0-45671))]
error	23:28:04.225069-0400	runningboardd	RBSStateCapture remove item called for untracked item 398-393-449568 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671])
error	23:28:04.225090-0400	runningboardd	RBSStateCapture remove item called for untracked item 398-393-449569 (target:[app<application.com.nexy.assistant.18914053.18914413(501)>:45671])
default	23:28:04.657093-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:28:04.657212-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	23:28:12.275743-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	23:28:12.275904-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	23:28:12.561602-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	23:28:12.564585-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:28:12.564595-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:28:12.564608-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:28:12.564615-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	23:28:12.564620-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	23:28:12.564950-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	23:28:12.565109-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	23:28:17.149372-0400	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	23:28:19.273394-0400	ControlCenter	Recent activity attributions changed to ["mic:com.apple.CoreSpeech", "scr:com.nexy.assistant"]
default	23:28:20.024914-0400	ControlCenter	Recent activity attributions changed to ["mic:com.apple.CoreSpeech", "scr:com.nexy.assistant"]
default	23:29:04.112124-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _appQuitTimer:] | _appQuitTimer fired for: ASN: 10074523, name: Nexy with url: file:///Applications/Nexy.app/
default	23:29:04.112354-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Last instance of app Nexy at /Applications/Nexy.app, handle lingering spawns.
default	23:29:04.112386-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Child applications for Nexy : (
)
default	23:29:04.112912-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | App Nexy is fully cleaned up.  No user notification is necessary.  Done with handling.
