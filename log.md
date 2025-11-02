default	13:45:18.308541-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:45:18.308640-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:45:18.309813-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:45:18.312195-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:45:18.314058-0500	runningboardd	Launch request for app<application.com.nexy.assistant.20102073.20102079(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:45:18.314111-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.20102073.20102079(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:95465] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-95465-1137121 target:app<application.com.nexy.assistant.20102073.20102079(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:45:18.314162-0500	runningboardd	Assertion 398-95465-1137121 (target:app<application.com.nexy.assistant.20102073.20102079(501)>) will be created as active
default	13:45:18.316865-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:45:18.316900-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.20102073.20102079(501)>
default	13:45:18.316914-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:45:18.316968-0500	runningboardd	app<application.com.nexy.assistant.20102073.20102079(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:45:18.345549-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] is not RunningBoard jetsam managed.
default	13:45:18.345556-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] This process will not be managed.
default	13:45:18.345562-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.20102073.20102079(501)>:25685]
default	13:45:18.345688-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:18.346474-0500	gamepolicyd	Hit the server for a process handle c2ca93000006455 that resolved to: [app<application.com.nexy.assistant.20102073.20102079(501)>:25685]
default	13:45:18.346496-0500	gamepolicyd	Received state update for 25685 (app<application.com.nexy.assistant.20102073.20102079(501)>, running-active-NotVisible
default	13:45:18.348980-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.20102073.20102079(501)>:25685]
default	13:45:18.349021-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079(501)>:25685] from originator [app<application.com.nexy.assistant.20102073.20102079(501)>:25685] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-1137122 target:25685 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:18.349088-0500	runningboardd	Assertion 398-398-1137122 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) will be created as active
default	13:45:18.349204-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring jetsam update because this process is not memory-managed
default	13:45:18.349215-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring suspend because this process is not lifecycle managed
default	13:45:18.349241-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Set darwin role to: UserInteractive
default	13:45:18.349272-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring GPU update because this process is not GPU managed
default	13:45:18.349318-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] reported to RB as running
default	13:45:18.349400-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring memory limit update because this process is not memory-managed
default	13:45:18.350157-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079(501)>:25685] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:25685" ID:398-363-1137123 target:25685 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:45:18.350264-0500	runningboardd	Assertion 398-363-1137123 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) will be created as active
default	13:45:18.350158-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x1271270 com.nexy.assistant starting stopped process.
default	13:45:18.350951-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:45:18.351087-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:45:18.353089-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring jetsam update because this process is not memory-managed
default	13:45:18.353120-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring suspend because this process is not lifecycle managed
default	13:45:18.353153-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring GPU update because this process is not GPU managed
default	13:45:18.353214-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring memory limit update because this process is not memory-managed
default	13:45:18.353298-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.20102073.20102079(501)>:25685]
default	13:45:18.354866-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:18.355055-0500	runningboardd	Invalidating assertion 398-95465-1137121 (target:app<application.com.nexy.assistant.20102073.20102079(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:95465]
default	13:45:18.355092-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring jetsam update because this process is not memory-managed
default	13:45:18.355124-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring suspend because this process is not lifecycle managed
default	13:45:18.355165-0500	gamepolicyd	Received state update for 25685 (app<application.com.nexy.assistant.20102073.20102079(501)>, running-active-NotVisible
default	13:45:18.355149-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring GPU update because this process is not GPU managed
default	13:45:18.355282-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring memory limit update because this process is not memory-managed
default	13:45:18.357760-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:18.378745-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring jetsam update because this process is not memory-managed
default	13:45:18.378768-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring suspend because this process is not lifecycle managed
default	13:45:18.378798-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring GPU update because this process is not GPU managed
default	13:45:18.378869-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring memory limit update because this process is not memory-managed
default	13:45:18.387145-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:18.461816-0500	gamepolicyd	Received state update for 25685 (app<application.com.nexy.assistant.20102073.20102079(501)>, running-active-NotVisible
default	13:45:18.492522-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	13:45:18.496968-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=511.122, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	13:45:18.500169-0500	tccd	AUTHREQ_SUBJECT: msgID=511.122, subject=com.nexy.assistant,
default	13:45:18.500540-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	13:45:18.755955-0500	Nexy	[0x1037f9370] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:45:18.755990-0500	Nexy	[0x1037f98b0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	13:45:18.836719-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x993ac00e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:45:18.836843-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x993ac00e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:45:18.836954-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x993ac00e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:45:18.837059-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x993ac00e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:45:18.890587-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:45:18.891979-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:45:18.892714-0500	Nexy	[0x103806140] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:45:18.894673-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20102073.20102079 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20102073.20102079>
default	13:45:18.897068-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:45:18.898578-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:45:18.898672-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:45:18.898751-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:45:18.898756-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:45:18.898773-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:45:18.898863-0500	Nexy	[0x994058000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:45:18.898988-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:45:18.899107-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25685.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:45:18.902338-0500	tccd	AUTHREQ_SUBJECT: msgID=25685.1, subject=com.nexy.assistant,
default	13:45:18.902642-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:18.909178-0500	Nexy	[0x994058000] invalidated after the last release of the connection object
default	13:45:18.909203-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:45:18.909364-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	13:45:18.910181-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6326, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:18.910731-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6326, subject=com.nexy.assistant,
default	13:45:18.911381-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
error	13:45:18.921133-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:45:18.921654-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6328, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:18.922101-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6328, subject=com.nexy.assistant,
default	13:45:18.922394-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:18.930545-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:45:18.930555-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x992a58bc0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	13:45:18.942394-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	13:45:18.942399-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	13:45:18.944190-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:45:18.944271-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:45:18.947897-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:45:20.218832-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid C9FAA19A-0815-4D0B-9DD5-A9FF3FC5C5F3 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52017,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x64a3391b tp_proto=0x06"
default	13:45:20.218866-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52017<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385488 t_state: SYN_SENT process: Nexy:25685 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa674f0c6
default	13:45:20.219332-0500	kernel	tcp connected: [<IPv4-redacted>:52017<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385488 t_state: ESTABLISHED process: Nexy:25685 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa674f0c6
default	13:45:20.219527-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52017<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385488 t_state: FIN_WAIT_1 process: Nexy:25685 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xa674f0c6
default	13:45:20.219532-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52017<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385488 t_state: FIN_WAIT_1 process: Nexy:25685 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:45:20.234165-0500	Nexy	[0x994058000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:45:20.240272-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x991de8e40) Selecting device 83 from constructor
default	13:45:20.240278-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x991de8e40)
default	13:45:20.240282-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x991de8e40) not already running
default	13:45:20.240283-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x991de8e40) nothing to teardown
default	13:45:20.240286-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x991de8e40) connecting device 83
default	13:45:20.240329-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x991de8e40) Device ID: 83 (Input:No | Output:Yes): true
default	13:45:20.240382-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x991de8e40) created ioproc 0xa for device 83
default	13:45:20.240436-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de8e40) adding 7 device listeners to device 83
default	13:45:20.240518-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de8e40) adding 0 device delegate listeners to device 83
default	13:45:20.240521-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x991de8e40)
default	13:45:20.240556-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:45:20.240564-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:45:20.240569-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:45:20.240572-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:45:20.240576-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:45:20.240619-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x991de8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:45:20.240626-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x991de8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:45:20.240629-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:45:20.240632-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de8e40) removing 0 device listeners from device 0
default	13:45:20.240634-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de8e40) removing 0 device delegate listeners from device 0
default	13:45:20.240637-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x991de8e40)
default	13:45:20.240643-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:45:20.240683-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x991de8e40) caller requesting device change from 83 to 89
default	13:45:20.240686-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x991de8e40)
default	13:45:20.240689-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x991de8e40) not already running
default	13:45:20.240689-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x991de8e40) disconnecting device 83
default	13:45:20.240691-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x991de8e40) destroying ioproc 0xa for device 83
default	13:45:20.240715-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:45:20.241272-0500	Nexy	[0x994058280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:45:20.241660-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef14c","name":"Nexy(25685)"}, "details":{"PID":25685,"session_type":"Primary"} }
default	13:45:20.241707-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":25685}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef14c, sessionType: 'prim', isRecording: false }, 
]
default	13:45:20.242021-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 25685, name = Nexy
default	13:45:20.242134-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x992a82660 with ID: 0x1ef14c
default	13:45:20.242656-0500	Nexy	[0x9940583c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	13:45:20.242724-0500	Nexy	No persisted cache on this platform.
error	13:45:20.242885-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=110316234997761 }
default	13:45:20.242892-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	13:45:20.242918-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:45:20.242961-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x991de8e40) connecting device 89
default	13:45:20.243001-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x991de8e40) Device ID: 89 (Input:Yes | Output:No): true
default	13:45:20.243590-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6329, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:20.244098-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6329, subject=com.nexy.assistant,
default	13:45:20.244400-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:20.250673-0500	tccd	AUTHREQ_PROMPTING: msgID=401.6329, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	13:45:22.046683-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	13:45:22.047667-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x991de8e40) created ioproc 0xa for device 89
default	13:45:22.047902-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de8e40) adding 7 device listeners to device 89
default	13:45:22.048141-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de8e40) adding 0 device delegate listeners to device 89
default	13:45:22.048154-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x991de8e40)
default	13:45:22.048166-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	13:45:22.048182-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:45:22.048362-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	13:45:22.048377-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	13:45:22.048383-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:45:22.048501-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x991de8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:45:22.048517-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x991de8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:45:22.048526-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:45:22.048492-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	13:45:22.048547-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de8e40) removing 7 device listeners from device 83
default	13:45:22.048814-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de8e40) removing 0 device delegate listeners from device 83
default	13:45:22.048832-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x991de8e40)
default	13:45:22.049947-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:45:22.051424-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6330, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:22.052731-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6330, subject=com.nexy.assistant,
default	13:45:22.054358-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:22.072685-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:45:22.073865-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6331, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:22.074774-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6331, subject=com.nexy.assistant,
default	13:45:22.075304-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:22.087788-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:45:22.089036-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6332, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:22.090821-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6332, subject=com.nexy.assistant,
default	13:45:22.091490-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:22.102865-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:45:22.103070-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:45:22.103162-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:45:22.103276-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:45:22.105515-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:45:22.105961-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:45:22.107562-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d83900] Created node ADM::com.nexy.assistant_44586.44378.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:45:22.107603-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d83900] Created node ADM::com.nexy.assistant_44586.44378.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:45:22.178817-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:45:22.180059-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:45:22.180035-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:44586 called from <private>
default	13:45:22.181041-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44586 called from <private>
default	13:45:22.181107-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44586)
default	13:45:22.183290-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:45:22.182477-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079(501)>:25685] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137145 target:25685 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:22.183026-0500	runningboardd	Assertion 398-334-1137145 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) will be created as active
default	13:45:22.181117-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44586 called from <private>
default	13:45:22.181121-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44586 called from <private>
default	13:45:22.183227-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:22.183234-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44585 called from <private>
default	13:45:22.183238-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44585 called from <private>
default	13:45:22.184649-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring jetsam update because this process is not memory-managed
default	13:45:22.186317-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:45:22.184927-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring suspend because this process is not lifecycle managed
default	13:45:22.186261-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring GPU update because this process is not GPU managed
default	13:45:22.188451-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring memory limit update because this process is not memory-managed
default	13:45:22.189480-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44586)
default	13:45:22.189490-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44586)
default	13:45:22.189491-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44586 called from <private>
default	13:45:22.189496-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44586 called from <private>
default	13:45:22.189496-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44586)
default	13:45:22.189500-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44586 called from <private>
default	13:45:22.189502-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44586)
default	13:45:22.189503-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44586 called from <private>
default	13:45:22.189568-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44586 called from <private>
default	13:45:22.189594-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44586 called from <private>
default	13:45:22.189621-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44586 called from <private>
default	13:45:22.189666-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44586 called from <private>
default	13:45:22.190049-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44586 called from <private>
default	13:45:22.190071-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44586 called from <private>
default	13:45:22.190895-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14c","name":"Nexy(25685)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:45:22.190943-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:45:22.190970-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:45:22.191148-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:22.191013-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef14c, Nexy(25685), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:45:22.191035-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:22.191030-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:22.191111-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:45:22.191251-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:45:22.191303-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14c, Nexy(25685), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 333 starting recording
default	13:45:22.191437-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:22.191250-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:22.191459-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:22.191703-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:45:22.191709-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:45:22.191529-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:45:22.191606-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14c, Nexy(25685), 'prim'', displayID:'com.nexy.assistant'}
default	13:45:22.191693-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
fault	13:45:22.200839-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20102073.20102079 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20102073.20102079>
default	13:45:22.202634-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:22.204765-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:22.202639-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:22.204432-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:22.207137-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:22.207181-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:22.207446-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:22.207451-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:22.214272-0500	runningboardd	Invalidating assertion 398-334-1137145 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) from originator [osservice<com.apple.powerd>:334]
default	13:45:22.207887-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:22.207962-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44586)
default	13:45:22.208256-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:22.210158-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6333, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:22.208306-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44586 called from <private>
default	13:45:22.215394-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:22.215403-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:22.215873-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44585 called from <private>
default	13:45:22.215878-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44585 called from <private>
default	13:45:22.215930-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
fault	13:45:22.216669-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20102073.20102079 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20102073.20102079>
default	13:45:22.217732-0500	gamepolicyd	Received state update for 25685 (app<application.com.nexy.assistant.20102073.20102079(501)>, running-active-NotVisible
default	13:45:22.217358-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6333, subject=com.nexy.assistant,
default	13:45:22.218458-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:22.223141-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:22.223331-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44585 called from <private>
default	13:45:22.223336-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44585 called from <private>
default	13:45:22.223412-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:22.228720-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:22.228857-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:22.228872-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:22.228889-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:22.228894-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:22.228898-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:22.228900-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:22.228903-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44585 called from <private>
default	13:45:22.228933-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44585 called from <private>
default	13:45:22.229116-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44585 called from <private>
default	13:45:22.229168-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44585 called from <private>
default	13:45:22.229217-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44585 called from <private>
default	13:45:22.229248-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44585 called from <private>
default	13:45:22.229315-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44585 called from <private>
default	13:45:22.229367-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44585 called from <private>
default	13:45:22.229428-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44585 called from <private>
default	13:45:22.229515-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44585 called from <private>
default	13:45:22.229578-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44585 called from <private>
default	13:45:22.229640-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44585 called from <private>
default	13:45:22.229686-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44585 called from <private>
default	13:45:22.229734-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44585 called from <private>
default	13:45:22.241292-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:22.241753-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:22.252459-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:45:22.253911-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:44586 called from <private>
default	13:45:22.253947-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:44586 called from <private>
default	13:45:22.257145-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:22.257330-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44586)
default	13:45:22.263644-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6334, subject=com.nexy.assistant,
default	13:45:22.263998-0500	runningboardd	Invalidating assertion 398-334-1137146 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) from originator [osservice<com.apple.powerd>:334]
default	13:45:22.264671-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:22.272963-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:22.294424-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.294430-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.294476-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.294508-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.294534-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.294569-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:22.294663-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:22.297169-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:45:22.298048-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079(501)>:25685] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137149 target:25685 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:22.298115-0500	runningboardd	Assertion 398-334-1137149 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) will be created as active
default	13:45:22.299725-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:44586 called from <private>
default	13:45:22.299748-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:44586 called from <private>
default	13:45:22.300450-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:45:22.301768-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44586 called from <private>
default	13:45:22.301995-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44586)
default	13:45:22.302023-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44586 called from <private>
default	13:45:22.302401-0500	runningboardd	Invalidating assertion 398-334-1137149 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) from originator [osservice<com.apple.powerd>:334]
default	13:45:22.302031-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44586 called from <private>
default	13:45:22.302942-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:45:22.303029-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:45:22.303474-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44586)
default	13:45:22.303571-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44586 called from <private>
default	13:45:22.303577-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44586 called from <private>
default	13:45:22.303586-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44586 called from <private>
default	13:45:22.304609-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6335, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:22.305736-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6335, subject=com.nexy.assistant,
default	13:45:22.306488-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:22.309355-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:45:22.309756-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:45:22.310373-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:22.310888-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:22.310981-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.310992-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.311005-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.311012-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.311027-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.311034-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:22.311618-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:22.311661-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.311719-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.311804-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.311849-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.311907-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.311985-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:22.312417-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:22.318631-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079(501)>:25685] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137150 target:25685 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:22.318670-0500	runningboardd	Assertion 398-334-1137150 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) will be created as active
default	13:45:22.325843-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:22.326078-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.326085-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.326091-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.326093-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.326098-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.326102-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:22.326153-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.326195-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.326229-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.326268-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.326303-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.326328-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:22.326466-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:45:22.326420-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.326633-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.326667-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.326785-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:22.326935-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:22.326961-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:22.327274-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:22.419250-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	13:45:23.347934-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:45:23.348237-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14c","name":"Nexy(25685)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:45:23.348329-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:23.348376-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:45:23.348411-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14c, Nexy(25685), 'prim'', displayID:'com.nexy.assistant'}
default	13:45:23.348454-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:45:23.348458-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14c, Nexy(25685), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 333 stopping recording
default	13:45:23.348479-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:45:23.348506-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:23.348654-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:45:23.348721-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:45:23.348565-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:45:23.348731-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:45:23.349232-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:23.349261-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:23.349276-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:45:23.349329-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:45:23.349077-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:23.349348-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:23.349395-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:23.349186-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:23.349426-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:45:23.352124-0500	runningboardd	Invalidating assertion 398-334-1137150 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) from originator [osservice<com.apple.powerd>:334]
default	13:45:23.353425-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:23.356235-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:23.356251-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:23.356268-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:23.356276-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:23.356282-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:23.356288-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:23.356369-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:23.376039-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring jetsam update because this process is not memory-managed
default	13:45:23.376049-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring suspend because this process is not lifecycle managed
default	13:45:23.376065-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring GPU update because this process is not GPU managed
default	13:45:23.376101-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring memory limit update because this process is not memory-managed
default	13:45:23.379261-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:23.379457-0500	runningboardd	Assertion did invalidate due to timeout: 398-398-1137122 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685])
default	13:45:23.382529-0500	gamepolicyd	Received state update for 25685 (app<application.com.nexy.assistant.20102073.20102079(501)>, running-active-NotVisible
default	13:45:23.449845-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x991de8e40) Selecting device 0 from destructor
default	13:45:23.449860-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x991de8e40)
default	13:45:23.449867-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x991de8e40) not already running
default	13:45:23.449872-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x991de8e40) disconnecting device 89
default	13:45:23.449879-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x991de8e40) destroying ioproc 0xa for device 89
default	13:45:23.449909-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:45:23.449944-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:45:23.450104-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x991de8e40) nothing to setup
default	13:45:23.450119-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de8e40) adding 0 device listeners to device 0
default	13:45:23.450128-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de8e40) adding 0 device delegate listeners to device 0
default	13:45:23.450135-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de8e40) removing 7 device listeners from device 89
default	13:45:23.450345-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de8e40) removing 0 device delegate listeners from device 89
default	13:45:23.450359-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x991de8e40)
default	13:45:23.581470-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring jetsam update because this process is not memory-managed
default	13:45:23.581480-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring suspend because this process is not lifecycle managed
default	13:45:23.581485-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring GPU update because this process is not GPU managed
default	13:45:23.581497-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring memory limit update because this process is not memory-managed
default	13:45:23.585066-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:23.585422-0500	gamepolicyd	Received state update for 25685 (app<application.com.nexy.assistant.20102073.20102079(501)>, running-active-NotVisible
default	13:45:23.649408-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25689.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=25689, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:45:23.651211-0500	tccd	AUTHREQ_SUBJECT: msgID=25689.1, subject=com.nexy.assistant,
default	13:45:23.652034-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	13:45:23.659898-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12290, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=25689, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:45:23.660424-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12290, subject=com.nexy.assistant,
default	13:45:23.660784-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	13:45:23.678193-0500	launchservicesd	CHECKIN:0x0-0x1271270 25689 com.nexy.assistant
default	13:45:23.679194-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:45:23.679285-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:45:23.680107-0500	runningboardd	Invalidating assertion 398-363-1137123 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	13:45:23.681018-0500	WindowServer	e290f[CreateApplication]: Process creation: 0x0-0x1271270 (Nexy) connectionID: E290F pid: 25689 in session 0x101
default	13:45:23.682753-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:45:23.686779-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	13:45:23.713706-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring jetsam update because this process is not memory-managed
default	13:45:23.713730-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring suspend because this process is not lifecycle managed
default	13:45:23.713793-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Set darwin role to: None
default	13:45:23.713861-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring GPU update because this process is not GPU managed
default	13:45:23.713924-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring memory limit update because this process is not memory-managed
default	13:45:23.718004-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079(501)>: running-suspended (role: None) (endowments: (null))
default	13:45:23.718236-0500	gamepolicyd	Received state update for 25685 (app<application.com.nexy.assistant.20102073.20102079(501)>, running-suspended-NotVisible
default	13:45:23.809472-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 25690: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 6f671a00 };
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
default	13:45:23.819097-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:45:23.857274-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x1271270} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:45:23.857291-0500	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 19337840
default	13:45:23.857698-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x1271270 (Nexy) connectionID: E290F pid: 25689 in session 0x101
default	13:45:23.857331-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:45:23.857731-0500	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x1271270 (Nexy) acq:0x801dacd20 count:1
default	13:45:23.858625-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x1271270 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1271270 (Nexy)"
)}
default	13:45:23.858876-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x6459 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1271270 (Nexy)"
)}
default	13:45:23.969821-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x991de9c40) Selecting device 83 from constructor
default	13:45:23.969826-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x991de9c40)
default	13:45:23.969830-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x991de9c40) not already running
default	13:45:23.969834-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x991de9c40) nothing to teardown
default	13:45:23.969835-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x991de9c40) connecting device 83
default	13:45:23.969882-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x991de9c40) Device ID: 83 (Input:No | Output:Yes): true
default	13:45:23.969948-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x991de9c40) created ioproc 0xb for device 83
default	13:45:23.970031-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de9c40) adding 7 device listeners to device 83
default	13:45:23.970156-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de9c40) adding 0 device delegate listeners to device 83
default	13:45:23.970163-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x991de9c40)
default	13:45:23.970207-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  24000 Hz, Float32, interleaved
default	13:45:23.970212-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:45:23.970218-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	13:45:23.970222-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:45:23.970227-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:45:23.970283-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x991de9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:45:23.970288-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x991de9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:45:23.970292-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:45:23.970293-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de9c40) removing 0 device listeners from device 0
default	13:45:23.970297-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de9c40) removing 0 device delegate listeners from device 0
default	13:45:23.970299-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x991de9c40)
default	13:45:23.970305-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:45:23.970349-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x991de9c40) caller requesting device change from 83 to 89
default	13:45:23.970354-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x991de9c40)
default	13:45:23.970356-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x991de9c40) not already running
default	13:45:23.970359-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x991de9c40) disconnecting device 83
default	13:45:23.970361-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x991de9c40) destroying ioproc 0xb for device 83
default	13:45:23.970371-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	13:45:23.970382-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:45:23.970432-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x991de9c40) connecting device 89
default	13:45:23.970487-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x991de9c40) Device ID: 89 (Input:Yes | Output:No): true
default	13:45:23.971139-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6336, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:23.971653-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6336, subject=com.nexy.assistant,
default	13:45:23.971951-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:23.978805-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x991de9c40) created ioproc 0xb for device 89
default	13:45:23.978883-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de9c40) adding 7 device listeners to device 89
default	13:45:23.978988-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de9c40) adding 0 device delegate listeners to device 89
default	13:45:23.978992-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x991de9c40)
default	13:45:23.978996-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	13:45:23.979002-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:45:23.979073-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	13:45:23.979078-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	13:45:23.979080-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:45:23.979129-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x991de9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:45:23.979134-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x991de9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:45:23.979136-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:45:23.979140-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de9c40) removing 7 device listeners from device 83
default	13:45:23.979233-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de9c40) removing 0 device delegate listeners from device 83
default	13:45:23.979238-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x991de9c40)
default	13:45:23.979582-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:45:23.980154-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6337, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:23.980570-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6337, subject=com.nexy.assistant,
default	13:45:23.980851-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:23.987449-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:45:23.987498-0500	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0x992a69ad0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	13:45:23.987613-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:45:23.988147-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6338, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:23.988492-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6338, subject=com.nexy.assistant,
default	13:45:23.989283-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:23.996536-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6339, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:23.997078-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6339, subject=com.nexy.assistant,
default	13:45:23.997739-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9b00 at /Applications/Nexy.app
default	13:45:24.007590-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14c","name":"Nexy(25685)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:45:24.007630-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:45:24.007648-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef14c, Nexy(25685), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	13:45:24.007664-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:45:24.010094-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:24.010184-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:45:24.009944-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef14c, Nexy(25685), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:45:24.006727-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:45:24.010318-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:45:24.010282-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079(501)>:25685] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137164 target:25685 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:24.010340-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14c, Nexy(25685), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 333 starting recording
default	13:45:24.010343-0500	runningboardd	Assertion 398-334-1137164 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) will be created as active
default	13:45:24.010481-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:24.010592-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:45:24.010715-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14c, Nexy(25685), 'prim'', displayID:'com.nexy.assistant'}
default	13:45:24.010809-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring jetsam update because this process is not memory-managed
default	13:45:24.010874-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring suspend because this process is not lifecycle managed
default	13:45:24.010936-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Set darwin role to: Background
default	13:45:24.010996-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring GPU update because this process is not GPU managed
default	13:45:24.010854-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:45:24.010860-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:45:24.011177-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:45:24.011073-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring memory limit update because this process is not memory-managed
default	13:45:24.010955-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:45:24.011477-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:24.011503-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:24.011576-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:24.011396-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:24.011656-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:24.011821-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:24.012006-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:24.012037-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	13:45:24.012048-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	13:45:24.012090-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	13:45:24.011456-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:24.011497-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
error	13:45:24.012168-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	13:45:24.012253-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:45:24.015657-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:45:24.015681-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:45:24.015701-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:24.015975-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:24.016016-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:24.016069-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:24.016105-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:24.016222-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:24.016277-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:24.016309-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:24.016366-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:24.016432-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:45:24.016412-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:24.016474-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:24.016938-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079(501)>: running-active (role: Background) (endowments: (null))
default	13:45:24.016508-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:24.017016-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:24.017323-0500	gamepolicyd	Received state update for 25685 (app<application.com.nexy.assistant.20102073.20102079(501)>, running-active-NotVisible
default	13:45:24.017147-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:24.017288-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:24.017421-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:24.017453-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:24.017487-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:24.017528-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:24.017743-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:25.419199-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	13:45:28.419215-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	13:45:31.412841-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	13:45:32.987322-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_44586.44378.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-55.348572], peaks:[-15.412088] ]
default	13:45:32.990436-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_44586.44378.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-55.143623], peaks:[-12.849987] ]
default	13:45:34.404706-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	13:45:37.118340-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:45:37.118851-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14c","name":"Nexy(25685)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:45:37.119054-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:37.119155-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:45:37.119204-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14c, Nexy(25685), 'prim'', displayID:'com.nexy.assistant'}
default	13:45:37.119273-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:45:37.119299-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14c, Nexy(25685), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 333 stopping recording
default	13:45:37.119337-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:45:37.119378-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:37.119425-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:45:37.119668-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:45:37.119995-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:37.120057-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:37.120135-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:37.120177-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:37.120213-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:45:37.120234-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:37.120327-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:45:37.120347-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:37.120361-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:45:37.120615-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:45:37.120652-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:45:37.125073-0500	runningboardd	Invalidating assertion 398-334-1137164 (target:[app<application.com.nexy.assistant.20102073.20102079(501)>:25685]) from originator [osservice<com.apple.powerd>:334]
default	13:45:37.127132-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:37.129489-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:37.129503-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:37.129518-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:37.129525-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:37.129534-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:37.129542-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:37.129652-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:37.231630-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring jetsam update because this process is not memory-managed
default	13:45:37.231654-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring suspend because this process is not lifecycle managed
default	13:45:37.231717-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Set darwin role to: None
default	13:45:37.231736-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring GPU update because this process is not GPU managed
default	13:45:37.231846-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] Ignoring memory limit update because this process is not memory-managed
default	13:45:37.236078-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079(501)>: running-suspended (role: None) (endowments: (null))
default	13:45:37.236705-0500	gamepolicyd	Received state update for 25685 (app<application.com.nexy.assistant.20102073.20102079(501)>, running-suspended-NotVisible
default	13:45:37.307596-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x991de9c40) Selecting device 0 from destructor
default	13:45:37.307631-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x991de9c40)
default	13:45:37.307647-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x991de9c40) not already running
default	13:45:37.307661-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x991de9c40) disconnecting device 89
default	13:45:37.307677-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x991de9c40) destroying ioproc 0xb for device 89
default	13:45:37.307739-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:45:37.307807-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:45:37.308145-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x991de9c40) nothing to setup
default	13:45:37.308176-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de9c40) adding 0 device listeners to device 0
default	13:45:37.308192-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x991de9c40) adding 0 device delegate listeners to device 0
default	13:45:37.308207-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de9c40) removing 7 device listeners from device 89
default	13:45:37.308727-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x991de9c40) removing 0 device delegate listeners from device 89
default	13:45:37.308759-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x991de9c40)
default	13:45:37.325256-0500	Nexy	[0x994058640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:45:37.326550-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25685.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:45:37.329624-0500	tccd	AUTHREQ_SUBJECT: msgID=25685.2, subject=com.nexy.assistant,
default	13:45:37.330821-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	13:45:37.350157-0500	Nexy	[0x994058640] invalidated after the last release of the connection object
default	13:45:37.351572-0500	Nexy	[0x994058640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:45:37.352222-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25685.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:45:37.353478-0500	tccd	AUTHREQ_SUBJECT: msgID=25685.3, subject=com.nexy.assistant,
default	13:45:37.354146-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	13:45:37.365972-0500	Nexy	[0x994058640] invalidated after the last release of the connection object
default	13:45:37.366178-0500	Nexy	[0x994058640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:45:37.366602-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25685.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:45:37.367440-0500	tccd	AUTHREQ_SUBJECT: msgID=25685.4, subject=com.nexy.assistant,
default	13:45:37.367988-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	13:45:37.377355-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[25685], responsiblePID[25685], responsiblePath: /Applications/Nexy.app to UID: 501
default	13:45:37.377509-0500	Nexy	[0x994058640] invalidated after the last release of the connection object
default	13:45:37.452394-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	13:45:37.474715-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	13:45:37.475224-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:45:37.475362-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:45:37.477252-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:45:38.074430-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	13:45:38.079837-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:45:38.094620-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	13:45:39.356251-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:39.356251-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44586)
default	13:45:39.356390-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44585 called from <private>
default	13:45:39.356403-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44585 called from <private>
default	13:45:39.356434-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44586 called from <private>
default	13:45:39.356447-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44586 called from <private>
default	13:45:39.377042-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:39.377113-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44586)
default	13:45:39.378362-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44586 called from <private>
default	13:45:39.378401-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:39.378432-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:39.378436-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44586 called from <private>
default	13:45:39.389906-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44585 called from <private>
default	13:45:39.389925-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44585 called from <private>
default	13:45:39.390019-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:39.398827-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:39.399903-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44585 called from <private>
default	13:45:39.399951-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44585 called from <private>
default	13:45:39.400177-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:39.408308-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:39.408541-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:39.408569-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:39.410468-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:39.410480-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:39.410511-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:39.410520-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:39.410531-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:39.410541-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:39.410547-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:39.410552-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:39.410584-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:39.410619-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:39.410618-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:39.410651-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:39.410657-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:39.410664-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:39.410670-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:39.410931-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:39.412065-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:39.412233-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:39.412307-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44585 called from <private>
default	13:45:39.412365-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44585 called from <private>
default	13:45:44.827116-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:45:44.837836-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:45:44.844444-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:45:50.962798-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:45:50.962944-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:45:50.964813-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:45:50.970135-0500	runningboardd	Launch request for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:45:50.970205-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:95465] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-95465-1137339 target:app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:45:50.970257-0500	runningboardd	Assertion 398-95465-1137339 (target:app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>) will be created as active
default	13:45:50.973184-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:45:50.973300-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:45:50.973334-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>
default	13:45:50.973349-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:45:50.973419-0500	runningboardd	app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:45:50.982387-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] is not RunningBoard jetsam managed.
default	13:45:50.982398-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] This process will not be managed.
default	13:45:50.982404-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:50.982518-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:50.983115-0500	gamepolicyd	Hit the server for a process handle 1be4fdc60000648c that resolved to: [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:50.983143-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:50.987454-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:50.987499-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-1137340 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:50.987580-0500	runningboardd	Assertion 398-398-1137340 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:50.987716-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:50.987735-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:50.987752-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Set darwin role to: UserInteractive
default	13:45:50.987767-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:50.987812-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:50.987848-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] reported to RB as running
default	13:45:50.988673-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x127e27d com.nexy.assistant starting stopped process.
default	13:45:50.988715-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:25740" ID:398-363-1137341 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:45:50.988859-0500	runningboardd	Assertion 398-363-1137341 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:50.989520-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:45:50.989661-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:45:50.990294-0500	kernel	Nexy[25740] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xbe7d7aa4c285228f. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:45:50.991246-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:50.991316-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:50.991353-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:50.991415-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:50.991545-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:50.995680-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:50.996000-0500	runningboardd	Invalidating assertion 398-95465-1137339 (target:app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:95465]
default	13:45:50.996036-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:50.996145-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:50.996176-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:50.996022-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:50.996243-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:51.004040-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:51.010849-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25739.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.open, pid=25739, auid=501, euid=501, binary_path=/usr/bin/open}, },
default	13:45:51.013062-0500	tccd	AUTHREQ_SUBJECT: msgID=25739.1, subject=com.nexy.assistant,
default	13:45:51.013865-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:45:51.026706-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12314, subject=com.nexy.assistant,
default	13:45:51.027141-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:45:51.088211-0500	Nexy	[0x104355ba0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:45:51.088248-0500	Nexy	[0x1043560e0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:45:51.098993-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:51.099003-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:51.099013-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:51.099070-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:51.099030-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:51.101573-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:51.101783-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
error	13:45:51.132474-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x747d840e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:45:51.132601-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x747d840e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:45:51.132716-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x747d840e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:45:51.132828-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x747d840e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:45:51.169928-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:45:51.171392-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:45:51.172243-0500	Nexy	[0x104362220] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:45:51.173839-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>
default	13:45:51.176208-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:45:51.177423-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:45:51.177504-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:45:51.177580-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:45:51.177587-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:45:51.177603-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:45:51.177690-0500	Nexy	[0x747e90000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:45:51.177750-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:45:51.177922-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25740.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:45:51.180941-0500	tccd	AUTHREQ_SUBJECT: msgID=25740.1, subject=com.nexy.assistant,
default	13:45:51.181252-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:45:51.188174-0500	Nexy	[0x747e90000] invalidated after the last release of the connection object
default	13:45:51.188255-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:45:51.188276-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:45:51.188430-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:45:51.189168-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6340, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:51.189886-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6340, subject=com.nexy.assistant,
default	13:45:51.190634-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
error	13:45:51.197509-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:45:51.198065-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6342, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:51.198712-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6342, subject=com.nexy.assistant,
default	13:45:51.199433-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:45:51.207770-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:45:51.207786-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x746870e80> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	13:45:51.221147-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	13:45:51.221153-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	13:45:51.222990-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:45:51.223061-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:45:51.226705-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:45:51.948669-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid FF618F6E-4030-45CE-9203-C4DCBAFC6E11 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52036,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xfab63977 tp_proto=0x06"
default	13:45:51.948700-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52036<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385714 t_state: SYN_SENT process: Nexy:25740 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8c489904
default	13:45:51.949100-0500	kernel	tcp connected: [<IPv4-redacted>:52036<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385714 t_state: ESTABLISHED process: Nexy:25740 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8c489904
default	13:45:51.949320-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52036<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385714 t_state: FIN_WAIT_1 process: Nexy:25740 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8c489904
default	13:45:51.949325-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52036<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385714 t_state: FIN_WAIT_1 process: Nexy:25740 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:45:51.957750-0500	Nexy	[0x747e90000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:45:51.963390-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7461f9c40) Selecting device 83 from constructor
default	13:45:51.963395-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7461f9c40)
default	13:45:51.963398-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7461f9c40) not already running
default	13:45:51.963401-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7461f9c40) nothing to teardown
default	13:45:51.963402-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7461f9c40) connecting device 83
default	13:45:51.963454-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7461f9c40) Device ID: 83 (Input:No | Output:Yes): true
default	13:45:51.963507-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7461f9c40) created ioproc 0xa for device 83
default	13:45:51.963565-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7461f9c40) adding 7 device listeners to device 83
default	13:45:51.963656-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7461f9c40) adding 0 device delegate listeners to device 83
default	13:45:51.963661-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7461f9c40)
default	13:45:51.963701-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:45:51.963712-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:45:51.963716-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:45:51.963721-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:45:51.963725-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:45:51.963774-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7461f9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:45:51.963779-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7461f9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:45:51.963783-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:45:51.963785-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7461f9c40) removing 0 device listeners from device 0
default	13:45:51.963788-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7461f9c40) removing 0 device delegate listeners from device 0
default	13:45:51.963789-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7461f9c40)
default	13:45:51.963795-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:45:51.963857-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7461f9c40) caller requesting device change from 83 to 89
default	13:45:51.963862-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7461f9c40)
default	13:45:51.963865-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7461f9c40) not already running
default	13:45:51.963869-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7461f9c40) disconnecting device 83
default	13:45:51.963871-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7461f9c40) destroying ioproc 0xa for device 83
default	13:45:51.963900-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:45:51.964140-0500	Nexy	[0x747e90280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:45:51.964602-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef14d","name":"Nexy(25740)"}, "details":{"PID":25740,"session_type":"Primary"} }
default	13:45:51.964642-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":25740}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef14d, sessionType: 'prim', isRecording: false }, 
]
default	13:45:51.965009-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 25740, name = Nexy
default	13:45:51.965152-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x746a66680 with ID: 0x1ef14d
default	13:45:51.965476-0500	Nexy	[0x747e903c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	13:45:51.965552-0500	Nexy	No persisted cache on this platform.
error	13:45:51.965708-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=110552458199041 }
default	13:45:51.965718-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	13:45:51.965744-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:45:51.965800-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7461f9c40) connecting device 89
default	13:45:51.965852-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7461f9c40) Device ID: 89 (Input:Yes | Output:No): true
default	13:45:51.966468-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6343, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:51.966973-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6343, subject=com.nexy.assistant,
default	13:45:51.967506-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:45:51.974786-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7461f9c40) created ioproc 0xa for device 89
default	13:45:51.974854-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7461f9c40) adding 7 device listeners to device 89
default	13:45:51.974946-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7461f9c40) adding 0 device delegate listeners to device 89
default	13:45:51.974951-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7461f9c40)
default	13:45:51.974955-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	13:45:51.974960-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:45:51.975027-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	13:45:51.975030-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	13:45:51.975033-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:45:51.975084-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7461f9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:45:51.975090-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7461f9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:45:51.975095-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:45:51.975096-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7461f9c40) removing 7 device listeners from device 83
default	13:45:51.975195-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7461f9c40) removing 0 device delegate listeners from device 83
default	13:45:51.975202-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7461f9c40)
default	13:45:51.975514-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:45:51.975961-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6344, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:51.976308-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6344, subject=com.nexy.assistant,
default	13:45:51.976556-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:45:51.982728-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:45:51.983215-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6345, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:51.983597-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6345, subject=com.nexy.assistant,
default	13:45:51.983874-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:45:51.990159-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:45:51.990866-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6346, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:51.991211-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6346, subject=com.nexy.assistant,
default	13:45:51.991456-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:45:51.997776-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:45:51.997845-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:45:51.998217-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:45:51.998353-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6c6a700] Created node ADM::com.nexy.assistant_44598.44378.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:45:51.998384-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6c6a700] Created node ADM::com.nexy.assistant_44598.44378.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:45:52.051095-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:45:52.052603-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:44598 called from <private>
default	13:45:52.052629-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:45:52.053533-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44598 called from <private>
default	13:45:52.053605-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44598)
default	13:45:52.053621-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44598 called from <private>
default	13:45:52.053626-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44598 called from <private>
default	13:45:52.056607-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137348 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:52.056660-0500	runningboardd	Assertion 398-334-1137348 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:52.055695-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:45:52.055705-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44597 called from <private>
default	13:45:52.055708-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44597 called from <private>
default	13:45:52.058631-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44586)
default	13:45:52.058650-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:52.058742-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44585 called from <private>
default	13:45:52.058753-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44586 called from <private>
default	13:45:52.058763-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44586 called from <private>
default	13:45:52.058751-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44585 called from <private>
default	13:45:52.060261-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:45:52.060681-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:45:52.061584-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44598)
default	13:45:52.061615-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44598)
default	13:45:52.061623-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44598 called from <private>
default	13:45:52.061630-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44598 called from <private>
default	13:45:52.061635-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44598 called from <private>
default	13:45:52.061639-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44598 called from <private>
default	13:45:52.061630-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44598)
default	13:45:52.061665-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44598)
default	13:45:52.064388-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:52.064470-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:52.064517-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:52.064662-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
fault	13:45:52.066437-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>
default	13:45:52.067208-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44598 called from <private>
default	13:45:52.067219-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44598 called from <private>
default	13:45:52.067226-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44598 called from <private>
fault	13:45:52.068264-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>
default	13:45:52.070173-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:52.070487-0500	runningboardd	Invalidating assertion 398-334-1137348 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [osservice<com.apple.powerd>:334]
default	13:45:52.072294-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:52.073852-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6347, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:52.075437-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14d","name":"Nexy(25740)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:45:52.075486-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:45:52.075514-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:45:52.075583-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef14d, Nexy(25740), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:45:52.075746-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:52.075763-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:52.075859-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:45:52.075969-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:45:52.075970-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:52.076025-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14d, Nexy(25740), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 334 starting recording
default	13:45:52.076172-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:52.076287-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:45:52.076333-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14d, Nexy(25740), 'prim'', displayID:'com.nexy.assistant'}
default	13:45:52.076441-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:45:52.076447-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:45:52.076003-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:52.076128-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:52.076422-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:45:52.077747-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44598)
default	13:45:52.078660-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:45:52.078737-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44586)
default	13:45:52.078666-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:45:52.078823-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44586 called from <private>
default	13:45:52.078846-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44586 called from <private>
default	13:45:52.080456-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:45:52.078186-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6347, subject=com.nexy.assistant,
default	13:45:52.082216-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:52.082549-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:52.082659-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:52.082595-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:45:52.084383-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:45:52.084455-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:45:52.084527-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:52.084656-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:52.085591-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.085638-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.085782-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.085820-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.085906-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.085936-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:52.086139-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:52.087646-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44597 called from <private>
default	13:45:52.087654-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44597 called from <private>
default	13:45:52.087706-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:45:52.091587-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44585 called from <private>
default	13:45:52.091625-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44585 called from <private>
default	13:45:52.091744-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:52.091976-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:45:52.092077-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44597 called from <private>
default	13:45:52.092084-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44597 called from <private>
default	13:45:52.092156-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:45:52.094326-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:45:52.094738-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:45:52.095922-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:45:52.096220-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:45:52.096230-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:45:52.096398-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:45:52.096404-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:45:52.096421-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:45:52.096426-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:45:52.096431-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:45:52.096451-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:45:52.096462-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:45:52.096544-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:45:52.096756-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:45:52.096860-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:45:52.096966-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:45:52.097043-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:45:52.097107-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:45:52.097168-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:45:52.097307-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:45:52.099875-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137349 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:52.099947-0500	runningboardd	Assertion 398-334-1137349 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:52.097853-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:44598 called from <private>
default	13:45:52.098042-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:44598 called from <private>
default	13:45:52.098232-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:45:52.100707-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44598 called from <private>
default	13:45:52.100716-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44598 called from <private>
default	13:45:52.102483-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.102495-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.102508-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.102530-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.102603-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.102616-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:52.102931-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:52.102181-0500	runningboardd	Invalidating assertion 398-334-1137349 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [osservice<com.apple.powerd>:334]
default	13:45:52.101943-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6348, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:52.107804-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:52.109620-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:45:52.110399-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:45:52.118593-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:52.120960-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:52.121035-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	13:45:52.121141-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:45:52.109625-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
error	13:45:52.121187-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	13:45:52.109637-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44597 called from <private>
default	13:45:52.109642-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44597 called from <private>
error	13:45:52.121395-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	13:45:52.125515-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:45:52.126866-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:52.126925-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:52.127007-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:52.128482-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:52.128534-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44585 called from <private>
default	13:45:52.128565-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44585 called from <private>
default	13:45:52.128608-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44585 called from <private>
default	13:45:52.128617-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44585 called from <private>
default	13:45:52.128626-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44585 called from <private>
default	13:45:52.128632-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44585 called from <private>
default	13:45:52.161134-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:45:52.161896-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137351 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:52.161942-0500	runningboardd	Assertion 398-334-1137351 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:52.164469-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:44598 called from <private>
default	13:45:52.164494-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:44598 called from <private>
default	13:45:52.166019-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44598 called from <private>
default	13:45:52.166162-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44598)
default	13:45:52.166174-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44598 called from <private>
default	13:45:52.166114-0500	runningboardd	Invalidating assertion 398-334-1137351 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [osservice<com.apple.powerd>:334]
default	13:45:52.166177-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44598 called from <private>
default	13:45:52.167026-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:45:52.167177-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:45:52.167833-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44598)
default	13:45:52.167844-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44598 called from <private>
default	13:45:52.167848-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44598 called from <private>
default	13:45:52.167927-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44598 called from <private>
default	13:45:52.168936-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6349, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:52.169790-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:45:52.169842-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:45:52.169864-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:52.169935-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:52.170217-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6349, subject=com.nexy.assistant,
default	13:45:52.170346-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.170362-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.170377-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.170388-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.170429-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.170494-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:52.170805-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:45:52.171502-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:52.178117-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:52.178170-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:52.178209-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:52.178339-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:52.181842-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137352 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:52.183337-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:44598 called from <private>
default	13:45:52.181951-0500	runningboardd	Assertion 398-334-1137352 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:52.184560-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:44598 called from <private>
default	13:45:52.184595-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:45:52.185679-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44598 called from <private>
default	13:45:52.186692-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:45:52.187119-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:52.187030-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:45:52.185853-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44598)
default	13:45:52.187437-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:52.185863-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44598 called from <private>
default	13:45:52.185866-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44598 called from <private>
default	13:45:52.187619-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:52.187659-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44598)
default	13:45:52.187643-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:52.187742-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:52.187743-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44598 called from <private>
default	13:45:52.187748-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44598 called from <private>
default	13:45:52.187756-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44598 called from <private>
default	13:45:52.188785-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6350, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:45:52.190061-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6350, subject=com.nexy.assistant,
default	13:45:52.190340-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:52.190768-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:45:52.192599-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:45:52.192819-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:45:52.192907-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:52.193548-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:52.193520-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.193598-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.193694-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.193718-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.193772-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.193814-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:52.194133-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:45:52.194469-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.194495-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.194555-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.194583-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.194641-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.194681-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:52.195872-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:52.196054-0500	runningboardd	Invalidating assertion 398-334-1137352 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [osservice<com.apple.powerd>:334]
default	13:45:52.203855-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:44598 called from <private>
default	13:45:52.202294-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137353 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:52.203588-0500	runningboardd	Assertion 398-334-1137353 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:52.204098-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.204117-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.204128-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.204135-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.204164-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.204818-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:52.209763-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:45:52.209779-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:45:52.209800-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:52.209928-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.210016-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.210339-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:45:52.210347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.210374-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:52.210602-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:52.210423-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.211639-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.211673-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.211719-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:52.211739-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:52.211777-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:52.294265-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:52.418919-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	13:45:53.234612-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:45:53.234952-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14d","name":"Nexy(25740)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:45:53.235192-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:53.235315-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:45:53.235389-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14d, Nexy(25740), 'prim'', displayID:'com.nexy.assistant'}
default	13:45:53.235507-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14d, Nexy(25740), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 334 stopping recording
default	13:45:53.235515-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:45:53.235567-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:45:53.235635-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:45:53.235712-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 334, PID = 25740, Name = sid:0x1ef14d, Nexy(25740), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:45:53.236040-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:45:53.236018-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:45:53.236042-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:45:53.236730-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:53.236535-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:53.236805-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:45:53.236629-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:53.236843-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:53.236891-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:45:53.237024-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:45:53.237054-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:45:53.237080-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:45:53.241106-0500	runningboardd	Invalidating assertion 398-334-1137353 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [osservice<com.apple.powerd>:334]
default	13:45:53.243642-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:45:53.246135-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:53.246149-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:53.246160-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:53.246165-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:45:53.246172-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:45:53.246181-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:45:53.246253-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:45:53.336674-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7461f9c40) Selecting device 0 from destructor
default	13:45:53.336700-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7461f9c40)
default	13:45:53.336711-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7461f9c40) not already running
default	13:45:53.336719-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7461f9c40) disconnecting device 89
default	13:45:53.336730-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7461f9c40) destroying ioproc 0xa for device 89
default	13:45:53.336771-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:45:53.336822-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:45:53.337061-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x7461f9c40) nothing to setup
default	13:45:53.337079-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7461f9c40) adding 0 device listeners to device 0
default	13:45:53.337088-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7461f9c40) adding 0 device delegate listeners to device 0
default	13:45:53.337097-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7461f9c40) removing 7 device listeners from device 89
default	13:45:53.337413-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7461f9c40) removing 0 device delegate listeners from device 89
default	13:45:53.337434-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7461f9c40)
default	13:45:53.345278-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:53.345294-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:53.345308-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:53.345331-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:53.348880-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:53.354296-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:53.438147-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25742.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=25742, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:45:53.438838-0500	tccd	AUTHREQ_SUBJECT: msgID=25742.1, subject=com.nexy.assistant,
default	13:45:53.439181-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:45:53.447730-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12315, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=25742, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:45:53.448224-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12315, subject=com.nexy.assistant,
default	13:45:53.448607-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:45:53.465420-0500	launchservicesd	CHECKIN:0x0-0x127e27d 25742 com.nexy.assistant
default	13:45:53.466125-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:45:53.466212-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:45:53.467160-0500	runningboardd	Invalidating assertion 398-363-1137341 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	13:45:53.467813-0500	WindowServer	9a963[CreateApplication]: Process creation: 0x0-0x127e27d (Nexy) connectionID: 9A963 pid: 25742 in session 0x101
default	13:45:53.469878-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:45:53.476620-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:45:53.493484-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 25690: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 0c681a00 };
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
default	13:45:53.504677-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:45:53.526813-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x127e27d (Nexy) connectionID: 9A963 pid: 25742 in session 0x101
default	13:45:53.526839-0500	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x127e27d (Nexy) acq:0x801daebc0 count:1
default	13:45:53.527291-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x127e27d removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x127e27d (Nexy)"
)}
default	13:45:53.527517-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x648e removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x127e27d (Nexy)"
)}
default	13:45:53.528686-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x127e27d} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:45:53.528704-0500	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 19391101
default	13:45:53.528750-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:45:53.575687-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:53.575700-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:53.575721-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Set darwin role to: None
default	13:45:53.575732-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:53.575751-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:53.578411-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-suspended (role: None) (endowments: (null))
default	13:45:53.578674-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-suspended-NotVisible
default	13:45:54.236016-0500	Nexy	[0x747e90640] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:45:54.236880-0500	Nexy	[0x747e908c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:45:54.240266-0500	Nexy	Received configuration update from daemon (initial)
default	13:45:54.283145-0500	Nexy	[0x747e90a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:45:54.283509-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:45:54.283616-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25740.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:45:54.284521-0500	tccd	AUTHREQ_SUBJECT: msgID=25740.2, subject=com.nexy.assistant,
default	13:45:54.284954-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:45:54.292882-0500	Nexy	[0x747e90a00] invalidated after the last release of the connection object
default	13:45:54.293348-0500	Nexy	[0x747e90a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:45:54.293543-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:45:54.293632-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25740.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:45:54.294089-0500	tccd	AUTHREQ_SUBJECT: msgID=25740.3, subject=com.nexy.assistant,
default	13:45:54.294461-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:45:54.301434-0500	Nexy	[0x747e90a00] invalidated after the last release of the connection object
default	13:45:54.301464-0500	Nexy	[0x747e90a00] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:45:54.301516-0500	Nexy	[0x747e90a00] invalidated after the last release of the connection object
default	13:45:54.301681-0500	Nexy	[0x747e90b40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:45:54.301940-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25740.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:45:54.302436-0500	tccd	AUTHREQ_SUBJECT: msgID=25740.4, subject=com.nexy.assistant,
default	13:45:54.302829-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:45:54.310287-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[25740], responsiblePID[25740], responsiblePath: /Applications/Nexy.app to UID: 501
default	13:45:54.310414-0500	Nexy	[0x747e90b40] invalidated after the last release of the connection object
default	13:45:54.310615-0500	Nexy	server port 0x0000ef13, session port 0x0000ed13
default	13:45:54.311144-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12316, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:45:54.311156-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:45:54.311861-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12316, subject=com.nexy.assistant,
default	13:45:54.312679-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	13:45:54.316884-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	13:45:54.334209-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:45:54.335711-0500	Nexy	server port 0x0000ed13, session port 0x0000ed13
default	13:45:54.336008-0500	Nexy	[0x747e90b40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:45:54.336056-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4E22C6E2-84F4-4777-94D0-BC112253BC76 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52037,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xcba204dd tp_proto=0x06"
default	13:45:54.336091-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52037<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385715 t_state: SYN_SENT process: Nexy:25740 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8c2c1fb4
default	13:45:54.336354-0500	kernel	tcp connected: [<IPv4-redacted>:52037<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385715 t_state: ESTABLISHED process: Nexy:25740 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8c2c1fb4
default	13:45:54.336986-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52037<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385715 t_state: FIN_WAIT_1 process: Nexy:25740 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8c2c1fb4
default	13:45:54.336992-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52037<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385715 t_state: FIN_WAIT_1 process: Nexy:25740 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:45:54.337049-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	13:45:54.337121-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6CB14921-CB9F-4F7C-8150-C7E8EEC3472A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52038,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x0ea3cd76 tp_proto=0x06"
default	13:45:54.337136-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52038<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385716 t_state: SYN_SENT process: Nexy:25740 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9b6d928e
default	13:45:54.337163-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	13:45:54.337268-0500	kernel	tcp connected: [<IPv4-redacted>:52038<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385716 t_state: ESTABLISHED process: Nexy:25740 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9b6d928e
default	13:45:54.337384-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52038<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385716 t_state: FIN_WAIT_1 process: Nexy:25740 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x9b6d928e
default	13:45:54.337388-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52038<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385716 t_state: FIN_WAIT_1 process: Nexy:25740 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:45:54.337752-0500	Nexy	nw_path_libinfo_path_check [71F23127-5E2F-4EB8-ABF8-2F1C74DB8151 IPv4#4e73ded8:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	13:45:54.337812-0500	Nexy	New connection 0x1769d3 main
default	13:45:54.337893-0500	Nexy	[0x747e90c80] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:45:54.338484-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 435FD114-E03C-4B59-84C9-876305745660 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52039,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x46b844d1 tp_proto=0x06"
default	13:45:54.338495-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52039<-><IPv4-redacted>:443] interface: utun6 (skipped: 5295)
so_gencnt: 4385717 t_state: SYN_SENT process: Nexy:25740 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xae2c885c
default	13:45:54.338625-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:45:54.338819-0500	kernel	tcp connected: [<IPv4-redacted>:52039<-><IPv4-redacted>:443] interface: utun6 (skipped: 5295)
so_gencnt: 4385717 t_state: ESTABLISHED process: Nexy:25740 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xae2c885c
default	13:45:54.339729-0500	Nexy	[0x747e90f00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:45:54.343135-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12317, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:45:54.343152-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=25740, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:45:54.343736-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12317, subject=com.nexy.assistant,
default	13:45:54.344217-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:45:54.371011-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	13:45:54.383575-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	13:45:54.386529-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:45:54.503134-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:45:54.505192-0500	Nexy	CHECKIN: pid=25740
default	13:45:54.512443-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:25740" ID:398-363-1137366 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:45:54.512523-0500	runningboardd	Assertion 398-363-1137366 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:54.512944-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:54.513000-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:54.513093-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Set darwin role to: UserInteractive
default	13:45:54.513143-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:54.512948-0500	Nexy	CHECKEDIN: pid=25740 asn=0x0-0x128027f foreground=0
default	13:45:54.513267-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:54.513319-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:25740" ID:398-363-1137367 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:45:54.513386-0500	runningboardd	Assertion 398-363-1137367 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:54.512391-0500	launchservicesd	CHECKIN:0x0-0x128027f 25740 com.nexy.assistant
default	13:45:54.513267-0500	Nexy	[0x747e91040] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	13:45:54.513596-0500	Nexy	[0x747e91180] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:45:54.513602-0500	Nexy	[0x747e91180] Connection returned listener port: 0x15403
default	13:45:54.513809-0500	Nexy	[0x746d5c600] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x747e91180.peer[363].0x746d5c600
default	13:45:54.516751-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:45:54.516900-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:45:54.517252-0500	Nexy	FRONTLOGGING: version 1
default	13:45:54.517524-0500	WindowServer	1769d3[CreateApplication]: Process creation: 0x0-0x128027f (Nexy) connectionID: 1769D3 pid: 25740 in session 0x101
default	13:45:54.517277-0500	Nexy	Registered, pid=25740 ASN=0x0,0x128027f
default	13:45:54.518143-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:54.518791-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:54.518969-0500	runningboardd	Invalidating assertion 398-363-1137366 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	13:45:54.519630-0500	Nexy	[0x747e91180] Connection returned listener port: 0x15403
default	13:45:54.520062-0500	Nexy	BringForward: pid=25740 asn=0x0-0x128027f bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	13:45:54.520395-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:45:54.521768-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:45:54.522476-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:45:54.542821-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:45:54.542915-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:45:54.550622-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:45:54.550630-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:45:54.550679-0500	Nexy	Initializing connection
default	13:45:54.550719-0500	Nexy	Removing all cached process handles
default	13:45:54.550738-0500	Nexy	Sending handshake request attempt #1 to server
default	13:45:54.550743-0500	Nexy	Creating connection to com.apple.runningboard
default	13:45:54.550750-0500	Nexy	[0x747e912c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:45:54.551059-0500	Nexy	[0x747e91180] Connection returned listener port: 0x15403
default	13:45:54.551182-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] as ready
default	13:45:54.551717-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 2d00000024 pid: 25740
default	13:45:54.551770-0500	Nexy	Handshake succeeded
default	13:45:54.551779-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>
default	13:45:54.553726-0500	Nexy	[0x747e91180] Connection returned listener port: 0x15403
default	13:45:54.554713-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:45:54.554723-0500	Nexy	[0x747e91400] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:45:54.554778-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:45:54.554805-0500	Nexy	[0x747e91680] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:45:54.556636-0500	WindowServer	1769d3[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x128027f (Nexy) mainConnectionID: 1769D3;
} for reason: updated frontmost process
default	13:45:54.556718-0500	WindowServer	1769d3[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x128027f (Nexy) -> <pid: 25740>
default	13:45:54.556839-0500	WindowServer	new deferring rules for pid:393: [
    [393-B070]; <keyboardFocus; Nexy:0x0-0x128027f>; () -> <pid: 25740>; reason: frontmost PSN --> outbound target,
    [393-B06F]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x128027f; pid: 393>; reason: frontmost PSN,
    [393-B06E]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	13:45:54.556956-0500	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-B070]; <keyboardFocus; Nexy:0x0-0x128027f>; () -> <pid: 25740>; reason: frontmost PSN --> outbound target,
    [393-B06F]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x128027f; pid: 393>; reason: frontmost PSN,
    [393-B06E]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	13:45:54.556638-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "frontmost:25740" ID:398-363-1137368 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractiveFocal" sourceEnvironment:"(null)">
	]>
default	13:45:54.556731-0500	runningboardd	Assertion 398-363-1137368 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:54.557342-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:54.557445-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:54.557538-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Set darwin role to: UserInteractiveFocal
default	13:45:54.557610-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:54.557722-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:54.558145-0500	Nexy	[0x747e91680] Connection returned listener port: 0x11c03
default	13:45:54.558585-0500	Nexy	Registered process with identifier 25740-1730567
default	13:45:54.558305-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "notification:25740" ID:398-363-1137369 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	13:45:54.558713-0500	runningboardd	Assertion 398-363-1137369 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:54.559067-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x128027f; pid: 393>,
    <pid: 25740>
]
default	13:45:54.562643-0500	Nexy	[0x747e91900] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	13:45:54.568248-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	13:45:54.568627-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:54.568670-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:54.568708-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:54.568787-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:54.571588-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 3100000032 pid: 25740
default	13:45:54.571583-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	13:45:54.575129-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	13:45:54.577864-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x746a50fa0
 (
    "<NSAquaAppearance: 0x746a51360>",
    "<NSSystemAppearance: 0x746a51400>"
)>
default	13:45:54.581435-0500	Nexy	[0x747e91e00] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	13:45:54.581716-0500	Nexy	[0x747e91f40] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	13:45:54.583244-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	13:45:54.583384-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	13:45:54.583391-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	13:45:54.583412-0500	Nexy	[0x747e92080] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	13:45:54.583424-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	13:45:54.583450-0500	Nexy	[0x747e92300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:45:54.583484-0500	Nexy	FBSWorkspace registering source: <private>
default	13:45:54.584131-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:45:54.584114-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	13:45:54.584275-0500	Nexy	<FBSWorkspaceScenesClient:0x746a51f40 <private>> attempting immediate handshake from activate
default	13:45:54.584304-0500	Nexy	<FBSWorkspaceScenesClient:0x746a51f40 <private>> sent handshake
default	13:45:54.584357-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	13:45:54.584702-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:54.584728-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:54.585346-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] Registering event dispatcher at init
default	13:45:54.585937-0500	ControlCenter	Created <FBWorkspace: 0xaf8597b60; <FBApplicationProcess: 0xaf8cfe100; app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740(v1A6807)>>
default	13:45:54.585963-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6> with intent background
default	13:45:54.586278-0500	runningboardd	Launch request for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:45:54.586380-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)> from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:398-632-1137370 target:app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	13:45:54.586505-0500	runningboardd	Assertion 398-632-1137370 (target:app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>) will be created as active
default	13:45:54.586538-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:398-632-1137370 target:app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:54.586843-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:54.587034-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	13:45:54.586855-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:54.587539-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:54.587891-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:54.588551-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	13:45:54.589787-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	13:45:54.590434-0500	Nexy	Requesting scene <FBSScene: 0x746a52440; com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA> from com.apple.controlcenter.statusitems
default	13:45:54.592057-0500	Nexy	Request for <FBSScene: 0x746a52440; com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA> complete!
default	13:45:54.592113-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	13:45:54.592705-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	13:45:54.593286-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	13:45:54.593477-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	13:45:54.593636-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	13:45:54.593655-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	13:45:54.593807-0500	Nexy	Requesting scene <FBSScene: 0x746a52080; com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	13:45:54.593914-0500	Nexy	Request for <FBSScene: 0x746a52080; com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView> complete!
default	13:45:54.595402-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] Bootstrap success!
default	13:45:54.595968-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] Setting process visibility to: Background
default	13:45:54.596031-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] No launch watchdog for this process, dropping initial assertion in 2.0s
default	13:45:54.596312-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:398-632-1137371 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	13:45:54.596374-0500	runningboardd	Assertion 398-632-1137371 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:54.596890-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:45:54.596771-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:54.596900-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	13:45:54.596849-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:54.596879-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:54.596947-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:54.600044-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:45:54.600055-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	13:45:54.600106-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	13:45:54.600429-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:45:54.600439-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	13:45:54.601110-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	13:45:54.601538-0500	ControlCenter	Adding: <FBApplicationProcess: 0xaf8cfe100; app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740(v1A6807)>
default	13:45:54.601983-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] Connection established.
default	13:45:54.602044-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xaf8b57090>
default	13:45:54.602070-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] Connection to remote process established!
default	13:45:54.602148-0500	ControlCenter	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:54.609168-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:54.609184-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xaf8cfe100; app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740(v1A6807)>
default	13:45:54.609287-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] Registered new scene: <FBWorkspaceScene: 0xaf5dc6580; com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA> (fromRemnant = 0)
default	13:45:54.609328-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] Workspace interruption policy did change: reconnect
default	13:45:54.609520-0500	ControlCenter	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA] Client process connected: [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:54.609527-0500	Nexy	Request for <FBSScene: 0x746a52440; com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA> complete!
default	13:45:54.609601-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:398-632-1137372 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	13:45:54.609675-0500	runningboardd	Assertion 398-632-1137372 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as inactive as originator process has not exited
default	13:45:54.609772-0500	Nexy	Registering for test daemon availability notify post.
default	13:45:54.609865-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:45:54.609920-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:45:54.609972-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:45:54.610065-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-1137373 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	13:45:54.610162-0500	runningboardd	Assertion 398-632-1137373 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:54.610243-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	13:45:54.610527-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:54.610568-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xaf8cfe100; app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740(v1A6807)>
default	13:45:54.610687-0500	Nexy	<FBSWorkspaceScenesClient:0x746a51f40 <private>> Reconnecting scene com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA
default	13:45:54.610716-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] Registered new scene: <FBWorkspaceScene: 0xaf5dc4b40; com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	13:45:54.610681-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:54.610737-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:54.610827-0500	ControlCenter	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:54.610790-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:54.610820-0500	Nexy	[0x747e92580] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	13:45:54.610824-0500	Nexy	Request for <FBSScene: 0x746a52080; com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView> complete!
default	13:45:54.611059-0500	Nexy	<FBSWorkspaceScenesClient:0x746a51f40 <private>> Reconnecting scene com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView
default	13:45:54.610904-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:54.611468-0500	Nexy	[0x747e91180] Connection returned listener port: 0x15403
default	13:45:54.611696-0500	Nexy	SignalReady: pid=25740 asn=0x0-0x128027f
default	13:45:54.612169-0500	Nexy	SIGNAL: pid=25740 asn=0x0x-0x128027f
default	13:45:54.614190-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:45:54.617326-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	13:45:54.617656-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:45:54.619494-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	13:45:54.619507-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	13:45:54.619540-0500	Nexy	[0x747e90dc0] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	13:45:54.619591-0500	Nexy	[0x747e90dc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:45:54.620290-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	13:45:54.621758-0500	Nexy	[0x747e90dc0] activating connection: mach=false listener=false peer=false name=com.apple.ViewBridgeAuxiliary
default	13:45:54.622068-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-25740). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	13:45:54.623006-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-25740)
default	13:45:54.623315-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(9F8C42C5, (bid:com.nexy.assistant-Item-0-25740)) for (bid:com.nexy.assistant-Item-0-25740)
default	13:45:54.623569-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-25740)]
default	13:45:54.623912-0500	ControlCenter	Created instance DisplayableId(2CDBD81A) in .menuBar for DisplayableAppStatusItemType(9F8C42C5, (bid:com.nexy.assistant-Item-0-25740)) .menuBar
default	13:45:54.626091-0500	Nexy	[0x747e92800] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:45:54.626372-0500	Nexy	[0x747e92940] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:45:54.626377-0500	Nexy	[0x747e92940] Connection returned listener port: 0x16503
default	13:45:54.626885-0500	Nexy	[0x747e90dc0] invalidated after the last release of the connection object
default	13:45:54.627532-0500	ControlCenter	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:54.627975-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:54.629897-0500	Nexy	[C:2] Alloc <private>
default	13:45:54.629931-0500	ControlCenter	Created ephemaral instance DisplayableId(2CDBD81A) for (bid:com.nexy.assistant-Item-0-25740) with positioning .ephemeral
default	13:45:54.629921-0500	Nexy	[0x747e926c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:45:54.630009-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
error	13:45:54.630064-0500	kernel	Sandbox: WindowManager(584) deny(1) mach-task-name others [Nexy(25740)]
default	13:45:54.630842-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25740-1137374 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:45:54.630942-0500	WindowManager	Connection activated | (25740) Nexy
default	13:45:54.630924-0500	runningboardd	Assertion 398-25740-1137374 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:54.632055-0500	runningboardd	Invalidating assertion 398-25740-1137374 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:54.632092-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:54.632240-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25740-1137375 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:45:54.632106-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:54.632299-0500	runningboardd	Assertion 398-25740-1137375 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:54.632298-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:54.632392-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:54.635044-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	13:45:54.635209-0500	runningboardd	Invalidating assertion 398-25740-1137375 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:54.635282-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25740-1137376 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:45:54.635315-0500	runningboardd	Assertion 398-25740-1137376 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:54.635411-0500	ControlCenter	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:54.635509-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:54.635921-0500	runningboardd	Invalidating assertion 398-25740-1137377 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:54.635986-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25740-1137378 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:45:54.636012-0500	runningboardd	Assertion 398-25740-1137378 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:54.636121-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA] Received action(s): NSStatusItemChangeVisibilityAction
default	13:45:54.636177-0500	runningboardd	Invalidating assertion 398-25740-1137378 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]
default	13:45:54.638799-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA] Observer <NSSceneStatusItem: 0x747e9aa00> handled action(s): <private>
default	13:45:54.639053-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	13:45:54.641586-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	13:45:54.641931-0500	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	13:45:54.641995-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:45:54.649127-0500	Nexy	[com.apple.controlcenter:5F83FCF5-ECB9-4F82-8183-DD129A03F1DA] Sending action(s) in update: NSSceneFenceAction
default	13:45:54.747976-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	13:45:54.751194-0500	Nexy	Start service name com.apple.spotlightknowledged
default	13:45:54.751805-0500	Nexy	[GMS] availability notification token 87
default	13:45:54.806510-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:54.806534-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:54.806550-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:54.806583-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:54.809758-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	13:45:54.810120-0500	ControlCenter	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:54.810219-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:54.837539-0500	kernel	udp connect: [<IPv4-redacted>:58151<-><IPv4-redacted>:443] interface:  (skipped: 1000)
so_gencnt: 4385720 so_state: 0x0002 process: Nexy:25740 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xb7b6a207
default	13:45:54.837549-0500	kernel	udp_connection_summary [<IPv4-redacted>:58151<-><IPv4-redacted>:443] interface:  (skipped: 1000)
so_gencnt: 4385720 so_state: 0x0002 process: Nexy:25740 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xb7b6a207 flowctl: 0us (0x)
default	13:45:54.854418-0500	ControlCenter	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6>:25740] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	13:45:54.854526-0500	runningboardd	Invalidating assertion 398-632-1137373 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	13:45:54.920603-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:54.920615-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:54.920627-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:54.920644-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:54.923757-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	13:45:54.924195-0500	ControlCenter	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:54.924401-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:55.131683-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "AppDrawing" ID:398-393-1137381 target:25740 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:45:55.131769-0500	runningboardd	Assertion 398-393-1137381 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) will be created as active
default	13:45:55.132215-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:55.132235-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:55.132255-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:55.132281-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:55.135658-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	13:45:55.136266-0500	ControlCenter	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:55.136425-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:55.462877-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:45:55.463031-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44597 called from <private>
default	13:45:55.463049-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44597 called from <private>
default	13:45:55.464831-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44598)
default	13:45:55.464867-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44598 called from <private>
default	13:45:55.464874-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44598 called from <private>
default	13:45:55.467731-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44586)
default	13:45:55.471019-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:55.471106-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44586 called from <private>
default	13:45:55.471123-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44586 called from <private>
default	13:45:55.471138-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44585 called from <private>
default	13:45:55.471158-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44585 called from <private>
default	13:45:55.483324-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:45:55.484445-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:55.489928-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:45:55.489947-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:45:55.491108-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44598)
default	13:45:55.491435-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44586)
default	13:45:55.491131-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44598 called from <private>
default	13:45:55.491513-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44586 called from <private>
default	13:45:55.491137-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44598 called from <private>
default	13:45:55.491523-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44586 called from <private>
default	13:45:55.492825-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:55.492847-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:55.501935-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44597 called from <private>
default	13:45:55.501952-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44597 called from <private>
default	13:45:55.502063-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:45:55.503269-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:45:55.503468-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44597 called from <private>
default	13:45:55.503479-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44597 called from <private>
default	13:45:55.503556-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:45:55.506474-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44585 called from <private>
default	13:45:55.506489-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44585 called from <private>
default	13:45:55.506686-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:55.508578-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:45:55.508822-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:45:55.508831-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:45:55.509111-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:45:55.509121-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:45:55.509135-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:45:55.509145-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:45:55.509172-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:45:55.509212-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:45:55.509238-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:45:55.509260-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:45:55.509289-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:45:55.509315-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:45:55.509324-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:45:55.509349-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:45:55.509401-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:45:55.509469-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:45:55.509546-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:45:55.510739-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:55.511683-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44585 called from <private>
default	13:45:55.511698-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44585 called from <private>
default	13:45:55.511862-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:55.516463-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:45:55.516504-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:45:55.516510-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:45:55.522618-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:55.516810-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44597 called from <private>
default	13:45:55.522825-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:55.516822-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44597 called from <private>
default	13:45:55.522855-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:55.523015-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:55.523025-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:55.523042-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:55.523052-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:55.523060-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:55.523066-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:55.523142-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:55.523155-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44585)
default	13:45:55.523363-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:55.523796-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:55.523936-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:55.524025-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:55.524293-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:55.524307-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44585 called from <private>
default	13:45:55.524313-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44585 called from <private>
default	13:45:55.532159-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44585)
default	13:45:55.532373-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44585 called from <private>
default	13:45:55.532407-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44585 called from <private>
default	13:45:55.532452-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44585 called from <private>
default	13:45:55.532461-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44585 called from <private>
default	13:45:55.881715-0500	runningboardd	Invalidating assertion 398-363-1137368 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	13:45:55.916182-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:55.916198-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:55.916223-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Set darwin role to: UserInteractive
default	13:45:55.916233-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:55.916251-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:55.919013-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:55.919390-0500	ControlCenter	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:55.919645-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:56.020847-0500	runningboardd	Assertion did invalidate due to timeout: 398-398-1137340 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740])
default	13:45:56.215420-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:56.215425-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:56.215431-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:56.215445-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:56.221278-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:56.221615-0500	ControlCenter	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:56.221745-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:56.694473-0500	runningboardd	Invalidating assertion 398-632-1137370 (target:app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>) from originator [osservice<com.apple.controlcenter(501)>:632]
default	13:45:56.798480-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>
default	13:45:56.808422-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:45:56.808650-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:45:56.808756-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:45:56.808955-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:45:56.821438-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:45:56.823287-0500	ControlCenter	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:45:59.600744-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	13:45:59.615067-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	13:45:59.623055-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:45:59.924305-0500	runningboardd	Assertion did invalidate due to timeout: 398-363-1137369 (target:[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740])
default	13:46:00.124063-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring jetsam update because this process is not memory-managed
default	13:46:00.124077-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring suspend because this process is not lifecycle managed
default	13:46:00.124084-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring GPU update because this process is not GPU managed
default	13:46:00.124099-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>:25740] Ignoring memory limit update because this process is not memory-managed
default	13:46:00.129023-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:46:00.129493-0500	ControlCenter	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:46:00.129697-0500	gamepolicyd	Received state update for 25740 (app<application.com.nexy.assistant.20102073.20102079.DB8BBF59-2336-4B7D-95A5-6F988B1EAFC6(501)>, running-active-NotVisible
default	13:46:00.919724-0500	kernel	Nexy[25767] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xc221e1b5fedd314b. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:46:00.919743-0500	kernel	Nexy[25767] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0xc221e1b5fedd314b. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:46:01.029263-0500	Nexy	[0x1042b5750] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:46:01.029304-0500	Nexy	[0x1042b5c90] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	13:46:01.075814-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xb2de2c0e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:46:01.075961-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xb2de2c0e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:46:01.076076-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xb2de2c0e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:46:01.076230-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xb2de2c0e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:46:01.114979-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:46:01.116615-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:46:01.117396-0500	Nexy	[0x1042b9e80] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	13:46:01.118680-0500	runningboardd	Resolved pid 25767 to [anon<Nexy>(501):25767]
default	13:46:01.118801-0500	runningboardd	[anon<Nexy>(501):25767] is not RunningBoard jetsam managed.
default	13:46:01.118809-0500	runningboardd	[anon<Nexy>(501):25767] This process will not be managed.
default	13:46:01.118983-0500	runningboardd	Resolved pid 25767 to [anon<Nexy>(501):25767]
default	13:46:01.119050-0500	runningboardd	[anon<Nexy>(501):25767] is not RunningBoard jetsam managed.
default	13:46:01.119060-0500	runningboardd	[anon<Nexy>(501):25767] This process will not be managed.
default	13:46:01.119066-0500	runningboardd	Now tracking process: [anon<Nexy>(501):25767]
fault	13:46:01.119213-0500	runningboardd	Two equal instances have unequal identities. <anon<Nexy>(501) pid=25767 AUID=501> and <anon<Nexy>(501)(0) pid=25767>
default	13:46:01.119494-0500	gamepolicyd	Hit the server for a process handle d8bad7b000064a7 that resolved to: [anon<Nexy>(501):25767]
default	13:46:01.119513-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:01.121292-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:46:01.122108-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:46:01.122195-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:46:01.122258-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:46:01.122266-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:46:01.122281-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:46:01.122420-0500	Nexy	[0xb2df5c000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:46:01.122477-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:46:01.122701-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25767.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:46:01.132895-0500	tccd	AUTHREQ_SUBJECT: msgID=25767.1, subject=com.nexy.assistant,
default	13:46:01.133253-0500	Nexy	[0xb2df5c000] invalidated after the last release of the connection object
default	13:46:01.133358-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:46:01.133383-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:46:01.133563-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:46:01.134418-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6351, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:01.134963-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6351, subject=com.nexy.assistant,
default	13:46:01.135325-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
error	13:46:01.142513-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:46:01.143069-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6353, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25685, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:01.143440-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6353, subject=com.nexy.assistant,
default	13:46:01.143718-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:01.151869-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:46:01.151880-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xb2c814b40> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	13:46:01.166169-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	13:46:01.166176-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	13:46:01.168037-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:46:01.168116-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:46:01.171670-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:46:01.721524-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	13:46:01.904392-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 11DE914F-88EF-404B-ABFE-B49AC755E7EB flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52046,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x71a4076a tp_proto=0x06"
default	13:46:01.904426-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52046<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385741 t_state: SYN_SENT process: Nexy:25767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8cae1292
default	13:46:01.905219-0500	kernel	tcp connected: [<IPv4-redacted>:52046<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385741 t_state: ESTABLISHED process: Nexy:25767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8cae1292
default	13:46:01.905467-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52046<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385741 t_state: FIN_WAIT_1 process: Nexy:25767 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8cae1292
default	13:46:01.905472-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52046<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385741 t_state: FIN_WAIT_1 process: Nexy:25767 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:46:01.914872-0500	Nexy	[0xb2df5c000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:46:01.920377-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb2c24d540) Selecting device 83 from constructor
default	13:46:01.920382-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24d540)
default	13:46:01.920386-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24d540) not already running
default	13:46:01.920387-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb2c24d540) nothing to teardown
default	13:46:01.920389-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb2c24d540) connecting device 83
default	13:46:01.920435-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24d540) Device ID: 83 (Input:No | Output:Yes): true
default	13:46:01.920492-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb2c24d540) created ioproc 0xa for device 83
default	13:46:01.920555-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24d540) adding 7 device listeners to device 83
default	13:46:01.920646-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24d540) adding 0 device delegate listeners to device 83
default	13:46:01.920650-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24d540)
default	13:46:01.920690-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:01.920701-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:46:01.920703-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:01.920708-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:46:01.920713-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:01.920769-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:01.920777-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:01.920779-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:01.920783-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24d540) removing 0 device listeners from device 0
default	13:46:01.920784-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24d540) removing 0 device delegate listeners from device 0
default	13:46:01.920788-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24d540)
default	13:46:01.920795-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:46:01.920849-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb2c24d540) caller requesting device change from 83 to 89
default	13:46:01.920855-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24d540)
default	13:46:01.920857-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24d540) not already running
default	13:46:01.920860-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb2c24d540) disconnecting device 83
default	13:46:01.920861-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb2c24d540) destroying ioproc 0xa for device 83
default	13:46:01.920893-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:46:01.921128-0500	Nexy	[0xb2df5c280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:46:01.921653-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef14c","name":"Nexy(25685)"}, "details":null }
default	13:46:01.921679-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef14c from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":25685})
default	13:46:01.921689-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":25685})
default	13:46:01.921745-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"PID":25767,"session_type":"Primary"} }
default	13:46:01.921793-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":25767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef14e, sessionType: 'prim', isRecording: false }, 
]
default	13:46:01.922477-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:01.922602-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 333, PID = 25685, Name = sid:0x1ef14c, Nexy(25685), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:01.923559-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:01.923616-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:01.923672-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xb2cae6680 with ID: 0x1ef14e
default	13:46:01.923140-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:01.923250-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 25767, name = Nexy
default	13:46:01.923453-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:01.924012-0500	Nexy	[0xb2df5c3c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	13:46:01.924087-0500	Nexy	No persisted cache on this platform.
error	13:46:01.924266-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=110668422316033 }
default	13:46:01.924273-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	13:46:01.924304-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:46:01.924663-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb2c24d540) connecting device 89
default	13:46:01.924858-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24d540) Device ID: 89 (Input:Yes | Output:No): true
default	13:46:01.925970-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6354, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:01.929111-0500	runningboardd	[app<application.com.nexy.assistant.20102073.20102079(501)>:25685] termination reported by launchd (0, 0, 0)
default	13:46:01.929136-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:46:01.929137-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.20102073.20102079(501)>:25685]
default	13:46:01.929330-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.20102073.20102079(501)>:25685]
default	13:46:01.929369-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:46:01.929506-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.20102073.20102079(501)>:25685]
default	13:46:01.929521-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.20102073.20102079(501)>:25685]
default	13:46:01.929799-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20102073.20102079(501)>: none (role: None) (endowments: (null))
default	13:46:01.929949-0500	audiomxd	  ServerSessionManager.mm:1322  Monitored process died, pid = 25685, name = Nexy
default	13:46:01.930886-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6354, subject=com.nexy.assistant,
default	13:46:01.934190-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_44586.44378.0_airpods noise suppression studio::out-0 issue_detected_sample_time=336960.000000 ] -- [ rms:[-56.567593], peaks:[-19.551113] ]
default	13:46:01.934221-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_44586.44378.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-58.486046], peaks:[-22.551039] ]
default	13:46:01.934012-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:01.936942-0500	launchservicesd	Hit the server for a process handle c2ca93000006455 that resolved to: [app<application.com.nexy.assistant.20102073.20102079(501)>:25685]
default	13:46:01.938340-0500	gamepolicyd	Received state update for 25685 (app<application.com.nexy.assistant.20102073.20102079(501)>, none-NotVisible
default	13:46:01.941976-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb2c24d540) created ioproc 0xa for device 89
default	13:46:01.942063-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24d540) adding 7 device listeners to device 89
default	13:46:01.942224-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24d540) adding 0 device delegate listeners to device 89
default	13:46:01.942229-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24d540)
default	13:46:01.942234-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	13:46:01.942239-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:01.942339-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	13:46:01.942346-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	13:46:01.942348-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:46:01.942411-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:01.942419-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:01.942423-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:01.942425-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24d540) removing 7 device listeners from device 83
default	13:46:01.942594-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24d540) removing 0 device delegate listeners from device 83
default	13:46:01.942599-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24d540)
default	13:46:01.943180-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:46:01.943716-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6355, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:01.944638-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:01.944811-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:01.944819-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6355, subject=com.nexy.assistant,
default	13:46:01.945429-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:01.952542-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:46:01.953047-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6356, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:01.953618-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6356, subject=com.nexy.assistant,
default	13:46:01.953972-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:01.961777-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:46:01.962742-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6357, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:01.963432-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6357, subject=com.nexy.assistant,
default	13:46:01.963927-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:01.971242-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:46:01.971328-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:46:01.971800-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:46:01.971946-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d84c00] Created node ADM::com.nexy.assistant_44610.44378.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:46:01.971992-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d84c00] Created node ADM::com.nexy.assistant_44610.44378.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:46:01.996268-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:46:01.997948-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137462 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:01.998001-0500	runningboardd	Assertion 398-334-1137462 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:01.999022-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:02.000170-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:01.997863-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:02.000298-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring role changes because this process is not role managed
default	13:46:02.000333-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:02.000405-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:02.002171-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:46:02.002360-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:46:02.002485-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:02.002737-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:02.002815-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:02.003019-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:46:02.003051-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14e, Nexy(25767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 335 starting recording
default	13:46:02.002603-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef14e, Nexy(25767), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:46:02.003509-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:02.003703-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:46:01.997895-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44609 called from <private>
default	13:46:02.003778-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14e, Nexy(25767), 'prim'', displayID:'com.nexy.assistant'}
default	13:46:01.997941-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44609 called from <private>
default	13:46:01.998042-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:46:02.002674-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:01.997472-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
fault	13:46:02.004499-0500	runningboardd	Two equal instances have unequal identities. <anon<Nexy>(501) pid=25767 AUID=501> and <anon<Nexy>(501)(0) pid=25767>
fault	13:46:02.005821-0500	runningboardd	Two equal instances have unequal identities. <anon<Nexy>(501) pid=25767 AUID=501> and <anon<Nexy>(501)(0) pid=25767>
default	13:46:02.000597-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44610)
default	13:46:02.000622-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:44610 called from <private>
default	13:46:01.997505-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44597 called from <private>
default	13:46:01.997514-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44597 called from <private>
default	13:46:02.000623-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44598)
default	13:46:02.000653-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44598 called from <private>
default	13:46:02.003998-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:02.001626-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44610 called from <private>
default	13:46:02.000660-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44598 called from <private>
default	13:46:02.004138-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:46:02.003912-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:46:02.008805-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:02.014121-0500	runningboardd	Invalidating assertion 398-334-1137462 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.powerd>:334]
default	13:46:02.014564-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:02.000667-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:46:02.014827-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44598)
default	13:46:02.014852-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44598 called from <private>
default	13:46:02.014858-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44598 called from <private>
default	13:46:02.015373-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:02.015383-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:02.014652-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:02.014790-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44610)
default	13:46:02.014801-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44610 called from <private>
default	13:46:02.015467-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:02.015870-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6358, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:02.015472-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:02.020555-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:02.025362-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44609 called from <private>
default	13:46:02.026000-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44597 called from <private>
default	13:46:02.025371-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44609 called from <private>
default	13:46:02.025425-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:02.026015-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44597 called from <private>
default	13:46:02.026190-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:02.026731-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6358, subject=com.nexy.assistant,
default	13:46:02.032103-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:02.036292-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:02.036535-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44609 called from <private>
default	13:46:02.036549-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44609 called from <private>
default	13:46:02.036614-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:02.040966-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:02.041048-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:46:02.041131-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:46:02.041284-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:46:02.042637-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.042648-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.042743-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:02.042818-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.042917-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:02.043430-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:02.046062-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:02.046186-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:02.046194-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:02.046380-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:02.046730-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:02.046770-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:02.046859-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:02.049946-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:02.046912-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:02.052320-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44597 called from <private>
default	13:46:02.053941-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:02.052427-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:02.053921-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44609 called from <private>
default	13:46:02.053929-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44609 called from <private>
default	13:46:02.055113-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:46:02.062725-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:02.055681-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:02.060430-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44610)
default	13:46:02.062747-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:02.060455-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44610 called from <private>
default	13:46:02.060462-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44610 called from <private>
default	13:46:02.055711-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:02.064735-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44610)
default	13:46:02.069247-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.069277-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.069314-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:02.069339-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.069363-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:02.069386-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:02.063297-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
error	13:46:02.057636-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	13:46:02.064858-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44610 called from <private>
default	13:46:02.064929-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44610 called from <private>
default	13:46:02.063539-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:02.065001-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44610 called from <private>
default	13:46:02.063601-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:02.057790-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:46:02.063648-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44597 called from <private>
default	13:46:02.074554-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:02.078752-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137463 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:02.078787-0500	runningboardd	Assertion 398-334-1137463 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:02.081213-0500	runningboardd	Invalidating assertion 398-334-1137463 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.powerd>:334]
default	13:46:02.085263-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:46:02.086158-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:46:02.088453-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d84c00] Created node ADM::com.nexy.assistant_44610.44378.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:46:02.088653-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d84c00] Created node ADM::com.nexy.assistant_44610.44378.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:46:02.100982-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.101058-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.101150-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:02.109126-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:02.125730-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44610 called from <private>
default	13:46:02.125737-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44610 called from <private>
default	13:46:02.125860-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44610)
default	13:46:02.125869-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44610 called from <private>
default	13:46:02.125873-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44610 called from <private>
default	13:46:02.128089-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44610 called from <private>
default	13:46:02.129225-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6360, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:02.132714-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6360, subject=com.nexy.assistant,
default	13:46:02.136030-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:02.140695-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:02.140726-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:46:02.148017-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:44610 called from <private>
default	13:46:02.150484-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:46:02.152120-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.152132-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:02.152159-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.152195-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:02.152376-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:02.152362-0500	runningboardd	Invalidating assertion 398-334-1137464 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.powerd>:334]
default	13:46:02.152563-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137465 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:02.152618-0500	runningboardd	Assertion 398-334-1137465 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:02.149630-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44610 called from <private>
default	13:46:02.151485-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44610)
default	13:46:02.155249-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6361, subject=com.nexy.assistant,
default	13:46:02.159878-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:02.160060-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.163206-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:02.164133-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:02.166971-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137466 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:02.167009-0500	runningboardd	Assertion 398-334-1137466 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:02.168486-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:44610 called from <private>
default	13:46:02.172893-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:46:02.173302-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.180001-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.180082-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:02.180144-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:02.180232-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:02.180242-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:02.191395-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:03.198445-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:46:03.198877-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:46:03.199114-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:03.199238-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:46:03.199311-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14e, Nexy(25767), 'prim'', displayID:'com.nexy.assistant'}
default	13:46:03.199421-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:46:03.199431-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14e, Nexy(25767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 335 stopping recording
default	13:46:03.199490-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:46:03.199557-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:03.199630-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:03.199966-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:46:03.199966-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:46:03.199991-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:03.200438-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:03.200532-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:03.200628-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:03.200702-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:03.200738-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:46:03.200783-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:03.200927-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:46:03.200956-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:03.200979-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:46:03.205176-0500	runningboardd	Invalidating assertion 398-334-1137466 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.powerd>:334]
default	13:46:03.208014-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:46:03.210885-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:03.210900-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:03.210915-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:03.210922-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:03.210928-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:03.210935-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:03.211085-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:03.304738-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb2c24d540) Selecting device 0 from destructor
default	13:46:03.304759-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24d540)
default	13:46:03.304769-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24d540) not already running
default	13:46:03.304776-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb2c24d540) disconnecting device 89
default	13:46:03.304785-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb2c24d540) destroying ioproc 0xa for device 89
default	13:46:03.304826-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:46:03.304868-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:46:03.305069-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb2c24d540) nothing to setup
default	13:46:03.305082-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24d540) adding 0 device listeners to device 0
default	13:46:03.305090-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24d540) adding 0 device delegate listeners to device 0
default	13:46:03.305099-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24d540) removing 7 device listeners from device 89
default	13:46:03.305361-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24d540) removing 0 device delegate listeners from device 89
default	13:46:03.305380-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24d540)
default	13:46:03.311955-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:03.311974-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:03.311985-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring role changes because this process is not role managed
default	13:46:03.311996-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:03.312047-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:03.320065-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:03.408895-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25769.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25769, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=25769, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:46:03.410024-0500	tccd	AUTHREQ_SUBJECT: msgID=25769.1, subject=com.nexy.assistant,
default	13:46:03.410362-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	13:46:03.418622-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12337, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25769, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=25769, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:46:03.419667-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12337, subject=com.nexy.assistant,
default	13:46:03.420193-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	13:46:03.444458-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
error	13:46:03.460197-0500	tccd	spooky magic for /Applications/Nexy.app/Contents/MacOS/Nexy (0x51282211) at text offset: 81920
default	13:46:03.461771-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 25690: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 57681a00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 0;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 0;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 655360;
    kTCCCodeIdentityTeamID = "";
}
default	13:46:03.472299-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:46:04.069767-0500	Nexy	[0xb2df5c640] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:46:04.070785-0500	Nexy	[0xb2df5c8c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:46:04.073337-0500	Nexy	Received configuration update from daemon (initial)
default	13:46:04.104048-0500	Nexy	[0xb2df5ca00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:46:04.104422-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:46:04.104547-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25767.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:46:04.105979-0500	tccd	AUTHREQ_SUBJECT: msgID=25767.2, subject=com.nexy.assistant,
default	13:46:04.106493-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	13:46:04.115047-0500	Nexy	[0xb2df5ca00] invalidated after the last release of the connection object
default	13:46:04.115470-0500	Nexy	[0xb2df5ca00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:46:04.115684-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:46:04.115776-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25767.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:46:04.116278-0500	tccd	AUTHREQ_SUBJECT: msgID=25767.3, subject=com.nexy.assistant,
default	13:46:04.116703-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	13:46:04.123811-0500	Nexy	[0xb2df5ca00] invalidated after the last release of the connection object
default	13:46:04.123838-0500	Nexy	[0xb2df5ca00] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:46:04.123887-0500	Nexy	[0xb2df5ca00] invalidated after the last release of the connection object
default	13:46:04.124032-0500	Nexy	[0xb2df5cb40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:46:04.124253-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25767.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:46:04.124711-0500	tccd	AUTHREQ_SUBJECT: msgID=25767.4, subject=com.nexy.assistant,
default	13:46:04.125015-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	13:46:04.132147-0500	Nexy	[0xb2df5cb40] invalidated after the last release of the connection object
default	13:46:04.132303-0500	Nexy	server port 0x0000bf07, session port 0x0000ed07
default	13:46:04.132824-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12338, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:46:04.132838-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:46:04.133239-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12338, subject=com.nexy.assistant,
default	13:46:04.133716-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	13:46:04.141416-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 45ED3C11-A553-4B14-B08E-ED49256E5597 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52050,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xfea28d42 tp_proto=0x06"
default	13:46:04.141450-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52050<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385756 t_state: SYN_SENT process: Nexy:25767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x91cfaa8f
default	13:46:04.141803-0500	kernel	tcp connected: [<IPv4-redacted>:52050<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385756 t_state: ESTABLISHED process: Nexy:25767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x91cfaa8f
default	13:46:04.145100-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	13:46:04.145097-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52050<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385756 t_state: FIN_WAIT_1 process: Nexy:25767 Duration: 0.003 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x91cfaa8f
default	13:46:04.145104-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52050<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385756 t_state: FIN_WAIT_1 process: Nexy:25767 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:46:04.145199-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	13:46:04.145222-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4E484B66-6EDB-41C5-B05D-A36047B680EA flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52051,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x188f3dad tp_proto=0x06"
default	13:46:04.145232-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52051<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385757 t_state: SYN_SENT process: Nexy:25767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x99ff9193
default	13:46:04.145476-0500	kernel	tcp connected: [<IPv4-redacted>:52051<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385757 t_state: ESTABLISHED process: Nexy:25767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x99ff9193
default	13:46:04.145597-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52051<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385757 t_state: FIN_WAIT_1 process: Nexy:25767 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x99ff9193
default	13:46:04.145603-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52051<-><IPv4-redacted>:53] interface: utun6 (skipped: 5295)
so_gencnt: 4385757 t_state: FIN_WAIT_1 process: Nexy:25767 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:46:04.145791-0500	Nexy	nw_path_libinfo_path_check [A7268979-ADA0-43C5-8FFA-79401C006226 IPv4#1d6b9163:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	13:46:04.146038-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3D42F44A-757D-4D32-B1F1-50B89423A4CE flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52052,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x501a08d2 tp_proto=0x06"
default	13:46:04.146044-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52052<-><IPv4-redacted>:443] interface: utun6 (skipped: 5295)
so_gencnt: 4385758 t_state: SYN_SENT process: Nexy:25767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbb86c417
default	13:46:04.146203-0500	kernel	tcp connected: [<IPv4-redacted>:52052<-><IPv4-redacted>:443] interface: utun6 (skipped: 5295)
so_gencnt: 4385758 t_state: ESTABLISHED process: Nexy:25767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbb86c417
default	13:46:04.306437-0500	Nexy	[0xb2df5cb40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:46:04.307740-0500	Nexy	[0xb2df5cc80] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:46:04.310558-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:46:04.316149-0500	Nexy	server port 0x0000ed07, session port 0x0000ed07
default	13:46:04.318753-0500	Nexy	New connection 0x1a597f main
default	13:46:04.324167-0500	Nexy	CHECKIN: pid=25767
default	13:46:04.329885-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:25767" ID:398-363-1137480 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:46:04.329941-0500	runningboardd	Assertion 398-363-1137480 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.329933-0500	launchservicesd	CHECKIN:0x0-0x128b28a 25767 com.nexy.assistant
default	13:46:04.330240-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:25767" ID:398-363-1137481 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:46:04.330070-0500	Nexy	CHECKEDIN: pid=25767 asn=0x0-0x128b28a foreground=0
default	13:46:04.330364-0500	Nexy	[0xb2df5cf00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	13:46:04.330259-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:04.330372-0500	runningboardd	Assertion 398-363-1137481 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.330343-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:04.330410-0500	runningboardd	[anon<Nexy>(501):25767] Set darwin role to: UserInteractive
default	13:46:04.330574-0500	Nexy	[0xb2df5d040] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:46:04.330579-0500	Nexy	[0xb2df5d040] Connection returned listener port: 0xdc03
default	13:46:04.330445-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:04.330811-0500	Nexy	[0xb2cc98600] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xb2df5d040.peer[363].0xb2cc98600
default	13:46:04.330518-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:04.331114-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:46:04.331258-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:46:04.331876-0500	Nexy	FRONTLOGGING: version 1
default	13:46:04.331897-0500	Nexy	Registered, pid=25767 ASN=0x0,0x128b28a
default	13:46:04.331923-0500	Nexy	[0xb2df5d180] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:46:04.332098-0500	WindowServer	1a597f[CreateApplication]: Process creation: 0x0-0x128b28a (Nexy) connectionID: 1A597F pid: 25767 in session 0x101
default	13:46:04.334779-0500	runningboardd	Invalidating assertion 398-363-1137480 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	13:46:04.334887-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:04.335057-0500	Nexy	[0xb2df5d040] Connection returned listener port: 0xdc03
default	13:46:04.335361-0500	Nexy	BringForward: pid=25767 asn=0x0-0x128b28a bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	13:46:04.335665-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:46:04.336788-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:46:04.337415-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:46:04.354271-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:46:04.354365-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:46:04.357955-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:46:04.357961-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:46:04.357990-0500	Nexy	Initializing connection
default	13:46:04.358015-0500	Nexy	Removing all cached process handles
default	13:46:04.358025-0500	Nexy	Sending handshake request attempt #1 to server
default	13:46:04.358028-0500	Nexy	Creating connection to com.apple.runningboard
default	13:46:04.358032-0500	Nexy	[0xb2df5d2c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:46:04.358244-0500	runningboardd	Setting client for [anon<Nexy>(501):25767] as ready
default	13:46:04.358282-0500	Nexy	[0xb2df5d040] Connection returned listener port: 0xdc03
default	13:46:04.358594-0500	Nexy	Handshake succeeded
default	13:46:04.358603-0500	Nexy	Identity resolved as anon<Nexy>(501)
default	13:46:04.358831-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 200000001b pid: 25767
default	13:46:04.360281-0500	Nexy	[0xb2df5d040] Connection returned listener port: 0xdc03
default	13:46:04.361071-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:46:04.361079-0500	Nexy	[0xb2df5d540] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:46:04.361110-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:46:04.361135-0500	Nexy	[0xb2df5d680] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:46:04.363327-0500	Nexy	[0xb2df5d680] Connection returned listener port: 0x14603
default	13:46:04.364108-0500	Nexy	Registered process with identifier 25767-1730642
default	13:46:04.364176-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "frontmost:25767" ID:398-363-1137482 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractiveFocal" sourceEnvironment:"(null)">
	]>
default	13:46:04.364216-0500	runningboardd	Assertion 398-363-1137482 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.364444-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:04.364660-0500	WindowServer	1a597f[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x128b28a (Nexy) mainConnectionID: 1A597F;
} for reason: updated frontmost process
default	13:46:04.364459-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:04.364501-0500	runningboardd	[anon<Nexy>(501):25767] Set darwin role to: UserInteractiveFocal
default	13:46:04.364727-0500	WindowServer	1a597f[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x128b28a (Nexy) -> <pid: 25767>
default	13:46:04.364562-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:04.364665-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:04.364892-0500	WindowServer	new deferring rules for pid:393: [
    [393-B09A]; <keyboardFocus; Nexy:0x0-0x128b28a>; () -> <pid: 25767>; reason: frontmost PSN --> outbound target,
    [393-B099]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x128b28a; pid: 393>; reason: frontmost PSN,
    [393-B098]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	13:46:04.365039-0500	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-B09A]; <keyboardFocus; Nexy:0x0-0x128b28a>; () -> <pid: 25767>; reason: frontmost PSN --> outbound target,
    [393-B099]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x128b28a; pid: 393>; reason: frontmost PSN,
    [393-B098]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	13:46:04.365607-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "notification:25767" ID:398-363-1137483 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	13:46:04.365932-0500	runningboardd	Assertion 398-363-1137483 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.367937-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x128b28a; pid: 393>,
    <pid: 25767>
]
default	13:46:04.370974-0500	Nexy	[0xb2df5d900] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	13:46:04.378113-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:04.378123-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:04.378133-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:04.378166-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:04.378763-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	13:46:04.379245-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:04.379344-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2400000020 pid: 25767
default	13:46:04.384902-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:04.385620-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xb2cacd220
 (
    "<NSAquaAppearance: 0xb2cacd400>",
    "<NSSystemAppearance: 0xb2cacd360>"
)>
default	13:46:04.389031-0500	Nexy	[0xb2df5de00] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	13:46:04.389230-0500	Nexy	[0xb2df5e080] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	13:46:04.390666-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	13:46:04.390806-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	13:46:04.390810-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	13:46:04.390826-0500	Nexy	[0xb2df5df40] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	13:46:04.390861-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	13:46:04.390892-0500	Nexy	[0xb2df5e1c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:46:04.390929-0500	Nexy	FBSWorkspace registering source: <private>
default	13:46:04.391328-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:46:04.391521-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	13:46:04.391874-0500	Nexy	<FBSWorkspaceScenesClient:0xb2cace080 <private>> attempting immediate handshake from activate
default	13:46:04.391906-0500	Nexy	<FBSWorkspaceScenesClient:0xb2cace080 <private>> sent handshake
default	13:46:04.391972-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	13:46:04.392219-0500	ControlCenter	Asked to bootstrap a new process for handle: [anon<Nexy>(501):25767]
default	13:46:04.392241-0500	ControlCenter	Creating process (sync=true) for handle: [anon<Nexy>(501):25767]
default	13:46:04.392309-0500	ControlCenter	[anon<Nexy>:25767] Registering event dispatcher at init
default	13:46:04.392375-0500	ControlCenter	Created <FBWorkspace: 0xaf868dd60; <FBProcess: 0xaf8cff900; anon<Nexy>:25767(v1A6852)>>
default	13:46:04.392391-0500	ControlCenter	Bootstrapping anon<Nexy>
default	13:46:04.392432-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	13:46:04.392584-0500	runningboardd	Launch request for anon<Nexy>(501)[0] is using uid 501 (divined from auid 501 euid 501)
default	13:46:04.392625-0500	runningboardd	Executing launch request for anon<Nexy>(501) (FBProcess) from requestor: [osservice<com.apple.controlcenter(501)>:632]
default	13:46:04.393409-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	13:46:04.393452-0500	ControlCenter	[anon<Nexy>:25767] Bootstrap success!
default	13:46:04.394062-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:398-632-1137484 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	13:46:04.394117-0500	runningboardd	Assertion 398-632-1137484 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.394186-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	13:46:04.394408-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:04.394619-0500	Nexy	Requesting scene <FBSScene: 0xb2cace3a0; com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7> from com.apple.controlcenter.statusitems
default	13:46:04.394422-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:04.394603-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:04.394819-0500	Nexy	Request for <FBSScene: 0xb2cace3a0; com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7> complete!
default	13:46:04.394769-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:04.394862-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	13:46:04.396122-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	13:46:04.396416-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	13:46:04.396671-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	13:46:04.396692-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	13:46:04.396953-0500	Nexy	Requesting scene <FBSScene: 0xb2cace4e0; com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	13:46:04.397046-0500	Nexy	Request for <FBSScene: 0xb2cace4e0; com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView> complete!
default	13:46:04.398056-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:46:04.398066-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	13:46:04.400831-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:46:04.400841-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	13:46:04.400883-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	13:46:04.401243-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:46:04.401252-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	13:46:04.402093-0500	ControlCenter	Adding: <FBProcess: 0xaf8cff900; anon<Nexy>:25767(v1A6852)>
default	13:46:04.402146-0500	ControlCenter	[anon<Nexy>:25767] Connection established.
default	13:46:04.402203-0500	ControlCenter	[anon<Nexy>:25767] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xaf8b57410>
default	13:46:04.402225-0500	ControlCenter	[anon<Nexy>:25767] Connection to remote process established!
default	13:46:04.402290-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:04.406436-0500	Nexy	Registering for test daemon availability notify post.
default	13:46:04.406461-0500	ControlCenter	Asked to bootstrap a new process for handle: [anon<Nexy>(501):25767]
default	13:46:04.406480-0500	ControlCenter	A process already exists for this handle: <FBProcess: 0xaf8cff900; anon<Nexy>:25767(v1A6852)>
default	13:46:04.406533-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:46:04.406575-0500	ControlCenter	[anon<Nexy>:25767] Registered new scene: <FBWorkspaceScene: 0xaf5086580; com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7> (fromRemnant = 0)
default	13:46:04.406595-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:46:04.406610-0500	ControlCenter	[anon<Nexy>:25767] Workspace interruption policy did change: reconnect
default	13:46:04.406658-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:46:04.406783-0500	Nexy	Request for <FBSScene: 0xb2cace3a0; com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7> complete!
default	13:46:04.406785-0500	ControlCenter	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7] Client process connected: [anon<Nexy>(501):25767]
default	13:46:04.406882-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:398-632-1137485 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	13:46:04.406958-0500	runningboardd	Assertion 398-632-1137485 (target:[anon<Nexy>(501):25767]) will be created as inactive as originator process has not exited
default	13:46:04.407049-0500	ControlCenter	[anon<Nexy>:25767] Setting process visibility to: Background
default	13:46:04.407350-0500	ControlCenter	Asked to bootstrap a new process for handle: [anon<Nexy>(501):25767]
default	13:46:04.407350-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-1137486 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	13:46:04.407367-0500	ControlCenter	A process already exists for this handle: <FBProcess: 0xaf8cff900; anon<Nexy>:25767(v1A6852)>
default	13:46:04.407427-0500	ControlCenter	[anon<Nexy>:25767] Registered new scene: <FBWorkspaceScene: 0xaf5086dc0; com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	13:46:04.407453-0500	runningboardd	Assertion 398-632-1137486 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.407562-0500	Nexy	Request for <FBSScene: 0xb2cace4e0; com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView> complete!
default	13:46:04.407531-0500	ControlCenter	[anon<Nexy>:25767] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	13:46:04.407715-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:04.407803-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:04.407567-0500	ControlCenter	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Client process connected: [anon<Nexy>(501):25767]
default	13:46:04.407829-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:04.407886-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:04.407982-0500	Nexy	<FBSWorkspaceScenesClient:0xb2cace080 <private>> Reconnecting scene com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7
default	13:46:04.408288-0500	Nexy	<FBSWorkspaceScenesClient:0xb2cace080 <private>> Reconnecting scene com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView
default	13:46:04.408453-0500	Nexy	[0xb2df5e580] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	13:46:04.408749-0500	Nexy	[0xb2df5d040] Connection returned listener port: 0xdc03
default	13:46:04.408941-0500	Nexy	SignalReady: pid=25767 asn=0x0-0x128b28a
default	13:46:04.409220-0500	Nexy	SIGNAL: pid=25767 asn=0x0x-0x128b28a
default	13:46:04.409848-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	13:46:04.414046-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:04.415153-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:46:04.417076-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	13:46:04.417081-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	13:46:04.417109-0500	Nexy	[0xb2df5cdc0] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	13:46:04.417176-0500	Nexy	[0xb2df5cdc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:46:04.418081-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	13:46:04.419600-0500	Nexy	[0xb2df5cdc0] activating connection: mach=false listener=false peer=false name=com.apple.ViewBridgeAuxiliary
default	13:46:04.419781-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-25767). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	13:46:04.420434-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-25767)
default	13:46:04.420533-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(421A29C0, (bid:com.nexy.assistant-Item-0-25767)) for (bid:com.nexy.assistant-Item-0-25767)
default	13:46:04.420893-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	13:46:04.421000-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-25767)]
default	13:46:04.421120-0500	ControlCenter	Created instance DisplayableId(AA4EC4A1) in .menuBar for DisplayableAppStatusItemType(421A29C0, (bid:com.nexy.assistant-Item-0-25767)) .menuBar
default	13:46:04.424726-0500	Nexy	[0xb2df5e6c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:46:04.425045-0500	Nexy	[0xb2df5e940] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:46:04.425050-0500	Nexy	[0xb2df5e940] Connection returned listener port: 0x1f703
default	13:46:04.425772-0500	Nexy	[0xb2df5cdc0] invalidated after the last release of the connection object
default	13:46:04.427711-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137487 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:04.427753-0500	runningboardd	Assertion 398-25767-1137487 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.428147-0500	runningboardd	Invalidating assertion 398-25767-1137487 (target:[anon<Nexy>(501):25767]) from originator [anon<Nexy>(501):25767]
default	13:46:04.428308-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137488 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:04.428392-0500	runningboardd	Assertion 398-25767-1137488 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.428306-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:04.428666-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:04.428720-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:04.428881-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:04.428071-0500	ControlCenter	Created ephemaral instance DisplayableId(AA4EC4A1) for (bid:com.nexy.assistant-Item-0-25767) with positioning .ephemeral
default	13:46:04.435599-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:04.435620-0500	runningboardd	Invalidating assertion 398-25767-1137488 (target:[anon<Nexy>(501):25767]) from originator [anon<Nexy>(501):25767]
default	13:46:04.435729-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137489 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:04.435782-0500	runningboardd	Assertion 398-25767-1137489 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.436166-0500	runningboardd	Invalidating assertion 398-25767-1137489 (target:[anon<Nexy>(501):25767]) from originator [anon<Nexy>(501):25767]
default	13:46:04.436269-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137490 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:04.436316-0500	runningboardd	Assertion 398-25767-1137490 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.436690-0500	runningboardd	Invalidating assertion 398-25767-1137490 (target:[anon<Nexy>(501):25767]) from originator [anon<Nexy>(501):25767]
default	13:46:04.436783-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137491 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:04.436822-0500	runningboardd	Assertion 398-25767-1137491 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.437166-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:46:04.437159-0500	runningboardd	Invalidating assertion 398-25767-1137491 (target:[anon<Nexy>(501):25767]) from originator [anon<Nexy>(501):25767]
default	13:46:04.437566-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7] Sending action(s) in update: NSSceneFenceAction
default	13:46:04.442034-0500	Nexy	[C:2] Alloc <private>
default	13:46:04.442055-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7] Received action(s): NSStatusItemChangeVisibilityAction
default	13:46:04.442056-0500	Nexy	[0xb2df5ca00] activating connection: mach=false listener=false peer=false name=(anonymous)
error	13:46:04.442176-0500	kernel	Sandbox: WindowManager(584) deny(1) mach-task-name others [Nexy(25767)]
default	13:46:04.443030-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7] Observer <NSSceneStatusItem: 0xb2df62a00> handled action(s): <private>
default	13:46:04.443424-0500	WindowManager	Connection activated | (25767) Nexy
default	13:46:04.443432-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	13:46:04.444789-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:46:04.445137-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:46:04.445353-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7] Sending action(s) in update: NSSceneFenceAction
default	13:46:04.534496-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:04.534526-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:04.534538-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:04.534557-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:04.535789-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	13:46:04.538184-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:04.538394-0500	Nexy	Start service name com.apple.spotlightknowledged
default	13:46:04.538927-0500	Nexy	[GMS] availability notification token 87
default	13:46:04.638833-0500	kernel	udp connect: [<IPv4-redacted>:52588<-><IPv4-redacted>:443] interface:  (skipped: 1000)
so_gencnt: 4385761 so_state: 0x0002 process: Nexy:25767 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x8a69a9e3
default	13:46:04.638844-0500	kernel	udp_connection_summary [<IPv4-redacted>:52588<-><IPv4-redacted>:443] interface:  (skipped: 1000)
so_gencnt: 4385761 so_state: 0x0002 process: Nexy:25767 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x8a69a9e3 flowctl: 0us (0x)
default	13:46:04.641787-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 8C7D4CC2-42B0-4756-8FDB-B38C4B0B5333 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52054,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x13ffc5a6 tp_proto=0x06"
default	13:46:04.641829-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52054<-><IPv4-redacted>:443] interface: utun6 (skipped: 5295)
so_gencnt: 4385763 t_state: SYN_SENT process: Nexy:25767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb68e5dbe
default	13:46:04.642189-0500	kernel	tcp connected: [<IPv4-redacted>:52054<-><IPv4-redacted>:443] interface: utun6 (skipped: 5295)
so_gencnt: 4385763 t_state: ESTABLISHED process: Nexy:25767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb68e5dbe
default	13:46:04.649172-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7] Sending action(s) in update: NSSceneFenceAction
default	13:46:04.668939-0500	ControlCenter	[anon<Nexy>:25767] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	13:46:04.669035-0500	runningboardd	Invalidating assertion 398-632-1137486 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	13:46:04.670660-0500	Nexy	[0xb2df5cdc0] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	13:46:04.672637-0500	Nexy	+[IMKClient subclass]: chose IMKClient_Modern
default	13:46:04.672652-0500	Nexy	+[IMKInputSession subclass]: chose IMKInputSession_Modern
default	13:46:04.674292-0500	Nexy	[0xb2df5e800] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	13:46:04.674869-0500	Nexy	[0xb2df5ea80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:46:04.688319-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25774.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25774, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=25774, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:46:04.689373-0500	tccd	AUTHREQ_SUBJECT: msgID=25774.1, subject=com.nexy.assistant,
default	13:46:04.689702-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	13:46:04.690601-0500	Nexy	[0xb2df5ebc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:46:04.690869-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25767.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:46:04.691443-0500	tccd	AUTHREQ_SUBJECT: msgID=25767.5, subject=com.nexy.assistant,
default	13:46:04.692173-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	13:46:04.697731-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12339, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25774, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=25774, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:46:04.698574-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12339, subject=com.nexy.assistant,
default	13:46:04.699132-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:04.699678-0500	Nexy	[0xb2df5ebc0] invalidated after the last release of the connection object
default	13:46:04.699817-0500	Nexy	[0xb2df5ebc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:46:04.700063-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25767.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:46:04.700659-0500	tccd	AUTHREQ_SUBJECT: msgID=25767.6, subject=com.nexy.assistant,
default	13:46:04.701363-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	13:46:04.708348-0500	Nexy	[0xb2df5ebc0] invalidated after the last release of the connection object
default	13:46:04.709969-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	13:46:04.711865-0500	Nexy	[0xb2df5ebc0] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	13:46:04.711930-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	13:46:04.711983-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	13:46:04.715806-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=18126.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=18126, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	13:46:04.715823-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=18126, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:46:04.716420-0500	tccd	AUTHREQ_SUBJECT: msgID=18126.4, subject=com.nexy.assistant,
default	13:46:04.716978-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	13:46:04.717401-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:04.727194-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12340, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:46:04.727207-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:46:04.727699-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12340, subject=com.nexy.assistant,
default	13:46:04.728037-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d1db000 at /Applications/Nexy.app
error	13:46:04.733485-0500	tccd	spooky magic for /Applications/Nexy.app/Contents/MacOS/Nexy (0x51282211) at text offset: 81920
default	13:46:04.734920-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 25690: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 62681a00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 0;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 0;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 655360;
    kTCCCodeIdentityTeamID = "";
}
default	13:46:04.745517-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:46:04.746180-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	13:46:04.760241-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:04.760291-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	13:46:04.760320-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	13:46:04.762382-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:04.762393-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:04.762403-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:04.762409-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:04.762417-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:04.762423-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:04.762595-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:04.774104-0500	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x128b28a (Nexy) mainConnectionID: 1A597F;
} for reason: deferringPolicyEvaluationSuppression
default	13:46:04.774199-0500	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x128b28a (Nexy) -> <pid: 25767>
default	13:46:04.774303-0500	WindowServer	new deferring rules for pid:393: [
    [393-B09D]; <keyboardFocus; Nexy:0x0-0x128b28a>; () -> <pid: 25767>; reason: frontmost PSN --> outbound target,
    [393-B09C]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x128b28a; pid: 393>; reason: frontmost PSN,
    [393-B09B]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	13:46:04.774336-0500	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-B09D]; <keyboardFocus; Nexy:0x0-0x128b28a>; () -> <pid: 25767>; reason: frontmost PSN --> outbound target,
    [393-B09C]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x128b28a; pid: 393>; reason: frontmost PSN,
    [393-B09B]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	13:46:04.775865-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x128b28a; pid: 393>,
    <pid: 25767>
]
default	13:46:04.776199-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:04.776210-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:04.776220-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:04.776238-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:04.780268-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:04.932527-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "AppDrawing" ID:398-393-1137496 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:04.932596-0500	runningboardd	Assertion 398-393-1137496 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:04.932909-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:04.932919-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:04.932929-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:04.932945-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:04.936283-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:05.426955-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:05.429250-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:05.427057-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44609 called from <private>
default	13:46:05.429311-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44597 called from <private>
default	13:46:05.427086-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44609 called from <private>
default	13:46:05.429316-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44597 called from <private>
default	13:46:05.430136-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44610)
default	13:46:05.430073-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44598)
default	13:46:05.430094-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44598 called from <private>
default	13:46:05.430180-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44610 called from <private>
default	13:46:05.430099-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44598 called from <private>
default	13:46:05.430186-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44610 called from <private>
default	13:46:05.452605-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:05.452539-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:05.452636-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44598)
default	13:46:05.452575-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44610)
default	13:46:05.452651-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44598 called from <private>
default	13:46:05.452593-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44610 called from <private>
default	13:46:05.452657-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44598 called from <private>
default	13:46:05.452605-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44610 called from <private>
default	13:46:05.452862-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:05.452660-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:05.452872-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:05.452668-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:05.464519-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44597 called from <private>
default	13:46:05.464535-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44597 called from <private>
default	13:46:05.464612-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:05.465826-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44609 called from <private>
default	13:46:05.465846-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44609 called from <private>
default	13:46:05.465928-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:05.469597-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:05.469996-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:05.469785-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44597 called from <private>
default	13:46:05.469798-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44597 called from <private>
default	13:46:05.470314-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44609 called from <private>
default	13:46:05.469924-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:05.470326-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44609 called from <private>
default	13:46:05.470422-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:05.473522-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:05.473790-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:05.473803-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:05.474026-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:05.474044-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:05.474055-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:05.474066-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:05.474072-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:05.474078-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:05.474083-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:05.474104-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:05.474127-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:05.474140-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:05.474183-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:05.474241-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:05.474276-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:05.474322-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:05.474390-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:05.479398-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:05.479568-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:05.479578-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:05.479770-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:05.479783-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:05.479796-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:05.479808-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:05.479815-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:05.479836-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:05.479871-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:05.479891-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:05.479908-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:05.480027-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:05.480062-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:05.480094-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:05.480146-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:05.480182-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:05.480221-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:05.485541-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:05.484648-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:05.485744-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:05.485755-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:05.485769-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44597 called from <private>
default	13:46:05.484918-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:05.485778-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44597 called from <private>
default	13:46:05.484926-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:05.484941-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44609 called from <private>
default	13:46:05.484951-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44609 called from <private>
default	13:46:05.496023-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb2c24dc40) Selecting device 83 from constructor
default	13:46:05.496047-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24dc40)
default	13:46:05.496196-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24dc40) not already running
default	13:46:05.496217-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb2c24dc40) nothing to teardown
default	13:46:05.496229-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb2c24dc40) connecting device 83
default	13:46:05.497195-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24dc40) Device ID: 83 (Input:No | Output:Yes): true
default	13:46:05.497358-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb2c24dc40) created ioproc 0xb for device 83
default	13:46:05.497498-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24dc40) adding 7 device listeners to device 83
default	13:46:05.497878-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24dc40) adding 0 device delegate listeners to device 83
default	13:46:05.497888-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24dc40)
default	13:46:05.498054-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:05.498084-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:46:05.498126-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:05.498136-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:46:05.498146-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:05.498287-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24dc40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:05.498305-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24dc40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:05.498311-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:05.498317-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24dc40) removing 0 device listeners from device 0
default	13:46:05.498321-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24dc40) removing 0 device delegate listeners from device 0
default	13:46:05.498326-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24dc40)
default	13:46:05.498337-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb2c24dc40) caller requesting device change from 83 to 83
default	13:46:05.498342-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24dc40)
default	13:46:05.498359-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xb2c24dc40) exiting with nothing to do
default	13:46:05.499224-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:46:05.499660-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:46:05.502619-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb2c24dc40) Selecting device 0 from destructor
default	13:46:05.502629-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24dc40)
default	13:46:05.502635-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24dc40) not already running
default	13:46:05.502640-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb2c24dc40) disconnecting device 83
default	13:46:05.502648-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb2c24dc40) destroying ioproc 0xb for device 83
default	13:46:05.502676-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	13:46:05.502743-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:46:05.502844-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb2c24dc40) nothing to setup
default	13:46:05.502852-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24dc40) adding 0 device listeners to device 0
default	13:46:05.502857-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24dc40) adding 0 device delegate listeners to device 0
default	13:46:05.502862-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24dc40) removing 7 device listeners from device 83
default	13:46:05.503201-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24dc40) removing 0 device delegate listeners from device 83
default	13:46:05.503215-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24dc40)
default	13:46:05.504137-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb2c24dc40) Selecting device 83 from constructor
default	13:46:05.504151-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24dc40)
default	13:46:05.504156-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24dc40) not already running
default	13:46:05.504160-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb2c24dc40) nothing to teardown
default	13:46:05.504165-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb2c24dc40) connecting device 83
default	13:46:05.504266-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24dc40) Device ID: 83 (Input:No | Output:Yes): true
default	13:46:05.504371-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb2c24dc40) created ioproc 0xc for device 83
default	13:46:05.504497-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24dc40) adding 7 device listeners to device 83
default	13:46:05.504740-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24dc40) adding 0 device delegate listeners to device 83
default	13:46:05.504750-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24dc40)
default	13:46:05.504848-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:05.504868-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:46:05.504874-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:05.504883-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:46:05.504893-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:05.505001-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24dc40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:05.505012-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24dc40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:05.505019-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:05.505024-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24dc40) removing 0 device listeners from device 0
default	13:46:05.505029-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24dc40) removing 0 device delegate listeners from device 0
default	13:46:05.505034-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24dc40)
default	13:46:05.505044-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb2c24dc40) caller requesting device change from 83 to 83
default	13:46:05.505048-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24dc40)
default	13:46:05.505053-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xb2c24dc40) exiting with nothing to do
default	13:46:05.505060-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	13:46:05.505434-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:46:05.505789-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:46:05.507483-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137499 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:05.507550-0500	runningboardd	Assertion 398-25767-1137499 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:05.507817-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137500 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:05.507823-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:05.507837-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:05.507853-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:05.507855-0500	runningboardd	Assertion 398-334-1137500 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:05.507916-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:05.511487-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:05.511517-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:05.511563-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:05.511615-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:05.511806-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:05.514684-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:05.572495-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	13:46:06.171816-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	13:46:06.172660-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	13:46:06.172746-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:46:06.172774-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef14e, Nexy(25767), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	13:46:06.172807-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:06.172841-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef14e, Nexy(25767), 'prim'', AudioCategory changed to 'MediaPlayback'
default	13:46:06.172863-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:06.172898-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	13:46:06.172909-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 335 starting playing
default	13:46:06.172981-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:06.173017-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:06.172964-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:06.172995-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	13:46:06.173039-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14e, Nexy(25767), 'prim'', displayID:'com.nexy.assistant'}
default	13:46:06.173099-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	13:46:06.173130-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	13:46:06.173188-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef14e to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":25767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef14e, sessionType: 'prim', isRecording: false }, 
]
default	13:46:06.173259-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	13:46:06.173290-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:06.173324-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:46:06.173475-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	13:46:06.173549-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	13:46:06.173576-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	13:46:06.173593-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	13:46:06.173603-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	13:46:06.173613-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	13:46:06.173655-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	13:46:06.173712-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	13:46:07.419142-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 100NumofApp 1
default	13:46:09.381344-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=0
default	13:46:09.383815-0500	runningboardd	Assertion did invalidate due to timeout: 398-363-1137483 (target:[anon<Nexy>(501):25767])
default	13:46:09.579819-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:09.579835-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:09.579848-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:09.579869-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:09.584244-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:10.418904-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 100NumofApp 1
default	13:46:11.331654-0500	runningboardd	Invalidating assertion 398-363-1137482 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	13:46:11.340886-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	13:46:11.379453-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:11.379466-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:11.379498-0500	runningboardd	[anon<Nexy>(501):25767] Set darwin role to: UserInteractive
default	13:46:11.379508-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:11.379527-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:11.385374-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:11.578663-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	13:46:11.578939-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:46:11.579044-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 335 stopping playing
default	13:46:11.579104-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:46:11.579160-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:11.579241-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:11.579349-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:11.579570-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:11.579551-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:46:11.579657-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:11.579564-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:11.579458-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef14e to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":25767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef14e, sessionType: 'prim', isRecording: false }, 
]
default	13:46:11.579689-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:46:11.586112-0500	runningboardd	Invalidating assertion 398-25767-1137499 (target:[anon<Nexy>(501):25767]) from originator [anon<Nexy>(501):25767]
default	13:46:11.586258-0500	runningboardd	Invalidating assertion 398-334-1137500 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.powerd>:334]
default	13:46:11.591108-0500	coreaudiod	Sending message. { reporterID=110668422316036, category=IO, type=error, message=["output_device_transport_list": Optional(Bluetooth), "issue_type": Optional(overload), "reporting_latency": Optional(20862666), "wg_external_wakeups": Optional(3), "anchor_sample_time": Optional(2684), "lateness": Optional(432), "input_device_transport_list": Optional(), "io_cycle": Optional(505), "safety_violation": Optional(1), "start_time": Optional(9419578929114), "cause_set": Optional(12), "careporting_timestamp": 1762109171.590934, "input_device_source_list": Optional(), "io_frame_counter": Optional(258560), "is_prewarming": Optional(0), "num_continuous_silent_io_cycles": Optional(86), "overload_type": Optional(Overload), "safety_violation_sample_gap": Optional(462), "safety_violation_time_gap": Optional(0.009625), "io_page_faults": Optional(0), "HostApplicationDisplayID": Optional(com.nexy.assistant), "multi_cycle_io_page_faults_duration": Optional(0), "deadline": Optional(261788), "other_active_clients": Optional([  ]), "wg_system_time_mach": Optional(2483), "i<…> }
default	13:46:11.690747-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:11.690761-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:11.690773-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:11.690794-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:11.695031-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:11.709235-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7] Sending action(s) in update: NSSceneFenceAction
default	13:46:11.766874-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25775.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25775, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=25775, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:46:11.768071-0500	tccd	AUTHREQ_SUBJECT: msgID=25775.1, subject=com.nexy.assistant,
default	13:46:11.768455-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:11.776947-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12343, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25775, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=25775, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:46:11.777750-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12343, subject=com.nexy.assistant,
default	13:46:11.778111-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:11.796811-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
error	13:46:11.816098-0500	tccd	spooky magic for /Applications/Nexy.app/Contents/MacOS/Nexy (0x51282211) at text offset: 81920
default	13:46:11.817734-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 25690: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 64681a00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 0;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 0;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 655360;
    kTCCCodeIdentityTeamID = "";
}
default	13:46:11.834734-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:46:12.423178-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25776.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25776, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=25776, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:46:12.424325-0500	tccd	AUTHREQ_SUBJECT: msgID=25776.1, subject=com.nexy.assistant,
default	13:46:12.424789-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:12.432992-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12346, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25776, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=25776, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:46:12.433789-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12346, subject=com.nexy.assistant,
default	13:46:12.434113-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:12.452649-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
error	13:46:12.467988-0500	tccd	spooky magic for /Applications/Nexy.app/Contents/MacOS/Nexy (0x51282211) at text offset: 81920
default	13:46:12.469489-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 25690: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 66681a00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 0;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 0;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 655360;
    kTCCCodeIdentityTeamID = "";
}
default	13:46:12.479317-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:46:13.275677-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb2c24e340) Selecting device 83 from constructor
default	13:46:13.275707-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24e340)
default	13:46:13.275758-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24e340) not already running
default	13:46:13.275769-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb2c24e340) nothing to teardown
default	13:46:13.275778-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb2c24e340) connecting device 83
default	13:46:13.276021-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24e340) Device ID: 83 (Input:No | Output:Yes): true
default	13:46:13.276251-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb2c24e340) created ioproc 0xd for device 83
default	13:46:13.276499-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 7 device listeners to device 83
default	13:46:13.276827-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device delegate listeners to device 83
default	13:46:13.276855-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24e340)
default	13:46:13.276989-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:13.277004-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:46:13.277013-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:13.277024-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:46:13.277035-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:13.277194-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:13.277214-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:13.277224-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:13.277231-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device listeners from device 0
default	13:46:13.277239-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device delegate listeners from device 0
default	13:46:13.277245-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24e340)
default	13:46:13.277273-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:46:13.277359-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb2c24e340) caller requesting device change from 83 to 89
default	13:46:13.277370-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24e340)
default	13:46:13.277379-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24e340) not already running
default	13:46:13.277385-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb2c24e340) disconnecting device 83
default	13:46:13.277394-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb2c24e340) destroying ioproc 0xd for device 83
default	13:46:13.277431-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xd}
default	13:46:13.277519-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:46:13.277687-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb2c24e340) connecting device 89
default	13:46:13.277926-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24e340) Device ID: 89 (Input:Yes | Output:No): true
default	13:46:13.280373-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6362, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.282449-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6362, subject=com.nexy.assistant,
default	13:46:13.283870-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.305063-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb2c24e340) created ioproc 0xb for device 89
default	13:46:13.305285-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 7 device listeners to device 89
default	13:46:13.305511-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device delegate listeners to device 89
default	13:46:13.305524-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24e340)
default	13:46:13.305536-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	13:46:13.305548-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:13.305730-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	13:46:13.305737-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	13:46:13.305742-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:46:13.305859-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:13.305871-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:13.305877-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:13.305882-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 7 device listeners from device 83
default	13:46:13.306080-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device delegate listeners from device 83
default	13:46:13.306088-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24e340)
default	13:46:13.306788-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:46:13.308163-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6363, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.309298-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6363, subject=com.nexy.assistant,
default	13:46:13.309978-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.322710-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:46:13.323599-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6364, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.324323-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6364, subject=com.nexy.assistant,
default	13:46:13.324822-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.335081-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb2c24e340) Selecting device 0 from destructor
default	13:46:13.335086-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24e340)
default	13:46:13.335088-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24e340) not already running
default	13:46:13.335094-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb2c24e340) disconnecting device 89
default	13:46:13.335098-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb2c24e340) destroying ioproc 0xb for device 89
default	13:46:13.335115-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:46:13.335136-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:46:13.335237-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb2c24e340) nothing to setup
default	13:46:13.335242-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device listeners to device 0
default	13:46:13.335247-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device delegate listeners to device 0
default	13:46:13.335252-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 7 device listeners from device 89
default	13:46:13.335417-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device delegate listeners from device 89
default	13:46:13.335424-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24e340)
default	13:46:13.335994-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb2c24e340) Selecting device 83 from constructor
default	13:46:13.336000-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24e340)
default	13:46:13.336004-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24e340) not already running
default	13:46:13.336007-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb2c24e340) nothing to teardown
default	13:46:13.336013-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb2c24e340) connecting device 83
default	13:46:13.336076-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24e340) Device ID: 83 (Input:No | Output:Yes): true
default	13:46:13.336142-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb2c24e340) created ioproc 0xe for device 83
default	13:46:13.336226-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 7 device listeners to device 83
default	13:46:13.336359-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device delegate listeners to device 83
default	13:46:13.336365-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24e340)
default	13:46:13.336416-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:13.336421-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:46:13.336425-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:13.336427-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:46:13.336432-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:13.336503-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:13.336509-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:13.336513-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:13.336517-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device listeners from device 0
default	13:46:13.336519-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device delegate listeners from device 0
default	13:46:13.336528-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24e340)
default	13:46:13.336536-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:46:13.336568-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb2c24e340) caller requesting device change from 83 to 89
default	13:46:13.336571-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24e340)
default	13:46:13.336574-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24e340) not already running
default	13:46:13.336576-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb2c24e340) disconnecting device 83
default	13:46:13.336580-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb2c24e340) destroying ioproc 0xe for device 83
default	13:46:13.336585-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xe}
default	13:46:13.336611-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:46:13.336674-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb2c24e340) connecting device 89
default	13:46:13.336735-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24e340) Device ID: 89 (Input:Yes | Output:No): true
default	13:46:13.337450-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6365, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.338080-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6365, subject=com.nexy.assistant,
default	13:46:13.338490-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.346244-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb2c24e340) created ioproc 0xc for device 89
default	13:46:13.346319-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 7 device listeners to device 89
default	13:46:13.346441-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device delegate listeners to device 89
default	13:46:13.346446-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24e340)
default	13:46:13.346448-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	13:46:13.346453-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:13.346539-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	13:46:13.346543-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	13:46:13.346545-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:46:13.346601-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:13.346605-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:13.346607-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:13.346611-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 7 device listeners from device 83
default	13:46:13.346709-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device delegate listeners from device 83
default	13:46:13.346714-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24e340)
default	13:46:13.346719-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	13:46:13.347067-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:46:13.347629-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6366, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.348050-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6366, subject=com.nexy.assistant,
default	13:46:13.348347-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.355365-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:46:13.355401-0500	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0xb2cad2070, from  1 ch,  24000 Hz, Float32 to  1 ch,  48000 Hz, Float32
default	13:46:13.355511-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:46:13.356034-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6367, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.356462-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6367, subject=com.nexy.assistant,
default	13:46:13.356760-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.363842-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137543 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:13.363882-0500	runningboardd	Assertion 398-25767-1137543 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:13.364192-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6368, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.364238-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:13.364326-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:13.364449-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:13.364638-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:13.365171-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6368, subject=com.nexy.assistant,
default	13:46:13.365688-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.368483-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:13.372740-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:46:13.372823-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:46:13.374355-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:44610 called from <private>
default	13:46:13.374358-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xc}
default	13:46:13.374387-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:46:13.375400-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44610 called from <private>
default	13:46:13.375767-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:13.375503-0500	runningboardd	Invalidating assertion 398-25767-1137543 (target:[anon<Nexy>(501):25767]) from originator [anon<Nexy>(501):25767]
default	13:46:13.375523-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44610)
default	13:46:13.375796-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44597 called from <private>
default	13:46:13.375540-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44610 called from <private>
default	13:46:13.375803-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44597 called from <private>
default	13:46:13.375545-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44610 called from <private>
default	13:46:13.375734-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:13.382556-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:46:13.383419-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:46:13.383599-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137544 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:13.383732-0500	runningboardd	Assertion 398-334-1137544 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:13.383933-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:13.383989-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:13.384021-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:13.384104-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:13.378700-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44598)
default	13:46:13.375741-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44609 called from <private>
default	13:46:13.376279-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44609 called from <private>
default	13:46:13.385620-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44610)
default	13:46:13.385632-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44610)
default	13:46:13.385634-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44610 called from <private>
default	13:46:13.385637-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44610)
default	13:46:13.385639-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44610 called from <private>
default	13:46:13.378727-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44598 called from <private>
default	13:46:13.385644-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44610)
default	13:46:13.385644-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44610 called from <private>
default	13:46:13.385668-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44610 called from <private>
default	13:46:13.378735-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44598 called from <private>
default	13:46:13.398216-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:13.398477-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:13.398709-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:13.398890-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:13.401966-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:46:13.402153-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:46:13.402226-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef14e, Nexy(25767), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	13:46:13.402463-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:13.402621-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef14e, Nexy(25767), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:46:13.402729-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:13.402834-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:13.402921-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:46:13.402864-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.402947-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14e, Nexy(25767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 335 starting recording
default	13:46:13.385698-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44610 called from <private>
default	13:46:13.403085-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:13.403170-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:46:13.403110-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.385744-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44610 called from <private>
default	13:46:13.385772-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44610 called from <private>
default	13:46:13.385797-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44610 called from <private>
default	13:46:13.389831-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44610 called from <private>
default	13:46:13.403232-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14e, Nexy(25767), 'prim'', displayID:'com.nexy.assistant'}
default	13:46:13.389894-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44610 called from <private>
default	13:46:13.396986-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:13.403049-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.403263-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.397005-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:13.398386-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:13.398452-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44597 called from <private>
default	13:46:13.398459-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44597 called from <private>
default	13:46:13.404670-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:13.404700-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:13.403311-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:46:13.404912-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44597 called from <private>
default	13:46:13.405014-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:13.405143-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44597 called from <private>
default	13:46:13.404553-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44610)
default	13:46:13.405349-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:13.404601-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:13.404745-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44598)
default	13:46:13.405653-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137545 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:13.405797-0500	runningboardd	Assertion 398-25767-1137545 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:13.404948-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44610 called from <private>
default	13:46:13.405638-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44598 called from <private>
default	13:46:13.405608-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:13.405694-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44598 called from <private>
default	13:46:13.405688-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:13.403310-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:46:13.406383-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:13.407042-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6369, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.408776-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:13.409503-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6369, subject=com.nexy.assistant,
default	13:46:13.410742-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.413480-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44609 called from <private>
default	13:46:13.413728-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44597 called from <private>
default	13:46:13.413490-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44609 called from <private>
default	13:46:13.413748-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44597 called from <private>
default	13:46:13.414252-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 3 3, id:44597 called from <private>
default	13:46:13.413537-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:13.414263-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 4 4, id:44597 called from <private>
default	13:46:13.415627-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:13.415891-0500	runningboardd	Invalidating assertion 398-334-1137544 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.powerd>:334]
default	13:46:13.415777-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:13.415986-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:13.416102-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:13.414360-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:13.420941-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:13.421066-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44609 called from <private>
default	13:46:13.421070-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44609 called from <private>
default	13:46:13.421109-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:13.425236-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:13.425565-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 4 4 id:44597 called from <private>
default	13:46:13.425578-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 3 3 id:44597 called from <private>
default	13:46:13.425673-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:13.427203-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:13.428078-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:46:13.429037-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:13.429164-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:13.429172-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:13.428906-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:46:13.429255-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:13.429261-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:13.429272-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:13.429276-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:13.429280-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:13.429281-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:13.429285-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:13.429306-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:13.429311-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:13.429358-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:13.429445-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:13.429488-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:13.429553-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:13.429591-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:13.429635-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:13.431957-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:44610 called from <private>
default	13:46:13.438945-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:13.439094-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44597 called from <private>
default	13:46:13.439104-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44597 called from <private>
default	13:46:13.439138-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:13.439115-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:13.439152-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:13.439160-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44597 called from <private>
default	13:46:13.439166-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44597 called from <private>
default	13:46:13.439130-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:13.439192-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44597 called from <private>
default	13:46:13.439132-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:13.439238-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44597 called from <private>
default	13:46:13.439280-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44609 called from <private>
default	13:46:13.439299-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44597 called from <private>
default	13:46:13.439284-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44609 called from <private>
default	13:46:13.439357-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44597 called from <private>
default	13:46:13.439382-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24dc40) Device ID: 83 (Input:No | Output:Yes): true
default	13:46:13.439420-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44597 called from <private>
default	13:46:13.441164-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:46:13.442414-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44610 called from <private>
default	13:46:13.442648-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44610)
default	13:46:13.442924-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.442656-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44610 called from <private>
default	13:46:13.442661-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44610 called from <private>
default	13:46:13.443154-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  24000 Hz, Float32, interleaved
default	13:46:13.443176-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:46:13.443250-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	13:46:13.443471-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.443975-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:46:13.445544-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:13.448018-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:13.448040-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	13:46:13.448050-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	13:46:13.448242-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	13:46:13.448402-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	13:46:13.439486-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44597 called from <private>
default	13:46:13.439590-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44597 called from <private>
default	13:46:13.447829-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6370, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.448652-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:46:13.445482-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:13.447329-0500	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0xb2cad1e00, from  2 ch,  48000 Hz, Float32, interleaved to  2 ch,  24000 Hz, Float32, interleaved
default	13:46:13.447360-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:46:13.455096-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6370, subject=com.nexy.assistant,
default	13:46:13.455961-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:13.456047-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	13:46:13.455832-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.456099-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	13:46:13.457103-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:13.463443-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:13.463496-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	13:46:13.463542-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	13:46:13.463584-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:46:13.467895-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:46:13.467972-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_44610.44378.0_airpods noise suppression studio::out-0 issue_detected_sample_time=24480.000000 ] -- [ rms:[-48.673817], peaks:[-24.435072] ]
default	13:46:13.468002-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_44610.44378.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-47.245201], peaks:[-25.254736] ]
default	13:46:13.468703-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d84c00] Created node ADM::com.nexy.assistant_44610.44378.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:46:13.468767-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d84c00] Created node ADM::com.nexy.assistant_44610.44378.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:46:13.469896-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:13.473762-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-1137548 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	13:46:13.473835-0500	runningboardd	Assertion 398-632-1137548 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:13.473917-0500	ControlCenter	[anon<Nexy>:25767] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	13:46:13.474226-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:13.474379-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:13.474406-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	13:46:13.474237-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:13.474428-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	13:46:13.474282-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:13.487488-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.487498-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.487504-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.487509-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.487512-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.487515-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:13.487617-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:13.491544-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:46:13.496721-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:46:13.496795-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:46:13.497071-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44610)
default	13:46:13.497164-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44610 called from <private>
default	13:46:13.497405-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137550 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:13.497436-0500	runningboardd	Assertion 398-25767-1137550 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:13.497169-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44610 called from <private>
default	13:46:13.497175-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44610 called from <private>
default	13:46:13.498900-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6371, subject=com.nexy.assistant,
default	13:46:13.499456-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.501044-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:13.504163-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:13.504189-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	13:46:13.504213-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	13:46:13.504895-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.505001-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.505033-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.505089-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.505121-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.505163-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:13.505367-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:13.507534-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:13.507555-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	13:46:13.507570-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	13:46:13.507576-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:46:13.509617-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137551 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:13.509654-0500	runningboardd	Assertion 398-334-1137551 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:13.512397-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:44610 called from <private>
default	13:46:13.520534-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.520539-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.520541-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:13.520653-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:13.520777-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:13.523957-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:13.523983-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	13:46:13.524005-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	13:46:13.529109-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.529136-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.529154-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.529160-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.529179-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.529200-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:13.529243-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.529268-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.529293-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.529314-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.529337-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.529361-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:13.529355-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:13.530581-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.530587-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.530591-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.530594-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.530597-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.530616-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:13.530632-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:46:13.674182-0500	ControlCenter	[anon<Nexy>:25767] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	13:46:13.674324-0500	runningboardd	Invalidating assertion 398-632-1137548 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	13:46:13.674933-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	13:46:13.675268-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:46:13.675374-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:13.675425-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:46:13.675463-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14e, Nexy(25767), 'prim'', displayID:'com.nexy.assistant'}
default	13:46:13.675508-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:46:13.675515-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14e, Nexy(25767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 335 stopping recording
default	13:46:13.675542-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:46:13.675570-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:13.675718-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:46:13.675600-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:13.675735-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:46:13.675725-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:13.676139-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:13.676167-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:13.676182-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.676002-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:13.676202-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:46:13.676100-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.676256-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:46:13.676269-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.676278-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:46:13.678800-0500	runningboardd	Invalidating assertion 398-25767-1137550 (target:[anon<Nexy>(501):25767]) from originator [anon<Nexy>(501):25767]
default	13:46:13.678862-0500	runningboardd	Invalidating assertion 398-334-1137551 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.powerd>:334]
default	13:46:13.685491-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:13.685554-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	13:46:13.685600-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	13:46:13.685619-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:46:13.686069-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.686079-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.686089-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.686096-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:13.686104-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:13.686110-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:13.686192-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:13.717341-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-1137552 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	13:46:13.717485-0500	runningboardd	Assertion 398-632-1137552 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:13.717612-0500	ControlCenter	[anon<Nexy>:25767] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	13:46:13.778613-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb2c24e340) Selecting device 0 from destructor
default	13:46:13.778631-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24e340)
default	13:46:13.778640-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24e340) not already running
default	13:46:13.778645-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb2c24e340) disconnecting device 89
default	13:46:13.778654-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb2c24e340) destroying ioproc 0xc for device 89
default	13:46:13.778697-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	13:46:13.778748-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:46:13.778947-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb2c24e340) nothing to setup
default	13:46:13.778961-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device listeners to device 0
default	13:46:13.778969-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device delegate listeners to device 0
default	13:46:13.778975-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 7 device listeners from device 89
default	13:46:13.779244-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device delegate listeners from device 89
default	13:46:13.779274-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24e340)
default	13:46:13.781580-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb2c24e340) Selecting device 83 from constructor
default	13:46:13.781598-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24e340)
default	13:46:13.781613-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24e340) not already running
default	13:46:13.781620-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb2c24e340) nothing to teardown
default	13:46:13.781625-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb2c24e340) connecting device 83
default	13:46:13.781802-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24e340) Device ID: 83 (Input:No | Output:Yes): true
default	13:46:13.781878-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:13.781893-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:13.781904-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:13.781944-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb2c24e340) created ioproc 0xf for device 83
default	13:46:13.781924-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:13.782135-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 7 device listeners to device 83
default	13:46:13.782368-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device delegate listeners to device 83
default	13:46:13.782378-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24e340)
default	13:46:13.782480-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  24000 Hz, Float32, interleaved
default	13:46:13.782493-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:46:13.782500-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	13:46:13.782510-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:46:13.782520-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:13.782641-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:13.782656-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:13.782664-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:13.782670-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device listeners from device 0
default	13:46:13.782675-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device delegate listeners from device 0
default	13:46:13.782680-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24e340)
default	13:46:13.782697-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:46:13.782762-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb2c24e340) caller requesting device change from 83 to 89
default	13:46:13.782773-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24e340)
default	13:46:13.782778-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24e340) not already running
default	13:46:13.782784-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb2c24e340) disconnecting device 83
default	13:46:13.782802-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb2c24e340) destroying ioproc 0xf for device 83
default	13:46:13.782839-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xf}
default	13:46:13.782875-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:46:13.782979-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb2c24e340) connecting device 89
default	13:46:13.783097-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24e340) Device ID: 89 (Input:Yes | Output:No): true
default	13:46:13.785299-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6372, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.786065-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:13.787628-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137553 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:13.787802-0500	runningboardd	Assertion 398-25767-1137553 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:13.788294-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:13.788360-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:13.789079-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:13.789186-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:13.789222-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137554 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:13.789330-0500	runningboardd	Assertion 398-334-1137554 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:13.789661-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6372, subject=com.nexy.assistant,
default	13:46:13.795527-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	13:46:13.797261-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	13:46:13.797370-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:46:13.797409-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef14e, Nexy(25767), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	13:46:13.797437-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:13.797525-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.797485-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef14e, Nexy(25767), 'prim'', AudioCategory changed to 'MediaPlayback'
default	13:46:13.797686-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.797727-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.797528-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.797585-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	13:46:13.797619-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 335 starting playing
default	13:46:13.797880-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:13.798003-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	13:46:13.798127-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14e, Nexy(25767), 'prim'', displayID:'com.nexy.assistant'}
default	13:46:13.798667-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	13:46:13.798978-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	13:46:13.798989-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:13.798840-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	13:46:13.798851-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef14e to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":25767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef14e, sessionType: 'prim', isRecording: false }, 
]
default	13:46:13.799138-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:46:13.799392-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.799334-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.799413-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	13:46:13.799423-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	13:46:13.799429-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	13:46:13.799437-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	13:46:13.799479-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	13:46:13.799527-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	13:46:13.802505-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:13.802517-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:13.802531-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:13.802550-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:13.810498-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb2c24e340) created ioproc 0xd for device 89
default	13:46:13.810725-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 7 device listeners to device 89
default	13:46:13.810931-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device delegate listeners to device 89
default	13:46:13.810940-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24e340)
default	13:46:13.810956-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	13:46:13.810976-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:13.811151-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	13:46:13.811165-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	13:46:13.811172-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:46:13.811311-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:13.811346-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:13.811355-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:13.811359-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 7 device listeners from device 83
default	13:46:13.811599-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device delegate listeners from device 83
default	13:46:13.811608-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24e340)
default	13:46:13.811628-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	13:46:13.812342-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:46:13.813334-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7] Sending action(s) in update: NSSceneFenceAction
default	13:46:13.813492-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6373, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.814712-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6373, subject=com.nexy.assistant,
default	13:46:13.815454-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.827079-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:46:13.827996-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6374, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:13.828685-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6374, subject=com.nexy.assistant,
default	13:46:13.829123-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:13.857568-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25778.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25778, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=25778, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:46:13.858690-0500	tccd	AUTHREQ_SUBJECT: msgID=25778.1, subject=com.nexy.assistant,
default	13:46:13.859041-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:13.866830-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12347, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25778, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=25778, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:46:13.867607-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12347, subject=com.nexy.assistant,
default	13:46:13.867924-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:13.884908-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:13.887834-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
error	13:46:13.901022-0500	tccd	spooky magic for /Applications/Nexy.app/Contents/MacOS/Nexy (0x51282211) at text offset: 81920
default	13:46:13.902529-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 25690: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 6b681a00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 0;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 0;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 655360;
    kTCCCodeIdentityTeamID = "";
}
default	13:46:13.903261-0500	ControlCenter	[anon<Nexy>:25767] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	13:46:13.903356-0500	runningboardd	Invalidating assertion 398-632-1137552 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	13:46:13.916788-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:46:13.924094-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:13.924108-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:13.924118-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:13.924134-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:13.930157-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:14.041399-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	13:46:14.041562-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:46:14.041600-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 335 stopping playing
default	13:46:14.041624-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:46:14.041640-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:14.041672-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:14.041776-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:14.041897-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:46:14.041908-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:14.041842-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef14e to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":25767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef14e, sessionType: 'prim', isRecording: false }, 
]
default	13:46:14.042135-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:14.043005-0500	runningboardd	Invalidating assertion 398-25767-1137553 (target:[anon<Nexy>(501):25767]) from originator [anon<Nexy>(501):25767]
default	13:46:14.044233-0500	runningboardd	Invalidating assertion 398-334-1137554 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.powerd>:334]
default	13:46:14.045399-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:14.045417-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:46:14.053308-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:14.053318-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:14.053327-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:14.053343-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:14.056341-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:14.344752-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137561 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:14.344875-0500	runningboardd	Assertion 398-25767-1137561 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:14.345330-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:14.345350-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:14.345365-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:14.345393-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:14.346728-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.6375, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:46:14.348679-0500	tccd	AUTHREQ_SUBJECT: msgID=401.6375, subject=com.nexy.assistant,
default	13:46:14.349837-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9500 at /Applications/Nexy.app
default	13:46:14.350651-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:14.374882-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xd}
default	13:46:14.375978-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:46:14.376080-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:46:14.376112-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef14e, Nexy(25767), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	13:46:14.376146-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:14.376230-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef14e, Nexy(25767), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:46:14.376467-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:14.376279-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:14.376410-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:14.376451-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:14.376512-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:14.376535-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:14.376630-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137562 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:14.376549-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:46:14.376734-0500	runningboardd	Assertion 398-334-1137562 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:14.376574-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14e, Nexy(25767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 335 starting recording
default	13:46:14.376641-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:14.376729-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:14.376888-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:46:14.377079-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:14.377120-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:14.377141-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:46:14.376676-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:14.377146-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:14.377155-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:14.376996-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14e, Nexy(25767), 'prim'', displayID:'com.nexy.assistant'}
default	13:46:14.377223-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:14.377109-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:46:14.377419-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:46:14.377667-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:14.377757-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:14.377789-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:14.377804-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	13:46:14.377814-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	13:46:14.377825-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	13:46:14.377877-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	13:46:14.377939-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:46:14.385059-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:14.390657-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:14.390775-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	13:46:14.390845-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	13:46:14.391594-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:14.391627-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.391642-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.391655-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.391664-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.391673-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.391680-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:14.391693-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.391704-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.391711-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.391719-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.391726-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.391741-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:14.391875-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:14.391932-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:46:14.392026-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.392039-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.392047-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.392060-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.392075-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.392081-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:14.422601-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-1137563 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	13:46:14.422848-0500	ControlCenter	[anon<Nexy>:25767] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	13:46:14.422766-0500	runningboardd	Assertion 398-632-1137563 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:14.423367-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:14.423418-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:14.423451-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:14.423511-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:14.427624-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:14.623739-0500	ControlCenter	[anon<Nexy>:25767] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	13:46:14.623933-0500	runningboardd	Invalidating assertion 398-632-1137563 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	13:46:14.730984-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:14.731018-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:14.731045-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:14.731096-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:14.738966-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:14.837425-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:14.837567-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:46:14.837652-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:46:14.837673-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	13:46:14.839943-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.839962-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.839977-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.839986-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.839993-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.840003-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:14.840058-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.840069-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.840078-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.840085-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.840094-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.840100-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:14.840219-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:14.840318-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.840331-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.840338-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.840346-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:14.840354-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:14.840362-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:15.375379-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	13:46:15.382457-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	13:46:15.382555-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	13:46:15.385742-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=18126.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=18126, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	13:46:15.385802-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=18126, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=25767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:46:15.388048-0500	tccd	AUTHREQ_SUBJECT: msgID=18126.5, subject=com.nexy.assistant,
default	13:46:15.389264-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:15.431235-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	13:46:15.454530-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:15.460520-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:15.460691-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant), [scr] Nexy (com.nexy.assistant)]
default	13:46:15.460764-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	13:46:15.462985-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.462999-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.463011-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:15.463018-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.463027-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:15.463033-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:15.463088-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.463099-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.463107-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:15.463113-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.463119-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:15.463125-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:15.463221-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:15.463324-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.463335-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.463342-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:15.463349-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.463356-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:15.463361-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:15.501842-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xd}
default	13:46:15.502075-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:46:15.502135-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:15.502165-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:46:15.502182-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14e, Nexy(25767), 'prim'', displayID:'com.nexy.assistant'}
default	13:46:15.502223-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef14e, Nexy(25767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 335 stopping recording
default	13:46:15.502237-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:46:15.502243-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:46:15.502264-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:15.502316-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:15.502418-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:46:15.502429-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:15.502444-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:46:15.502584-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:15.502636-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:15.502613-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:15.502665-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:46:15.502697-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:46:15.503707-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:15.503726-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:46:15.503676-0500	runningboardd	Invalidating assertion 398-25767-1137561 (target:[anon<Nexy>(501):25767]) from originator [anon<Nexy>(501):25767]
default	13:46:15.503737-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:15.503745-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:46:15.503866-0500	runningboardd	Invalidating assertion 398-334-1137562 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.powerd>:334]
default	13:46:15.511810-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:46:15.511894-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	13:46:15.511954-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	13:46:15.511971-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:46:15.512568-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.512583-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.512595-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:15.512602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:46:15.512609-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:46:15.512614-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:46:15.512742-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:46:15.607623-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb2c24e340) Selecting device 0 from destructor
default	13:46:15.607640-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb2c24e340)
default	13:46:15.607652-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb2c24e340) not already running
default	13:46:15.607660-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb2c24e340) disconnecting device 89
default	13:46:15.607666-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb2c24e340) destroying ioproc 0xd for device 89
default	13:46:15.607693-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xd}
default	13:46:15.607736-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:46:15.607899-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb2c24e340) nothing to setup
default	13:46:15.607918-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device listeners to device 0
default	13:46:15.607928-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb2c24e340) adding 0 device delegate listeners to device 0
default	13:46:15.607937-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 7 device listeners from device 89
default	13:46:15.608234-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb2c24e340) removing 0 device delegate listeners from device 89
default	13:46:15.608253-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb2c24e340)
default	13:46:15.611104-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:15.611118-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:15.611126-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:15.611169-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:15.615346-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:15.924803-0500	Nexy	nw_path_libinfo_path_check [D7BB7B09-2D39-4266-8332-5A33F9E2CA94 Hostname#59c5c15d:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	13:46:15.925103-0500	mDNSResponder	[R468007] DNSServiceCreateConnection START PID[25767](Nexy)
default	13:46:15.925210-0500	mDNSResponder	[R468008] DNSServiceQueryRecord START -- qname: <mask.hash: 'lETfDsfMRrhKUOGbaqIqQA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 25767 (Nexy), name hash: b360ab20
default	13:46:15.926323-0500	mDNSResponder	[R468009] DNSServiceQueryRecord START -- qname: <mask.hash: 'lETfDsfMRrhKUOGbaqIqQA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 25767 (Nexy), name hash: b360ab20
default	13:46:15.960236-0500	kernel	SK[5]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 8BBC28EC-027A-4214-B968-9AE1DE9305DC flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.52056,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x2308beb4 tp_proto=0x06"
default	13:46:15.960313-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:52056<-><IPv4-redacted>:80] interface: utun6 (skipped: 5295)
so_gencnt: 4385794 t_state: SYN_SENT process: Nexy:25767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb8614226
default	13:46:15.960741-0500	kernel	tcp connected: [<IPv4-redacted>:52056<-><IPv4-redacted>:80] interface: utun6 (skipped: 5295)
so_gencnt: 4385794 t_state: ESTABLISHED process: Nexy:25767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb8614226
default	13:46:16.053378-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-1137571 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	13:46:16.053695-0500	runningboardd	Assertion 398-632-1137571 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:16.053967-0500	ControlCenter	[anon<Nexy>:25767] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	13:46:16.054454-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:16.054485-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:16.054511-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:16.054639-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:16.060573-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:16.169683-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:52056<-><IPv4-redacted>:80] interface: utun6 (skipped: 5295)
so_gencnt: 4385794 t_state: LAST_ACK process: Nexy:25767 Duration: 0.209 sec Conn_Time: 0.000 sec bytes in/out: 380/22212 pkts in/out: 2/8 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.218 ms rttvar: 0.750 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb8614226
default	13:46:16.169702-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52056<-><IPv4-redacted>:80] interface: utun6 (skipped: 5295)
so_gencnt: 4385794 t_state: LAST_ACK process: Nexy:25767 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:46:16.181927-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [anon<Nexy>(501):25767] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-25767-1137572 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	13:46:16.182105-0500	runningboardd	Assertion 398-25767-1137572 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:16.182988-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:16.183125-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:16.182998-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1137573 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:16.183211-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:16.183316-0500	runningboardd	Assertion 398-334-1137573 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:16.183346-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:16.187150-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	13:46:16.188791-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	13:46:16.189014-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:46:16.189078-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef14e, Nexy(25767), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	13:46:16.189177-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:16.189279-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef14e, Nexy(25767), 'prim'', AudioCategory changed to 'MediaPlayback'
default	13:46:16.189335-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:16.189397-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	13:46:16.189425-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 335 starting playing
default	13:46:16.189619-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:16.189712-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:16.189829-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:16.189970-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	13:46:16.190217-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef14e, Nexy(25767), 'prim'', displayID:'com.nexy.assistant'}
default	13:46:16.190397-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	13:46:16.190990-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	13:46:16.191133-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	13:46:16.191020-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:16.190608-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef14e to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":25767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef14e, sessionType: 'prim', isRecording: false }, 
]
default	13:46:16.190625-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	13:46:16.191442-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	13:46:16.191580-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	13:46:16.191627-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	13:46:16.191651-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	13:46:16.191667-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	13:46:16.191685-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	13:46:16.191765-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	13:46:16.191863-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	13:46:16.197810-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:16.197827-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:16.197860-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:16.197890-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:16.199121-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:16.202706-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:16.218101-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7] Sending action(s) in update: NSSceneFenceAction
default	13:46:16.252168-0500	ControlCenter	[anon<Nexy>:25767] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	13:46:16.252264-0500	runningboardd	Invalidating assertion 398-632-1137571 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	13:46:16.268795-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=25782.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25782, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=25782, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:46:16.269954-0500	tccd	AUTHREQ_SUBJECT: msgID=25782.1, subject=com.nexy.assistant,
default	13:46:16.270422-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:16.278964-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.12348, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=25782, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/usr/bin/osascript}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=25782, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:46:16.279782-0500	tccd	AUTHREQ_SUBJECT: msgID=393.12348, subject=com.nexy.assistant,
default	13:46:16.280114-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	13:46:16.299964-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
error	13:46:16.315045-0500	tccd	spooky magic for /Applications/Nexy.app/Contents/MacOS/Nexy (0x51282211) at text offset: 81920
default	13:46:16.316590-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 25690: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 75681a00 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 0;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 0;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 655360;
    kTCCCodeIdentityTeamID = "";
}
default	13:46:16.327130-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:46:16.360219-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:16.360234-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:16.360244-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:16.360264-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:16.366997-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:16.404647-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 100NumofApp 1
default	13:46:16.578684-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	13:46:16.578901-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:46:16.578962-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 335 stopping playing
default	13:46:16.578996-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:46:16.579025-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:16.579066-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:16.579225-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:16.579230-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:46:16.579258-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:16.579236-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:46:16.579121-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:16.579272-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:46:16.579159-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef14e to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":25767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef14e, sessionType: 'prim', isRecording: false }, 
]
default	13:46:16.581690-0500	runningboardd	Invalidating assertion 398-25767-1137572 (target:[anon<Nexy>(501):25767]) from originator [anon<Nexy>(501):25767]
default	13:46:16.581763-0500	runningboardd	Invalidating assertion 398-334-1137573 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.powerd>:334]
default	13:46:16.688313-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:16.688349-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:16.688368-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring GPU update because this process is not GPU managed
default	13:46:16.688396-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring memory limit update because this process is not memory-managed
default	13:46:16.693172-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:17.632662-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:17.632738-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44597 called from <private>
default	13:46:17.632953-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:17.632755-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44597 called from <private>
default	13:46:17.633028-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44609 called from <private>
default	13:46:17.633047-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44609 called from <private>
default	13:46:17.634336-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44598)
default	13:46:17.634341-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44610)
default	13:46:17.634361-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44598 called from <private>
default	13:46:17.634367-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44610 called from <private>
default	13:46:17.634367-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44598 called from <private>
default	13:46:17.634375-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44610 called from <private>
default	13:46:17.653328-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:17.653351-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:17.653657-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:17.653685-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44609 called from <private>
default	13:46:17.653697-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44609 called from <private>
default	13:46:17.657426-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:17.657459-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:17.659718-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:17.663069-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44609 called from <private>
default	13:46:17.663090-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44609 called from <private>
default	13:46:17.663120-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:17.663130-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:17.663137-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44609 called from <private>
default	13:46:17.663144-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44609 called from <private>
default	13:46:17.663149-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44609 called from <private>
default	13:46:17.663155-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44609 called from <private>
default	13:46:17.664127-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:17.664020-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:17.664403-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44610)
default	13:46:17.664387-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44598)
default	13:46:17.664424-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44610 called from <private>
default	13:46:17.664412-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44598 called from <private>
default	13:46:17.664436-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44610 called from <private>
default	13:46:17.664418-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44598 called from <private>
default	13:46:17.664932-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:17.664943-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:17.666831-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44609 called from <private>
default	13:46:17.666848-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44609 called from <private>
default	13:46:17.675991-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44609 called from <private>
default	13:46:17.676014-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44609 called from <private>
default	13:46:17.676147-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:17.677809-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:44597 called from <private>
default	13:46:17.677829-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:44597 called from <private>
default	13:46:17.677917-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:17.680876-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:17.681169-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44609 called from <private>
default	13:46:17.681181-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44609 called from <private>
default	13:46:17.681313-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44609)
default	13:46:17.685983-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:17.686455-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:44597 called from <private>
default	13:46:17.686467-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:44597 called from <private>
default	13:46:17.686594-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:17.691715-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44609)
default	13:46:17.691950-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44609 called from <private>
default	13:46:17.691960-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44609 called from <private>
default	13:46:17.691982-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44609 called from <private>
default	13:46:17.691992-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44609 called from <private>
default	13:46:17.692001-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44609 called from <private>
default	13:46:17.692007-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44609 called from <private>
default	13:46:17.692013-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44609 called from <private>
default	13:46:17.692020-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44609 called from <private>
default	13:46:17.692056-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:44609 called from <private>
default	13:46:17.692132-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:44609 called from <private>
default	13:46:17.692188-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24dc40) Device ID: 83 (Input:No | Output:Yes): true
default	13:46:17.692199-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44609 called from <private>
default	13:46:17.692260-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24dc40)
default	13:46:17.692344-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44609 called from <private>
default	13:46:17.692500-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:17.692509-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:46:17.692564-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:17.692676-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:46:17.692717-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:17.693207-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:46:17.693536-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24dc40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:17.693552-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24dc40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:17.693558-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:17.693716-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb2c24dc40) Device ID: 83 (Input:No | Output:Yes): true
default	13:46:17.693727-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb2c24dc40)
default	13:46:17.693844-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:17.693852-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	13:46:17.693866-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:46:17.693892-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	13:46:17.693943-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:46:17.694333-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:46:17.694539-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb2c24dc40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:46:17.694574-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb2c24dc40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:46:17.694607-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	13:46:17.695462-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:17.695724-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:17.695738-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:17.695930-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:17.695940-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:17.695955-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:17.695964-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:17.695971-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:17.695979-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:17.695991-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:17.696012-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:17.696053-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(44597)
default	13:46:17.696181-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:17.696245-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:17.696290-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:17.696367-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:17.696394-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:44597 called from <private>
default	13:46:17.696450-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:44597 called from <private>
default	13:46:17.702656-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(44597)
default	13:46:17.702691-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:44597 called from <private>
default	13:46:17.702698-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:44597 called from <private>
default	13:46:17.703139-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:44597 called from <private>
default	13:46:17.703149-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:44597 called from <private>
default	13:46:17.718550-0500	WindowServer	1a597f[StealKeyFocusReturningID]: [DeferringManager] Updating policy {
    advicePolicy: .keyThief;
    frontmostProcess: 0x0-0x19019 (Finder) mainConnectionID: 7B703;
    keyThiefConnectionID: 1A597F;
} for reason: key thief updated 1a597f 0x0-0x128b28a (Nexy)
default	13:46:17.718576-0500	WindowServer	<BSCompoundAssertion:0x7fb015380> (com.apple.backboard.hid.delivery.localDelivery.preventFlushing) acquire for reason:key thief updated 1a597f 0x0-0x128b28a (Nexy) <14902> acq:0x8012c6f00 count:1
default	13:46:17.756897-0500	Nexy	[com.apple.controlcenter:673F5617-EDAA-4E45-A9D8-06E2ABDF26D7] Sending action(s) in update: NSSceneFenceAction
default	13:46:17.783812-0500	runningboardd	Acquiring assertion targeting [anon<Nexy>(501):25767] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "AppVisible" ID:398-393-1137583 target:25767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:46:17.783853-0500	runningboardd	Assertion 398-393-1137583 (target:[anon<Nexy>(501):25767]) will be created as active
default	13:46:17.784112-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring jetsam update because this process is not memory-managed
default	13:46:17.784128-0500	runningboardd	[anon<Nexy>(501):25767] Ignoring suspend because this process is not lifecycle managed
default	13:46:17.787955-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), running-NotVisible
default	13:46:18.997752-0500	Nexy	[C:3] Alloc com.apple.backboard.hid-services.xpc
default	13:46:18.997827-0500	Nexy	[0xb2df5f840] activating connection: mach=false listener=false peer=false name=(anonymous)
error	13:46:18.998466-0500	Nexy	Unable to obtain a task name port right for pid 393: (os/kern) failure (0x5)
default	13:46:18.998940-0500	Nexy	BKSHIDEventDeliveryManager - connection activation
default	13:46:19.001611-0500	Nexy	terminate:
default	13:46:19.001636-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Terminating
default	13:46:19.001652-0500	Nexy	-[NSApplication _pushPersistentStateTerminationGeneration] sPersistentStateTerminateStackHeight -> 1
default	13:46:19.001773-0500	Nexy	Attempting sudden termination (1st attempt)
default	13:46:19.001791-0500	Nexy	Checking whether app should terminate
default	13:46:19.002679-0500	Nexy	Asking app delegate whether applicationShouldTerminate:
default	13:46:19.002707-0500	Nexy	replyToApplicationShouldTerminate:YES
default	13:46:19.002758-0500	Nexy	App termination approved
default	13:46:19.002770-0500	Nexy	Termination commencing
default	13:46:19.002779-0500	Nexy	Attempting sudden termination (2nd attempt)
default	13:46:19.003948-0500	Nexy	Termination complete. Exiting without sudden termination.
default	13:46:21.005706-0500	Nexy	Entering exit handler.
default	13:46:21.005728-0500	Nexy	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	13:46:21.005665-0500	Nexy	[0xb2df5f980] activating connection: mach=true listener=false peer=false name=com.apple.powerlog.plxpclogger.xpc
default	13:46:21.005865-0500	Nexy	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	13:46:21.005928-0500	Nexy	[0xb2df5c8c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:46:21.005990-0500	Nexy	Exiting exit handler.
default	13:46:21.006514-0500	Nexy	XPC connection invalidated (daemon unloaded/disabled)
default	13:46:21.010509-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x128b28a (Nexy) connectionID: 1A597F pid: 25767 in session 0x101
default	13:46:21.010529-0500	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x128b28a (Nexy) acq:0x8012c68e0 count:1
default	13:46:21.010761-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x128b28a removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x128b28a (Nexy)"
)}
default	13:46:21.011802-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x64a7 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x128b28a (Nexy)"
)}
default	13:46:21.012254-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef14e","name":"Nexy(25767)"}, "details":null }
default	13:46:21.012301-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef14e from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":25767})
default	13:46:21.012314-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":25767})
default	13:46:21.012830-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:46:21.012931-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 335, PID = 25767, Name = sid:0x1ef14e, Nexy(25767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:46:21.013262-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:21.013313-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:21.013417-0500	WindowManager	Connection invalidated | (25767) Nexy
default	13:46:21.013326-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:21.013113-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:21.013190-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:21.013847-0500	ControlCenter	[anon<Nexy>:25767] Workspace connection invalidated.
default	13:46:21.013463-0500	runningboardd	Invalidating assertion 398-393-1137583 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.WindowServer(88)>:393]
default	13:46:21.013868-0500	ControlCenter	[anon<Nexy>:25767] Now flagged as pending exit for reason: workspace client connection invalidated
default	13:46:21.022083-0500	runningboardd	XPC connection invalidated: [anon<Nexy>(501):25767]
default	13:46:21.022936-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:46:21.023071-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:46:21.024478-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_44610.44378.0_airpods noise suppression studio::out-0 issue_detected_sample_time=30720.000000 ] -- [ rms:[-47.346184], peaks:[-24.145245] ]
default	13:46:21.024502-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_44610.44378.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-42.226315], peaks:[-18.691643] ]
default	13:46:21.026005-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52054<-><IPv4-redacted>:443] interface: utun6 (skipped: 5295)
so_gencnt: 4385763 t_state: FIN_WAIT_1 process: Nexy:25767 Duration: 16.384 sec Conn_Time: 0.001 sec bytes in/out: 510211/962 pkts in/out: 57/7 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 40 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.187 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb68e5dbe
default	13:46:21.026021-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52054<-><IPv4-redacted>:443] interface: utun6 (skipped: 5295)
so_gencnt: 4385763 t_state: FIN_WAIT_1 process: Nexy:25767 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:46:21.026086-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:52052<-><IPv4-redacted>:443] interface: utun6 (skipped: 5295)
so_gencnt: 4385758 t_state: FIN_WAIT_1 process: Nexy:25767 Duration: 16.881 sec Conn_Time: 0.001 sec bytes in/out: 3360/1734 pkts in/out: 3/4 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.312 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xbb86c417
default	13:46:21.026092-0500	kernel	tcp_connection_summary [<IPv4-redacted>:52052<-><IPv4-redacted>:443] interface: utun6 (skipped: 5295)
so_gencnt: 4385758 t_state: FIN_WAIT_1 process: Nexy:25767 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:46:21.026124-0500	mDNSResponder	[R468007] DNSServiceCreateConnection STOP PID[25767](Nexy)
default	13:46:21.026308-0500	runningboardd	[anon<Nexy>(501):25767] termination reported by proc_exit
default	13:46:21.028656-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x128b28a} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:46:21.028970-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:46:21.028676-0500	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 19444362
default	13:46:21.028738-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:46:21.030077-0500	runningboardd	Invalidating assertion 398-363-1137481 (target:[anon<Nexy>(501):25767]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	13:46:21.046561-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), none-NotVisible
default	13:46:21.129817-0500	runningboardd	Removing process: [anon<Nexy>(501):25767]
default	13:46:21.130067-0500	runningboardd	removeJobWithInstance called for identity without existing job [anon<Nexy>(501):25767]
default	13:46:21.130079-0500	runningboardd	Removing assertions for terminated process: [anon<Nexy>(501):25767]
default	13:46:21.135158-0500	ControlCenter	[anon<Nexy>:25767] Process exited: <RBSProcessExitContext| unknown>.
default	13:46:21.135171-0500	ControlCenter	[anon<Nexy>:25767] Setting process task state to: Not Running
default	13:46:21.135221-0500	audiomxd	  ServerSessionManager.mm:1322  Monitored process died, pid = 25767, name = Nexy
default	13:46:21.135181-0500	ControlCenter	[anon<Nexy>:25767] Setting process visibility to: Unknown
default	13:46:21.135205-0500	ControlCenter	[anon<Nexy>:25767] Invalidating workspace.
default	13:46:21.135355-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), none-NotVisible
default	13:46:21.135222-0500	ControlCenter	Removing source registration for processHandle: [anon<Nexy>(501):25767]
default	13:46:21.135484-0500	gamepolicyd	Received state update for 25767 (anon<Nexy>(501), none-NotVisible
default	13:46:21.135521-0500	ControlCenter	Removing: <FBProcess: 0xaf8cff900; anon<Nexy>:25767(v1A6852)>
default	13:46:21.137846-0500	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-25767)
default	13:46:21.140796-0500	ControlCenter	Removing ephemeral displayable instance DisplayableId(AA4EC4A1) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-25767)
default	13:46:21.140857-0500	ControlCenter	Removing displayables [DisplayableAppStatusItem(AA4EC4A1, (bid:com.nexy.assistant-Item-0-25767))]
default	13:46:23.858367-0500	loginwindow	-[ApplicationManager(AppDeathHandler) _appQuitTimer:] | _appQuitTimer fired for: ASN: 19337840, name: Nexy with url: file:///Applications/Nexy.app/
default	13:46:23.858647-0500	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | There are other instances of Nexy at /Applications/Nexy.app.  Done with this instance.
