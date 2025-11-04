default	09:58:06.992003-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	09:58:06.992160-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	09:58:06.995138-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	09:58:07.003319-0500	runningboardd	Launch request for app<application.com.nexy.assistant.20563096.20563102(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	09:58:07.003432-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.20563096.20563102(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:17422] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-17422-1464660 target:app<application.com.nexy.assistant.20563096.20563102(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	09:58:07.003571-0500	runningboardd	Assertion 398-17422-1464660 (target:app<application.com.nexy.assistant.20563096.20563102(501)>) will be created as active
default	09:58:07.008140-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	09:58:07.008179-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.20563096.20563102(501)>
default	09:58:07.008219-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	09:58:07.008337-0500	runningboardd	app<application.com.nexy.assistant.20563096.20563102(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	09:58:07.019659-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	09:58:07.040157-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] is not RunningBoard jetsam managed.
default	09:58:07.040183-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] This process will not be managed.
default	09:58:07.040195-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.20563096.20563102(501)>:37925]
default	09:58:07.040357-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	09:58:07.041240-0500	gamepolicyd	Hit the server for a process handle 14170ae800009425 that resolved to: [app<application.com.nexy.assistant.20563096.20563102(501)>:37925]
default	09:58:07.041275-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:07.047631-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.20563096.20563102(501)>:37925]
default	09:58:07.047694-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-1464661 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:07.047821-0500	runningboardd	Assertion 398-398-1464661 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:07.048002-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:07.048017-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:07.048037-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: UserInteractive
default	09:58:07.048047-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:07.048080-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:07.048135-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] reported to RB as running
default	09:58:07.049659-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:37925" ID:398-363-1464662 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	09:58:07.049618-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x1685684 com.nexy.assistant starting stopped process.
default	09:58:07.049827-0500	runningboardd	Assertion 398-363-1464662 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:07.051073-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	09:58:07.052186-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:07.052247-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:07.052272-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:07.052335-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:07.052417-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.20563096.20563102(501)>:37925]
default	09:58:07.054306-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	09:58:07.054698-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:07.054608-0500	runningboardd	Invalidating assertion 398-17422-1464660 (target:app<application.com.nexy.assistant.20563096.20563102(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:17422]
default	09:58:07.054653-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:07.054687-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:07.054843-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:07.054917-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:07.055790-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	09:58:07.058613-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	09:58:07.158473-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:07.158483-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:07.158493-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:07.158513-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:07.158677-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:07.162053-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	09:58:07.162537-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:07.260869-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	09:58:07.262336-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=511.140, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	09:58:07.271389-0500	tccd	AUTHREQ_SUBJECT: msgID=511.140, subject=com.nexy.assistant,
default	09:58:07.273040-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	09:58:07.291829-0500	kernel	Nexy[37925] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xce309a59126913b1. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:58:07.291857-0500	kernel	Nexy[37925] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0xce309a59126913b1. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:58:07.636991-0500	Nexy	[0x101f20550] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	09:58:07.637063-0500	Nexy	[0x101f20a90] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	09:58:07.773619-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xa76a80000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:07.773848-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xa76a80000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:07.774056-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xa76a80000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:07.774262-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xa76a80000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	09:58:07.868258-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	09:58:07.872490-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	09:58:07.874008-0500	Nexy	[0x101f231b0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	09:58:07.877938-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:58:07.881520-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	09:58:07.883305-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:07.883471-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:07.883605-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	09:58:07.883618-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	09:58:07.883650-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:07.883835-0500	Nexy	[0xa78168000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:58:07.884121-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	09:58:07.884514-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:07.890876-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.1, subject=com.nexy.assistant,
default	09:58:07.891496-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:07.903052-0500	Nexy	[0xa78168000] invalidated after the last release of the connection object
default	09:58:07.903104-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:07.903388-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	09:58:07.906301-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9082, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:07.907066-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9082, subject=com.nexy.assistant,
default	09:58:07.907605-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
error	09:58:07.918803-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	09:58:07.919810-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9084, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:07.920614-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9084, subject=com.nexy.assistant,
default	09:58:07.921159-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:07.936713-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	09:58:07.936749-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xa76a8c840> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	09:58:07.963903-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:07.964046-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:07.968359-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:10.152667-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid BEEC3DAB-5CBF-4036-9A0D-BE49BAFF2959 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54470,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xb200293e tp_proto=0x06"
default	09:58:10.152796-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54470<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507669 t_state: SYN_SENT process: Nexy:37925 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x88fa1887
default	09:58:10.167143-0500	kernel	tcp connected: [<IPv4-redacted>:54470<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507669 t_state: ESTABLISHED process: Nexy:37925 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x88fa1887
default	09:58:10.167434-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54470<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507669 t_state: FIN_WAIT_1 process: Nexy:37925 Duration: 0.015 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 14 ms so_error: 0 svc/tc: 0 flow: 0x88fa1887
default	09:58:10.167452-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54470<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507669 t_state: FIN_WAIT_1 process: Nexy:37925 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	09:58:10.196614-0500	Nexy	[0xa78168000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	09:58:10.211554-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa78130740) Selecting device 85 from constructor
default	09:58:10.211565-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa78130740)
default	09:58:10.211570-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa78130740) not already running
default	09:58:10.211575-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xa78130740) nothing to teardown
default	09:58:10.211580-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa78130740) connecting device 85
default	09:58:10.211669-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa78130740) Device ID: 85 (Input:No | Output:Yes): true
default	09:58:10.212138-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa78130740) created ioproc 0xa for device 85
default	09:58:10.212255-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 7 device listeners to device 85
default	09:58:10.212412-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 0 device delegate listeners to device 85
default	09:58:10.212419-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa78130740)
default	09:58:10.212502-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:10.212511-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	09:58:10.212522-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:10.212532-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	09:58:10.212539-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:10.212624-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa78130740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:10.212632-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa78130740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:10.212636-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:10.212641-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 0 device listeners from device 0
default	09:58:10.212645-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 0 device delegate listeners from device 0
default	09:58:10.212647-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa78130740)
default	09:58:10.212662-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	09:58:10.212779-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xa78130740) caller requesting device change from 85 to 91
default	09:58:10.212791-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa78130740)
default	09:58:10.212796-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa78130740) not already running
default	09:58:10.212800-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa78130740) disconnecting device 85
default	09:58:10.212805-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa78130740) destroying ioproc 0xa for device 85
default	09:58:10.214241-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	09:58:10.215487-0500	Nexy	[0xa78168280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	09:58:10.218364-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef210","name":"Nexy(37925)"}, "details":{"PID":37925,"session_type":"Primary"} }
default	09:58:10.218468-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":37925}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef210, sessionType: 'prim', isRecording: false }, 
]
default	09:58:10.219336-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 37925, name = Nexy
default	09:58:10.219588-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xa76a9a660 with ID: 0x1ef210
default	09:58:10.221729-0500	Nexy	[0xa781683c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	09:58:10.221899-0500	Nexy	No persisted cache on this platform.
error	09:58:10.222928-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=162886634700801 }
default	09:58:10.222944-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	09:58:10.223004-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:10.223104-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa78130740) connecting device 91
default	09:58:10.223184-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa78130740) Device ID: 91 (Input:Yes | Output:No): true
default	09:58:10.224535-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9085, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:10.225687-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9085, subject=com.nexy.assistant,
default	09:58:10.226270-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:10.239506-0500	tccd	AUTHREQ_PROMPTING: msgID=401.9085, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	09:58:12.233769-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	09:58:12.234633-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	09:58:12.234659-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa78130740) created ioproc 0xa for device 91
default	09:58:12.234935-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 7 device listeners to device 91
default	09:58:12.235228-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 0 device delegate listeners to device 91
default	09:58:12.235244-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa78130740)
default	09:58:12.235256-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	09:58:12.235272-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:12.235467-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	09:58:12.235480-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	09:58:12.235487-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	09:58:12.235620-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa78130740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:12.235635-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa78130740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:12.235644-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:12.235650-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 7 device listeners from device 85
default	09:58:12.235879-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 0 device delegate listeners from device 85
default	09:58:12.235891-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa78130740)
default	09:58:12.236835-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:12.238562-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9086, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:12.239886-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9086, subject=com.nexy.assistant,
default	09:58:12.240988-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:12.256278-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:12.257479-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9087, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:12.258430-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9087, subject=com.nexy.assistant,
default	09:58:12.259018-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:12.272197-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	09:58:12.274296-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9088, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:12.275434-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9088, subject=com.nexy.assistant,
default	09:58:12.276109-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:12.288217-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:12.288541-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:12.288672-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:12.288865-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:12.290324-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:12.291687-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	09:58:12.292211-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf5808000] Created node ADM::com.nexy.assistant_52807.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:12.292277-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf5808000] Created node ADM::com.nexy.assistant_52807.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:12.372165-0500	runningboardd	Assertion did invalidate due to timeout: 398-398-1464661 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925])
default	09:58:12.373823-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:12.375685-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52807 called from <private>
default	09:58:12.375725-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:12.376524-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52806)
default	09:58:12.376559-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52806 called from <private>
default	09:58:12.376568-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52806 called from <private>
default	09:58:12.376776-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52807 called from <private>
default	09:58:12.379039-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464670 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:12.379126-0500	runningboardd	Assertion 398-334-1464670 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:12.381675-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:12.381755-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:12.382164-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:12.382288-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:12.383454-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:12.376828-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52807)
default	09:58:12.376846-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52807 called from <private>
default	09:58:12.376852-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52807 called from <private>
default	09:58:12.376951-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52807)
default	09:58:12.378590-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52807 called from <private>
default	09:58:12.378632-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52807 called from <private>
default	09:58:12.385221-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	09:58:12.386413-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:58:12.388526-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52807)
default	09:58:12.388560-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52807)
default	09:58:12.388566-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52807 called from <private>
default	09:58:12.388572-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52807)
default	09:58:12.388580-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52807 called from <private>
default	09:58:12.388591-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52807 called from <private>
default	09:58:12.388597-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52807 called from <private>
default	09:58:12.388621-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52807)
default	09:58:12.388628-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52807 called from <private>
default	09:58:12.388684-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52807 called from <private>
default	09:58:12.388689-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52807)
default	09:58:12.388720-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52807 called from <private>
default	09:58:12.388793-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52807 called from <private>
default	09:58:12.388848-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52807 called from <private>
default	09:58:12.388901-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52807 called from <private>
fault	09:58:12.390166-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:58:12.392222-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	09:58:12.392474-0500	runningboardd	Invalidating assertion 398-334-1464670 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:12.392795-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:12.395941-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52807 called from <private>
default	09:58:12.395966-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52807 called from <private>
default	09:58:12.402498-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52807)
default	09:58:12.402745-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef210","name":"Nexy(37925)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	09:58:12.402827-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	09:58:12.403305-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:12.403426-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef210, Nexy(37925), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	09:58:12.403609-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:12.403740-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:12.403656-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:12.403901-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	09:58:12.403944-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef210, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 529 starting recording
default	09:58:12.404153-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:12.404253-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:12.402519-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52807 called from <private>
default	09:58:12.403095-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52806)
default	09:58:12.404313-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef210, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:12.404469-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	09:58:12.404283-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:12.404478-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:12.404584-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52806 called from <private>
default	09:58:12.404649-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:12.404619-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52806 called from <private>
default	09:58:12.404311-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:12.405190-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9089, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:12.404716-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:12.407747-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9089, subject=com.nexy.assistant,
default	09:58:12.408440-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:12.408452-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:12.408543-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:12.408582-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:12.408750-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:12.409989-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.410005-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.410016-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.410022-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.410048-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.410074-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:12.410402-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:12.415777-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52806 called from <private>
default	09:58:12.415795-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52806 called from <private>
default	09:58:12.415864-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52806)
default	09:58:12.422851-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52806)
default	09:58:12.422998-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52806 called from <private>
default	09:58:12.423011-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52806 called from <private>
default	09:58:12.423073-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52806)
default	09:58:12.425981-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:12.426049-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.426068-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.426081-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.426089-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.426105-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.426111-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:12.426340-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:12.426425-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:12.438234-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52806 called from <private>
default	09:58:12.439011-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52807 called from <private>
default	09:58:12.439112-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:12.468202-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:12.503161-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:12.504264-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464672 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:12.504336-0500	runningboardd	Assertion 398-334-1464672 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:12.505647-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52807 called from <private>
default	09:58:12.505889-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
error	09:58:12.508891-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 89
default	09:58:12.508788-0500	runningboardd	Invalidating assertion 398-334-1464672 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:12.508903-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52807 called from <private>
default	09:58:12.508912-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52807 called from <private>
default	09:58:12.509597-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52807)
default	09:58:12.509618-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52807 called from <private>
default	09:58:12.509624-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52807 called from <private>
default	09:58:12.510256-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:12.510376-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:12.510731-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52807)
default	09:58:12.510852-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52807 called from <private>
default	09:58:12.510862-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52807 called from <private>
default	09:58:12.510874-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52807 called from <private>
default	09:58:12.512397-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9091, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:12.513587-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9091, subject=com.nexy.assistant,
default	09:58:12.514430-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:12.516206-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:12.516272-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:12.516311-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:12.516469-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:12.516669-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.516683-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.516695-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.516709-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.516717-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.516725-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:12.516927-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:12.517098-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.517107-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.517117-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.517123-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.517132-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.517138-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:12.517472-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:12.530154-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464674 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:12.530211-0500	runningboardd	Assertion 398-334-1464674 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:12.531344-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52807 called from <private>
default	09:58:12.540031-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:12.540076-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:12.540112-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:12.541541-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.541549-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.541563-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.541570-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.541583-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.541594-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:12.541621-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.541644-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.541657-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.541676-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.541687-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.541692-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:12.541760-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:12.542213-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.542221-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.542232-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.542272-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:12.542306-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:12.542347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:12.542359-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	09:58:12.568244-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:12.568254-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:12.568264-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:12.568279-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:12.572074-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	09:58:12.572648-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:13.557686-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:13.558283-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef210","name":"Nexy(37925)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	09:58:13.558537-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:13.558661-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:13.558729-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef210, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:13.558841-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:13.558850-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef210, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 529 stopping recording
default	09:58:13.558904-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	09:58:13.558969-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:13.559065-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:13.559355-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	09:58:13.559307-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	09:58:13.559329-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:13.560004-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:13.560081-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:13.559813-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:13.560117-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:13.559904-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:13.560164-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	09:58:13.560295-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:58:13.560323-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:13.560348-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	09:58:13.564096-0500	runningboardd	Invalidating assertion 398-334-1464674 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:13.569542-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:13.571762-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:13.571782-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:13.571804-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:13.571814-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:13.571824-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:13.571835-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:13.571960-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:13.660105-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa78130740) Selecting device 0 from destructor
default	09:58:13.660136-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa78130740)
default	09:58:13.660152-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa78130740) not already running
default	09:58:13.660166-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa78130740) disconnecting device 91
default	09:58:13.660181-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa78130740) destroying ioproc 0xa for device 91
default	09:58:13.660234-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:13.660286-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:13.660465-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xa78130740) nothing to setup
default	09:58:13.660481-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 0 device listeners to device 0
default	09:58:13.660490-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 0 device delegate listeners to device 0
default	09:58:13.660495-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 7 device listeners from device 91
default	09:58:13.660726-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 0 device delegate listeners from device 91
default	09:58:13.660741-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa78130740)
default	09:58:13.667318-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:13.667331-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:13.667341-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:13.667361-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:13.670996-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	09:58:13.671806-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:13.916258-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37931.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=37931, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	09:58:13.917874-0500	tccd	AUTHREQ_SUBJECT: msgID=37931.1, subject=com.nexy.assistant,
default	09:58:13.918622-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	09:58:13.933273-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.14892, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=37931, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	09:58:13.934353-0500	tccd	AUTHREQ_SUBJECT: msgID=393.14892, subject=com.nexy.assistant,
default	09:58:13.935072-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	09:58:13.961899-0500	launchservicesd	CHECKIN:0x0-0x1685684 37931 com.nexy.assistant
default	09:58:13.962824-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	09:58:13.962960-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	09:58:13.964819-0500	WindowServer	a2223[CreateApplication]: Process creation: 0x0-0x1685684 (Nexy) connectionID: A2223 pid: 37931 in session 0x101
default	09:58:13.969448-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	09:58:13.969544-0500	runningboardd	Invalidating assertion 398-363-1464662 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	09:58:13.977474-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	09:58:14.075576-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:14.075591-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:14.075614-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:58:14.075624-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:14.075642-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:14.078937-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:58:14.079174-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:58:14.117999-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 37932: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 4e702200 };
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
default	09:58:14.127619-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	09:58:14.175270-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x1685684} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	09:58:14.175293-0500	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 23615108
default	09:58:14.175353-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	09:58:14.177304-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x1685684 (Nexy) connectionID: A2223 pid: 37931 in session 0x101
default	09:58:14.177337-0500	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x1685684 (Nexy) acq:0x801ab0200 count:1
default	09:58:14.177656-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x1685684 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1685684 (Nexy)"
)}
default	09:58:14.177881-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x942b removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1685684 (Nexy)"
)}
default	09:58:14.348716-0500	Nexy	[0xa78168640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:14.349469-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:14.350748-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.2, subject=com.nexy.assistant,
default	09:58:14.351445-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	09:58:14.364053-0500	Nexy	[0xa78168640] invalidated after the last release of the connection object
default	09:58:14.364871-0500	Nexy	[0xa78168640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:14.365386-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:14.366625-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.3, subject=com.nexy.assistant,
default	09:58:14.367270-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	09:58:14.378612-0500	Nexy	[0xa78168640] invalidated after the last release of the connection object
default	09:58:14.380604-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa78130740) Selecting device 85 from constructor
default	09:58:14.380615-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa78130740)
default	09:58:14.380620-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa78130740) not already running
default	09:58:14.380625-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xa78130740) nothing to teardown
default	09:58:14.380628-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa78130740) connecting device 85
default	09:58:14.380743-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa78130740) Device ID: 85 (Input:No | Output:Yes): true
default	09:58:14.380891-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa78130740) created ioproc 0xb for device 85
default	09:58:14.381006-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 7 device listeners to device 85
default	09:58:14.381172-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 0 device delegate listeners to device 85
default	09:58:14.381179-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa78130740)
default	09:58:14.381247-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	09:58:14.381254-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	09:58:14.381259-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	09:58:14.381266-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	09:58:14.381272-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:14.381377-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa78130740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:14.381390-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa78130740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:14.381396-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:14.381401-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 0 device listeners from device 0
default	09:58:14.381405-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 0 device delegate listeners from device 0
default	09:58:14.381408-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa78130740)
default	09:58:14.381426-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	09:58:14.381493-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xa78130740) caller requesting device change from 85 to 91
default	09:58:14.381500-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa78130740)
default	09:58:14.381504-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa78130740) not already running
default	09:58:14.381508-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa78130740) disconnecting device 85
default	09:58:14.381511-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa78130740) destroying ioproc 0xb for device 85
default	09:58:14.381535-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	09:58:14.381567-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:14.381654-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa78130740) connecting device 91
default	09:58:14.381745-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa78130740) Device ID: 91 (Input:Yes | Output:No): true
default	09:58:14.383069-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9092, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:14.384073-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9092, subject=com.nexy.assistant,
default	09:58:14.384665-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:14.397110-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa78130740) created ioproc 0xb for device 91
default	09:58:14.397229-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 7 device listeners to device 91
default	09:58:14.397399-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 0 device delegate listeners to device 91
default	09:58:14.397407-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa78130740)
default	09:58:14.397413-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	09:58:14.397420-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:14.397602-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	09:58:14.397609-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	09:58:14.397614-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	09:58:14.397703-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa78130740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:14.397716-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa78130740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:14.397721-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:14.397732-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 7 device listeners from device 85
default	09:58:14.397890-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 0 device delegate listeners from device 85
default	09:58:14.397897-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa78130740)
default	09:58:14.398526-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:14.400053-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9093, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:14.401410-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9093, subject=com.nexy.assistant,
default	09:58:14.402276-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:14.414310-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	09:58:14.414416-0500	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0xa79188cf0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	09:58:14.414645-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:14.415608-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9094, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:14.416380-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9094, subject=com.nexy.assistant,
default	09:58:14.416906-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:14.430994-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9095, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:14.432894-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9095, subject=com.nexy.assistant,
default	09:58:14.434926-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:14.452070-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	09:58:14.454313-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef210","name":"Nexy(37925)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	09:58:14.454432-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	09:58:14.454473-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef210, Nexy(37925), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	09:58:14.454502-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:14.454725-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef210, Nexy(37925), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	09:58:14.454866-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:14.454988-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:14.455146-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	09:58:14.455187-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef210, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 529 starting recording
default	09:58:14.454909-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:14.455317-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464684 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:14.455555-0500	runningboardd	Assertion 398-334-1464684 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:14.455564-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:14.455622-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:14.455658-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:14.455430-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:14.455481-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:14.455560-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:14.455769-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:14.455702-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef210, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:14.456037-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	09:58:14.456048-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:14.455909-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:14.455935-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:14.456201-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	09:58:14.456051-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:14.456480-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:14.456239-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:58:14.456545-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:14.456355-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:14.456569-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:14.456582-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	09:58:14.456589-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	09:58:14.456599-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	09:58:14.456679-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	09:58:14.456604-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:14.457015-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:58:14.462070-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
default	09:58:14.462776-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:14.465204-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:14.465348-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:14.465400-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:14.465984-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:14.465996-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:14.466008-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:14.466021-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:14.466029-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:14.466037-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:14.466057-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:14.466084-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:14.466094-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:14.466099-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:14.466109-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:14.466114-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:14.466363-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:14.468386-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	09:58:14.468527-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:14.468538-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:14.468544-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:14.468553-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:14.468561-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:14.468568-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:16.685807-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	09:58:19.660939-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	09:58:22.691184-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	09:58:23.432607-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52807.52730.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-34.512077], peaks:[-12.770037] ]
default	09:58:23.435621-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52807.52730.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-36.121754], peaks:[-16.367809] ]
default	09:58:25.691086-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	09:58:27.568974-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	09:58:27.569505-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef210","name":"Nexy(37925)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	09:58:27.569735-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:27.569847-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:27.569919-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef210, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:27.570030-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:27.570049-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef210, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 529 stopping recording
default	09:58:27.570120-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	09:58:27.570184-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:27.570257-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:27.570540-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	09:58:27.570683-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	09:58:27.570776-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:27.571002-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:27.571100-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:27.571198-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:27.571269-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:27.571302-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	09:58:27.571419-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:27.571463-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:58:27.571501-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:27.571527-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	09:58:27.575088-0500	runningboardd	Invalidating assertion 398-334-1464684 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:27.579922-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:27.582298-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:27.582315-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:27.582331-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:27.582340-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:27.582349-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:27.582356-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:27.582503-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:27.681422-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:27.681456-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:27.681524-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:58:27.681550-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:27.681611-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:27.687428-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:58:27.688093-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:58:27.768879-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa78130740) Selecting device 0 from destructor
default	09:58:27.768910-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa78130740)
default	09:58:27.768929-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa78130740) not already running
default	09:58:27.768942-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa78130740) disconnecting device 91
default	09:58:27.768956-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa78130740) destroying ioproc 0xb for device 91
default	09:58:27.769015-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	09:58:27.769095-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:27.769444-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xa78130740) nothing to setup
default	09:58:27.769475-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 0 device listeners to device 0
default	09:58:27.769490-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa78130740) adding 0 device delegate listeners to device 0
default	09:58:27.769505-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 7 device listeners from device 91
default	09:58:27.769946-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa78130740) removing 0 device delegate listeners from device 91
default	09:58:27.769972-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa78130740)
default	09:58:27.797056-0500	Nexy	[0xa78168500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:27.798202-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:27.799882-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.4, subject=com.nexy.assistant,
default	09:58:27.800879-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	09:58:27.818260-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[37925], responsiblePID[37925], responsiblePath: /Applications/Nexy.app to UID: 501
default	09:58:27.818588-0500	Nexy	[0xa78168500] invalidated after the last release of the connection object
default	09:58:27.902093-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	09:58:27.927303-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	09:58:27.931193-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	09:58:27.932029-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	09:58:27.933348-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	09:58:28.524504-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	09:58:28.527996-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	09:58:28.541280-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	09:58:29.806746-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52807)
default	09:58:29.807291-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52807 called from <private>
default	09:58:29.807331-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52807 called from <private>
default	09:58:29.807370-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52806)
default	09:58:29.808077-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52806 called from <private>
default	09:58:29.808115-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52806 called from <private>
default	09:58:29.841842-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52806 called from <private>
default	09:58:29.842410-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52806)
default	09:58:29.842020-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52806 called from <private>
default	09:58:34.678744-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	09:58:34.693692-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:34.703185-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	09:58:41.336210-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef210","name":"Nexy(37925)"}, "details":null }
default	09:58:41.336281-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef210 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":37925})
default	09:58:41.336307-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":37925})
default	09:58:41.338979-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:41.339262-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 529, PID = 37925, Name = sid:0x1ef210, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:41.339469-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:41.339684-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:41.339863-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:41.339983-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:41.351511-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:41.351841-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:41.354717-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52807.52730.0_airpods noise suppression studio::out-0 issue_detected_sample_time=336960.000000 ] -- [ rms:[-36.238941], peaks:[-15.291010] ]
default	09:58:41.354748-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52807.52730.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-34.688694], peaks:[-15.254970] ]
default	09:58:41.361511-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:41.361613-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:41.528409-0500	Nexy	[0x105fa30f0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	09:58:41.528486-0500	Nexy	[0x105fa3670] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	09:58:41.615573-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x760bcc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:41.615798-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x760bcc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:41.616012-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x760bcc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:41.616215-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x760bcc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	09:58:41.687844-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	09:58:41.690921-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	09:58:41.692364-0500	Nexy	[0x105fb2070] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	09:58:41.694339-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	09:58:41.695914-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:41.696111-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:41.696245-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	09:58:41.696257-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	09:58:41.696284-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:41.696474-0500	Nexy	[0x761790000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:58:41.696554-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	09:58:41.696989-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:41.702831-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.1, subject=com.nexy.assistant,
default	09:58:41.703418-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:41.714441-0500	Nexy	[0x761790000] invalidated after the last release of the connection object
default	09:58:41.714561-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:41.714596-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:41.714852-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	09:58:41.716226-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9096, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:41.716954-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9096, subject=com.nexy.assistant,
default	09:58:41.717489-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
error	09:58:41.728557-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	09:58:41.729459-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9098, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:41.730154-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9098, subject=com.nexy.assistant,
default	09:58:41.730667-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:41.743689-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	09:58:41.743771-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x7605ac3a0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	09:58:41.764235-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	09:58:41.764246-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	09:58:41.767251-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:41.767390-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:41.771835-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:43.194386-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 57EC6BE3-A455-4762-ACB9-C172D6D486F2 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54475,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x35fb3ffe tp_proto=0x06"
default	09:58:43.194500-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54475<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507956 t_state: SYN_SENT process: Nexy:37925 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa0980c8d
default	09:58:43.281215-0500	kernel	tcp connected: [<IPv4-redacted>:54475<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507956 t_state: ESTABLISHED process: Nexy:37925 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa0980c8d
default	09:58:43.281532-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54475<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507956 t_state: FIN_WAIT_1 process: Nexy:37925 Duration: 0.087 sec Conn_Time: 0.087 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 87.000 ms rttvar: 43.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xa0980c8d
default	09:58:43.281543-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54475<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507956 t_state: FIN_WAIT_1 process: Nexy:37925 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	09:58:43.298861-0500	Nexy	[0x761790000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	09:58:43.308103-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7614b8e40) Selecting device 85 from constructor
default	09:58:43.308116-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7614b8e40)
default	09:58:43.308124-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7614b8e40) not already running
default	09:58:43.308126-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7614b8e40) nothing to teardown
default	09:58:43.308130-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7614b8e40) connecting device 85
default	09:58:43.308229-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7614b8e40) Device ID: 85 (Input:No | Output:Yes): true
default	09:58:43.308342-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7614b8e40) created ioproc 0xa for device 85
default	09:58:43.308446-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7614b8e40) adding 7 device listeners to device 85
default	09:58:43.308608-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7614b8e40) adding 0 device delegate listeners to device 85
default	09:58:43.308619-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7614b8e40)
default	09:58:43.308691-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:43.308708-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	09:58:43.308715-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:43.308721-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	09:58:43.308727-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:43.308816-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7614b8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:43.308825-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7614b8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:43.308830-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:43.308835-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7614b8e40) removing 0 device listeners from device 0
default	09:58:43.308837-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7614b8e40) removing 0 device delegate listeners from device 0
default	09:58:43.308841-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7614b8e40)
default	09:58:43.308856-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	09:58:43.308944-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7614b8e40) caller requesting device change from 85 to 91
default	09:58:43.308950-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7614b8e40)
default	09:58:43.308954-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7614b8e40) not already running
default	09:58:43.308958-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7614b8e40) disconnecting device 85
default	09:58:43.308960-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7614b8e40) destroying ioproc 0xa for device 85
default	09:58:43.309010-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	09:58:43.309530-0500	Nexy	[0x761790280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	09:58:43.310508-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef211","name":"Nexy(37925)"}, "details":{"PID":37925,"session_type":"Primary"} }
default	09:58:43.310596-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":37925}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef211, sessionType: 'prim', isRecording: false }, 
]
default	09:58:43.310947-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x760bea680 with ID: 0x1ef211
default	09:58:43.311645-0500	Nexy	[0x7617903c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	09:58:43.311800-0500	Nexy	No persisted cache on this platform.
error	09:58:43.312140-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=162886634700801 }
default	09:58:43.312156-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	09:58:43.312212-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:43.312303-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7614b8e40) connecting device 91
default	09:58:43.312386-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7614b8e40) Device ID: 91 (Input:Yes | Output:No): true
default	09:58:43.313750-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9099, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:43.314913-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9099, subject=com.nexy.assistant,
default	09:58:43.315537-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:43.327800-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7614b8e40) created ioproc 0xa for device 91
default	09:58:43.327915-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7614b8e40) adding 7 device listeners to device 91
default	09:58:43.328100-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7614b8e40) adding 0 device delegate listeners to device 91
default	09:58:43.328110-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7614b8e40)
default	09:58:43.328116-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	09:58:43.328125-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:43.328248-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	09:58:43.328257-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	09:58:43.328263-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	09:58:43.328372-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7614b8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:43.328387-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7614b8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:43.328394-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:43.328398-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7614b8e40) removing 7 device listeners from device 85
default	09:58:43.328553-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7614b8e40) removing 0 device delegate listeners from device 85
default	09:58:43.328561-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7614b8e40)
default	09:58:43.329166-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:43.330116-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9100, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:43.330884-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9100, subject=com.nexy.assistant,
default	09:58:43.331425-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:43.342536-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:43.343419-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9101, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:43.344125-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9101, subject=com.nexy.assistant,
default	09:58:43.344646-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:43.356148-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	09:58:43.357471-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9102, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:43.358164-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9102, subject=com.nexy.assistant,
default	09:58:43.358685-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:43.370235-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:43.370398-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:43.371151-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:43.371448-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf653a100] Created node ADM::com.nexy.assistant_52820.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:43.371520-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf653a100] Created node ADM::com.nexy.assistant_52820.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:43.442797-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:43.444456-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52820 called from <private>
default	09:58:43.444523-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:43.449655-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464755 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:43.449845-0500	runningboardd	Assertion 398-334-1464755 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:43.445287-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52820 called from <private>
default	09:58:43.445427-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52820)
default	09:58:43.445451-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52820 called from <private>
default	09:58:43.445456-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52820 called from <private>
default	09:58:43.447017-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52819)
default	09:58:43.450133-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52819 called from <private>
default	09:58:43.451297-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52819 called from <private>
default	09:58:43.451556-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:43.451677-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:43.451761-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:58:43.452635-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:43.453732-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:43.452929-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:43.454391-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	09:58:43.455281-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
fault	09:58:43.468702-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:58:43.468971-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
default	09:58:43.469388-0500	runningboardd	Invalidating assertion 398-334-1464755 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:43.469767-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:43.470273-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52820)
default	09:58:43.474458-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52820)
default	09:58:43.475960-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52820)
default	09:58:43.476078-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52820)
default	09:58:43.476227-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52820)
default	09:58:43.476463-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52819)
default	09:58:43.476557-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52819 called from <private>
default	09:58:43.476638-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52819 called from <private>
default	09:58:43.477606-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52820 called from <private>
default	09:58:43.477622-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52820 called from <private>
default	09:58:43.477967-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52820 called from <private>
default	09:58:43.477986-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52820 called from <private>
default	09:58:43.477993-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52820 called from <private>
default	09:58:43.478002-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52820 called from <private>
default	09:58:43.478009-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52820 called from <private>
default	09:58:43.480714-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52819 called from <private>
default	09:58:43.480770-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52819 called from <private>
error	09:58:43.487427-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:58:43.487716-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52819)
default	09:58:43.487742-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52819)
default	09:58:43.490375-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9103, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:43.491061-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:43.490832-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52819 called from <private>
default	09:58:43.491200-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:43.491278-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52819 called from <private>
default	09:58:43.491274-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:43.491482-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:43.492291-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9103, subject=com.nexy.assistant,
default	09:58:43.493103-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef211","name":"Nexy(37925)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	09:58:43.493354-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	09:58:43.493535-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:43.493916-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:43.493716-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef211, Nexy(37925), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	09:58:43.494035-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:43.494206-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	09:58:43.494272-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef211, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 530 starting recording
default	09:58:43.494517-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:43.494482-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.494534-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.495003-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:43.495182-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef211, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:43.496161-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:43.495481-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:43.496330-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:43.496265-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.494353-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:43.496079-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
error	09:58:43.509363-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	09:58:43.509646-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	09:58:43.519227-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52819 called from <private>
default	09:58:43.519274-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52819 called from <private>
default	09:58:43.519433-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52819)
default	09:58:43.527856-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464756 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:43.527975-0500	runningboardd	Assertion 398-334-1464756 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:43.525516-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52820 called from <private>
default	09:58:43.528597-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52820 called from <private>
default	09:58:43.528645-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:43.530143-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52820 called from <private>
default	09:58:43.530164-0500	runningboardd	Invalidating assertion 398-334-1464756 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:43.530174-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52820 called from <private>
default	09:58:43.530200-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52820 called from <private>
default	09:58:43.530216-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52820 called from <private>
default	09:58:43.530225-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52820 called from <private>
default	09:58:43.530359-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52820)
default	09:58:43.530420-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52820 called from <private>
default	09:58:43.530431-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52820 called from <private>
default	09:58:43.535326-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9104, subject=com.nexy.assistant,
default	09:58:43.536355-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:43.550509-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:43.552042-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6ed8900] Created node ADM::com.nexy.assistant_52820.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:43.552104-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6ed8900] Created node ADM::com.nexy.assistant_52820.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:43.574487-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:43.574500-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:43.574537-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:58:43.574548-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:43.574568-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:43.577966-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:58:43.578306-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:58:43.588902-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:43.593451-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52820 called from <private>
default	09:58:43.593030-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464758 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:43.593921-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 1 1 id:52820 called from <private>
default	09:58:43.594125-0500	runningboardd	Assertion 398-334-1464758 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:43.593993-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:43.594558-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:43.594599-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:43.594708-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:58:43.594753-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:43.594878-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:43.596198-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52820 called from <private>
default	09:58:43.596766-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52820)
default	09:58:43.596851-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52820 called from <private>
default	09:58:43.596921-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52820 called from <private>
default	09:58:43.597346-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:43.597511-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:43.599035-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52820)
default	09:58:43.599853-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52820 called from <private>
default	09:58:43.599937-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52820 called from <private>
default	09:58:43.600236-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52820 called from <private>
default	09:58:43.602897-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9105, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:43.604089-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9105, subject=com.nexy.assistant,
default	09:58:43.604706-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:43.607475-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.607490-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.607502-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:43.607510-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.607517-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:43.607536-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:43.607681-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:43.623209-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464759 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:43.623667-0500	runningboardd	Assertion 398-334-1464759 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:43.626173-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52820 called from <private>
default	09:58:43.634063-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:43.634138-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:43.634190-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:43.635812-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.635842-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.635886-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:43.635898-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.635926-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:43.635934-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:43.635987-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.636013-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.636022-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:43.636028-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.636044-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:43.636082-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:43.636171-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:43.636600-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.636614-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.636620-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:43.636626-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:43.636631-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:43.636636-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:43.636740-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	09:58:44.898930-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:44.899554-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef211","name":"Nexy(37925)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	09:58:44.899796-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:44.899923-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:44.900000-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef211, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:44.900118-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:44.900125-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef211, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 530 stopping recording
default	09:58:44.900186-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	09:58:44.900257-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:44.900336-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:44.900640-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	09:58:44.900896-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	09:58:44.900990-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:44.901130-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:44.901226-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:44.901319-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:44.901386-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:44.901432-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	09:58:44.901560-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:44.901606-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:58:44.901657-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:44.901684-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	09:58:44.906434-0500	runningboardd	Invalidating assertion 398-334-1464759 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:44.908000-0500	coreaudiod	Sending message. { reporterID=162886634700802, category=IO, type=error, message=["multi_cycle_io_page_faults_duration": Optional(0), "HostApplicationDisplayID": Optional(com.nexy.assistant), "io_cycle_usage": Optional(1), "wg_cycles": Optional(5173889), "output_device_source_list": Optional(), "cause_set": Optional(4), "is_recovering": Optional(0), "careporting_timestamp": 1762268324.9076328, "issue_type": Optional(overload), "anchor_sample_time": Optional(104), "wg_external_wakeups": Optional(3), "time_since_prev_overload": Optional(491335978950041), "num_continuous_silent_io_cycles": Optional(0), "lateness": Optional(1207), "scheduler_latency": Optional(24416), "output_device_transport_list": Optional(), "input_device_transport_list": Optional(Bluetooth), "safety_violation_time_gap": Optional(0), "reporting_latency": Optional(58537041), "input_device_source_list": Optional(Unknown), "wg_user_time_mach": Optional(107474), "cause": Optional(ClientHALIODurationExceededBudget), "start_time": Optional(11792061746359), "sample_rate": Optional(24000), "<…> }
default	09:58:44.910271-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:44.912256-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:44.912271-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:44.912286-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:44.912293-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:44.912301-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:44.912307-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:44.912525-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:45.007946-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:45.007961-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:45.008006-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:58:45.008018-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:45.008042-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:45.015327-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:58:45.016006-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:58:45.043032-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7614b8e40) Selecting device 0 from destructor
default	09:58:45.043062-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7614b8e40)
default	09:58:45.043078-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7614b8e40) not already running
default	09:58:45.043092-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7614b8e40) disconnecting device 91
default	09:58:45.043106-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7614b8e40) destroying ioproc 0xa for device 91
default	09:58:45.043155-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:45.043219-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:45.043539-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x7614b8e40) nothing to setup
default	09:58:45.043569-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7614b8e40) adding 0 device listeners to device 0
default	09:58:45.043585-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7614b8e40) adding 0 device delegate listeners to device 0
default	09:58:45.043600-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7614b8e40) removing 7 device listeners from device 91
default	09:58:45.044100-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7614b8e40) removing 0 device delegate listeners from device 91
default	09:58:45.044130-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7614b8e40)
default	09:58:45.181477-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37960.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=37960, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	09:58:45.182995-0500	tccd	AUTHREQ_SUBJECT: msgID=37960.1, subject=com.nexy.assistant,
default	09:58:45.183732-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:45.197649-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.14918, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=37960, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	09:58:45.198563-0500	tccd	AUTHREQ_SUBJECT: msgID=393.14918, subject=com.nexy.assistant,
default	09:58:45.199209-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:45.243096-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:45.260250-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 37932: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 a6702200 };
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
default	09:58:45.273006-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	09:58:45.732623-0500	Nexy	[0x761790640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:45.733403-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:45.740787-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.2, subject=com.nexy.assistant,
default	09:58:45.741481-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:45.754193-0500	Nexy	[0x761790640] invalidated after the last release of the connection object
default	09:58:45.755300-0500	Nexy	[0x761790640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:45.755944-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:45.757452-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.3, subject=com.nexy.assistant,
default	09:58:45.758177-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:45.770107-0500	Nexy	[0x761790640] invalidated after the last release of the connection object
default	09:58:46.290271-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef211","name":"Nexy(37925)"}, "details":null }
default	09:58:46.290299-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef211 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":37925})
default	09:58:46.290312-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":37925})
default	09:58:46.291028-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:46.291079-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 530, PID = 37925, Name = sid:0x1ef211, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:46.291667-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:46.291718-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:46.291253-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:46.291574-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:46.296138-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:46.296286-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:46.297388-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52820.52730.0_airpods noise suppression studio::out-0 issue_detected_sample_time=28800.000000 ] -- [ rms:[-37.748962], peaks:[-17.663349] ]
default	09:58:46.297405-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52820.52730.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-39.820396], peaks:[-21.011993] ]
default	09:58:46.304558-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:46.304642-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:46.308999-0500	kernel	Nexy[37925] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xd7f057c62112f37d. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:58:46.309016-0500	kernel	Nexy[37925] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0xd7f057c62112f37d. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:58:46.476398-0500	Nexy	[0x1018a9190] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	09:58:46.476473-0500	Nexy	[0x1018a96d0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	09:58:46.561203-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x774adc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:46.561433-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x774adc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:46.561639-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x774adc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:46.561839-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x774adc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	09:58:46.635519-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	09:58:46.638633-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	09:58:46.640137-0500	Nexy	[0x1018ae390] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	09:58:46.642087-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	09:58:46.643649-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:46.643851-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:46.643997-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	09:58:46.644011-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	09:58:46.644038-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:46.644227-0500	Nexy	[0x775b68000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:58:46.644293-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	09:58:46.644784-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:46.650676-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.1, subject=com.nexy.assistant,
default	09:58:46.651324-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:46.662363-0500	Nexy	[0x775b68000] invalidated after the last release of the connection object
default	09:58:46.662494-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:46.662532-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:46.662842-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	09:58:46.664328-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9106, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:46.665086-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9106, subject=com.nexy.assistant,
default	09:58:46.665641-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
error	09:58:46.676706-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	09:58:46.677613-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9108, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:46.678319-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9108, subject=com.nexy.assistant,
default	09:58:46.678824-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:46.691423-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	09:58:46.691442-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x774abc900> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	09:58:46.714663-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:46.714802-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:46.719558-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:47.127574-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52829)
default	09:58:47.127593-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52830)
default	09:58:47.127621-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52829 called from <private>
default	09:58:47.127645-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52829 called from <private>
default	09:58:47.127655-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52830 called from <private>
default	09:58:47.127660-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52830 called from <private>
default	09:58:47.148221-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52830)
default	09:58:47.148248-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52830 called from <private>
default	09:58:47.148257-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52830 called from <private>
default	09:58:47.149573-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52829)
default	09:58:47.152230-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52829 called from <private>
default	09:58:47.152240-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52829 called from <private>
default	09:58:47.164467-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52829 called from <private>
default	09:58:47.164633-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52829 called from <private>
default	09:58:47.164787-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52829)
default	09:58:47.173300-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52829)
default	09:58:47.173666-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52829 called from <private>
default	09:58:47.173676-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52829 called from <private>
default	09:58:47.173861-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52829 called from <private>
default	09:58:47.173887-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52829 called from <private>
default	09:58:47.173954-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52829)
default	09:58:47.178047-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52829)
default	09:58:47.178433-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52829 called from <private>
default	09:58:47.178518-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52829 called from <private>
default	09:58:47.178622-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52829)
default	09:58:47.181535-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52829)
default	09:58:47.181832-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52829 called from <private>
default	09:58:47.181900-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52829 called from <private>
default	09:58:47.181922-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52829 called from <private>
default	09:58:47.181930-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52829 called from <private>
default	09:58:47.182007-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52829 called from <private>
default	09:58:47.182081-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52829 called from <private>
default	09:58:47.182111-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52829 called from <private>
default	09:58:47.182121-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52829 called from <private>
default	09:58:47.182136-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52829 called from <private>
default	09:58:47.182142-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52829 called from <private>
default	09:58:47.182148-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52829 called from <private>
default	09:58:47.182153-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52829 called from <private>
default	09:58:47.182158-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52829 called from <private>
default	09:58:47.182194-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52829 called from <private>
default	09:58:47.182260-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52829 called from <private>
default	09:58:47.182286-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52829 called from <private>
default	09:58:48.189852-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 9DF307E4-C4CC-4B9F-AA3A-FB0E3322601C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54478,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x48354ae8 tp_proto=0x06"
default	09:58:48.189968-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54478<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507991 t_state: SYN_SENT process: Nexy:37925 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x87dfe0df
default	09:58:48.209639-0500	kernel	tcp connected: [<IPv4-redacted>:54478<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507991 t_state: ESTABLISHED process: Nexy:37925 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x87dfe0df
default	09:58:48.209969-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54478<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507991 t_state: FIN_WAIT_1 process: Nexy:37925 Duration: 0.021 sec Conn_Time: 0.020 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 20.000 ms rttvar: 10.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x87dfe0df
default	09:58:48.209980-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54478<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5507991 t_state: FIN_WAIT_1 process: Nexy:37925 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	09:58:48.227431-0500	Nexy	[0x775b68000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	09:58:48.236732-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x776107840) Selecting device 85 from constructor
default	09:58:48.236743-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x776107840)
default	09:58:48.236751-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x776107840) not already running
default	09:58:48.236754-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x776107840) nothing to teardown
default	09:58:48.236758-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x776107840) connecting device 85
default	09:58:48.236841-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x776107840) Device ID: 85 (Input:No | Output:Yes): true
default	09:58:48.236936-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x776107840) created ioproc 0xa for device 85
default	09:58:48.237030-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x776107840) adding 7 device listeners to device 85
default	09:58:48.237184-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x776107840) adding 0 device delegate listeners to device 85
default	09:58:48.237190-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x776107840)
default	09:58:48.237251-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:48.237258-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	09:58:48.237263-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:48.237277-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	09:58:48.237284-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:48.237396-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x776107840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:48.237409-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x776107840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:48.237413-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:48.237417-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x776107840) removing 0 device listeners from device 0
default	09:58:48.237421-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x776107840) removing 0 device delegate listeners from device 0
default	09:58:48.237426-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x776107840)
default	09:58:48.237441-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	09:58:48.237534-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x776107840) caller requesting device change from 85 to 91
default	09:58:48.237540-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x776107840)
default	09:58:48.237545-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x776107840) not already running
default	09:58:48.237548-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x776107840) disconnecting device 85
default	09:58:48.237551-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x776107840) destroying ioproc 0xa for device 85
default	09:58:48.237601-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	09:58:48.238106-0500	Nexy	[0x775b68280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	09:58:48.239027-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef212","name":"Nexy(37925)"}, "details":{"PID":37925,"session_type":"Primary"} }
default	09:58:48.239113-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":37925}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef212, sessionType: 'prim', isRecording: false }, 
]
default	09:58:48.239464-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x774afe680 with ID: 0x1ef212
default	09:58:48.240139-0500	Nexy	[0x775b683c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	09:58:48.240278-0500	Nexy	No persisted cache on this platform.
error	09:58:48.240598-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=162886634700801 }
default	09:58:48.240613-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	09:58:48.240668-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:48.240762-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x776107840) connecting device 91
default	09:58:48.240855-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x776107840) Device ID: 91 (Input:Yes | Output:No): true
default	09:58:48.242188-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9109, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:48.243343-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9109, subject=com.nexy.assistant,
default	09:58:48.243963-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:48.256032-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x776107840) created ioproc 0xa for device 91
default	09:58:48.256161-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x776107840) adding 7 device listeners to device 91
default	09:58:48.256337-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x776107840) adding 0 device delegate listeners to device 91
default	09:58:48.256345-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x776107840)
default	09:58:48.256352-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	09:58:48.256362-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:48.256469-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	09:58:48.256477-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	09:58:48.256481-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	09:58:48.256571-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x776107840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:48.256582-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x776107840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:48.256587-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:48.256592-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x776107840) removing 7 device listeners from device 85
default	09:58:48.256750-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x776107840) removing 0 device delegate listeners from device 85
default	09:58:48.256757-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x776107840)
default	09:58:48.257323-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:48.258327-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9110, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:48.259170-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9110, subject=com.nexy.assistant,
default	09:58:48.259742-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:48.270836-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:48.271820-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9111, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:48.272597-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9111, subject=com.nexy.assistant,
default	09:58:48.273129-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:48.284584-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	09:58:48.286026-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9112, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:48.286798-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9112, subject=com.nexy.assistant,
default	09:58:48.287336-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:48.298985-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:48.299138-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:48.299870-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:48.300147-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf653a400] Created node ADM::com.nexy.assistant_52830.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:48.300276-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf653a400] Created node ADM::com.nexy.assistant_52830.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:48.345076-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:48.347232-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52830 called from <private>
default	09:58:48.347290-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:48.354605-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464775 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:48.347299-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:48.354707-0500	runningboardd	Assertion 398-334-1464775 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:48.348375-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52830 called from <private>
default	09:58:48.348500-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52829)
default	09:58:48.348519-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52829 called from <private>
default	09:58:48.349550-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52830)
default	09:58:48.350686-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52829 called from <private>
default	09:58:48.354909-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52830 called from <private>
default	09:58:48.355434-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52830 called from <private>
default	09:58:48.355623-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:48.355958-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:48.356440-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:58:48.356606-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:48.356833-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:48.358198-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:48.358654-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	09:58:48.358760-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
fault	09:58:48.360666-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:58:48.362076-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
default	09:58:48.362462-0500	runningboardd	Invalidating assertion 398-334-1464775 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:48.362884-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:48.374465-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52830)
default	09:58:48.374528-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52830)
default	09:58:48.374602-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52830)
default	09:58:48.379884-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52830)
default	09:58:48.379921-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52830)
default	09:58:48.380353-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52829)
default	09:58:48.380395-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52829 called from <private>
default	09:58:48.380404-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52829 called from <private>
default	09:58:48.380712-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52830 called from <private>
default	09:58:48.380763-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52830 called from <private>
default	09:58:48.381432-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:48.381587-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:48.381599-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52830 called from <private>
default	09:58:48.381623-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52830 called from <private>
default	09:58:48.381659-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:48.381633-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52830 called from <private>
default	09:58:48.381639-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52830 called from <private>
default	09:58:48.381649-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52830 called from <private>
default	09:58:48.382096-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:48.382963-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.383018-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.383053-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.383157-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.383399-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.383455-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:48.384440-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:48.384603-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.386013-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.386121-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.386161-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.386198-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.387510-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:48.388170-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:48.393919-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52829 called from <private>
default	09:58:48.394021-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52829 called from <private>
error	09:58:48.396930-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:58:48.397413-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52829)
default	09:58:48.397953-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52829 called from <private>
default	09:58:48.397984-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52829 called from <private>
default	09:58:48.406682-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52829)
default	09:58:48.406183-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9113, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:48.407335-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52829 called from <private>
default	09:58:48.407548-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef212","name":"Nexy(37925)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	09:58:48.407465-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52829 called from <private>
default	09:58:48.407491-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52829 called from <private>
default	09:58:48.407501-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52829 called from <private>
default	09:58:48.407651-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	09:58:48.407948-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52829 called from <private>
default	09:58:48.407982-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52829 called from <private>
default	09:58:48.407701-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:48.408387-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52829 called from <private>
default	09:58:48.407958-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:48.408399-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52829 called from <private>
default	09:58:48.408113-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:48.408384-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	09:58:48.408416-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef212, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 531 starting recording
default	09:58:48.408725-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:48.408843-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:48.409012-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef212, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:48.408852-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9113, subject=com.nexy.assistant,
default	09:58:48.407767-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef212, Nexy(37925), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	09:58:48.432666-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:48.432842-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:48.434554-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464776 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:48.434650-0500	runningboardd	Assertion 398-334-1464776 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:48.439490-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52830 called from <private>
default	09:58:48.439532-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52830 called from <private>
default	09:58:48.439579-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 1 1, id:52830 called from <private>
default	09:58:48.439588-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 1 2 2, id:52830 called from <private>
default	09:58:48.439574-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:48.439598-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 1 2 2 id:52830 called from <private>
default	09:58:48.439609-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 1 1 id:52830 called from <private>
default	09:58:48.445728-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9114, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:48.447357-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9114, subject=com.nexy.assistant,
default	09:58:48.462994-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:48.464610-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf61fe100] Created node ADM::com.nexy.assistant_52830.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:48.464674-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf61fe100] Created node ADM::com.nexy.assistant_52830.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:48.469775-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:48.469789-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:48.469842-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:58:48.469854-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:48.469872-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:48.503667-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:48.506700-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464777 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:48.506911-0500	runningboardd	Assertion 398-334-1464777 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:48.509229-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52830 called from <private>
default	09:58:48.509352-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:48.509371-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:48.509478-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:58:48.509490-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:48.509542-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:48.510116-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52830 called from <private>
default	09:58:48.510169-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:48.511920-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52830 called from <private>
default	09:58:48.512206-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52830)
default	09:58:48.512233-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52830 called from <private>
default	09:58:48.512243-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52830 called from <private>
default	09:58:48.512814-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:48.512964-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:48.513842-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52830)
default	09:58:48.514178-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52830 called from <private>
default	09:58:48.514214-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52830 called from <private>
default	09:58:48.514270-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52830 called from <private>
error	09:58:48.514514-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:58:48.516469-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9115, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:48.516664-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
default	09:58:48.517095-0500	runningboardd	Invalidating assertion 398-334-1464777 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:48.518042-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:48.518479-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9115, subject=com.nexy.assistant,
default	09:58:48.519670-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:48.519637-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:48.519723-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:48.519772-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:48.520009-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:48.520662-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.520689-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.520759-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.520767-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.520773-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.520781-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:48.537820-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464778 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:48.539444-0500	runningboardd	Assertion 398-334-1464778 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:48.539876-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52830 called from <private>
default	09:58:48.547871-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:48.547914-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:48.547986-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:48.548456-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.548465-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.548479-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.548486-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.548494-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.548501-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:48.548520-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.548531-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.548540-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.548546-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.548551-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.548557-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:48.548686-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:48.549285-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	09:58:48.549369-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.549447-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.549483-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.549525-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:48.549597-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:48.549638-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:49.690691-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	09:58:49.758373-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:49.758846-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef212","name":"Nexy(37925)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	09:58:49.759043-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:49.759160-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:49.759231-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef212, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:49.759342-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:49.759355-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef212, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 531 stopping recording
default	09:58:49.759413-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	09:58:49.759476-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:49.759551-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:49.759836-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	09:58:49.759865-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	09:58:49.759924-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:49.760276-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:49.760360-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:49.760463-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:49.760535-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:49.760575-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	09:58:49.760617-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:49.760776-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:58:49.760807-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:49.760833-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	09:58:49.764405-0500	runningboardd	Invalidating assertion 398-334-1464778 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:49.771373-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:49.771974-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:49.771996-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:49.772017-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:49.772031-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:49.772056-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:49.772070-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:49.772250-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:49.870058-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:49.870086-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:49.870157-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:58:49.870189-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:49.870234-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:49.877294-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:58:49.877913-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:58:49.959651-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x776107840) Selecting device 0 from destructor
default	09:58:49.959681-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x776107840)
default	09:58:49.959697-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x776107840) not already running
default	09:58:49.959712-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x776107840) disconnecting device 91
default	09:58:49.959724-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x776107840) destroying ioproc 0xa for device 91
default	09:58:49.959779-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:49.959845-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:49.960182-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x776107840) nothing to setup
default	09:58:49.960212-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x776107840) adding 0 device listeners to device 0
default	09:58:49.960227-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x776107840) adding 0 device delegate listeners to device 0
default	09:58:49.960239-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x776107840) removing 7 device listeners from device 91
default	09:58:49.960784-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x776107840) removing 0 device delegate listeners from device 91
default	09:58:49.960817-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x776107840)
default	09:58:50.119183-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37970.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=37970, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	09:58:50.120672-0500	tccd	AUTHREQ_SUBJECT: msgID=37970.1, subject=com.nexy.assistant,
default	09:58:50.121387-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:50.135982-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.14922, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=37970, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	09:58:50.136948-0500	tccd	AUTHREQ_SUBJECT: msgID=393.14922, subject=com.nexy.assistant,
default	09:58:50.137651-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:50.171149-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:50.191276-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 37932: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 c1702200 };
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
default	09:58:50.205707-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	09:58:50.354847-0500	Nexy	[0x775b68640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:50.355590-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:50.362560-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.2, subject=com.nexy.assistant,
default	09:58:50.363193-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:50.375169-0500	Nexy	[0x775b68640] invalidated after the last release of the connection object
default	09:58:50.375910-0500	Nexy	[0x775b68640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:50.376405-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:50.377705-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.3, subject=com.nexy.assistant,
default	09:58:50.378374-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:50.389657-0500	Nexy	[0x775b68640] invalidated after the last release of the connection object
default	09:58:50.909646-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef212","name":"Nexy(37925)"}, "details":null }
default	09:58:50.909723-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef212 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":37925})
default	09:58:50.909754-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":37925})
default	09:58:50.910531-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:50.910887-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 531, PID = 37925, Name = sid:0x1ef212, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:50.911185-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.911317-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.911488-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.911602-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.936469-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.936672-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:50.940176-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:50.940397-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:50.941313-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52830.52730.0_airpods noise suppression studio::out-0 issue_detected_sample_time=26880.000000 ] -- [ rms:[-40.275082], peaks:[-23.566854] ]
default	09:58:50.941325-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52830.52730.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-38.183868], peaks:[-22.109682] ]
default	09:58:51.123279-0500	Nexy	[0x1043efa40] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	09:58:51.123347-0500	Nexy	[0x1043eff80] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	09:58:51.213932-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xb44a24000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:51.214169-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xb44a24000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:51.214379-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xb44a24000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:51.214581-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xb44a24000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	09:58:51.290733-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	09:58:51.293668-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	09:58:51.295120-0500	Nexy	[0x1043dd1d0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	09:58:51.297065-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	09:58:51.298610-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:51.298840-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:51.299007-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	09:58:51.299020-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	09:58:51.299051-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:51.299242-0500	Nexy	[0xb460a8000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:58:51.299295-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	09:58:51.299810-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:51.306139-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.1, subject=com.nexy.assistant,
default	09:58:51.306811-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:51.318279-0500	Nexy	[0xb460a8000] invalidated after the last release of the connection object
default	09:58:51.318540-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:51.318588-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:51.318871-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	09:58:51.320736-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9116, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:51.321605-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9116, subject=com.nexy.assistant,
default	09:58:51.322197-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
error	09:58:51.334291-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	09:58:51.335251-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9118, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:51.336231-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9118, subject=com.nexy.assistant,
default	09:58:51.336878-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:51.351106-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	09:58:51.351234-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xb44a38720> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	09:58:51.376965-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:51.377149-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:51.382375-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:51.987170-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52841)
default	09:58:51.987210-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52841 called from <private>
default	09:58:51.987219-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52841 called from <private>
default	09:58:51.988557-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52842)
default	09:58:51.988579-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52842 called from <private>
default	09:58:51.988586-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52842 called from <private>
default	09:58:52.008451-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52841)
default	09:58:52.009083-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52842)
default	09:58:52.009099-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52842 called from <private>
default	09:58:52.009107-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52842 called from <private>
default	09:58:52.012697-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52841 called from <private>
default	09:58:52.012773-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52841 called from <private>
default	09:58:52.025366-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52841 called from <private>
default	09:58:52.025393-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52841 called from <private>
default	09:58:52.025566-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52841)
default	09:58:52.030565-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52841)
default	09:58:52.031683-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52841 called from <private>
default	09:58:52.031765-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52841 called from <private>
default	09:58:52.032449-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52841 called from <private>
default	09:58:52.032457-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52841 called from <private>
default	09:58:52.032561-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52841)
default	09:58:52.037061-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52841)
default	09:58:52.037576-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52841 called from <private>
default	09:58:52.037611-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52841 called from <private>
default	09:58:52.037724-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52841)
default	09:58:52.041996-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52841)
default	09:58:52.042345-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52841 called from <private>
default	09:58:52.042352-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52841 called from <private>
default	09:58:52.042538-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52841 called from <private>
default	09:58:52.042546-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52841 called from <private>
default	09:58:52.042552-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52841 called from <private>
default	09:58:52.042566-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52841 called from <private>
default	09:58:52.042572-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52841 called from <private>
default	09:58:52.042577-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52841 called from <private>
default	09:58:52.042660-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52841 called from <private>
default	09:58:52.042757-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52841 called from <private>
default	09:58:52.042902-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52841 called from <private>
default	09:58:52.043006-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52841 called from <private>
default	09:58:52.043088-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52841 called from <private>
default	09:58:52.043095-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52841 called from <private>
default	09:58:52.043102-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52841 called from <private>
default	09:58:52.043107-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52841 called from <private>
default	09:58:52.943569-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 5E781AFE-609C-4554-8DD0-08FF6BC913C9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54483,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x614d1494 tp_proto=0x06"
default	09:58:52.943689-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54483<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508067 t_state: SYN_SENT process: Nexy:37925 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb5186eb2
default	09:58:52.963002-0500	kernel	tcp connected: [<IPv4-redacted>:54483<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508067 t_state: ESTABLISHED process: Nexy:37925 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb5186eb2
default	09:58:52.963309-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54483<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508067 t_state: FIN_WAIT_1 process: Nexy:37925 Duration: 0.020 sec Conn_Time: 0.020 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 20.000 ms rttvar: 10.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xb5186eb2
default	09:58:52.963320-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54483<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508067 t_state: FIN_WAIT_1 process: Nexy:37925 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	09:58:52.980751-0500	Nexy	[0xb460a8000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	09:58:52.989979-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb46fc0040) Selecting device 85 from constructor
default	09:58:52.990006-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb46fc0040)
default	09:58:52.990025-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb46fc0040) not already running
default	09:58:52.990031-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb46fc0040) nothing to teardown
default	09:58:52.990040-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb46fc0040) connecting device 85
default	09:58:52.990192-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb46fc0040) Device ID: 85 (Input:No | Output:Yes): true
default	09:58:52.990324-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb46fc0040) created ioproc 0xa for device 85
default	09:58:52.990500-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb46fc0040) adding 7 device listeners to device 85
default	09:58:52.990772-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb46fc0040) adding 0 device delegate listeners to device 85
default	09:58:52.990801-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb46fc0040)
default	09:58:52.990933-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:52.990961-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	09:58:52.990978-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:52.991000-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	09:58:52.991008-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:52.991209-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb46fc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:52.991241-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb46fc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:52.991255-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:52.991261-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb46fc0040) removing 0 device listeners from device 0
default	09:58:52.991267-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb46fc0040) removing 0 device delegate listeners from device 0
default	09:58:52.991272-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb46fc0040)
default	09:58:52.991291-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	09:58:52.991417-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb46fc0040) caller requesting device change from 85 to 91
default	09:58:52.991427-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb46fc0040)
default	09:58:52.991431-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb46fc0040) not already running
default	09:58:52.991436-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb46fc0040) disconnecting device 85
default	09:58:52.991441-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb46fc0040) destroying ioproc 0xa for device 85
default	09:58:52.991488-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	09:58:52.991950-0500	Nexy	[0xb460a8280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	09:58:52.992728-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef213","name":"Nexy(37925)"}, "details":{"PID":37925,"session_type":"Primary"} }
default	09:58:52.992805-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":37925}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef213, sessionType: 'prim', isRecording: false }, 
]
default	09:58:52.993120-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xb44a4a680 with ID: 0x1ef213
default	09:58:52.993710-0500	Nexy	[0xb460a83c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	09:58:52.993825-0500	Nexy	No persisted cache on this platform.
error	09:58:52.994106-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=162886634700801 }
default	09:58:52.994119-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	09:58:52.994169-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:52.994261-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb46fc0040) connecting device 91
default	09:58:52.994340-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb46fc0040) Device ID: 91 (Input:Yes | Output:No): true
default	09:58:52.995493-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9119, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:52.996675-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9119, subject=com.nexy.assistant,
default	09:58:52.997309-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:53.010194-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb46fc0040) created ioproc 0xa for device 91
default	09:58:53.010317-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb46fc0040) adding 7 device listeners to device 91
default	09:58:53.010494-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb46fc0040) adding 0 device delegate listeners to device 91
default	09:58:53.010504-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb46fc0040)
default	09:58:53.010512-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	09:58:53.010521-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:53.010649-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	09:58:53.010659-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	09:58:53.010665-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	09:58:53.010760-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb46fc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:53.010772-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb46fc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:53.010778-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:53.010782-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb46fc0040) removing 7 device listeners from device 85
default	09:58:53.010950-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb46fc0040) removing 0 device delegate listeners from device 85
default	09:58:53.010957-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb46fc0040)
default	09:58:53.011528-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:53.012516-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9120, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:53.013289-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9120, subject=com.nexy.assistant,
default	09:58:53.013797-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:53.025336-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:53.026276-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9121, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:53.027169-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9121, subject=com.nexy.assistant,
default	09:58:53.028083-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:53.039804-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	09:58:53.041330-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9122, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:53.042330-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9122, subject=com.nexy.assistant,
default	09:58:53.043195-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:53.054708-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:53.054848-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:53.055993-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:53.056313-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf5b62a00] Created node ADM::com.nexy.assistant_52842.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:53.056381-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf5b62a00] Created node ADM::com.nexy.assistant_52842.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:53.100214-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:53.101774-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52842 called from <private>
default	09:58:53.101814-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:53.101825-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:53.104717-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52842 called from <private>
default	09:58:53.104906-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52842)
default	09:58:53.104921-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52842 called from <private>
default	09:58:53.108319-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464803 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:53.108393-0500	runningboardd	Assertion 398-334-1464803 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:53.104928-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52842 called from <private>
default	09:58:53.105691-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52841)
default	09:58:53.105705-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52841 called from <private>
default	09:58:53.105710-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52841 called from <private>
default	09:58:53.109720-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:53.109901-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:53.110394-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:58:53.110770-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:53.111218-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:53.112569-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:53.113708-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	09:58:53.116003-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
fault	09:58:53.118853-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:58:53.120079-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
default	09:58:53.120481-0500	runningboardd	Invalidating assertion 398-334-1464803 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:53.121196-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:53.121715-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52842)
default	09:58:53.121818-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52842)
default	09:58:53.121834-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52842)
default	09:58:53.121845-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52842)
default	09:58:53.136182-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52841)
default	09:58:53.136626-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52842 called from <private>
default	09:58:53.136656-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52842 called from <private>
default	09:58:53.136810-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52842)
default	09:58:53.136869-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52842 called from <private>
default	09:58:53.136986-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52842 called from <private>
default	09:58:53.137005-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52842 called from <private>
default	09:58:53.137015-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52842 called from <private>
default	09:58:53.137022-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52842 called from <private>
default	09:58:53.137028-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52842 called from <private>
default	09:58:53.137034-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52842 called from <private>
default	09:58:53.137042-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52842 called from <private>
default	09:58:53.137068-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52842 called from <private>
error	09:58:53.137444-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:58:53.138216-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef213","name":"Nexy(37925)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	09:58:53.138318-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	09:58:53.138379-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:53.138451-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef213, Nexy(37925), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	09:58:53.138724-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:53.138505-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:53.138501-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:53.138642-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:53.138865-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	09:58:53.138905-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef213, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 532 starting recording
default	09:58:53.139139-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:53.139163-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9123, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:53.138926-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:53.139209-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:53.139072-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:53.139343-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:53.139202-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:53.139281-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef213, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:53.139364-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:53.139473-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:53.139713-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:53.140013-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	09:58:53.140067-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:53.140644-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9123, subject=com.nexy.assistant,
default	09:58:53.141145-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.141367-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.141439-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.141551-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.141588-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.141645-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:53.142138-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:53.142422-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:53.147378-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52841 called from <private>
default	09:58:53.147595-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52841 called from <private>
default	09:58:53.147664-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52841 called from <private>
default	09:58:53.147677-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52841 called from <private>
default	09:58:53.147900-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52841)
default	09:58:53.166517-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52841 called from <private>
default	09:58:53.167366-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52841 called from <private>
default	09:58:53.179249-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52842 called from <private>
default	09:58:53.179335-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:53.189419-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9124, subject=com.nexy.assistant,
default	09:58:53.189994-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:53.190047-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:53.190088-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:53.190341-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:53.190538-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.190552-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:53.190550-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.190560-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.190566-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.190572-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.190579-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:53.190854-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:53.205840-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:53.207592-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf653a400] Created node ADM::com.nexy.assistant_52842.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:53.207654-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf653a400] Created node ADM::com.nexy.assistant_52842.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:53.224577-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:53.224598-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:53.224657-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:58:53.224674-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:53.224705-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:53.228393-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:58:53.228852-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:58:53.246109-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:53.250870-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464805 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:53.250971-0500	runningboardd	Assertion 398-334-1464805 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:53.251389-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:53.251404-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:53.251486-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:58:53.251529-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:53.251662-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:53.252557-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52842 called from <private>
default	09:58:53.252682-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52842 called from <private>
default	09:58:53.252744-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:53.254725-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52842 called from <private>
default	09:58:53.255106-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52842)
default	09:58:53.255201-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52842 called from <private>
default	09:58:53.255213-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52842 called from <private>
default	09:58:53.255779-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:53.255922-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:53.256737-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52842)
default	09:58:53.257296-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52842 called from <private>
default	09:58:53.257420-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52842 called from <private>
default	09:58:53.257478-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52842 called from <private>
error	09:58:53.257848-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:58:53.259454-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
default	09:58:53.259759-0500	runningboardd	Invalidating assertion 398-334-1464805 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:53.259895-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9125, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:53.260205-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:53.261203-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9125, subject=com.nexy.assistant,
default	09:58:53.262384-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:53.262705-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:53.262772-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:53.262826-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:53.263046-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:53.263854-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.263871-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.263885-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.263890-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.263917-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.263963-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:53.264259-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:53.280312-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464806 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:53.280509-0500	runningboardd	Assertion 398-334-1464806 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:53.280474-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52842 called from <private>
default	09:58:53.291385-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:53.291434-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:53.291475-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:53.291932-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.291944-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.291955-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.291960-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.291968-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.291975-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:53.292016-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.292026-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.292079-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.292121-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.292193-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.292213-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:53.292354-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:53.292763-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	09:58:53.292897-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.292918-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.292973-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.293186-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:53.293226-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:53.293271-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:54.563121-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:54.563690-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef213","name":"Nexy(37925)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	09:58:54.563945-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:54.564069-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:54.564136-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef213, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:54.564239-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:54.564255-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef213, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 532 stopping recording
default	09:58:54.564311-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	09:58:54.564373-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:54.564455-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:54.564822-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	09:58:54.565002-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	09:58:54.565097-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:54.565294-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:54.565388-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:54.565490-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:54.565557-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:54.565592-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	09:58:54.565664-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:54.565813-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:58:54.565841-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:54.565866-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	09:58:54.569994-0500	runningboardd	Invalidating assertion 398-334-1464806 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:54.577617-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:54.578313-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:54.578330-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:54.578363-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:54.578377-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:54.578388-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:54.578397-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:54.578521-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:54.670039-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb46fc0040) Selecting device 0 from destructor
default	09:58:54.670061-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb46fc0040)
default	09:58:54.670068-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb46fc0040) not already running
default	09:58:54.670074-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb46fc0040) disconnecting device 91
default	09:58:54.670082-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb46fc0040) destroying ioproc 0xa for device 91
default	09:58:54.670124-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:54.670161-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:54.670336-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb46fc0040) nothing to setup
default	09:58:54.670350-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb46fc0040) adding 0 device listeners to device 0
default	09:58:54.670357-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb46fc0040) adding 0 device delegate listeners to device 0
default	09:58:54.670366-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb46fc0040) removing 7 device listeners from device 91
default	09:58:54.670617-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb46fc0040) removing 0 device delegate listeners from device 91
default	09:58:54.670631-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb46fc0040)
default	09:58:54.674622-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:54.674655-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:54.674716-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:58:54.674736-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:54.674793-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:54.679128-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:58:54.679650-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:58:54.812712-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37973.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=37973, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	09:58:54.814246-0500	tccd	AUTHREQ_SUBJECT: msgID=37973.1, subject=com.nexy.assistant,
default	09:58:54.814975-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:54.828780-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.14923, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=37973, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	09:58:54.829701-0500	tccd	AUTHREQ_SUBJECT: msgID=393.14923, subject=com.nexy.assistant,
default	09:58:54.830373-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:54.867862-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:54.884919-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 37932: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 c9702200 };
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
default	09:58:54.898365-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	09:58:55.041476-0500	Nexy	[0xb460a8640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:55.042051-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:55.047935-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.2, subject=com.nexy.assistant,
default	09:58:55.048504-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:55.059947-0500	Nexy	[0xb460a8640] invalidated after the last release of the connection object
default	09:58:55.060486-0500	Nexy	[0xb460a8640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:55.060936-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:55.062141-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.3, subject=com.nexy.assistant,
default	09:58:55.062772-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:55.073877-0500	Nexy	[0xb460a8640] invalidated after the last release of the connection object
default	09:58:55.592942-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef213","name":"Nexy(37925)"}, "details":null }
default	09:58:55.593007-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef213 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":37925})
default	09:58:55.593034-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":37925})
default	09:58:55.594508-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:55.594770-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 532, PID = 37925, Name = sid:0x1ef213, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:55.596210-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:55.596318-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:55.595468-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:55.595916-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:55.605151-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:55.605376-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:55.607057-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52842.52730.0_airpods noise suppression studio::out-0 issue_detected_sample_time=29760.000000 ] -- [ rms:[-39.131191], peaks:[-19.752935] ]
default	09:58:55.607079-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52842.52730.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-35.820705], peaks:[-15.248713] ]
default	09:58:55.615586-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:55.615679-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:55.767533-0500	Nexy	[0x101c96f60] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	09:58:55.767602-0500	Nexy	[0x101c974e0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	09:58:55.856942-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x79ebbc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:55.857167-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x79ebbc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:55.857373-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x79ebbc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:58:55.857577-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x79ebbc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	09:58:55.928077-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	09:58:55.931041-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	09:58:55.932579-0500	Nexy	[0x101c9c330] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	09:58:55.934530-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	09:58:55.936084-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:55.936285-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:58:55.936423-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	09:58:55.936433-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	09:58:55.936463-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:55.936655-0500	Nexy	[0x79fc3c000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:58:55.936703-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	09:58:55.937211-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:55.942980-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.1, subject=com.nexy.assistant,
default	09:58:55.943574-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:55.954525-0500	Nexy	[0x79fc3c000] invalidated after the last release of the connection object
default	09:58:55.954668-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:55.954708-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:58:55.954983-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	09:58:55.956340-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9126, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:55.957142-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9126, subject=com.nexy.assistant,
default	09:58:55.957710-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
error	09:58:55.968871-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	09:58:55.969774-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9128, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:55.970475-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9128, subject=com.nexy.assistant,
default	09:58:55.971005-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:55.984291-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	09:58:55.984308-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x79ebc4920> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	09:58:56.009128-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:56.009282-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:56.013991-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:58:56.795481-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52853)
default	09:58:56.795522-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52853 called from <private>
default	09:58:56.795531-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52853 called from <private>
default	09:58:56.796968-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52854)
default	09:58:56.796988-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52854 called from <private>
default	09:58:56.796994-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52854 called from <private>
default	09:58:56.814143-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52853)
default	09:58:56.818248-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52854)
default	09:58:56.818288-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52854 called from <private>
default	09:58:56.818298-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52854 called from <private>
default	09:58:56.820622-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52853 called from <private>
default	09:58:56.820636-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52853 called from <private>
default	09:58:56.834297-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52853 called from <private>
default	09:58:56.834355-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52853 called from <private>
default	09:58:56.834501-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52853)
default	09:58:56.840296-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52853)
default	09:58:56.841171-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52853 called from <private>
default	09:58:56.841178-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52853 called from <private>
default	09:58:56.841319-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52853)
default	09:58:56.849315-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52853)
default	09:58:56.849666-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52853 called from <private>
default	09:58:56.849751-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52853 called from <private>
default	09:58:56.849879-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52853 called from <private>
default	09:58:56.849888-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52853 called from <private>
default	09:58:56.849894-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52853 called from <private>
default	09:58:56.849899-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52853 called from <private>
default	09:58:56.849905-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52853 called from <private>
default	09:58:56.849909-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52853 called from <private>
default	09:58:56.849965-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52853 called from <private>
default	09:58:56.850049-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52853 called from <private>
default	09:58:56.850246-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52853 called from <private>
default	09:58:56.850298-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52853 called from <private>
default	09:58:56.850438-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52853 called from <private>
default	09:58:56.850533-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52853 called from <private>
default	09:58:56.850739-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52853)
default	09:58:56.850754-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52853 called from <private>
default	09:58:56.850761-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52853 called from <private>
default	09:58:56.853858-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52853)
default	09:58:56.854471-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52853 called from <private>
default	09:58:56.854497-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52853 called from <private>
default	09:58:56.854516-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52853 called from <private>
default	09:58:56.854522-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52853 called from <private>
default	09:58:57.459477-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid AE4AD6E5-FA28-4AF8-9EDF-581D75B222C2 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54485,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xf7518db7 tp_proto=0x06"
default	09:58:57.459587-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54485<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508078 t_state: SYN_SENT process: Nexy:37925 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbab1c5dc
default	09:58:57.475820-0500	kernel	tcp connected: [<IPv4-redacted>:54485<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508078 t_state: ESTABLISHED process: Nexy:37925 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbab1c5dc
default	09:58:57.476121-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54485<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508078 t_state: FIN_WAIT_1 process: Nexy:37925 Duration: 0.017 sec Conn_Time: 0.017 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 17.000 ms rttvar: 8.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xbab1c5dc
default	09:58:57.476133-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54485<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508078 t_state: FIN_WAIT_1 process: Nexy:37925 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	09:58:57.492906-0500	Nexy	[0x79fc3c000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	09:58:57.502078-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x79ffc7840) Selecting device 85 from constructor
default	09:58:57.502089-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x79ffc7840)
default	09:58:57.502096-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x79ffc7840) not already running
default	09:58:57.502101-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x79ffc7840) nothing to teardown
default	09:58:57.502110-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x79ffc7840) connecting device 85
default	09:58:57.502207-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x79ffc7840) Device ID: 85 (Input:No | Output:Yes): true
default	09:58:57.502327-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x79ffc7840) created ioproc 0xa for device 85
default	09:58:57.502428-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x79ffc7840) adding 7 device listeners to device 85
default	09:58:57.502572-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x79ffc7840) adding 0 device delegate listeners to device 85
default	09:58:57.502578-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x79ffc7840)
default	09:58:57.502645-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:57.502654-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	09:58:57.502660-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	09:58:57.502675-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	09:58:57.502682-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:57.502773-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x79ffc7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:57.502782-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x79ffc7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:57.502785-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:57.502790-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x79ffc7840) removing 0 device listeners from device 0
default	09:58:57.502794-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x79ffc7840) removing 0 device delegate listeners from device 0
default	09:58:57.502799-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x79ffc7840)
default	09:58:57.502815-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	09:58:57.502898-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x79ffc7840) caller requesting device change from 85 to 91
default	09:58:57.502906-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x79ffc7840)
default	09:58:57.502909-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x79ffc7840) not already running
default	09:58:57.502913-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x79ffc7840) disconnecting device 85
default	09:58:57.502918-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x79ffc7840) destroying ioproc 0xa for device 85
default	09:58:57.502964-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	09:58:57.503483-0500	Nexy	[0x79fc3c280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	09:58:57.504425-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef214","name":"Nexy(37925)"}, "details":{"PID":37925,"session_type":"Primary"} }
default	09:58:57.504503-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":37925}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef214, sessionType: 'prim', isRecording: false }, 
]
default	09:58:57.504846-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x79ebd6680 with ID: 0x1ef214
default	09:58:57.505533-0500	Nexy	[0x79fc3c3c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	09:58:57.505669-0500	Nexy	No persisted cache on this platform.
error	09:58:57.505995-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=162886634700801 }
default	09:58:57.506011-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	09:58:57.506062-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:57.506153-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x79ffc7840) connecting device 91
default	09:58:57.506231-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x79ffc7840) Device ID: 91 (Input:Yes | Output:No): true
default	09:58:57.507591-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9129, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:57.508788-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9129, subject=com.nexy.assistant,
default	09:58:57.509394-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:57.521480-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x79ffc7840) created ioproc 0xa for device 91
default	09:58:57.521606-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x79ffc7840) adding 7 device listeners to device 91
default	09:58:57.521776-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x79ffc7840) adding 0 device delegate listeners to device 91
default	09:58:57.521787-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x79ffc7840)
default	09:58:57.521795-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	09:58:57.521805-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:58:57.521918-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	09:58:57.521924-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	09:58:57.521929-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	09:58:57.522023-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x79ffc7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:58:57.522037-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x79ffc7840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:58:57.522042-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:58:57.522047-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x79ffc7840) removing 7 device listeners from device 85
default	09:58:57.522202-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x79ffc7840) removing 0 device delegate listeners from device 85
default	09:58:57.522211-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x79ffc7840)
default	09:58:57.522789-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:57.523714-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9130, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:57.524673-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9130, subject=com.nexy.assistant,
default	09:58:57.525788-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:57.536921-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:58:57.537833-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9131, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:57.538602-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9131, subject=com.nexy.assistant,
default	09:58:57.539860-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:57.551345-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	09:58:57.552838-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9132, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:57.553905-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9132, subject=com.nexy.assistant,
default	09:58:57.555044-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:57.566505-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:58:57.566653-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:58:57.567372-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:57.567650-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf5809500] Created node ADM::com.nexy.assistant_52854.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:57.567719-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf5809500] Created node ADM::com.nexy.assistant_52854.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:57.610718-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:57.612783-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52854 called from <private>
default	09:58:57.612835-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:57.612839-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:57.620332-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:58:57.619749-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464810 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:57.620819-0500	runningboardd	Assertion 398-334-1464810 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:57.621181-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:57.621493-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:57.621503-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:57.615118-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52854 called from <private>
default	09:58:57.615283-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52854)
default	09:58:57.621568-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:58:57.621598-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:57.615303-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52854 called from <private>
default	09:58:57.615312-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52854 called from <private>
default	09:58:57.615500-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52853)
default	09:58:57.615515-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52853 called from <private>
default	09:58:57.621720-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:57.615521-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52853 called from <private>
fault	09:58:57.624468-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:58:57.631047-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52854)
default	09:58:57.631689-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52854)
fault	09:58:57.632342-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:58:57.634428-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52854)
default	09:58:57.634972-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52854)
default	09:58:57.635528-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
default	09:58:57.635934-0500	runningboardd	Invalidating assertion 398-334-1464810 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:57.636181-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:57.640770-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52854)
default	09:58:57.640937-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52854 called from <private>
default	09:58:57.641180-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52854 called from <private>
default	09:58:57.641211-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52854 called from <private>
default	09:58:57.641222-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52854 called from <private>
default	09:58:57.641230-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52854 called from <private>
default	09:58:57.641237-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52854 called from <private>
default	09:58:57.641242-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52854 called from <private>
default	09:58:57.642952-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52853)
default	09:58:57.645068-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52853 called from <private>
default	09:58:57.645179-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52853 called from <private>
default	09:58:57.645785-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52853 called from <private>
default	09:58:57.645828-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52853 called from <private>
error	09:58:57.646126-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:58:57.646298-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52853)
default	09:58:57.646411-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52853)
default	09:58:57.646492-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52853 called from <private>
default	09:58:57.646569-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52853 called from <private>
default	09:58:57.646581-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52853 called from <private>
default	09:58:57.646589-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52853 called from <private>
default	09:58:57.646956-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52853 called from <private>
default	09:58:57.647070-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52853 called from <private>
default	09:58:57.647447-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef214","name":"Nexy(37925)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	09:58:57.647550-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	09:58:57.647619-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:57.647671-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef214, Nexy(37925), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	09:58:57.647725-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:57.647880-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:57.647730-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:57.647809-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:57.647984-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:57.647888-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:57.647939-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	09:58:57.647985-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef214, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 533 starting recording
default	09:58:57.648078-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:57.648111-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:57.648206-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef214, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:57.648263-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:57.648219-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9133, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:57.649451-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9133, subject=com.nexy.assistant,
default	09:58:57.650098-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:57.652498-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:57.652642-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:57.652717-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:57.655134-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:57.656241-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.656316-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.656351-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.656407-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.656501-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.656658-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:57.657247-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:57.657896-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.658359-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.658566-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.658792-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.658965-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.659336-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52853 called from <private>
default	09:58:57.659365-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52853 called from <private>
default	09:58:57.659056-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:57.659424-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	09:58:57.659457-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:57.659790-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52853)
default	09:58:57.659892-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52853 called from <private>
default	09:58:57.659904-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52853 called from <private>
default	09:58:57.659842-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:57.682084-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52853)
default	09:58:57.682179-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52854 called from <private>
default	09:58:57.682193-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52854 called from <private>
default	09:58:57.687441-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:58:57.688430-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52854)
default	09:58:57.695532-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:57.695776-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:57.695905-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:57.709244-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:58:57.710330-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf61fe100] Created node ADM::com.nexy.assistant_52854.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:57.710391-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf61fe100] Created node ADM::com.nexy.assistant_52854.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:58:57.741082-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:57.741094-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:57.741136-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:58:57.741147-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:57.741175-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:57.744468-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:58:57.745248-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:58:57.745601-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464812 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:57.745666-0500	runningboardd	Assertion 398-334-1464812 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:57.745625-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:58:57.746391-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:57.746732-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:57.746825-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:58:57.746876-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:57.746980-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:57.747097-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52854 called from <private>
default	09:58:57.747256-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52854 called from <private>
default	09:58:57.747347-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:58:57.751240-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52854 called from <private>
default	09:58:57.751447-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52854 called from <private>
error	09:58:57.751796-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:58:57.753191-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9135, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:57.754319-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9135, subject=com.nexy.assistant,
default	09:58:57.755034-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
default	09:58:57.755187-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:57.755260-0500	runningboardd	Invalidating assertion 398-334-1464812 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:57.755676-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:58:57.759608-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:57.759663-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:57.759717-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:57.760750-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.760795-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:57.760812-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.760859-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.760888-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.760911-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.760961-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:57.761461-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	09:58:57.768332-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.770801-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464813 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:57.770869-0500	runningboardd	Assertion 398-334-1464813 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:57.778743-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52854)
default	09:58:57.779023-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52854 called from <private>
default	09:58:57.779045-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52854 called from <private>
default	09:58:57.779078-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52854 called from <private>
error	09:58:57.779288-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:58:57.780669-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9136, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:58:57.783147-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:58:57.786046-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.786062-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.786078-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.786088-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.786098-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.786104-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:57.786120-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.786129-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.786154-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.786164-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.786174-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.786214-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:57.786396-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:57.786530-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.786540-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.786600-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	09:58:57.786592-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.786640-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.786689-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.786734-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:57.798222-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464814 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:58:57.798291-0500	runningboardd	Assertion 398-334-1464814 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:58:57.802500-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52854 called from <private>
default	09:58:57.813169-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:58:57.813376-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:58:57.813533-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:57.827680-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.827688-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.827697-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.827702-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.827709-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.827713-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:57.827723-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.827739-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.827770-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.827778-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.827790-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.827815-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:57.827888-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:57.828629-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	09:58:57.828708-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.828717-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.828727-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.828732-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:57.828737-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:57.828743-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:58.682915-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	09:58:59.021893-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:59.022106-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef214","name":"Nexy(37925)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	09:58:59.022197-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:59.022247-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:58:59.022274-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef214, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:58:59.022321-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:58:59.022325-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef214, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 533 stopping recording
default	09:58:59.022347-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	09:58:59.022372-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:58:59.022520-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	09:58:59.022403-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:58:59.022758-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:59.022783-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:59.022795-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	09:58:59.022687-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:58:59.022725-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:59.022840-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:59.022856-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:58:59.022881-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:58:59.022921-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	09:58:59.023482-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	09:58:59.023494-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:58:59.025744-0500	runningboardd	Invalidating assertion 398-334-1464814 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:58:59.031634-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:58:59.031956-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:59.031968-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:59.031977-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:59.031990-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:58:59.032000-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:58:59.032006-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:58:59.032135-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:58:59.047583-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:58:59.047599-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:58:59.047643-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:58:59.047658-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:58:59.047710-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:58:59.051858-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:58:59.052192-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:58:59.211397-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x79ffc7840) Selecting device 0 from destructor
default	09:58:59.211421-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x79ffc7840)
default	09:58:59.211431-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x79ffc7840) not already running
default	09:58:59.211437-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x79ffc7840) disconnecting device 91
default	09:58:59.211447-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x79ffc7840) destroying ioproc 0xa for device 91
default	09:58:59.211493-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:58:59.211529-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:58:59.211733-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x79ffc7840) nothing to setup
default	09:58:59.211747-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x79ffc7840) adding 0 device listeners to device 0
default	09:58:59.211755-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x79ffc7840) adding 0 device delegate listeners to device 0
default	09:58:59.211764-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x79ffc7840) removing 7 device listeners from device 91
default	09:58:59.212021-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x79ffc7840) removing 0 device delegate listeners from device 91
default	09:58:59.212038-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x79ffc7840)
default	09:58:59.351721-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37976.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=37976, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	09:58:59.353385-0500	tccd	AUTHREQ_SUBJECT: msgID=37976.1, subject=com.nexy.assistant,
default	09:58:59.354166-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:59.372481-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.14926, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=37976, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	09:58:59.373775-0500	tccd	AUTHREQ_SUBJECT: msgID=393.14926, subject=com.nexy.assistant,
default	09:58:59.374552-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:59.405080-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:59.423796-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 37932: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 d1702200 };
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
default	09:58:59.437736-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	09:58:59.616075-0500	Nexy	[0x79fc3c640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:59.616697-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:59.623325-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.2, subject=com.nexy.assistant,
default	09:58:59.623944-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:59.635481-0500	Nexy	[0x79fc3c640] invalidated after the last release of the connection object
default	09:58:59.636190-0500	Nexy	[0x79fc3c640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:58:59.636667-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:58:59.637797-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.3, subject=com.nexy.assistant,
default	09:58:59.638405-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:58:59.649547-0500	Nexy	[0x79fc3c640] invalidated after the last release of the connection object
default	09:59:00.168329-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef214","name":"Nexy(37925)"}, "details":null }
default	09:59:00.168365-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef214 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":37925})
default	09:59:00.168376-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":37925})
default	09:59:00.169935-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:00.170540-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:00.170603-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:00.170180-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 533, PID = 37925, Name = sid:0x1ef214, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:59:00.170325-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:00.170449-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:00.176506-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:59:00.176752-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:59:00.178708-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52854.52730.0_airpods noise suppression studio::out-0 issue_detected_sample_time=26880.000000 ] -- [ rms:[-41.422810], peaks:[-24.901159] ]
default	09:59:00.178735-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52854.52730.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-39.489498], peaks:[-21.363966] ]
default	09:59:00.185853-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:00.185945-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:00.188400-0500	kernel	Nexy[37925] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xce309a59126913b1. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:59:00.188426-0500	kernel	Nexy[37925] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0xce309a59126913b1. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:59:00.347507-0500	Nexy	[0x103131210] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	09:59:00.347584-0500	Nexy	[0x103131350] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	09:59:00.434776-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x7c6af4000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:59:00.435009-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x7c6af4000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:59:00.435220-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x7c6af4000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:59:00.435424-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x7c6af4000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	09:59:00.508218-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	09:59:00.511156-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	09:59:00.512706-0500	Nexy	[0x103136810] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	09:59:00.514702-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	09:59:00.516277-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:59:00.516474-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:59:00.516607-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	09:59:00.516619-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	09:59:00.516652-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:59:00.517049-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	09:59:00.516932-0500	Nexy	[0x7c7b70000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:59:00.517497-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:59:00.523353-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.1, subject=com.nexy.assistant,
default	09:59:00.523924-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:00.535518-0500	Nexy	[0x7c7b70000] invalidated after the last release of the connection object
default	09:59:00.535727-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:59:00.535764-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:59:00.536057-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	09:59:00.537497-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9137, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:00.538311-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9137, subject=com.nexy.assistant,
default	09:59:00.538841-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
error	09:59:00.550860-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	09:59:00.551882-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9139, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:00.552820-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9139, subject=com.nexy.assistant,
default	09:59:00.553399-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:00.568857-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	09:59:00.568888-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x7c6c3f520> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	09:59:00.592936-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:59:00.593086-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:59:00.598190-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:59:01.251713-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52865)
default	09:59:01.251789-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52865 called from <private>
default	09:59:01.251802-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52865 called from <private>
default	09:59:01.258270-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52866)
default	09:59:01.258312-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52866 called from <private>
default	09:59:01.258320-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52866 called from <private>
default	09:59:01.276542-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52865)
default	09:59:01.276870-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52866)
default	09:59:01.276887-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52866 called from <private>
default	09:59:01.276892-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52866 called from <private>
default	09:59:01.280004-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52865 called from <private>
default	09:59:01.280073-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52865 called from <private>
default	09:59:01.292881-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52865 called from <private>
default	09:59:01.292917-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52865 called from <private>
default	09:59:01.293179-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52865)
default	09:59:01.299895-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52865)
default	09:59:01.300201-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52865 called from <private>
default	09:59:01.300210-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52865 called from <private>
default	09:59:01.300436-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52865 called from <private>
default	09:59:01.300446-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52865 called from <private>
default	09:59:01.300545-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52865)
default	09:59:01.309509-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52865)
default	09:59:01.309849-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52865 called from <private>
default	09:59:01.309874-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52865 called from <private>
default	09:59:01.310045-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52865)
default	09:59:01.313570-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52865)
default	09:59:01.313935-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52865 called from <private>
default	09:59:01.313957-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52865 called from <private>
default	09:59:01.314018-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52865 called from <private>
default	09:59:01.314027-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52865 called from <private>
default	09:59:01.314054-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52865 called from <private>
default	09:59:01.314059-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52865 called from <private>
default	09:59:01.314064-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52865 called from <private>
default	09:59:01.314121-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52865 called from <private>
default	09:59:01.314176-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52865 called from <private>
default	09:59:01.314201-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52865 called from <private>
default	09:59:01.314264-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52865 called from <private>
default	09:59:01.314337-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52865 called from <private>
default	09:59:01.314359-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52865 called from <private>
default	09:59:01.314366-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52865 called from <private>
default	09:59:01.314374-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52865 called from <private>
default	09:59:01.314380-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52865 called from <private>
default	09:59:02.107959-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4F97FFF8-AF57-42F0-AB23-FE7FA47D0F29 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54487,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x93fa54ba tp_proto=0x06"
default	09:59:02.108041-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54487<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508089 t_state: SYN_SENT process: Nexy:37925 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xad93c790
default	09:59:02.154280-0500	kernel	tcp connected: [<IPv4-redacted>:54487<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508089 t_state: ESTABLISHED process: Nexy:37925 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xad93c790
default	09:59:02.154582-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54487<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508089 t_state: FIN_WAIT_1 process: Nexy:37925 Duration: 0.046 sec Conn_Time: 0.046 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 46.000 ms rttvar: 23.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xad93c790
default	09:59:02.154588-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54487<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508089 t_state: FIN_WAIT_1 process: Nexy:37925 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	09:59:02.173055-0500	Nexy	[0x7c7b70000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	09:59:02.182450-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7c80fce40) Selecting device 85 from constructor
default	09:59:02.182461-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7c80fce40)
default	09:59:02.182468-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7c80fce40) not already running
default	09:59:02.182472-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7c80fce40) nothing to teardown
default	09:59:02.182476-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7c80fce40) connecting device 85
default	09:59:02.182580-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7c80fce40) Device ID: 85 (Input:No | Output:Yes): true
default	09:59:02.182693-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7c80fce40) created ioproc 0xa for device 85
default	09:59:02.182791-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7c80fce40) adding 7 device listeners to device 85
default	09:59:02.182960-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7c80fce40) adding 0 device delegate listeners to device 85
default	09:59:02.182966-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7c80fce40)
default	09:59:02.183047-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	09:59:02.183057-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	09:59:02.183063-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	09:59:02.183078-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	09:59:02.183085-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:59:02.183199-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7c80fce40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:59:02.183211-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7c80fce40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:59:02.183216-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:59:02.183219-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7c80fce40) removing 0 device listeners from device 0
default	09:59:02.183223-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7c80fce40) removing 0 device delegate listeners from device 0
default	09:59:02.183228-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7c80fce40)
default	09:59:02.183239-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	09:59:02.183335-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7c80fce40) caller requesting device change from 85 to 91
default	09:59:02.183341-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7c80fce40)
default	09:59:02.183345-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7c80fce40) not already running
default	09:59:02.183347-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7c80fce40) disconnecting device 85
default	09:59:02.183403-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7c80fce40) destroying ioproc 0xa for device 85
default	09:59:02.183501-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	09:59:02.184017-0500	Nexy	[0x7c7b70280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	09:59:02.184963-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef215","name":"Nexy(37925)"}, "details":{"PID":37925,"session_type":"Primary"} }
default	09:59:02.185045-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":37925}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef215, sessionType: 'prim', isRecording: false }, 
]
default	09:59:02.185376-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x7c6b1a680 with ID: 0x1ef215
default	09:59:02.186037-0500	Nexy	[0x7c7b703c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	09:59:02.186172-0500	Nexy	No persisted cache on this platform.
error	09:59:02.186489-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=162886634700801 }
default	09:59:02.186505-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	09:59:02.186556-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:59:02.186649-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7c80fce40) connecting device 91
default	09:59:02.186727-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7c80fce40) Device ID: 91 (Input:Yes | Output:No): true
default	09:59:02.188057-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9140, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:02.189238-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9140, subject=com.nexy.assistant,
default	09:59:02.189851-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:02.201884-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7c80fce40) created ioproc 0xa for device 91
default	09:59:02.201992-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7c80fce40) adding 7 device listeners to device 91
default	09:59:02.202179-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7c80fce40) adding 0 device delegate listeners to device 91
default	09:59:02.202188-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7c80fce40)
default	09:59:02.202195-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	09:59:02.202204-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:59:02.202323-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	09:59:02.202332-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	09:59:02.202337-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	09:59:02.202430-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7c80fce40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:59:02.202440-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7c80fce40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:59:02.202446-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:59:02.202450-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7c80fce40) removing 7 device listeners from device 85
default	09:59:02.202615-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7c80fce40) removing 0 device delegate listeners from device 85
default	09:59:02.202624-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7c80fce40)
default	09:59:02.203191-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:59:02.204179-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9141, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:02.205018-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9141, subject=com.nexy.assistant,
default	09:59:02.205596-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:02.216692-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:59:02.217598-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9142, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:02.218316-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9142, subject=com.nexy.assistant,
default	09:59:02.218825-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:02.230058-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	09:59:02.231502-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9143, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:02.232266-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9143, subject=com.nexy.assistant,
default	09:59:02.232811-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:02.244400-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:59:02.244556-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:59:02.245760-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:59:02.246136-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf5b62a00] Created node ADM::com.nexy.assistant_52866.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:59:02.246217-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf5b62a00] Created node ADM::com.nexy.assistant_52866.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:59:02.289664-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:59:02.292433-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52866 called from <private>
default	09:59:02.292491-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:59:02.292496-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:59:02.296251-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464833 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:59:02.296722-0500	runningboardd	Assertion 398-334-1464833 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:59:02.294720-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52866 called from <private>
default	09:59:02.294914-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52866)
default	09:59:02.294934-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52866 called from <private>
default	09:59:02.295018-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52865)
default	09:59:02.296770-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52866 called from <private>
default	09:59:02.297755-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:02.298135-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:02.299632-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:59:02.301440-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:02.301569-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:59:02.303462-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:59:02.304582-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:59:02.296932-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52865 called from <private>
default	09:59:02.297401-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52865 called from <private>
fault	09:59:02.310686-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:59:02.321331-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
fault	09:59:02.321825-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:59:02.322717-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:59:02.322228-0500	runningboardd	Invalidating assertion 398-334-1464833 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:59:02.326946-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52866)
default	09:59:02.327264-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52866)
default	09:59:02.327435-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52866)
default	09:59:02.327512-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52866)
default	09:59:02.327601-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52866)
default	09:59:02.328088-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52865)
default	09:59:02.328119-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52865 called from <private>
default	09:59:02.328129-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52865 called from <private>
default	09:59:02.328371-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52866 called from <private>
default	09:59:02.328385-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52866 called from <private>
default	09:59:02.328397-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52866 called from <private>
default	09:59:02.328469-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52866 called from <private>
default	09:59:02.328524-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52866 called from <private>
default	09:59:02.328531-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52866 called from <private>
default	09:59:02.328592-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52866 called from <private>
default	09:59:02.328758-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52866 called from <private>
default	09:59:02.328810-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52866 called from <private>
default	09:59:02.328933-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52866 called from <private>
default	09:59:02.328996-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52866 called from <private>
error	09:59:02.330533-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:59:02.331315-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52865 called from <private>
default	09:59:02.331449-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52865 called from <private>
default	09:59:02.331715-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52865)
default	09:59:02.331866-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52865)
default	09:59:02.332061-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52865 called from <private>
default	09:59:02.333722-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9144, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:02.337884-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9144, subject=com.nexy.assistant,
default	09:59:02.340176-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52865 called from <private>
default	09:59:02.340156-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:02.340626-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52865 called from <private>
default	09:59:02.340748-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52865 called from <private>
default	09:59:02.377473-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	09:59:02.377507-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:59:02.378043-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.378055-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.378067-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.378074-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.378102-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.378108-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:02.378259-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:02.379021-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52865 called from <private>
default	09:59:02.379082-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52865 called from <private>
default	09:59:02.381407-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52866 called from <private>
default	09:59:02.385858-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:02.390430-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.390439-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.390448-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.390508-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:59:02.390454-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.390460-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.390465-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:02.391843-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52866 called from <private>
default	09:59:02.391994-0500	runningboardd	Invalidating assertion 398-334-1464834 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:59:02.392347-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52866)
default	09:59:02.392416-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52866 called from <private>
default	09:59:02.392425-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52866 called from <private>
default	09:59:02.401540-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:59:02.412889-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:59:02.413899-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf5809500] Created node ADM::com.nexy.assistant_52866.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:59:02.424137-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:02.424148-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:02.424177-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:59:02.424187-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:02.424207-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:59:02.448405-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:59:02.450879-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464835 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:59:02.451848-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52866 called from <private>
default	09:59:02.453176-0500	runningboardd	Assertion 398-334-1464835 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:59:02.453206-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52866 called from <private>
default	09:59:02.453493-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:59:02.453620-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:02.453708-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:02.453826-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:59:02.453886-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:02.454277-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:59:02.455523-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52866 called from <private>
default	09:59:02.455897-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52866)
default	09:59:02.455986-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52866 called from <private>
default	09:59:02.455997-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52866 called from <private>
default	09:59:02.456653-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:59:02.456793-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:59:02.457451-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52866)
default	09:59:02.457839-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52866 called from <private>
default	09:59:02.457870-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52866 called from <private>
default	09:59:02.457926-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52866 called from <private>
error	09:59:02.458157-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:59:02.459660-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9146, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:02.460587-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9146, subject=com.nexy.assistant,
default	09:59:02.460733-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
default	09:59:02.464793-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:59:02.464839-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:59:02.464878-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:59:02.465291-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.465312-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.465339-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.465352-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.465361-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.465370-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:02.465389-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.465413-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.465421-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.465430-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.465455-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.465497-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:02.465610-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:02.480334-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464836 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:59:02.480818-0500	runningboardd	Assertion 398-334-1464836 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:59:02.483830-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52866 called from <private>
default	09:59:02.492309-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.492321-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.492335-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.492340-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.492347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.492352-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:02.492429-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:02.510123-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.510133-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.510162-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.510174-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.510184-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.510191-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:02.510214-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.510226-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.510236-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.510268-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.510278-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.510287-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:02.510404-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:02.511102-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.511113-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.511121-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.511126-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:02.511132-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:02.511137-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:02.511189-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	09:59:03.677902-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:59:03.678524-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef215","name":"Nexy(37925)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	09:59:03.678782-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 534, PID = 37925, Name = sid:0x1ef215, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:03.678910-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 534, PID = 37925, Name = sid:0x1ef215, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:59:03.678980-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef215, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:59:03.679089-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:59:03.679092-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef215, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 534 stopping recording
default	09:59:03.679148-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 534, PID = 37925, Name = sid:0x1ef215, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	09:59:03.679214-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 534, PID = 37925, Name = sid:0x1ef215, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:03.679286-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 534, PID = 37925, Name = sid:0x1ef215, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:59:03.679594-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	09:59:03.679537-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	09:59:03.679586-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:59:03.680289-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:59:03.680361-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:59:03.680095-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:59:03.680399-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	09:59:03.680191-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:03.680531-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:03.680579-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:59:03.680612-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:03.680636-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	09:59:03.683744-0500	runningboardd	Invalidating assertion 398-334-1464836 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:59:03.690747-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:59:03.691179-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:03.691195-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:03.691220-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:03.691231-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:03.691237-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:03.691246-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:03.691334-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:03.791357-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:03.791385-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:03.791446-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:59:03.791474-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:03.791554-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:59:03.799578-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:59:03.800023-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:59:03.817115-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7c80fce40) Selecting device 0 from destructor
default	09:59:03.817128-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7c80fce40)
default	09:59:03.817137-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7c80fce40) not already running
default	09:59:03.817142-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7c80fce40) disconnecting device 91
default	09:59:03.817150-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7c80fce40) destroying ioproc 0xa for device 91
default	09:59:03.817177-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:59:03.817203-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:59:03.817343-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x7c80fce40) nothing to setup
default	09:59:03.817356-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7c80fce40) adding 0 device listeners to device 0
default	09:59:03.817362-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7c80fce40) adding 0 device delegate listeners to device 0
default	09:59:03.817368-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7c80fce40) removing 7 device listeners from device 91
default	09:59:03.817596-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7c80fce40) removing 0 device delegate listeners from device 91
default	09:59:03.817610-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7c80fce40)
default	09:59:03.951803-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37979.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=37979, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	09:59:03.953510-0500	tccd	AUTHREQ_SUBJECT: msgID=37979.1, subject=com.nexy.assistant,
default	09:59:03.954325-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:03.973505-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.14928, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=37979, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	09:59:03.974844-0500	tccd	AUTHREQ_SUBJECT: msgID=393.14928, subject=com.nexy.assistant,
default	09:59:03.975580-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:04.011653-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:04.029499-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 37932: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 d9702200 };
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
default	09:59:04.043993-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	09:59:04.213103-0500	Nexy	[0x7c7b70640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:59:04.213845-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:59:04.221754-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.2, subject=com.nexy.assistant,
default	09:59:04.222522-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:04.234909-0500	Nexy	[0x7c7b70640] invalidated after the last release of the connection object
default	09:59:04.236028-0500	Nexy	[0x7c7b70640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:59:04.236685-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:59:04.238198-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.3, subject=com.nexy.assistant,
default	09:59:04.238926-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:04.251351-0500	Nexy	[0x7c7b70640] invalidated after the last release of the connection object
default	09:59:04.770970-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef215","name":"Nexy(37925)"}, "details":null }
default	09:59:04.771013-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef215 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":37925})
default	09:59:04.771028-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":37925})
default	09:59:04.772130-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 534, PID = 37925, Name = sid:0x1ef215, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:04.772236-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 534, PID = 37925, Name = sid:0x1ef215, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:59:04.773329-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:04.773406-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:04.772655-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:04.773201-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:04.779278-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:59:04.779490-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:59:04.781531-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52866.52730.0_airpods noise suppression studio::out-0 issue_detected_sample_time=26880.000000 ] -- [ rms:[-36.357582], peaks:[-13.741871] ]
default	09:59:04.781569-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52866.52730.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-37.403847], peaks:[-18.280090] ]
default	09:59:04.789406-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:04.789495-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:04.790512-0500	kernel	Nexy[37925] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x15f5682f8cbcdd33. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:59:04.790530-0500	kernel	Nexy[37925] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0x15f5682f8cbcdd33. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:59:04.942959-0500	Nexy	[0x1056cfbd0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	09:59:04.943033-0500	Nexy	[0x1056d0110] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	09:59:05.029824-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x902aa0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:59:05.030052-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x902aa0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:59:05.030262-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x902aa0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:59:05.030468-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x902aa0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	09:59:05.101495-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	09:59:05.104212-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	09:59:05.105758-0500	Nexy	[0x1056d1ef0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	09:59:05.107678-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	09:59:05.109230-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:59:05.109431-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:59:05.109568-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	09:59:05.109580-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	09:59:05.109610-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:59:05.109803-0500	Nexy	[0x903d34000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:59:05.109883-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	09:59:05.110338-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:59:05.116121-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.1, subject=com.nexy.assistant,
default	09:59:05.116722-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:05.128209-0500	Nexy	[0x903d34000] invalidated after the last release of the connection object
default	09:59:05.128370-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:59:05.128407-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:59:05.128693-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	09:59:05.130064-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9147, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:05.130894-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9147, subject=com.nexy.assistant,
default	09:59:05.131474-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
error	09:59:05.142858-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	09:59:05.143863-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9149, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:05.144581-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9149, subject=com.nexy.assistant,
default	09:59:05.145098-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:05.158668-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	09:59:05.158689-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x902aac840> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	09:59:05.181883-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:59:05.182019-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:59:05.186908-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:59:05.909291-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52877)
default	09:59:05.909332-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52877 called from <private>
default	09:59:05.909338-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52877 called from <private>
default	09:59:05.910427-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52878)
default	09:59:05.910450-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52878 called from <private>
default	09:59:05.910459-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52878 called from <private>
default	09:59:05.928729-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52878)
default	09:59:05.928760-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52878 called from <private>
default	09:59:05.928767-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52878 called from <private>
default	09:59:05.931262-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52877)
default	09:59:05.933885-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52877 called from <private>
default	09:59:05.933900-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52877 called from <private>
default	09:59:05.947197-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52877 called from <private>
default	09:59:05.947230-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52877 called from <private>
default	09:59:05.947983-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52877)
default	09:59:05.960268-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52877)
default	09:59:05.960788-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52877 called from <private>
default	09:59:05.960829-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52877 called from <private>
default	09:59:05.960895-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52877)
default	09:59:05.966070-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52877)
default	09:59:05.966449-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52877 called from <private>
default	09:59:05.966461-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52877 called from <private>
default	09:59:05.966820-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52877 called from <private>
default	09:59:05.966943-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52877 called from <private>
default	09:59:05.967056-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52877 called from <private>
default	09:59:05.967065-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52877 called from <private>
default	09:59:05.967101-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52877 called from <private>
default	09:59:05.967123-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52877 called from <private>
default	09:59:05.967150-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52877 called from <private>
default	09:59:05.967160-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52877 called from <private>
default	09:59:05.967168-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52877 called from <private>
default	09:59:05.967173-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52877 called from <private>
default	09:59:05.967178-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52877 called from <private>
default	09:59:05.967210-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52877)
default	09:59:05.967217-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52877 called from <private>
default	09:59:05.967328-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52877 called from <private>
default	09:59:05.967402-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52877 called from <private>
default	09:59:05.968897-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52877)
default	09:59:05.968924-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52877 called from <private>
default	09:59:05.968934-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52877 called from <private>
default	09:59:05.969281-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52877 called from <private>
default	09:59:05.969384-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52877 called from <private>
default	09:59:06.642453-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D1EF0CE7-694C-4485-8632-521217D50E98 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54489,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xb5f74e7f tp_proto=0x06"
default	09:59:06.642571-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54489<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508105 t_state: SYN_SENT process: Nexy:37925 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x99f7b4d6
default	09:59:06.657470-0500	kernel	tcp connected: [<IPv4-redacted>:54489<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508105 t_state: ESTABLISHED process: Nexy:37925 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x99f7b4d6
default	09:59:06.657761-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54489<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508105 t_state: FIN_WAIT_1 process: Nexy:37925 Duration: 0.016 sec Conn_Time: 0.015 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 15.000 ms rttvar: 7.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x99f7b4d6
default	09:59:06.657771-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54489<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508105 t_state: FIN_WAIT_1 process: Nexy:37925 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	09:59:06.674503-0500	Nexy	[0x903d34000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	09:59:06.683541-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x90427b840) Selecting device 85 from constructor
default	09:59:06.683552-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x90427b840)
default	09:59:06.683557-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x90427b840) not already running
default	09:59:06.683562-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x90427b840) nothing to teardown
default	09:59:06.683564-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x90427b840) connecting device 85
default	09:59:06.683675-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x90427b840) Device ID: 85 (Input:No | Output:Yes): true
default	09:59:06.683788-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x90427b840) created ioproc 0xa for device 85
default	09:59:06.683888-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x90427b840) adding 7 device listeners to device 85
default	09:59:06.684042-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x90427b840) adding 0 device delegate listeners to device 85
default	09:59:06.684050-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x90427b840)
default	09:59:06.684118-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	09:59:06.684124-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	09:59:06.684129-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	09:59:06.684144-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	09:59:06.684153-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:59:06.684240-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x90427b840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:59:06.684248-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x90427b840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:59:06.684253-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:59:06.684257-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x90427b840) removing 0 device listeners from device 0
default	09:59:06.684262-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x90427b840) removing 0 device delegate listeners from device 0
default	09:59:06.684266-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x90427b840)
default	09:59:06.684279-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	09:59:06.684365-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x90427b840) caller requesting device change from 85 to 91
default	09:59:06.684371-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x90427b840)
default	09:59:06.684376-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x90427b840) not already running
default	09:59:06.684380-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x90427b840) disconnecting device 85
default	09:59:06.684384-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x90427b840) destroying ioproc 0xa for device 85
default	09:59:06.684431-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	09:59:06.684932-0500	Nexy	[0x903d34280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	09:59:06.685853-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef216","name":"Nexy(37925)"}, "details":{"PID":37925,"session_type":"Primary"} }
default	09:59:06.685937-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":37925}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef216, sessionType: 'prim', isRecording: false }, 
]
default	09:59:06.686269-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x902ac2680 with ID: 0x1ef216
default	09:59:06.686925-0500	Nexy	[0x903d343c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	09:59:06.687058-0500	Nexy	No persisted cache on this platform.
error	09:59:06.687371-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=162886634700801 }
default	09:59:06.687386-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	09:59:06.687439-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:59:06.687530-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x90427b840) connecting device 91
default	09:59:06.687604-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x90427b840) Device ID: 91 (Input:Yes | Output:No): true
default	09:59:06.688925-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9150, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:06.690073-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9150, subject=com.nexy.assistant,
default	09:59:06.690687-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:06.702662-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x90427b840) created ioproc 0xa for device 91
default	09:59:06.702779-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x90427b840) adding 7 device listeners to device 91
default	09:59:06.702939-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x90427b840) adding 0 device delegate listeners to device 91
default	09:59:06.702948-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x90427b840)
default	09:59:06.702954-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	09:59:06.702963-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:59:06.703072-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	09:59:06.703078-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	09:59:06.703082-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	09:59:06.703174-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x90427b840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:59:06.703187-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x90427b840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:59:06.703193-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:59:06.703197-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x90427b840) removing 7 device listeners from device 85
default	09:59:06.703356-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x90427b840) removing 0 device delegate listeners from device 85
default	09:59:06.703363-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x90427b840)
default	09:59:06.703944-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:59:06.704848-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9151, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:06.705602-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9151, subject=com.nexy.assistant,
default	09:59:06.706136-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:06.716953-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:59:06.717909-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9152, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:06.718710-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9152, subject=com.nexy.assistant,
default	09:59:06.719275-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:06.730814-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	09:59:06.732220-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9153, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:06.732968-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9153, subject=com.nexy.assistant,
default	09:59:06.733510-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:06.744787-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:59:06.744941-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:59:06.745682-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:59:06.745959-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf61fe100] Created node ADM::com.nexy.assistant_52878.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:59:06.746037-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf61fe100] Created node ADM::com.nexy.assistant_52878.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:59:06.789828-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:59:06.791779-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52878 called from <private>
default	09:59:06.791838-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:59:06.791879-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:59:06.793246-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52878 called from <private>
default	09:59:06.793574-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52878)
default	09:59:06.793597-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52878 called from <private>
default	09:59:06.793605-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52878 called from <private>
default	09:59:06.794184-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52877)
default	09:59:06.794203-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52877 called from <private>
default	09:59:06.798343-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464840 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:59:06.798841-0500	runningboardd	Assertion 398-334-1464840 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:59:06.794210-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52877 called from <private>
default	09:59:06.799371-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:06.799442-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:06.799582-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:59:06.799712-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:06.800494-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
fault	09:59:06.801651-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:59:06.802445-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:59:06.803162-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	09:59:06.812386-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:59:06.814699-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
default	09:59:06.815278-0500	runningboardd	Invalidating assertion 398-334-1464840 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:59:06.817281-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:59:06.818428-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52878)
default	09:59:06.818635-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52878)
default	09:59:06.818651-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52878)
default	09:59:06.818664-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52878)
default	09:59:06.820348-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52878)
default	09:59:06.821434-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52877)
default	09:59:06.821573-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52877 called from <private>
default	09:59:06.821592-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52877 called from <private>
default	09:59:06.821881-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52878 called from <private>
default	09:59:06.821896-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52878 called from <private>
default	09:59:06.822093-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52878 called from <private>
default	09:59:06.822109-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52878 called from <private>
default	09:59:06.822141-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52878 called from <private>
default	09:59:06.822149-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52878 called from <private>
default	09:59:06.822248-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52878 called from <private>
error	09:59:06.822886-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:59:06.823496-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52877 called from <private>
default	09:59:06.823527-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52877 called from <private>
default	09:59:06.823898-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52877)
default	09:59:06.823949-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52877 called from <private>
default	09:59:06.823961-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52877 called from <private>
default	09:59:06.824160-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52877)
default	09:59:06.824198-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52877 called from <private>
default	09:59:06.824208-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52877 called from <private>
default	09:59:06.824594-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef216","name":"Nexy(37925)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	09:59:06.824697-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	09:59:06.824759-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52877 called from <private>
default	09:59:06.824769-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:59:06.824785-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52877 called from <private>
default	09:59:06.824812-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9154, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:06.824830-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef216, Nexy(37925), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	09:59:06.824883-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:06.824913-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:06.824947-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:59:06.825002-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:06.825014-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	09:59:06.825030-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef216, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 535 starting recording
default	09:59:06.825059-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:06.825115-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:06.825107-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:06.825139-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:59:06.825169-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef216, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:59:06.825234-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:59:06.826208-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	09:59:06.826231-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:59:06.826451-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52877 called from <private>
default	09:59:06.826658-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52877 called from <private>
default	09:59:06.826746-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9154, subject=com.nexy.assistant,
default	09:59:06.827033-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52877)
default	09:59:06.827143-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52877)
default	09:59:06.827685-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52877 called from <private>
default	09:59:06.827703-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52877 called from <private>
default	09:59:06.827728-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52877 called from <private>
default	09:59:06.827739-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52877 called from <private>
default	09:59:06.827749-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52877 called from <private>
default	09:59:06.827754-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52877 called from <private>
default	09:59:06.828018-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:06.850975-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:06.851445-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:06.853454-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:59:06.853009-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:59:06.860377-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:59:06.860577-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:59:06.872513-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.872596-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52877)
default	09:59:06.872524-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.872536-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.872731-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52877)
default	09:59:06.872543-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.872550-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.872591-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:06.872993-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52877 called from <private>
default	09:59:06.873013-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52877 called from <private>
default	09:59:06.873054-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52877 called from <private>
default	09:59:06.873092-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52877 called from <private>
default	09:59:06.873115-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52877 called from <private>
default	09:59:06.872976-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:06.873136-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52877 called from <private>
default	09:59:06.873480-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9155, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:06.880284-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:59:06.881200-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.881222-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.881237-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.881247-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.881257-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.881264-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:06.881326-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.881341-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.881381-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.881411-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.881431-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.881438-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:06.881571-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:06.881751-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.881766-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.881774-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.881781-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.881788-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.881794-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:06.881828-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	09:59:06.890667-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:59:06.892148-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf653a400] Created node ADM::com.nexy.assistant_52878.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:59:06.892210-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf653a400] Created node ADM::com.nexy.assistant_52878.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:59:06.907706-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.907720-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.907737-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.907747-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.907753-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.907761-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:06.907845-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:06.919476-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:06.919491-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:06.919544-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:59:06.919558-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:06.919575-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:59:06.923418-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:59:06.923953-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:59:06.931317-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:59:06.932893-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464842 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:59:06.933013-0500	runningboardd	Assertion 398-334-1464842 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:59:06.937170-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:06.937184-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:06.937248-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:59:06.937273-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:06.937361-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:59:06.937630-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52878 called from <private>
default	09:59:06.937828-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:59:06.951214-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:59:06.951319-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:59:06.951409-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:59:06.951925-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.951956-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.963749-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464843 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:59:06.964565-0500	runningboardd	Assertion 398-334-1464843 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:59:06.967214-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52878 called from <private>
default	09:59:06.967293-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52878 called from <private>
default	09:59:06.967957-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52878 called from <private>
default	09:59:06.968044-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:59:06.969989-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52878 called from <private>
default	09:59:06.970056-0500	runningboardd	Invalidating assertion 398-334-1464843 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:59:06.970403-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52878)
default	09:59:06.970463-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52878 called from <private>
default	09:59:06.970482-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52878 called from <private>
default	09:59:06.971160-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:59:06.971309-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:59:06.971750-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52878)
default	09:59:06.971977-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52878 called from <private>
default	09:59:06.972002-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52878 called from <private>
default	09:59:06.972023-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52878 called from <private>
error	09:59:06.972254-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:59:06.979188-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.979201-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.979212-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.979217-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:06.979223-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:06.979228-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:06.979310-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:06.996117-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464844 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:59:06.997919-0500	runningboardd	Assertion 398-334-1464844 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:59:07.009109-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:59:07.009140-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:59:07.009171-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:59:07.690419-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	09:59:08.199215-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:59:08.199841-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef216","name":"Nexy(37925)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	09:59:08.200073-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:08.200187-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:59:08.200254-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef216, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:59:08.200365-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:59:08.200371-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef216, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 535 stopping recording
default	09:59:08.200429-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	09:59:08.200499-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:08.200588-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:59:08.200887-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	09:59:08.201150-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	09:59:08.201180-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:59:08.201347-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:59:08.201437-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:08.201540-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:59:08.201616-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:59:08.201652-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:08.201694-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	09:59:08.201822-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:59:08.201859-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:08.201889-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	09:59:08.206480-0500	runningboardd	Invalidating assertion 398-334-1464844 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:59:08.215173-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:59:08.215713-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:08.215730-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:08.215744-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:08.215753-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:08.215760-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:08.215769-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:08.215897-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:08.307668-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:08.307698-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:08.307774-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:59:08.307800-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:08.307849-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:59:08.313750-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:59:08.314296-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:59:08.338831-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x90427b840) Selecting device 0 from destructor
default	09:59:08.338852-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x90427b840)
default	09:59:08.338865-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x90427b840) not already running
default	09:59:08.338870-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x90427b840) disconnecting device 91
default	09:59:08.338877-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x90427b840) destroying ioproc 0xa for device 91
default	09:59:08.338921-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:59:08.338963-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:59:08.339159-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x90427b840) nothing to setup
default	09:59:08.339174-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x90427b840) adding 0 device listeners to device 0
default	09:59:08.339183-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x90427b840) adding 0 device delegate listeners to device 0
default	09:59:08.339190-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x90427b840) removing 7 device listeners from device 91
default	09:59:08.339442-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x90427b840) removing 0 device delegate listeners from device 91
default	09:59:08.339457-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x90427b840)
default	09:59:08.477727-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37981.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=37981, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	09:59:08.479162-0500	tccd	AUTHREQ_SUBJECT: msgID=37981.1, subject=com.nexy.assistant,
default	09:59:08.479863-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:08.493674-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.14929, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=37981, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	09:59:08.494507-0500	tccd	AUTHREQ_SUBJECT: msgID=393.14929, subject=com.nexy.assistant,
default	09:59:08.495136-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:08.528553-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:08.546325-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 37932: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 de702200 };
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
default	09:59:08.559158-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	09:59:08.707927-0500	Nexy	[0x903d34640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:59:08.708678-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:59:08.715586-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.2, subject=com.nexy.assistant,
default	09:59:08.716192-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:08.728416-0500	Nexy	[0x903d34640] invalidated after the last release of the connection object
default	09:59:08.729192-0500	Nexy	[0x903d34640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:59:08.729666-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:59:08.730782-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.3, subject=com.nexy.assistant,
default	09:59:08.731429-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:08.742722-0500	Nexy	[0x903d34640] invalidated after the last release of the connection object
default	09:59:09.262548-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef216","name":"Nexy(37925)"}, "details":null }
default	09:59:09.262593-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef216 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":37925})
default	09:59:09.262605-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":37925})
default	09:59:09.263842-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:09.264169-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 535, PID = 37925, Name = sid:0x1ef216, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:59:09.264468-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:09.264702-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:09.264756-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:09.264630-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:09.271385-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:59:09.271570-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:59:09.274086-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52878.52730.0_airpods noise suppression studio::out-0 issue_detected_sample_time=27360.000000 ] -- [ rms:[-40.245979], peaks:[-22.037584] ]
default	09:59:09.274178-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52878.52730.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-39.348717], peaks:[-22.136526] ]
default	09:59:09.280311-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:09.280416-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:09.282426-0500	kernel	Nexy[37925] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xce309a59126913b1. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:59:09.282454-0500	kernel	Nexy[37925] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0xce309a59126913b1. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	09:59:09.439845-0500	Nexy	[0x1056d1780] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	09:59:09.439918-0500	Nexy	[0x1056d1d00] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	09:59:09.525892-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xc7aba0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:59:09.526127-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xc7aba0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:59:09.526339-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xc7aba0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	09:59:09.526545-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xc7aba0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	09:59:09.596925-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	09:59:09.599428-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	09:59:09.600790-0500	Nexy	[0x1056d5030] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	09:59:09.602488-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	09:59:09.603811-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:59:09.603996-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	09:59:09.604132-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	09:59:09.604145-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	09:59:09.604175-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:59:09.604351-0500	Nexy	[0xc7bb14000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:59:09.604402-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	09:59:09.604831-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:59:09.610155-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.1, subject=com.nexy.assistant,
default	09:59:09.610722-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:09.621726-0500	Nexy	[0xc7bb14000] invalidated after the last release of the connection object
default	09:59:09.621860-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:59:09.621890-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	09:59:09.622129-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	09:59:09.623383-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9158, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:09.624201-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9158, subject=com.nexy.assistant,
default	09:59:09.624813-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
error	09:59:09.636178-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	09:59:09.637164-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9160, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:09.638175-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9160, subject=com.nexy.assistant,
default	09:59:09.639144-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:09.652107-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	09:59:09.652126-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xc7abb47e0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	09:59:09.675225-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:59:09.675362-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:59:09.680193-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	09:59:10.423007-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52889)
default	09:59:10.423047-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52889 called from <private>
default	09:59:10.423055-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52889 called from <private>
default	09:59:10.425369-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52890)
default	09:59:10.425384-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52890 called from <private>
default	09:59:10.425390-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52890 called from <private>
default	09:59:10.444983-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52890)
default	09:59:10.445012-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52890 called from <private>
default	09:59:10.445019-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52890 called from <private>
default	09:59:10.446542-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52889)
default	09:59:10.448631-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52889 called from <private>
default	09:59:10.448653-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52889 called from <private>
default	09:59:10.463206-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52889 called from <private>
default	09:59:10.463244-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52889 called from <private>
default	09:59:10.463746-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52889)
default	09:59:10.466933-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52889)
default	09:59:10.467236-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52889 called from <private>
default	09:59:10.467246-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52889 called from <private>
default	09:59:10.467638-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52889 called from <private>
default	09:59:10.467753-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52889 called from <private>
default	09:59:10.467880-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52889)
default	09:59:10.475831-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52889)
default	09:59:10.476000-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52889 called from <private>
default	09:59:10.476021-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52889 called from <private>
default	09:59:10.476171-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52889)
default	09:59:10.478817-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52889)
default	09:59:10.478943-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52889 called from <private>
default	09:59:10.478951-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52889 called from <private>
default	09:59:10.478980-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52889 called from <private>
default	09:59:10.478988-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52889 called from <private>
default	09:59:10.478995-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52889 called from <private>
default	09:59:10.479000-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52889 called from <private>
default	09:59:10.479006-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52889 called from <private>
default	09:59:10.479011-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52889 called from <private>
default	09:59:10.479161-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52889 called from <private>
default	09:59:10.479259-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52889 called from <private>
default	09:59:10.479351-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52889 called from <private>
default	09:59:10.479454-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52889 called from <private>
default	09:59:10.479557-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52889 called from <private>
default	09:59:10.479654-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52889 called from <private>
default	09:59:10.479784-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52889 called from <private>
default	09:59:10.480051-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52889 called from <private>
default	09:59:11.140199-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 828B0210-E105-48D8-8ED4-B7B193C14E37 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54491,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x959a2dee tp_proto=0x06"
default	09:59:11.140280-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54491<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508349 t_state: SYN_SENT process: Nexy:37925 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x90b7bb90
default	09:59:11.155124-0500	kernel	tcp connected: [<IPv4-redacted>:54491<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508349 t_state: ESTABLISHED process: Nexy:37925 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x90b7bb90
default	09:59:11.155416-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54491<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508349 t_state: FIN_WAIT_1 process: Nexy:37925 Duration: 0.015 sec Conn_Time: 0.015 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 15.000 ms rttvar: 7.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x90b7bb90
default	09:59:11.155427-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54491<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5508349 t_state: FIN_WAIT_1 process: Nexy:37925 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	09:59:11.172182-0500	Nexy	[0xc7bb14000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	09:59:11.181168-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xc7b85d540) Selecting device 85 from constructor
default	09:59:11.181180-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc7b85d540)
default	09:59:11.181189-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc7b85d540) not already running
default	09:59:11.181191-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc7b85d540) nothing to teardown
default	09:59:11.181195-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc7b85d540) connecting device 85
default	09:59:11.181283-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc7b85d540) Device ID: 85 (Input:No | Output:Yes): true
default	09:59:11.181396-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc7b85d540) created ioproc 0xa for device 85
default	09:59:11.181499-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc7b85d540) adding 7 device listeners to device 85
default	09:59:11.181658-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc7b85d540) adding 0 device delegate listeners to device 85
default	09:59:11.181668-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc7b85d540)
default	09:59:11.181734-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	09:59:11.181740-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	09:59:11.181745-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	09:59:11.181761-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	09:59:11.181770-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:59:11.181885-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc7b85d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:59:11.181895-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc7b85d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:59:11.181901-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:59:11.181905-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc7b85d540) removing 0 device listeners from device 0
default	09:59:11.181909-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc7b85d540) removing 0 device delegate listeners from device 0
default	09:59:11.181911-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc7b85d540)
default	09:59:11.181926-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	09:59:11.182024-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc7b85d540) caller requesting device change from 85 to 91
default	09:59:11.182033-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc7b85d540)
default	09:59:11.182037-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc7b85d540) not already running
default	09:59:11.182040-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc7b85d540) disconnecting device 85
default	09:59:11.182045-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc7b85d540) destroying ioproc 0xa for device 85
default	09:59:11.182090-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	09:59:11.182610-0500	Nexy	[0xc7bb14280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	09:59:11.183521-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef217","name":"Nexy(37925)"}, "details":{"PID":37925,"session_type":"Primary"} }
default	09:59:11.183604-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":37925}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef217, sessionType: 'prim', isRecording: false }, 
]
default	09:59:11.183945-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xc7abde680 with ID: 0x1ef217
default	09:59:11.184644-0500	Nexy	[0xc7bb143c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	09:59:11.184782-0500	Nexy	No persisted cache on this platform.
error	09:59:11.185116-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=162886634700801 }
default	09:59:11.185129-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	09:59:11.185182-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:59:11.185271-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc7b85d540) connecting device 91
default	09:59:11.185344-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc7b85d540) Device ID: 91 (Input:Yes | Output:No): true
default	09:59:11.186716-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9161, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:11.187899-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9161, subject=com.nexy.assistant,
default	09:59:11.188502-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:11.200525-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc7b85d540) created ioproc 0xa for device 91
default	09:59:11.200648-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc7b85d540) adding 7 device listeners to device 91
default	09:59:11.200800-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc7b85d540) adding 0 device delegate listeners to device 91
default	09:59:11.200807-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc7b85d540)
default	09:59:11.200814-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	09:59:11.200823-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	09:59:11.200936-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	09:59:11.200942-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	09:59:11.200947-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	09:59:11.201029-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc7b85d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	09:59:11.201041-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc7b85d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	09:59:11.201046-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	09:59:11.201050-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc7b85d540) removing 7 device listeners from device 85
default	09:59:11.201234-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc7b85d540) removing 0 device delegate listeners from device 85
default	09:59:11.201241-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc7b85d540)
default	09:59:11.201796-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:59:11.202723-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9162, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:11.203480-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9162, subject=com.nexy.assistant,
default	09:59:11.203999-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:11.215322-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	09:59:11.216332-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9163, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:11.217138-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9163, subject=com.nexy.assistant,
default	09:59:11.217681-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:11.229388-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	09:59:11.230878-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9164, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:11.231648-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9164, subject=com.nexy.assistant,
default	09:59:11.232189-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:11.243563-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:59:11.243709-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:59:11.244995-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:59:11.245429-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf5b62a00] Created node ADM::com.nexy.assistant_52890.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:59:11.245501-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf5b62a00] Created node ADM::com.nexy.assistant_52890.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:59:11.288289-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:59:11.290329-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:59:11.290478-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52890 called from <private>
default	09:59:11.290530-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:59:11.292212-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52890 called from <private>
default	09:59:11.298011-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464848 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:59:11.298556-0500	runningboardd	Assertion 398-334-1464848 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:59:11.299657-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:11.292360-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52890)
default	09:59:11.292376-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52890 called from <private>
default	09:59:11.300245-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:11.292382-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52890 called from <private>
default	09:59:11.292979-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52889)
default	09:59:11.300405-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:59:11.292995-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52889 called from <private>
default	09:59:11.293003-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52889 called from <private>
default	09:59:11.300498-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:11.300956-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
fault	09:59:11.302690-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:59:11.304322-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:59:11.304780-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	09:59:11.305829-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20563096.20563102 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20563096.20563102>
default	09:59:11.309484-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-active (role: Background) (endowments: (null))
default	09:59:11.309917-0500	runningboardd	Invalidating assertion 398-334-1464848 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:59:11.310203-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-active-NotVisible
default	09:59:11.313030-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52890)
default	09:59:11.313368-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52890)
default	09:59:11.313383-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52890)
default	09:59:11.323231-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52889)
default	09:59:11.323309-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52889 called from <private>
default	09:59:11.323575-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52889 called from <private>
default	09:59:11.324496-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52890 called from <private>
default	09:59:11.324517-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52890 called from <private>
default	09:59:11.325002-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52890 called from <private>
default	09:59:11.325038-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52890 called from <private>
default	09:59:11.325056-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52890 called from <private>
default	09:59:11.325073-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52890 called from <private>
default	09:59:11.325100-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52890 called from <private>
default	09:59:11.325913-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52889 called from <private>
default	09:59:11.325932-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52889 called from <private>
default	09:59:11.326849-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:59:11.326930-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:59:11.326986-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:59:11.327303-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef217","name":"Nexy(37925)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	09:59:11.327380-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	09:59:11.327425-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:59:11.327501-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef217, Nexy(37925), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	09:59:11.327595-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:11.327678-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:11.327789-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:59:11.327929-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	09:59:11.327959-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef217, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 536 starting recording
default	09:59:11.327974-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:11.327796-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:11.328197-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:11.328125-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:11.328212-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:59:11.328279-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef217, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:59:11.329134-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.329178-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.329256-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.329304-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.329376-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.328385-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:59:11.329421-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:11.330241-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
error	09:59:11.339212-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:59:11.339179-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:59:11.340594-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.340627-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.340645-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.340652-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.340660-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.340666-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:11.341561-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:11.342592-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	09:59:11.340905-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52889)
default	09:59:11.344407-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52889)
default	09:59:11.342633-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:59:11.350622-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.350801-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.350794-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:11.351252-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.351468-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.351609-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.351691-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:11.351762-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:11.352396-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.9165, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	09:59:11.362348-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52889 called from <private>
default	09:59:11.362404-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52889 called from <private>
default	09:59:11.362540-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52889 called from <private>
default	09:59:11.362569-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52889 called from <private>
default	09:59:11.362668-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52889)
default	09:59:11.362907-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52889)
default	09:59:11.363147-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52889 called from <private>
default	09:59:11.363162-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52889 called from <private>
default	09:59:11.363428-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52889)
default	09:59:11.374867-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	09:59:11.375026-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	09:59:11.376597-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464849 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:59:11.376686-0500	runningboardd	Assertion 398-334-1464849 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:59:11.383138-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52890 called from <private>
default	09:59:11.383438-0500	runningboardd	Invalidating assertion 398-334-1464849 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:59:11.383618-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52890)
default	09:59:11.383717-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52890 called from <private>
default	09:59:11.383750-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52890 called from <private>
default	09:59:11.384080-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:59:11.384222-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:59:11.384613-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52890)
default	09:59:11.384812-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52890 called from <private>
default	09:59:11.384829-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52890 called from <private>
default	09:59:11.384890-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52890 called from <private>
error	09:59:11.385154-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:59:11.389535-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:11.404470-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	09:59:11.406054-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf61fe100] Created node ADM::com.nexy.assistant_52890.52730.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	09:59:11.406116-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf61fe100] Created node ADM::com.nexy.assistant_52890.52730.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	09:59:11.416410-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:11.416424-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:11.416475-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:59:11.416486-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:11.416507-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:59:11.420778-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:59:11.421403-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:59:11.421935-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.421946-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.421955-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.421961-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.421966-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.421972-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:11.422039-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:11.446440-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	09:59:11.449839-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464850 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:59:11.452197-0500	runningboardd	Assertion 398-334-1464850 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:59:11.452671-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:11.452682-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:11.452737-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: Background
default	09:59:11.452786-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:11.452877-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52890 called from <private>
default	09:59:11.452949-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52890 called from <private>
default	09:59:11.452846-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:59:11.453011-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	09:59:11.455423-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52890 called from <private>
default	09:59:11.455780-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52890)
default	09:59:11.455822-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52890 called from <private>
default	09:59:11.455832-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52890 called from <private>
default	09:59:11.456478-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	09:59:11.456640-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	09:59:11.457180-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52890)
default	09:59:11.457561-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52890 called from <private>
default	09:59:11.457613-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52890 called from <private>
default	09:59:11.457640-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52890 called from <private>
error	09:59:11.457849-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	09:59:11.461733-0500	tccd	AUTHREQ_SUBJECT: msgID=401.9167, subject=com.nexy.assistant,
default	09:59:11.462680-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x983168900 at /Applications/Nexy.app
default	09:59:11.482048-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20563096.20563102(501)>:37925] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1464851 target:37925 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	09:59:11.484930-0500	runningboardd	Assertion 398-334-1464851 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) will be created as active
default	09:59:11.486170-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52890 called from <private>
default	09:59:11.496699-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	09:59:11.496752-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	09:59:11.496793-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	09:59:11.497179-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.497189-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.497201-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.497214-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.497220-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.497226-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:11.497262-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.497297-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.497327-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.497356-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:11.497364-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:11.497370-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:11.497524-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:12.799572-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:59:12.800041-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef217","name":"Nexy(37925)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	09:59:12.800215-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:12.800292-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	09:59:12.800338-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef217, Nexy(37925), 'prim'', displayID:'com.nexy.assistant'}
default	09:59:12.800415-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	09:59:12.800420-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef217, Nexy(37925), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 536 stopping recording
default	09:59:12.800455-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	09:59:12.800506-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	09:59:12.800549-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 536, PID = 37925, Name = sid:0x1ef217, Nexy(37925), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	09:59:12.800812-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	09:59:12.801002-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	09:59:12.801048-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	09:59:12.801143-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:59:12.801203-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:12.801275-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	09:59:12.801317-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	09:59:12.801342-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	09:59:12.801393-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:12.801464-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	09:59:12.801496-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	09:59:12.801512-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	09:59:12.805013-0500	runningboardd	Invalidating assertion 398-334-1464851 (target:[app<application.com.nexy.assistant.20563096.20563102(501)>:37925]) from originator [osservice<com.apple.powerd>:334]
default	09:59:12.812398-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	09:59:12.812983-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:12.812999-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:12.813014-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:12.813023-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	09:59:12.813031-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	09:59:12.813043-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	09:59:12.813183-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	09:59:12.911556-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring jetsam update because this process is not memory-managed
default	09:59:12.911566-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring suspend because this process is not lifecycle managed
default	09:59:12.911619-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Set darwin role to: None
default	09:59:12.911632-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring GPU update because this process is not GPU managed
default	09:59:12.911649-0500	runningboardd	[app<application.com.nexy.assistant.20563096.20563102(501)>:37925] Ignoring memory limit update because this process is not memory-managed
default	09:59:12.915186-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20563096.20563102(501)>: running-suspended (role: None) (endowments: (null))
default	09:59:12.916220-0500	gamepolicyd	Received state update for 37925 (app<application.com.nexy.assistant.20563096.20563102(501)>, running-suspended-NotVisible
default	09:59:12.985529-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc7b85d540) Selecting device 0 from destructor
default	09:59:12.985555-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc7b85d540)
default	09:59:12.985565-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc7b85d540) not already running
default	09:59:12.985573-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc7b85d540) disconnecting device 91
default	09:59:12.985583-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc7b85d540) destroying ioproc 0xa for device 91
default	09:59:12.985630-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	09:59:12.985676-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	09:59:12.985917-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xc7b85d540) nothing to setup
default	09:59:12.985930-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc7b85d540) adding 0 device listeners to device 0
default	09:59:12.985938-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc7b85d540) adding 0 device delegate listeners to device 0
default	09:59:12.985945-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc7b85d540) removing 7 device listeners from device 91
default	09:59:12.986212-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc7b85d540) removing 0 device delegate listeners from device 91
default	09:59:12.986231-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc7b85d540)
default	09:59:13.115858-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37984.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=37984, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	09:59:13.117326-0500	tccd	AUTHREQ_SUBJECT: msgID=37984.1, subject=com.nexy.assistant,
default	09:59:13.118052-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:13.131957-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.14930, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=37984, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	09:59:13.132924-0500	tccd	AUTHREQ_SUBJECT: msgID=393.14930, subject=com.nexy.assistant,
default	09:59:13.133621-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:13.168059-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:13.186409-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 37932: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 e6702200 };
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
default	09:59:13.199098-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	09:59:13.342987-0500	Nexy	[0xc7bb14640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:59:13.343712-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:59:13.350779-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.2, subject=com.nexy.assistant,
default	09:59:13.351433-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:13.363609-0500	Nexy	[0xc7bb14640] invalidated after the last release of the connection object
default	09:59:13.364347-0500	Nexy	[0xc7bb14640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	09:59:13.364856-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=37925.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=37925, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	09:59:13.366122-0500	tccd	AUTHREQ_SUBJECT: msgID=37925.3, subject=com.nexy.assistant,
default	09:59:13.366784-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	09:59:13.378473-0500	Nexy	[0xc7bb14640] invalidated after the last release of the connection object
