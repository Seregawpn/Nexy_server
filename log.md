default	20:30:09.061058-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:30:09.061209-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:30:09.062786-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	20:30:09.066632-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:30:09.070065-0500	runningboardd	Launch request for app<application.com.nexy.assistant.21676800.21676806(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:30:09.070216-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.21676800.21676806(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:13823] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:397-13823-200881 target:app<application.com.nexy.assistant.21676800.21676806(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:30:09.070338-0500	runningboardd	Assertion 397-13823-200881 (target:app<application.com.nexy.assistant.21676800.21676806(501)>) will be created as active
default	20:30:09.077249-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	20:30:09.077294-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.21676800.21676806(501)>
default	20:30:09.077311-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	20:30:09.077378-0500	runningboardd	app<application.com.nexy.assistant.21676800.21676806(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	20:30:09.107177-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21676800.21676806(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:30:09.110522-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.21676800.21676806(501)>:34055]
default	20:30:09.110605-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] from originator [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:397-397-200886 target:34055 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:30:09.110794-0500	runningboardd	Assertion 397-397-200886 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055]) will be created as active
default	20:30:09.117398-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring jetsam update because this process is not memory-managed
default	20:30:09.117410-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring suspend because this process is not lifecycle managed
default	20:30:09.117428-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Set darwin role to: UserInteractive
default	20:30:09.117438-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring GPU update because this process is not GPU managed
default	20:30:09.117499-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring memory limit update because this process is not memory-managed
default	20:30:09.117582-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] reported to RB as running
default	20:30:09.122205-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:30:09.231848-0500	gamepolicyd	Received state update for 34055 (app<application.com.nexy.assistant.21676800.21676806(501)>, running-active-NotVisible
default	20:30:09.267088-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	20:30:09.269270-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=460.28, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=460, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	20:30:09.278136-0500	tccd	AUTHREQ_SUBJECT: msgID=460.28, subject=com.nexy.assistant,
default	20:30:09.278863-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974000 at /Applications/Nexy.app
default	20:30:09.299266-0500	kernel	Nexy[34055] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x9a8aa8e449744dfd. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:30:09.299292-0500	kernel	Nexy[34055] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0x9a8aa8e449744dfd. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:30:09.429217-0500	Nexy	[0x1039a9820] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:30:09.429279-0500	Nexy	[0x1039a9de0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	20:30:09.697041-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x10399d260 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:30:09.697269-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x10399d260 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:30:09.697480-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x10399d260 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:30:09.697681-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x10399d260 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:30:09.698896-0500	Nexy	[0x103998280] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:30:09.699625-0500	Nexy	[0x8d46a4000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:30:09.699963-0500	Nexy	[0x8d46a4140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:30:09.700393-0500	Nexy	[0x8d46a4280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:30:09.701375-0500	Nexy	Received configuration update from daemon (initial)
default	20:30:09.702457-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:30:09.702809-0500	Nexy	[0x8d46a43c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:30:09.703471-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34055.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:30:09.705120-0500	tccd	AUTHREQ_SUBJECT: msgID=34055.1, subject=com.nexy.assistant,
default	20:30:09.705770-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974300 at /Applications/Nexy.app
default	20:30:09.720664-0500	Nexy	[0x8d46a43c0] invalidated after the last release of the connection object
default	20:30:09.723325-0500	Nexy	server port 0x00003213, session port 0x00003213
default	20:30:09.724730-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2763, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:30:09.724761-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:30:09.725977-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2763, subject=com.nexy.assistant,
default	20:30:09.726737-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974300 at /Applications/Nexy.app
default	20:30:09.745301-0500	Nexy	New connection 0xb2163 main
default	20:30:09.747867-0500	Nexy	CHECKIN: pid=34055
default	20:30:09.756731-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] from originator [osservice<com.apple.coreservices.launchservicesd>:361] with description <RBSAssertionDescriptor| "uielement:34055" ID:397-361-200891 target:34055 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:30:09.756799-0500	runningboardd	Assertion 397-361-200891 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055]) will be created as active
default	20:30:09.756799-0500	Nexy	CHECKEDIN: pid=34055 asn=0x0-0x501501 foreground=0
default	20:30:09.757011-0500	Nexy	[0x8d46a43c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:30:09.756686-0500	launchservicesd	CHECKIN:0x0-0x501501 34055 com.nexy.assistant
default	20:30:09.757019-0500	Nexy	[0x8d46a43c0] Connection returned listener port: 0x4503
default	20:30:09.757215-0500	runningboardd	Invalidating assertion 397-361-200887 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055]) from originator [osservice<com.apple.coreservices.launchservicesd>:361]
default	20:30:09.757246-0500	Nexy	[0x8d46cc300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x8d46a43c0.peer[361].0x8d46cc300
default	20:30:09.757570-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:30:09.757656-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:30:09.758426-0500	Nexy	FRONTLOGGING: version 1
default	20:30:09.758434-0500	Nexy	Registered, pid=34055 ASN=0x0,0x501501
default	20:30:09.758594-0500	WindowServer	b2163[CreateApplication]: Process creation: 0x0-0x501501 (Nexy) connectionID: B2163 pid: 34055 in session 0x101
default	20:30:09.759181-0500	Nexy	[0x8d46a4500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:30:09.759318-0500	Nexy	[0x8d46a43c0] Connection returned listener port: 0x4503
default	20:30:09.759809-0500	Nexy	BringForward: pid=34055 asn=0x0-0x501501 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	20:30:09.759833-0500	Nexy	BringFrontModifier: pid=34055 asn=0x0-0x501501 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	20:30:09.760278-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:30:09.761614-0500	Nexy	No persisted cache on this platform.
default	20:30:09.762454-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:30:09.762942-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:30:09.764609-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	20:30:09.764617-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	20:30:09.764663-0500	Nexy	Initializing connection
default	20:30:09.764699-0500	Nexy	Removing all cached process handles
default	20:30:09.764719-0500	Nexy	Sending handshake request attempt #1 to server
default	20:30:09.764725-0500	Nexy	Creating connection to com.apple.runningboard
default	20:30:09.764733-0500	Nexy	[0x8d46a4640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	20:30:09.765055-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] as ready
default	20:30:09.765113-0500	Nexy	[0x8d46a43c0] Connection returned listener port: 0x4503
default	20:30:09.765599-0500	Nexy	Handshake succeeded
default	20:30:09.765613-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.21676800.21676806(501)>
default	20:30:09.766047-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 34055
default	20:30:09.772356-0500	Nexy	[0x8d46a43c0] Connection returned listener port: 0x4503
default	20:30:09.775444-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	20:30:09.775496-0500	Nexy	[0x8d46a48c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	20:30:09.775615-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	20:30:09.775712-0500	Nexy	[0x8d46a4a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:30:09.777430-0500	Nexy	[0x8d46a4a00] Connection returned listener port: 0x6d03
default	20:30:09.777970-0500	Nexy	Registered process with identifier 34055-289956
default	20:30:10.003906-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:30:10.007968-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:30:10.009444-0500	Nexy	[0x8d46a4b40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:30:10.012336-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21676800.21676806 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21676800.21676806>
default	20:30:10.016079-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:30:10.017862-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:30:10.018554-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:30:10.018795-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:30:10.018826-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:30:10.018872-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:30:10.019062-0500	Nexy	[0x8d46a4c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:30:10.019156-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:30:10.019820-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34055.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:30:10.027821-0500	tccd	AUTHREQ_SUBJECT: msgID=34055.2, subject=com.nexy.assistant,
default	20:30:10.028522-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee85e00 at /Applications/Nexy.app
default	20:30:10.040889-0500	Nexy	[0x8d46a4c80] invalidated after the last release of the connection object
default	20:30:10.041042-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:30:10.041081-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:30:10.041292-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:30:10.043443-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1539, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:10.044295-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1539, subject=com.nexy.assistant,
default	20:30:10.044842-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ecdaa00 at /Applications/Nexy.app
error	20:30:10.057955-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=404, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	20:30:10.058955-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1541, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:10.059812-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1541, subject=com.nexy.assistant,
default	20:30:10.060318-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee86a00 at /Applications/Nexy.app
default	20:30:10.074598-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:30:10.074912-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x8d58353a0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	20:30:10.089148-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	20:30:10.089163-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	20:30:10.091887-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:30:10.092010-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:30:10.095988-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:30:12.537224-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D7D3A870-C85E-4006-8E2A-A27E7C4D9DA6 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51354,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x59d15054 tp_proto=0x06"
default	20:30:12.537313-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51354<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1001854 t_state: SYN_SENT process: Nexy:34055 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb5fc6feb
default	20:30:12.538041-0500	kernel	tcp connected: [<IPv4-redacted>:51354<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1001854 t_state: ESTABLISHED process: Nexy:34055 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb5fc6feb
default	20:30:12.538319-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:51354<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1001854 t_state: FIN_WAIT_1 process: Nexy:34055 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb5fc6feb
default	20:30:12.538327-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51354<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1001854 t_state: FIN_WAIT_1 process: Nexy:34055 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:30:12.569320-0500	Nexy	[0x8d46a4c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:30:12.583398-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x1039b8300) Selecting device 85 from constructor
default	20:30:12.583409-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x1039b8300)
default	20:30:12.583415-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x1039b8300) not already running
default	20:30:12.583421-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x1039b8300) nothing to teardown
default	20:30:12.583426-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x1039b8300) connecting device 85
default	20:30:12.583548-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x1039b8300) Device ID: 85 (Input:No | Output:Yes): true
default	20:30:12.584156-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x1039b8300) created ioproc 0xa for device 85
default	20:30:12.584273-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039b8300) adding 7 device listeners to device 85
default	20:30:12.584428-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039b8300) adding 0 device delegate listeners to device 85
default	20:30:12.584434-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x1039b8300)
default	20:30:12.584503-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:30:12.584512-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	20:30:12.584518-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:30:12.584525-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	20:30:12.584532-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:30:12.584621-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x1039b8300) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:30:12.584634-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x1039b8300) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:30:12.584640-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:30:12.584650-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039b8300) removing 0 device listeners from device 0
default	20:30:12.584656-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039b8300) removing 0 device delegate listeners from device 0
default	20:30:12.584661-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x1039b8300)
default	20:30:12.584676-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:30:12.584772-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x1039b8300) caller requesting device change from 85 to 91
default	20:30:12.584779-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x1039b8300)
default	20:30:12.584784-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x1039b8300) not already running
default	20:30:12.584789-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x1039b8300) disconnecting device 85
default	20:30:12.584794-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x1039b8300) destroying ioproc 0xa for device 85
default	20:30:12.584872-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:30:12.585385-0500	Nexy	[0x8d46a4f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:30:12.586843-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1c5058","name":"Nexy(34055)"}, "details":{"PID":34055,"session_type":"Primary"} }
default	20:30:12.586929-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":34055}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1c5058, sessionType: 'prim', isRecording: false }, 
]
default	20:30:12.587724-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 34055, name = Nexy
default	20:30:12.588010-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x8d56212e0 with ID: 0x1c5058
default	20:30:12.588920-0500	Nexy	[0x8d46a5040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	20:30:12.589324-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=146265111265281 }
default	20:30:12.589339-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	20:30:12.589390-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:30:12.589476-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x1039b8300) connecting device 91
default	20:30:12.589565-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x1039b8300) Device ID: 91 (Input:Yes | Output:No): true
default	20:30:12.590995-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1542, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:12.592253-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1542, subject=com.nexy.assistant,
default	20:30:12.592889-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee86a00 at /Applications/Nexy.app
default	20:30:12.606443-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x1039b8300) created ioproc 0xa for device 91
default	20:30:12.606585-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039b8300) adding 7 device listeners to device 91
default	20:30:12.606745-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039b8300) adding 0 device delegate listeners to device 91
default	20:30:12.606753-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x1039b8300)
default	20:30:12.606761-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	20:30:12.606771-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:30:12.606903-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:30:12.606913-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	20:30:12.606918-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:30:12.607019-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x1039b8300) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:30:12.607032-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x1039b8300) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:30:12.607038-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:30:12.607043-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039b8300) removing 7 device listeners from device 85
default	20:30:12.607198-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039b8300) removing 0 device delegate listeners from device 85
default	20:30:12.607208-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x1039b8300)
default	20:30:12.607837-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:30:12.609082-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1543, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:12.610217-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1543, subject=com.nexy.assistant,
default	20:30:12.610867-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee86a00 at /Applications/Nexy.app
default	20:30:12.624577-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:30:12.625730-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1544, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:12.626673-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1544, subject=com.nexy.assistant,
default	20:30:12.627240-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee86a00 at /Applications/Nexy.app
default	20:30:12.640608-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:30:12.642182-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1545, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:12.643157-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1545, subject=com.nexy.assistant,
default	20:30:12.643728-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee86a00 at /Applications/Nexy.app
default	20:30:12.656806-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:30:12.656964-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:30:12.657799-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:30:12.659595-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50505200] Created node ADM::com.nexy.assistant_8333.8241.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:30:12.659653-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50505200] Created node ADM::com.nexy.assistant_8333.8241.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:30:12.744390-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:30:12.746176-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:8333 called from <private>
default	20:30:12.746247-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:30:12.747374-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8333 called from <private>
default	20:30:12.747543-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8333)
default	20:30:12.747562-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8333 called from <private>
default	20:30:12.747570-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8333 called from <private>
default	20:30:12.748059-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8332)
default	20:30:12.750852-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:397-332-200906 target:34055 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:30:12.750976-0500	runningboardd	Assertion 397-332-200906 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055]) will be created as active
default	20:30:12.753433-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring jetsam update because this process is not memory-managed
default	20:30:12.753464-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring suspend because this process is not lifecycle managed
default	20:30:12.748074-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8332 called from <private>
default	20:30:12.748080-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8332 called from <private>
default	20:30:12.753494-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring GPU update because this process is not GPU managed
default	20:30:12.753551-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring memory limit update because this process is not memory-managed
default	20:30:12.756860-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:30:12.757656-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	20:30:12.755887-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21676800.21676806 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21676800.21676806>
default	20:30:12.759761-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8333)
default	20:30:12.759810-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8333)
default	20:30:12.759823-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8333)
default	20:30:12.759834-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8333)
default	20:30:12.761619-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:8333 called from <private>
default	20:30:12.761629-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:8333 called from <private>
default	20:30:12.761642-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8333 called from <private>
default	20:30:12.761648-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8333 called from <private>
default	20:30:12.761653-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:8333 called from <private>
default	20:30:12.761660-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:8333 called from <private>
default	20:30:12.761665-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8333 called from <private>
default	20:30:12.761828-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8333 called from <private>
default	20:30:12.765733-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5058","name":"Nexy(34055)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:30:12.766341-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:30:12.766912-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:30:12.769160-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:12.769315-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:30:12.769346-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1c5058, Nexy(34055), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:30:12.769515-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:30:12.769545-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5058, Nexy(34055), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 89 starting recording
default	20:30:12.769746-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:12.761862-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:8333 called from <private>
default	20:30:12.761904-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:8333 called from <private>
default	20:30:12.763744-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8333)
default	20:30:12.764214-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8333 called from <private>
default	20:30:12.765778-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8332 called from <private>
default	20:30:12.765818-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8332 called from <private>
default	20:30:12.769830-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:30:12.769903-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5058, Nexy(34055), 'prim'', displayID:'com.nexy.assistant'}
default	20:30:12.768193-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8332)
default	20:30:12.769691-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:12.770103-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:12.770503-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:30:12.770147-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:30:12.766994-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1546, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:12.770396-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:12.770186-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:30:12.770617-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:12.777591-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:8332 called from <private>
default	20:30:12.777611-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:8332 called from <private>
default	20:30:12.777712-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8332)
default	20:30:12.782392-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1546, subject=com.nexy.assistant,
default	20:30:12.785398-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee86a00 at /Applications/Nexy.app
default	20:30:12.788177-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21676800.21676806(501)>: running-active (role: UserInteractive) (endowments: <private>)
fault	20:30:12.785654-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21676800.21676806 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21676800.21676806>
default	20:30:12.789181-0500	runningboardd	Invalidating assertion 397-332-200906 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055]) from originator [osservice<com.apple.powerd>:332]
default	20:30:12.795295-0500	gamepolicyd	Received state update for 34055 (app<application.com.nexy.assistant.21676800.21676806(501)>, running-active-NotVisible
default	20:30:12.796572-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8332)
default	20:30:12.796812-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:8332 called from <private>
default	20:30:12.796821-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:8332 called from <private>
default	20:30:12.796955-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8332)
default	20:30:12.830549-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee86a00 at /Applications/Nexy.app
default	20:30:12.849159-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50505200] Created node ADM::com.nexy.assistant_8333.8241.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:30:12.849217-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50505200] Created node ADM::com.nexy.assistant_8333.8241.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:30:12.884689-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:30:12.886245-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:8333 called from <private>
default	20:30:12.887181-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:8333 called from <private>
default	20:30:12.888057-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:30:12.889164-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:397-332-200908 target:34055 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:30:12.889245-0500	runningboardd	Assertion 397-332-200908 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055]) will be created as active
default	20:30:12.890060-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8333 called from <private>
default	20:30:12.890968-0500	runningboardd	Invalidating assertion 397-332-200908 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055]) from originator [osservice<com.apple.powerd>:332]
default	20:30:12.890249-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8333)
default	20:30:12.890266-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8333 called from <private>
default	20:30:12.891160-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:30:12.890273-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8333 called from <private>
default	20:30:12.891534-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:30:12.891973-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8333)
default	20:30:12.892131-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:8333 called from <private>
default	20:30:12.892142-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:8333 called from <private>
default	20:30:12.892154-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8333 called from <private>
default	20:30:12.893898-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring jetsam update because this process is not memory-managed
default	20:30:12.893912-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring suspend because this process is not lifecycle managed
default	20:30:12.893920-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring GPU update because this process is not GPU managed
default	20:30:12.893939-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring memory limit update because this process is not memory-managed
default	20:30:12.894048-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1548, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:12.895519-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1548, subject=com.nexy.assistant,
default	20:30:12.896384-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee86a00 at /Applications/Nexy.app
default	20:30:12.898240-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:30:12.898293-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:30:12.898335-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:30:12.898627-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:30:12.899024-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:12.899040-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:12.899054-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:12.899060-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:12.899068-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:12.899097-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:12.900840-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21676800.21676806(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:30:12.900892-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:30:12.908416-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:12.908431-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:12.908443-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:12.908452-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:12.916142-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:397-332-200909 target:34055 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:30:12.917156-0500	runningboardd	Assertion 397-332-200909 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055]) will be created as active
default	20:30:12.917488-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:8333 called from <private>
default	20:30:12.917804-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring jetsam update because this process is not memory-managed
default	20:30:12.918243-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring suspend because this process is not lifecycle managed
default	20:30:12.918302-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring GPU update because this process is not GPU managed
default	20:30:12.918423-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring memory limit update because this process is not memory-managed
default	20:30:12.921855-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21676800.21676806(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:30:13.002376-0500	gamepolicyd	Received state update for 34055 (app<application.com.nexy.assistant.21676800.21676806(501)>, running-active-NotVisible
default	20:30:13.945389-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:30:13.945862-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5058","name":"Nexy(34055)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:30:13.946052-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:13.946136-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:30:13.946188-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5058, Nexy(34055), 'prim'', displayID:'com.nexy.assistant'}
default	20:30:13.946270-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:30:13.946276-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5058, Nexy(34055), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 89 stopping recording
default	20:30:13.946310-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:30:13.946346-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:13.946387-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:30:13.946541-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:30:13.946554-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:30:13.946583-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x218B0001 category Not set
default	20:30:13.950340-0500	runningboardd	Invalidating assertion 397-332-200909 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055]) from originator [osservice<com.apple.powerd>:332]
default	20:30:13.950997-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:13.951065-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:13.951097-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:30:13.950790-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:13.950901-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:13.951231-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:13.951275-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:30:13.951353-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:13.951469-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:30:13.954206-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:30:13.956592-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:13.956607-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:13.956623-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:13.956634-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:13.956643-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:13.956650-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:13.956809-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:30:14.047357-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x1039b8300) Selecting device 0 from destructor
default	20:30:14.047382-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x1039b8300)
default	20:30:14.047398-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x1039b8300) not already running
default	20:30:14.047409-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x1039b8300) disconnecting device 91
default	20:30:14.047415-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x1039b8300) destroying ioproc 0xa for device 91
default	20:30:14.047457-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:30:14.047497-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:30:14.047665-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x1039b8300) nothing to setup
default	20:30:14.047679-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039b8300) adding 0 device listeners to device 0
default	20:30:14.047688-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039b8300) adding 0 device delegate listeners to device 0
default	20:30:14.047693-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039b8300) removing 7 device listeners from device 91
default	20:30:14.047933-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039b8300) removing 0 device delegate listeners from device 91
default	20:30:14.047947-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x1039b8300)
default	20:30:14.051960-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring jetsam update because this process is not memory-managed
default	20:30:14.051975-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring suspend because this process is not lifecycle managed
default	20:30:14.051986-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring GPU update because this process is not GPU managed
default	20:30:14.052010-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring memory limit update because this process is not memory-managed
default	20:30:14.055771-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21676800.21676806(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:30:14.056515-0500	gamepolicyd	Received state update for 34055 (app<application.com.nexy.assistant.21676800.21676806(501)>, running-active-NotVisible
default	20:30:14.109783-0500	runningboardd	Assertion did invalidate due to timeout: 397-397-200886 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055])
default	20:30:14.172460-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring jetsam update because this process is not memory-managed
default	20:30:14.172472-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring suspend because this process is not lifecycle managed
default	20:30:14.172482-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring GPU update because this process is not GPU managed
default	20:30:14.172499-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring memory limit update because this process is not memory-managed
default	20:30:14.176565-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21676800.21676806(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:30:14.176984-0500	gamepolicyd	Received state update for 34055 (app<application.com.nexy.assistant.21676800.21676806(501)>, running-active-NotVisible
default	20:30:14.191250-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34058.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=34058, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:30:14.192585-0500	tccd	AUTHREQ_SUBJECT: msgID=34058.1, subject=com.nexy.assistant,
default	20:30:14.193146-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974300 at /Applications/Nexy.app
default	20:30:14.207334-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2764, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=34058, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:30:14.208141-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2764, subject=com.nexy.assistant,
default	20:30:14.208668-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974300 at /Applications/Nexy.app
default	20:30:14.235234-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977000 at /Applications/Nexy.app
default	20:30:14.254817-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 33579: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b9860100 ae6c0400 };
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
default	20:30:14.265626-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:30:14.473094-0500	Nexy	[0x8d46a5400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:30:14.473773-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34055.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:30:14.474939-0500	tccd	AUTHREQ_SUBJECT: msgID=34055.3, subject=com.nexy.assistant,
default	20:30:14.475573-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977c00 at /Applications/Nexy.app
default	20:30:14.488675-0500	Nexy	[0x8d46a5400] invalidated after the last release of the connection object
default	20:30:14.503226-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x1039bdad0) Selecting device 85 from constructor
default	20:30:14.503241-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x1039bdad0)
default	20:30:14.503247-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x1039bdad0) not already running
default	20:30:14.503252-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x1039bdad0) nothing to teardown
default	20:30:14.503256-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x1039bdad0) connecting device 85
default	20:30:14.503362-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x1039bdad0) Device ID: 85 (Input:No | Output:Yes): true
default	20:30:14.503482-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x1039bdad0) created ioproc 0xb for device 85
default	20:30:14.503612-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039bdad0) adding 7 device listeners to device 85
default	20:30:14.503798-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039bdad0) adding 0 device delegate listeners to device 85
default	20:30:14.503807-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x1039bdad0)
default	20:30:14.503884-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	20:30:14.503892-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	20:30:14.503897-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	20:30:14.503905-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	20:30:14.503914-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:30:14.504004-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x1039bdad0) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:30:14.504014-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x1039bdad0) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:30:14.504019-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:30:14.504024-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039bdad0) removing 0 device listeners from device 0
default	20:30:14.504029-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039bdad0) removing 0 device delegate listeners from device 0
default	20:30:14.504031-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x1039bdad0)
default	20:30:14.504049-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:30:14.504111-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x1039bdad0) caller requesting device change from 85 to 91
default	20:30:14.504117-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x1039bdad0)
default	20:30:14.504128-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x1039bdad0) not already running
default	20:30:14.504132-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x1039bdad0) disconnecting device 85
default	20:30:14.504137-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x1039bdad0) destroying ioproc 0xb for device 85
default	20:30:14.504163-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	20:30:14.504200-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:30:14.504278-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x1039bdad0) connecting device 91
default	20:30:14.504350-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x1039bdad0) Device ID: 91 (Input:Yes | Output:No): true
default	20:30:14.505570-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1549, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:14.506705-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1549, subject=com.nexy.assistant,
default	20:30:14.507311-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ecdaa00 at /Applications/Nexy.app
default	20:30:14.520031-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x1039bdad0) created ioproc 0xb for device 91
default	20:30:14.520137-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039bdad0) adding 7 device listeners to device 91
default	20:30:14.520308-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039bdad0) adding 0 device delegate listeners to device 91
default	20:30:14.520315-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x1039bdad0)
default	20:30:14.520323-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	20:30:14.520332-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:30:14.520437-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:30:14.520445-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	20:30:14.520450-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:30:14.520545-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x1039bdad0) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:30:14.520560-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x1039bdad0) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:30:14.520565-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:30:14.520570-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039bdad0) removing 7 device listeners from device 85
default	20:30:14.520723-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039bdad0) removing 0 device delegate listeners from device 85
default	20:30:14.520733-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x1039bdad0)
default	20:30:14.521315-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:30:14.522281-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1550, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:14.523133-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1550, subject=com.nexy.assistant,
default	20:30:14.523684-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87000 at /Applications/Nexy.app
default	20:30:14.535929-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	20:30:14.536051-0500	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0x8d6678750, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	20:30:14.536232-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:30:14.537220-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1551, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:14.537965-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1551, subject=com.nexy.assistant,
default	20:30:14.538491-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87000 at /Applications/Nexy.app
default	20:30:14.552081-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1552, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:14.552953-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1552, subject=com.nexy.assistant,
default	20:30:14.553533-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87000 at /Applications/Nexy.app
default	20:30:14.569906-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:30:14.572854-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5058","name":"Nexy(34055)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:30:14.572962-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:30:14.572992-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1c5058, Nexy(34055), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:30:14.573019-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:30:14.573204-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:397-332-200917 target:34055 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:30:14.573091-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1c5058, Nexy(34055), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:30:14.573195-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:14.573270-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:14.573362-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:30:14.573323-0500	runningboardd	Assertion 397-332-200917 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055]) will be created as active
default	20:30:14.573462-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:14.573479-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:30:14.573374-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:14.573509-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5058, Nexy(34055), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 89 starting recording
default	20:30:14.573412-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:14.573720-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring jetsam update because this process is not memory-managed
default	20:30:14.573636-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:14.573765-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring suspend because this process is not lifecycle managed
default	20:30:14.573723-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:30:14.573812-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring GPU update because this process is not GPU managed
default	20:30:14.573798-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5058, Nexy(34055), 'prim'', displayID:'com.nexy.assistant'}
default	20:30:14.573559-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:14.573915-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:30:14.573626-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:14.573925-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:30:14.573894-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring memory limit update because this process is not memory-managed
default	20:30:14.573879-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:30:14.574116-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x218B0001 category Not set
default	20:30:14.575373-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:14.575458-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:14.575484-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:14.575498-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	20:30:14.575505-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	20:30:14.575514-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	20:30:14.575552-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:30:14.579839-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21676800.21676806(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:30:14.580389-0500	gamepolicyd	Received state update for 34055 (app<application.com.nexy.assistant.21676800.21676806(501)>, running-active-NotVisible
default	20:30:14.583245-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:30:14.583318-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:30:14.583369-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:30:14.584060-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:14.584070-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:14.584084-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:14.584095-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:14.584155-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:14.584206-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:14.584243-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:14.584252-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:14.584284-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:14.584314-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:14.584430-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:30:14.584343-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:14.584444-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:14.586121-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:14.586133-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:14.586143-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:14.586149-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:14.586155-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:14.586162-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:14.586353-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:30:17.362898-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	20:30:18.393326-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:30:18.393538-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:30:18.402332-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:30:18.402421-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:30:19.796458-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	20:30:20.363135-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	20:30:20.759126-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:30:23.363171-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	20:30:23.550328-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_8333.8241.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-33.991879], peaks:[-13.493796] ]
default	20:30:23.553082-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_8333.8241.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-37.335918], peaks:[-16.346502] ]
default	20:30:26.363101-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	20:30:27.597064-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:30:27.597595-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5058","name":"Nexy(34055)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:30:27.597831-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:27.597949-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:30:27.598021-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5058, Nexy(34055), 'prim'', displayID:'com.nexy.assistant'}
default	20:30:27.598156-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:30:27.598195-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5058, Nexy(34055), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 89 stopping recording
default	20:30:27.598253-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:30:27.598319-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:27.598392-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:30:27.598603-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:30:27.598633-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:30:27.598674-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x218B0001 category Not set
default	20:30:27.602786-0500	runningboardd	Invalidating assertion 397-332-200917 (target:[app<application.com.nexy.assistant.21676800.21676806(501)>:34055]) from originator [osservice<com.apple.powerd>:332]
default	20:30:27.603271-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:27.603106-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:27.603318-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:27.603349-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:30:27.603193-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:27.603384-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:27.603491-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:30:27.603506-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:27.603560-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:30:27.606038-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:30:27.609798-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:27.609812-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:27.609827-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:27.609834-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:27.609843-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:27.609853-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:27.609977-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:30:27.699311-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x1039bdad0) Selecting device 0 from destructor
default	20:30:27.699341-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x1039bdad0)
default	20:30:27.699357-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x1039bdad0) not already running
default	20:30:27.699369-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x1039bdad0) disconnecting device 91
default	20:30:27.699404-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x1039bdad0) destroying ioproc 0xb for device 91
default	20:30:27.699464-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:30:27.699532-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:30:27.699855-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x1039bdad0) nothing to setup
default	20:30:27.699879-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039bdad0) adding 0 device listeners to device 0
default	20:30:27.699892-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x1039bdad0) adding 0 device delegate listeners to device 0
default	20:30:27.699907-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039bdad0) removing 7 device listeners from device 91
default	20:30:27.700390-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x1039bdad0) removing 0 device delegate listeners from device 91
default	20:30:27.700422-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x1039bdad0)
default	20:30:27.709641-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring jetsam update because this process is not memory-managed
default	20:30:27.709655-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring suspend because this process is not lifecycle managed
default	20:30:27.709666-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring GPU update because this process is not GPU managed
default	20:30:27.709700-0500	runningboardd	[app<application.com.nexy.assistant.21676800.21676806(501)>:34055] Ignoring memory limit update because this process is not memory-managed
default	20:30:27.714740-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21676800.21676806(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:30:27.715467-0500	gamepolicyd	Received state update for 34055 (app<application.com.nexy.assistant.21676800.21676806(501)>, running-active-NotVisible
default	20:30:29.810986-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8332)
default	20:30:29.811060-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8332 called from <private>
default	20:30:29.811079-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8332 called from <private>
default	20:30:29.812009-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8333)
default	20:30:29.812038-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8333 called from <private>
default	20:30:29.812051-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8333 called from <private>
default	20:30:29.825987-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8333)
default	20:30:29.826047-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8333 called from <private>
default	20:30:29.826057-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:8333 called from <private>
default	20:30:29.826204-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8332 called from <private>
default	20:30:29.826219-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8332 called from <private>
default	20:30:29.826792-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8332)
default	20:30:29.826818-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:8332 called from <private>
default	20:30:29.826853-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:8332 called from <private>
default	20:30:29.832434-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8332)
default	20:30:29.832659-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:8332 called from <private>
default	20:30:29.832720-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:8332 called from <private>
default	20:30:29.832945-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8332)
default	20:30:29.833363-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8332)
default	20:30:29.833481-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8332)
default	20:30:29.839204-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:8332 called from <private>
default	20:30:29.839227-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:8332 called from <private>
default	20:30:29.840548-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 3 3, id:8332 called from <private>
default	20:30:29.840565-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 4 4, id:8332 called from <private>
default	20:30:29.840704-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8332)
default	20:30:29.844907-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8332)
default	20:30:29.845088-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 4 4 id:8332 called from <private>
default	20:30:29.845098-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 3 3 id:8332 called from <private>
default	20:30:29.845237-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8332)
default	20:30:29.851636-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8332)
default	20:30:29.851897-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:8332 called from <private>
default	20:30:29.851910-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:8332 called from <private>
default	20:30:29.851934-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:8332 called from <private>
default	20:30:29.851952-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:8332 called from <private>
default	20:30:29.851959-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8332 called from <private>
default	20:30:29.851965-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:8332 called from <private>
default	20:30:29.851970-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8332 called from <private>
default	20:30:29.852018-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8332 called from <private>
default	20:30:29.852195-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8332 called from <private>
default	20:30:29.852277-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:8332 called from <private>
default	20:30:29.852344-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8332 called from <private>
default	20:30:29.852401-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8332 called from <private>
default	20:30:29.852456-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8332 called from <private>
default	20:30:29.852525-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:8332 called from <private>
default	20:30:29.852579-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8332 called from <private>
default	20:30:29.852642-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8332 called from <private>
default	20:30:29.852701-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8332 called from <private>
default	20:30:29.852761-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:8332 called from <private>
default	20:30:54.272196-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1c5058","name":"Nexy(34055)"}, "details":null }
default	20:30:54.272243-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1c5058 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":34055})
default	20:30:54.270910-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x501501 (Nexy) connectionID: B2163 pid: 34055 in session 0x101
default	20:30:54.272260-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":34055})
default	20:30:54.272897-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:54.270961-0500	WindowServer	<BSCompoundAssertion:0x7c9011500> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x501501 (Nexy) acq:0x7c627b240 count:1
default	20:30:54.273000-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 89, PID = 34055, Name = sid:0x1c5058, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:30:54.273332-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:54.273117-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:54.273382-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:54.273262-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:54.274010-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x501501 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x501501 (Nexy)"
)}
default	20:30:54.274348-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x8507 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x501501 (Nexy)"
)}
default	20:30:54.278336-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.21676800.21676806(501)>:34055]
default	20:30:54.280044-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:30:54.280225-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:30:54.280957-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_8333.8241.0_airpods noise suppression studio::out-0 issue_detected_sample_time=336960.000000 ] -- [ rms:[-34.650745], peaks:[-5.351093] ]
default	20:30:54.280989-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_8333.8241.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-34.805714], peaks:[-15.910248] ]
default	20:30:54.282587-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:54.282687-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:54.288336-0500	kernel	Nexy[34055] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xee64bbf1ea832fb7. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:30:54.288352-0500	kernel	Nexy[34055] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0xee64bbf1ea832fb7. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:30:54.345722-0500	Nexy	[0x1019b0020] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:30:54.345799-0500	Nexy	[0x1019b0560] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	20:30:54.474390-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x1019b8fa0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:30:54.474625-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x1019b8fa0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:30:54.474833-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x1019b8fa0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:30:54.475035-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x1019b8fa0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:30:54.476258-0500	Nexy	[0x1019b5380] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:30:54.477056-0500	Nexy	[0x8deeec000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:30:54.477380-0500	Nexy	[0x8deeec140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:30:54.477813-0500	Nexy	[0x8deeec280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:30:54.478398-0500	Nexy	Received configuration update from daemon (initial)
default	20:30:54.480066-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:30:54.480432-0500	Nexy	[0x8deeec3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:30:54.481103-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34055.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:30:54.482767-0500	tccd	AUTHREQ_SUBJECT: msgID=34055.1, subject=com.nexy.assistant,
default	20:30:54.483421-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977c00 at /Applications/Nexy.app
default	20:30:54.497503-0500	Nexy	[0x8deeec3c0] invalidated after the last release of the connection object
default	20:30:54.498081-0500	Nexy	server port 0x00003713, session port 0x00003713
default	20:30:54.499186-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2765, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:30:54.499212-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:30:54.500032-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2765, subject=com.nexy.assistant,
default	20:30:54.500601-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977c00 at /Applications/Nexy.app
default	20:30:54.516320-0500	Nexy	New connection 0x102523 main
default	20:30:54.518707-0500	Nexy	CHECKIN: pid=34055
default	20:30:54.524704-0500	launchservicesd	CHECKIN:0x0-0x501501 34055 com.nexy.assistant
default	20:30:54.524817-0500	Nexy	CHECKEDIN: pid=34055 asn=0x0-0x501501 foreground=0
default	20:30:54.525058-0500	Nexy	[0x8deeec3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:30:54.525065-0500	Nexy	[0x8deeec3c0] Connection returned listener port: 0x5003
default	20:30:54.525248-0500	Nexy	[0x8def14300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x8deeec3c0.peer[361].0x8def14300
default	20:30:54.525625-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:30:54.525753-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:30:54.526622-0500	Nexy	FRONTLOGGING: version 1
default	20:30:54.526627-0500	Nexy	Registered, pid=34055 ASN=0x0,0x501501
default	20:30:54.526873-0500	WindowServer	102523[CreateApplication]: Process creation: 0x0-0x501501 (Nexy) connectionID: 102523 pid: 34055 in session 0x101
default	20:30:54.527189-0500	Nexy	[0x8deeec500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:30:54.527940-0500	Nexy	[0x8deeec3c0] Connection returned listener port: 0x5003
default	20:30:54.528357-0500	Nexy	BringForward: pid=34055 asn=0x0-0x501501 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	20:30:54.528382-0500	Nexy	BringFrontModifier: pid=34055 asn=0x0-0x501501 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	20:30:54.529031-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:30:54.531585-0500	Nexy	No persisted cache on this platform.
default	20:30:54.532618-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:30:54.533551-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:30:54.535443-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	20:30:54.535454-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	20:30:54.535511-0500	Nexy	Initializing connection
default	20:30:54.535552-0500	Nexy	Removing all cached process handles
default	20:30:54.535573-0500	Nexy	Sending handshake request attempt #1 to server
default	20:30:54.535581-0500	Nexy	Creating connection to com.apple.runningboard
default	20:30:54.535587-0500	Nexy	[0x8deeec640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	20:30:54.535957-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] as ready
default	20:30:54.536056-0500	Nexy	[0x8deeec3c0] Connection returned listener port: 0x5003
default	20:30:54.536534-0500	Nexy	Handshake succeeded
default	20:30:54.536549-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.21676800.21676806(501)>
default	20:30:54.537158-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 34055
default	20:30:54.542232-0500	Nexy	[0x8deeec3c0] Connection returned listener port: 0x5003
default	20:30:54.546060-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	20:30:54.546083-0500	Nexy	[0x8deeec8c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	20:30:54.546200-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	20:30:54.546252-0500	Nexy	[0x8deeeca00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:30:54.547780-0500	Nexy	[0x8deeeca00] Connection returned listener port: 0x6403
default	20:30:54.549151-0500	Nexy	Registered process with identifier 34055-289990
default	20:30:54.674952-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:30:54.678523-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:30:54.679995-0500	Nexy	[0x8deeecb40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	20:30:54.681941-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:30:54.683484-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:30:54.683657-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:30:54.683794-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:30:54.683808-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:30:54.683836-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:30:54.683970-0500	Nexy	[0x8deeecc80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:30:54.684113-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:30:54.684565-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34055.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:30:54.691206-0500	tccd	AUTHREQ_SUBJECT: msgID=34055.2, subject=com.nexy.assistant,
default	20:30:54.691814-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87900 at /Applications/Nexy.app
default	20:30:54.704083-0500	Nexy	[0x8deeecc80] invalidated after the last release of the connection object
default	20:30:54.704231-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:30:54.704269-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:30:54.704569-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:30:54.705864-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1553, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:54.706686-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1553, subject=com.nexy.assistant,
default	20:30:54.707237-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ecdaa00 at /Applications/Nexy.app
error	20:30:54.719625-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=404, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	20:30:54.720632-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1555, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:54.721479-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1555, subject=com.nexy.assistant,
default	20:30:54.722050-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87600 at /Applications/Nexy.app
default	20:30:54.736099-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:30:54.736115-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x8df047e20> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	20:30:54.751334-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	20:30:54.751346-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	20:30:54.754117-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:30:54.754265-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:30:54.758629-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:30:56.200700-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid EC82DFD3-8052-4DCA-9B06-CAD40450295F flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51361,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xf00299b4 tp_proto=0x06"
default	20:30:56.200777-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51361<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002217 t_state: SYN_SENT process: Nexy:34055 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x93ba0569
default	20:30:56.201436-0500	kernel	tcp connected: [<IPv4-redacted>:51361<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002217 t_state: ESTABLISHED process: Nexy:34055 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x93ba0569
default	20:30:56.201695-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:51361<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002217 t_state: FIN_WAIT_1 process: Nexy:34055 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x93ba0569
default	20:30:56.201709-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51361<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002217 t_state: FIN_WAIT_1 process: Nexy:34055 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:30:56.218355-0500	Nexy	[0x8deeecc80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:30:56.227446-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x8de27c040) Selecting device 85 from constructor
default	20:30:56.227458-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x8de27c040)
default	20:30:56.227464-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x8de27c040) not already running
default	20:30:56.227468-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x8de27c040) nothing to teardown
default	20:30:56.227471-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x8de27c040) connecting device 85
default	20:30:56.227572-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x8de27c040) Device ID: 85 (Input:No | Output:Yes): true
default	20:30:56.227670-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x8de27c040) created ioproc 0xa for device 85
default	20:30:56.227760-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27c040) adding 7 device listeners to device 85
default	20:30:56.227897-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27c040) adding 0 device delegate listeners to device 85
default	20:30:56.227907-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x8de27c040)
default	20:30:56.227971-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:30:56.227977-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	20:30:56.227983-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:30:56.227989-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	20:30:56.227998-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:30:56.228089-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x8de27c040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:30:56.228099-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x8de27c040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:30:56.228104-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:30:56.228108-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27c040) removing 0 device listeners from device 0
default	20:30:56.228111-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27c040) removing 0 device delegate listeners from device 0
default	20:30:56.228121-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x8de27c040)
default	20:30:56.228136-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:30:56.228214-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x8de27c040) caller requesting device change from 85 to 91
default	20:30:56.228221-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x8de27c040)
default	20:30:56.228225-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x8de27c040) not already running
default	20:30:56.228229-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x8de27c040) disconnecting device 85
default	20:30:56.228234-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x8de27c040) destroying ioproc 0xa for device 85
default	20:30:56.228286-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:30:56.228764-0500	Nexy	[0x8deeecf00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:30:56.229722-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1c5059","name":"Nexy(34055)"}, "details":{"PID":34055,"session_type":"Primary"} }
default	20:30:56.229808-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":34055}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1c5059, sessionType: 'prim', isRecording: false }, 
]
default	20:30:56.230165-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x8df259280 with ID: 0x1c5059
default	20:30:56.230732-0500	Nexy	[0x8deeed040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	20:30:56.231115-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=146265111265281 }
default	20:30:56.231129-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	20:30:56.231183-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:30:56.231266-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x8de27c040) connecting device 91
default	20:30:56.231339-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x8de27c040) Device ID: 91 (Input:Yes | Output:No): true
default	20:30:56.232718-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1556, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:56.233973-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1556, subject=com.nexy.assistant,
default	20:30:56.234610-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87600 at /Applications/Nexy.app
default	20:30:56.247953-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x8de27c040) created ioproc 0xa for device 91
default	20:30:56.248054-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27c040) adding 7 device listeners to device 91
default	20:30:56.248213-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27c040) adding 0 device delegate listeners to device 91
default	20:30:56.248222-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x8de27c040)
default	20:30:56.248229-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	20:30:56.248238-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:30:56.248342-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:30:56.248351-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	20:30:56.248356-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:30:56.248434-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x8de27c040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:30:56.248442-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x8de27c040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:30:56.248447-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:30:56.248450-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27c040) removing 7 device listeners from device 85
default	20:30:56.248594-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27c040) removing 0 device delegate listeners from device 85
default	20:30:56.248600-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x8de27c040)
default	20:30:56.249141-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:30:56.250128-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1557, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:56.250997-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1557, subject=com.nexy.assistant,
default	20:30:56.251560-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87600 at /Applications/Nexy.app
default	20:30:56.263842-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:30:56.264781-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1558, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:56.265574-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1558, subject=com.nexy.assistant,
default	20:30:56.266124-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87600 at /Applications/Nexy.app
default	20:30:56.278804-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:30:56.280203-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1559, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:56.280975-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1559, subject=com.nexy.assistant,
default	20:30:56.281500-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87600 at /Applications/Nexy.app
default	20:30:56.293905-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:30:56.294059-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:30:56.294770-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:30:56.295044-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50506400] Created node ADM::com.nexy.assistant_8345.8241.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:30:56.295111-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50506400] Created node ADM::com.nexy.assistant_8345.8241.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:30:56.338047-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:30:56.339899-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:8345 called from <private>
default	20:30:56.339948-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:30:56.339998-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:30:56.341312-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8345 called from <private>
default	20:30:56.341487-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8345)
default	20:30:56.341506-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8345 called from <private>
default	20:30:56.341512-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8345 called from <private>
default	20:30:56.341763-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8344)
default	20:30:56.341777-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8344 called from <private>
default	20:30:56.342355-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] as candidate for concrete target as it is terminating
default	20:30:56.341900-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8344 called from <private>
fault	20:30:56.346607-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21676800.21676806 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21676800.21676806>
default	20:30:56.348689-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:30:56.349436-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:30:56.350733-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8345)
default	20:30:56.350754-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8345)
default	20:30:56.350764-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8345)
default	20:30:56.350776-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8345)
default	20:30:56.350773-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:8345 called from <private>
default	20:30:56.350792-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:8345 called from <private>
default	20:30:56.350801-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:8345 called from <private>
default	20:30:56.350807-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:8345 called from <private>
default	20:30:56.350840-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:8345 called from <private>
default	20:30:56.350881-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:8345 called from <private>
default	20:30:56.350902-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8345 called from <private>
default	20:30:56.350955-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8345 called from <private>
default	20:30:56.353033-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:8345 called from <private>
default	20:30:56.353044-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:8345 called from <private>
fault	20:30:56.352550-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21676800.21676806 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21676800.21676806>
default	20:30:56.356564-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8344)
default	20:30:56.357022-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5059","name":"Nexy(34055)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:30:56.357117-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:30:56.357168-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:30:56.357629-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1c5059, Nexy(34055), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:30:56.356973-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8344 called from <private>
default	20:30:56.356981-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8344 called from <private>
default	20:30:56.357775-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:56.357878-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:56.358124-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:30:56.358484-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:30:56.358525-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5059, Nexy(34055), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 90 starting recording
default	20:30:56.359363-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:56.359544-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:56.359584-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:30:56.357136-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8345)
default	20:30:56.357155-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8345 called from <private>
default	20:30:56.359652-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5059, Nexy(34055), 'prim'', displayID:'com.nexy.assistant'}
default	20:30:56.358063-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:56.359829-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:30:56.358989-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1560, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:56.359841-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:30:56.359777-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:30:56.359818-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:56.362380-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1560, subject=com.nexy.assistant,
default	20:30:56.363444-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87600 at /Applications/Nexy.app
default	20:30:56.369199-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:8344 called from <private>
default	20:30:56.369214-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:8344 called from <private>
default	20:30:56.369323-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8344)
default	20:30:56.379456-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8344)
default	20:30:56.379667-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:8344 called from <private>
default	20:30:56.379704-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:8344 called from <private>
default	20:30:56.379767-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8344)
default	20:30:56.386173-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:56.386879-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8344 called from <private>
default	20:30:56.390199-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:56.390221-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	20:30:56.390322-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:30:56.403393-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:8345 called from <private>
default	20:30:56.403419-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:8345 called from <private>
default	20:30:56.412473-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1561, subject=com.nexy.assistant,
default	20:30:56.413765-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87600 at /Applications/Nexy.app
default	20:30:56.430811-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:30:56.432548-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50506400] Created node ADM::com.nexy.assistant_8345.8241.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:30:56.432611-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50506400] Created node ADM::com.nexy.assistant_8345.8241.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:30:56.471146-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:30:56.474765-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:8345 called from <private>
default	20:30:56.474817-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:8345 called from <private>
default	20:30:56.473480-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] as candidate for concrete target as it is terminating
default	20:30:56.475049-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:30:56.476677-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8345 called from <private>
default	20:30:56.476816-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8345)
default	20:30:56.476839-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8345 called from <private>
default	20:30:56.476846-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8345 called from <private>
default	20:30:56.477608-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:30:56.477751-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:30:56.478161-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8345)
default	20:30:56.478332-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:8345 called from <private>
default	20:30:56.478343-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:8345 called from <private>
default	20:30:56.478357-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8345 called from <private>
default	20:30:56.480032-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1562, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:30:56.481268-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1562, subject=com.nexy.assistant,
default	20:30:56.482151-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc1ee87600 at /Applications/Nexy.app
default	20:30:56.484534-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:30:56.484601-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:30:56.484659-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:30:56.484852-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:30:56.485544-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.485574-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.485589-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:56.485596-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.485605-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:56.485615-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:56.485932-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:30:56.500235-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:8345 called from <private>
default	20:30:56.500474-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] as candidate for concrete target as it is terminating
default	20:30:56.509613-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:30:56.509659-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:30:56.509704-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:30:56.510358-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.510369-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.510412-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:56.510432-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.510467-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:56.510535-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:56.510576-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.510624-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.510677-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:56.510720-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.510792-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:30:56.510813-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:56.510859-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:56.511097-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.511105-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.511111-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:56.511126-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:56.511193-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:56.511221-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:30:56.511224-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:57.525764-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:30:57.526170-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5059","name":"Nexy(34055)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:30:57.526309-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:57.526371-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:30:57.526403-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5059, Nexy(34055), 'prim'', displayID:'com.nexy.assistant'}
default	20:30:57.526469-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:30:57.526469-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5059, Nexy(34055), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 90 stopping recording
default	20:30:57.526495-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:30:57.526521-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:30:57.526549-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:30:57.526655-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:30:57.526667-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:30:57.526783-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x218B0001 category Not set
default	20:30:57.529604-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:57.529663-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:57.529720-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:57.529751-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:30:57.529768-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:57.529786-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:30:57.529863-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:30:57.529875-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:30:57.529890-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:30:57.532044-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:30:57.534286-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:57.534297-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:57.534316-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:57.534333-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:57.534341-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:57.534348-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:57.534460-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:30:57.628004-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x8de27c040) Selecting device 0 from destructor
default	20:30:57.628030-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x8de27c040)
default	20:30:57.628040-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x8de27c040) not already running
default	20:30:57.628046-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x8de27c040) disconnecting device 91
default	20:30:57.628066-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x8de27c040) destroying ioproc 0xa for device 91
default	20:30:57.628124-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:30:57.628173-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:30:57.628382-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x8de27c040) nothing to setup
default	20:30:57.628400-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27c040) adding 0 device listeners to device 0
default	20:30:57.628411-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27c040) adding 0 device delegate listeners to device 0
default	20:30:57.628418-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27c040) removing 7 device listeners from device 91
default	20:30:57.628706-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27c040) removing 0 device delegate listeners from device 91
default	20:30:57.628725-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x8de27c040)
default	20:30:57.765007-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34068.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=34068, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:30:57.766453-0500	tccd	AUTHREQ_SUBJECT: msgID=34068.1, subject=com.nexy.assistant,
default	20:30:57.767070-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977c00 at /Applications/Nexy.app
default	20:30:57.782149-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2766, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=34068, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:30:57.783023-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2766, subject=com.nexy.assistant,
default	20:30:57.783581-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977c00 at /Applications/Nexy.app
default	20:30:57.827707-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977900 at /Applications/Nexy.app
default	20:30:57.846693-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 33579: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b9860100 c86c0400 };
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
default	20:30:57.860784-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:30:58.779654-0500	Nexy	[0x8deeed400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:30:58.780345-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:30:58.780530-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34055.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:30:58.781805-0500	tccd	AUTHREQ_SUBJECT: msgID=34055.3, subject=com.nexy.assistant,
default	20:30:58.782478-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977300 at /Applications/Nexy.app
default	20:30:58.795816-0500	Nexy	[0x8deeed400] invalidated after the last release of the connection object
default	20:30:58.795938-0500	Nexy	[0x8deeed400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:30:58.796370-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:30:58.796547-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34055.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:30:58.797872-0500	tccd	AUTHREQ_SUBJECT: msgID=34055.4, subject=com.nexy.assistant,
default	20:30:58.798969-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977300 at /Applications/Nexy.app
default	20:30:58.811942-0500	Nexy	[0x8deeed400] invalidated after the last release of the connection object
default	20:30:58.812015-0500	Nexy	[0x8deeed400] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	20:30:58.812113-0500	Nexy	[0x8deeed400] invalidated after the last release of the connection object
default	20:30:58.812892-0500	Nexy	server port 0x00010d0f, session port 0x00003713
default	20:30:58.817744-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 33028746-6868-4450-A4A8-593A103C5EBA flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51362,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x248dcade tp_proto=0x06"
default	20:30:58.817832-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51362<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002227 t_state: SYN_SENT process: Nexy:34055 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x88381839
default	20:30:58.818546-0500	kernel	tcp connected: [<IPv4-redacted>:51362<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002227 t_state: ESTABLISHED process: Nexy:34055 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x88381839
default	20:30:58.819004-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:51362<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002227 t_state: FIN_WAIT_1 process: Nexy:34055 Duration: 0.002 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x88381839
default	20:30:58.819015-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51362<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002227 t_state: FIN_WAIT_1 process: Nexy:34055 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:30:58.832755-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:30:58.832742-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3B387E33-2520-4AB0-ADDB-6D9E0D119EC1 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51363,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x9b6e3086 tp_proto=0x06"
default	20:30:58.832943-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:30:58.832806-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51363<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002228 t_state: SYN_SENT process: Nexy:34055 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9cd028ab
default	20:30:58.833327-0500	kernel	tcp connected: [<IPv4-redacted>:51363<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002228 t_state: ESTABLISHED process: Nexy:34055 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9cd028ab
default	20:30:58.833555-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:51363<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002228 t_state: FIN_WAIT_1 process: Nexy:34055 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x9cd028ab
default	20:30:58.833570-0500	kernel	tcp_connection_summary [<IPv4-redacted>:51363<-><IPv4-redacted>:53] interface: utun6 (skipped: 714)
so_gencnt: 1002228 t_state: FIN_WAIT_1 process: Nexy:34055 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:30:58.833890-0500	Nexy	nw_path_libinfo_path_check [9DFCD907-E51D-42FA-853E-03D37F6C317F IPv4#700ed863:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:30:58.834383-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3EB3A429-0416-4FDE-9875-D0792F8798D5 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51364,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x808a38f9 tp_proto=0x06"
default	20:30:58.834403-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51364<-><IPv4-redacted>:443] interface: utun6 (skipped: 714)
so_gencnt: 1002229 t_state: SYN_SENT process: Nexy:34055 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x85835975
default	20:30:58.834779-0500	kernel	tcp connected: [<IPv4-redacted>:51364<-><IPv4-redacted>:443] interface: utun6 (skipped: 714)
so_gencnt: 1002229 t_state: ESTABLISHED process: Nexy:34055 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x85835975
default	20:30:59.253164-0500	Nexy	[0x8deeed540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:30:59.253979-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34055.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:30:59.261106-0500	tccd	AUTHREQ_SUBJECT: msgID=34055.5, subject=com.nexy.assistant,
default	20:30:59.261742-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f975500 at /Applications/Nexy.app
default	20:30:59.274861-0500	Nexy	[0x8deeed540] invalidated after the last release of the connection object
default	20:30:59.625477-0500	kernel	udp connect: [<IPv4-redacted>:55956<-><IPv4-redacted>:443] interface:  (skipped: 519)
so_gencnt: 1002241 so_state: 0x0002 process: Nexy:34055 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x884c4331
default	20:30:59.625503-0500	kernel	udp_connection_summary [<IPv4-redacted>:55956<-><IPv4-redacted>:443] interface:  (skipped: 519)
so_gencnt: 1002241 so_state: 0x0002 process: Nexy:34055 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x884c4331 flowctl: 0us (0x)
default	20:30:59.627130-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid C6A982A0-2F8F-4AF2-80A7-0A3B60F38250 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.51366,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x46128c66 tp_proto=0x06"
default	20:30:59.627191-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:51366<-><IPv4-redacted>:443] interface: utun6 (skipped: 714)
so_gencnt: 1002243 t_state: SYN_SENT process: Nexy:34055 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb54c99a3
default	20:30:59.627855-0500	kernel	tcp connected: [<IPv4-redacted>:51366<-><IPv4-redacted>:443] interface: utun6 (skipped: 714)
so_gencnt: 1002243 t_state: ESTABLISHED process: Nexy:34055 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb54c99a3
default	20:30:59.678805-0500	Nexy	[0x8deeed7c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:30:59.679476-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34055.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:30:59.680561-0500	tccd	AUTHREQ_SUBJECT: msgID=34055.6, subject=com.nexy.assistant,
default	20:30:59.681202-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976d00 at /Applications/Nexy.app
default	20:30:59.694399-0500	Nexy	[0x8deeed7c0] invalidated after the last release of the connection object
default	20:30:59.694493-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:30:59.694884-0500	Nexy	[0x8deeed7c0] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	20:30:59.694993-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	20:30:59.696171-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	20:30:59.698750-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=23272.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=23272, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:30:59.698779-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=23272, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:30:59.699645-0500	tccd	AUTHREQ_SUBJECT: msgID=23272.3, subject=com.nexy.assistant,
default	20:30:59.699702-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34074.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=34074, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:30:59.700361-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976d00 at /Applications/Nexy.app
default	20:30:59.701112-0500	tccd	AUTHREQ_SUBJECT: msgID=34074.1, subject=com.nexy.assistant,
default	20:30:59.701812-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976400 at /Applications/Nexy.app
default	20:30:59.716635-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2767, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=34074, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:30:59.717529-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2767, subject=com.nexy.assistant,
default	20:30:59.718100-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976400 at /Applications/Nexy.app
default	20:30:59.731292-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2768, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:30:59.731314-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:30:59.732100-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2768, subject=com.nexy.assistant,
default	20:30:59.732656-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976400 at /Applications/Nexy.app
default	20:30:59.752798-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8344)
default	20:30:59.752835-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8344 called from <private>
default	20:30:59.752842-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8344 called from <private>
default	20:30:59.753328-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8345)
default	20:30:59.753341-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8345 called from <private>
default	20:30:59.753346-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8345 called from <private>
default	20:30:59.755455-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	20:30:59.764467-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8345)
default	20:30:59.764491-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8345 called from <private>
default	20:30:59.764497-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:8345 called from <private>
default	20:30:59.765674-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8344 called from <private>
default	20:30:59.765682-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8344 called from <private>
default	20:30:59.767255-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8344)
default	20:30:59.776330-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:8344 called from <private>
default	20:30:59.776345-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:8344 called from <private>
default	20:30:59.776444-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8344)
default	20:30:59.781066-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8344)
default	20:30:59.781240-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:8344 called from <private>
default	20:30:59.781249-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:8344 called from <private>
default	20:30:59.781327-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8344)
default	20:30:59.787489-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(8344)
default	20:30:59.787619-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:8344 called from <private>
default	20:30:59.787627-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:8344 called from <private>
default	20:30:59.787653-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8344 called from <private>
default	20:30:59.787659-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:8344 called from <private>
default	20:30:59.787667-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8344 called from <private>
default	20:30:59.787672-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8344 called from <private>
default	20:30:59.787677-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8344 called from <private>
default	20:30:59.787698-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:8344 called from <private>
default	20:30:59.787739-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8344 called from <private>
default	20:30:59.787806-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8344 called from <private>
default	20:30:59.787872-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:8344 called from <private>
default	20:30:59.787940-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:8344 called from <private>
default	20:30:59.788003-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:8344 called from <private>
default	20:30:59.788048-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:8344 called from <private>
default	20:30:59.788201-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(8344)
default	20:30:59.788214-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:8344 called from <private>
default	20:30:59.788219-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:8344 called from <private>
default	20:30:59.814918-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974000 at /Applications/Nexy.app
default	20:30:59.826411-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:30:59.826471-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:30:59.826505-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:30:59.827323-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:59.827334-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:59.827347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:59.827362-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:30:59.827369-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:30:59.827375-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:30:59.827457-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:30:59.845118-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:31:00.184614-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x8de27d540) Selecting device 85 from constructor
default	20:31:00.184633-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x8de27d540)
default	20:31:00.184642-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x8de27d540) not already running
default	20:31:00.184647-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x8de27d540) nothing to teardown
default	20:31:00.184650-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x8de27d540) connecting device 85
default	20:31:00.184757-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x8de27d540) Device ID: 85 (Input:No | Output:Yes): true
default	20:31:00.184875-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x8de27d540) created ioproc 0xb for device 85
default	20:31:00.185008-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27d540) adding 7 device listeners to device 85
default	20:31:00.185221-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27d540) adding 0 device delegate listeners to device 85
default	20:31:00.185235-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x8de27d540)
default	20:31:00.185333-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:31:00.185352-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	20:31:00.185362-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:31:00.185369-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	20:31:00.185379-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:31:00.185492-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x8de27d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:31:00.185508-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x8de27d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:31:00.185513-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:31:00.185519-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27d540) removing 0 device listeners from device 0
default	20:31:00.185524-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27d540) removing 0 device delegate listeners from device 0
default	20:31:00.185529-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x8de27d540)
default	20:31:00.185542-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x8de27d540) caller requesting device change from 85 to 85
default	20:31:00.185545-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x8de27d540)
default	20:31:00.185550-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x8de27d540) exiting with nothing to do
default	20:31:00.186005-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:31:00.186505-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:31:00.189201-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x8de27d540) Selecting device 0 from destructor
default	20:31:00.189214-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x8de27d540)
default	20:31:00.189222-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x8de27d540) not already running
default	20:31:00.189227-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x8de27d540) disconnecting device 85
default	20:31:00.189234-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x8de27d540) destroying ioproc 0xb for device 85
default	20:31:00.189265-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	20:31:00.189299-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:31:00.189439-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x8de27d540) nothing to setup
default	20:31:00.189452-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27d540) adding 0 device listeners to device 0
default	20:31:00.189459-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27d540) adding 0 device delegate listeners to device 0
default	20:31:00.189465-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27d540) removing 7 device listeners from device 85
default	20:31:00.189685-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27d540) removing 0 device delegate listeners from device 85
default	20:31:00.189697-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x8de27d540)
default	20:31:00.191080-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x8de27d540) Selecting device 85 from constructor
default	20:31:00.191096-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x8de27d540)
default	20:31:00.191102-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x8de27d540) not already running
default	20:31:00.191107-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x8de27d540) nothing to teardown
default	20:31:00.191112-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x8de27d540) connecting device 85
default	20:31:00.191219-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x8de27d540) Device ID: 85 (Input:No | Output:Yes): true
default	20:31:00.191338-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x8de27d540) created ioproc 0xc for device 85
default	20:31:00.191464-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27d540) adding 7 device listeners to device 85
default	20:31:00.191672-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8de27d540) adding 0 device delegate listeners to device 85
default	20:31:00.191685-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x8de27d540)
default	20:31:00.191772-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:31:00.191788-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	20:31:00.191796-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:31:00.191802-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	20:31:00.191812-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:31:00.191916-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x8de27d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:31:00.191931-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x8de27d540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:31:00.191937-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	20:31:00.191943-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27d540) removing 0 device listeners from device 0
default	20:31:00.191947-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8de27d540) removing 0 device delegate listeners from device 0
default	20:31:00.191951-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x8de27d540)
default	20:31:00.191962-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x8de27d540) caller requesting device change from 85 to 85
default	20:31:00.191967-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x8de27d540)
default	20:31:00.191972-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x8de27d540) exiting with nothing to do
default	20:31:00.191978-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	20:31:00.192373-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:31:00.192707-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:31:00.195715-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] as candidate for concrete target as it is terminating
default	20:31:00.257381-0500	Nexy	[0x8deeedb80] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	20:31:00.270728-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	20:31:00.275897-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2400000020 pid: 34055
default	20:31:00.291704-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x8deddc780
 (
    "<NSDarkAquaAppearance: 0x8deddc6e0>",
    "<NSSystemAppearance: 0x8deddc640>"
)>
default	20:31:00.294749-0500	Nexy	[0x8deeee080] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	20:31:00.296320-0500	Nexy	[0x8deeee1c0] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	20:31:00.299237-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	20:31:00.299595-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	20:31:00.299606-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	20:31:00.299648-0500	Nexy	[0x8deeee300] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	20:31:00.299666-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	20:31:00.299743-0500	Nexy	[0x8deeee440] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:31:00.299818-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:00.300626-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:00.300740-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	20:31:00.301629-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> attempting immediate handshake from activate
default	20:31:00.301691-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> sent handshake
default	20:31:00.301822-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	20:31:00.302587-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> was invalidated
default	20:31:00.302598-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	20:31:00.302603-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:31:00.304342-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	20:31:00.305519-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	20:31:00.306186-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0820; com.apple.controlcenter:A287528E-D1B5-4FC2-BF22-5876096B761B> from com.apple.controlcenter.statusitems
error	20:31:00.306462-0500	Nexy	Error creating <FBSScene: 0x8dd0c0820; com.apple.controlcenter:A287528E-D1B5-4FC2-BF22-5876096B761B>: <NSError: 0x8defe4930; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	20:31:00.306531-0500	Nexy	Request for <FBSScene: 0x8dd0c0820; com.apple.controlcenter:A287528E-D1B5-4FC2-BF22-5876096B761B> complete!
default	20:31:00.313683-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	20:31:00.333642-0500	Nexy	Registering for test daemon availability notify post.
default	20:31:00.333815-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:31:00.333915-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:31:00.334011-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:31:00.338150-0500	Nexy	[0x8deeee800] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	20:31:00.338881-0500	Nexy	[0x8deeec3c0] Connection returned listener port: 0x5003
default	20:31:00.339287-0500	Nexy	SignalReady: pid=34055 asn=0x0-0x501501
default	20:31:00.339705-0500	Nexy	SIGNAL: pid=34055 asn=0x0x-0x501501
default	20:31:00.340317-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:31:00.343405-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976d00 at /Applications/Nexy.app
error	20:31:00.349220-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
default	20:31:00.358942-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:31:00.358951-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	20:31:00.358987-0500	Nexy	[0x8deeed680] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	20:31:00.359103-0500	Nexy	[0x8deeed680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:31:00.360078-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:31:00.363029-0500	Nexy	[C:2] Alloc <private>
default	20:31:00.363082-0500	Nexy	[0x8deeed680] activating connection: mach=false listener=false peer=false name=(anonymous)
error	20:31:00.363328-0500	kernel	Sandbox: WindowManager(580) deny(1) mach-task-name others [Nexy(34055)]
default	20:31:00.364341-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] as candidate for concrete target as it is terminating
default	20:31:00.364387-0500	runningboardd	Acquiring assertion targeting 34055 from originator [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-34055-201053 target:34055 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	20:31:00.364681-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 34055 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 34055 does not exist}>
error	20:31:00.364698-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 34055 with code: 2 - RBSAssertionErrorDomain
default	20:31:00.364846-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] as candidate for concrete target as it is terminating
default	20:31:00.364876-0500	runningboardd	Acquiring assertion targeting 34055 from originator [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-34055-201054 target:34055 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	20:31:00.364995-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 34055 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 34055 does not exist}>
error	20:31:00.365010-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 34055 with code: 2 - RBSAssertionErrorDomain
default	20:31:00.365111-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] as candidate for concrete target as it is terminating
default	20:31:00.365130-0500	runningboardd	Acquiring assertion targeting 34055 from originator [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-34055-201055 target:34055 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	20:31:00.365225-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 34055 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 34055 does not exist}>
error	20:31:00.365235-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 34055 with code: 2 - RBSAssertionErrorDomain
default	20:31:00.365329-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] as candidate for concrete target as it is terminating
default	20:31:00.365353-0500	runningboardd	Acquiring assertion targeting 34055 from originator [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-34055-201056 target:34055 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	20:31:00.365432-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 34055 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 34055 does not exist}>
error	20:31:00.365441-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 34055 with code: 2 - RBSAssertionErrorDomain
default	20:31:00.365479-0500	WindowManager	Connection activated | (34055) Nexy
default	20:31:00.365561-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] as candidate for concrete target as it is terminating
default	20:31:00.365583-0500	runningboardd	Acquiring assertion targeting 34055 from originator [app<application.com.nexy.assistant.21676800.21676806(501)>:34055] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-34055-201057 target:34055 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	20:31:00.365664-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 34055 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 34055 does not exist}>
error	20:31:00.365675-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 34055 with code: 2 - RBSAssertionErrorDomain
default	20:31:00.457909-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	20:31:00.462507-0500	Nexy	Start service name com.apple.spotlightknowledged
default	20:31:00.463524-0500	Nexy	[GMS] availability notification token 76
default	20:31:00.489269-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	20:31:00.490081-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5059","name":"Nexy(34055)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:31:00.490190-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:31:00.490223-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1c5059, Nexy(34055), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:31:00.490258-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:31:00.490314-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1c5059, Nexy(34055), 'prim'', AudioCategory changed to 'MediaPlayback'
default	20:31:00.490361-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:31:00.490366-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:31:00.490377-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 90 starting playing
default	20:31:00.490449-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:31:00.490497-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:31:00.490530-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5059, Nexy(34055), 'prim'', displayID:'com.nexy.assistant'}
default	20:31:00.490556-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	20:31:00.490550-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:31:00.490592-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:31:00.490605-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:31:00.490624-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1c5059 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":34055}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1c5059, sessionType: 'prim', isRecording: false }, 
]
default	20:31:00.490690-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:31:00.490704-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:31:00.490807-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x218B0001 category Not set
default	20:31:00.491760-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:31:00.491837-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:31:00.491863-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:31:00.491879-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	20:31:00.491889-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	20:31:00.491899-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	20:31:00.491944-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	20:31:01.350851-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:01.350924-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:01.351073-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0d20 <private>> attempting immediate handshake from activate
default	20:31:01.351149-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0d20 <private>> sent handshake
default	20:31:01.351777-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:BE0D3C32-2973-4FD9-BD59-11376C523F44> from com.apple.controlcenter.statusitems
default	20:31:01.352339-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0d20 <private>> was invalidated
default	20:31:01.352437-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:31:01.352602-0500	Nexy	Request for <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:BE0D3C32-2973-4FD9-BD59-11376C523F44> complete!
error	20:31:01.352612-0500	Nexy	Error creating <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:BE0D3C32-2973-4FD9-BD59-11376C523F44>: <NSError: 0x8dec039f0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:01.352703-0500	Nexy	No scene exists for identity: com.apple.controlcenter:BE0D3C32-2973-4FD9-BD59-11376C523F44
default	20:31:01.352848-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	20:31:01.355618-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:01.355643-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:01.355710-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> attempting immediate handshake from activate
default	20:31:01.355735-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> sent handshake
default	20:31:01.355830-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	20:31:01.356353-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	20:31:01.356384-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> was invalidated
default	20:31:01.356398-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:31:01.356772-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	20:31:01.356826-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	20:31:01.357258-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0780; com.apple.controlcenter:BE0D3C32-2973-4FD9-BD59-11376C523F44-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	20:31:01.357460-0500	Nexy	Error creating <FBSScene: 0x8dd0c0780; com.apple.controlcenter:BE0D3C32-2973-4FD9-BD59-11376C523F44-Aux[1]-NSStatusItemView>: <NSError: 0x8dec03c60; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	20:31:01.357515-0500	Nexy	Request for <FBSScene: 0x8dd0c0780; com.apple.controlcenter:BE0D3C32-2973-4FD9-BD59-11376C523F44-Aux[1]-NSStatusItemView> complete!
error	20:31:01.357882-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:01.357904-0500	Nexy	[com.apple.controlcenter:BE0D3C32-2973-4FD9-BD59-11376C523F44] No matching scene to invalidate for this identity.
error	20:31:01.357937-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:01.357985-0500	Nexy	Unhandled disconnected scene <private>
error	20:31:01.358093-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:31:02.359266-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:02.359302-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:02.359395-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> attempting immediate handshake from activate
default	20:31:02.359426-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> sent handshake
default	20:31:02.359759-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:C47D245C-AB5F-481C-A7B3-86C3A8D39DAD> from com.apple.controlcenter.statusitems
default	20:31:02.360080-0500	Nexy	Request for <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:C47D245C-AB5F-481C-A7B3-86C3A8D39DAD> complete!
default	20:31:02.360306-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> was invalidated
default	20:31:02.360335-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:31:02.360402-0500	Nexy	Error creating <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:C47D245C-AB5F-481C-A7B3-86C3A8D39DAD>: <NSError: 0x8dec03840; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:02.360423-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C47D245C-AB5F-481C-A7B3-86C3A8D39DAD
default	20:31:02.360460-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:02.360479-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:02.360527-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0d20 <private>> attempting immediate handshake from activate
default	20:31:02.360558-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0d20 <private>> sent handshake
default	20:31:02.360716-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:C47D245C-AB5F-481C-A7B3-86C3A8D39DAD-Aux[2]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:31:02.361004-0500	Nexy	Request for <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:C47D245C-AB5F-481C-A7B3-86C3A8D39DAD-Aux[2]-NSStatusItemView> complete!
default	20:31:02.361042-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0d20 <private>> was invalidated
default	20:31:02.361063-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:31:02.361114-0500	Nexy	Error creating <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:C47D245C-AB5F-481C-A7B3-86C3A8D39DAD-Aux[2]-NSStatusItemView>: <NSError: 0x8dec03930; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:02.361131-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C47D245C-AB5F-481C-A7B3-86C3A8D39DAD-Aux[2]-NSStatusItemView
default	20:31:02.361907-0500	Nexy	[com.apple.controlcenter:C47D245C-AB5F-481C-A7B3-86C3A8D39DAD-Aux[2]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	20:31:02.362262-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:02.362283-0500	Nexy	[com.apple.controlcenter:C47D245C-AB5F-481C-A7B3-86C3A8D39DAD] No matching scene to invalidate for this identity.
error	20:31:02.362314-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:02.362332-0500	Nexy	[com.apple.controlcenter:C47D245C-AB5F-481C-A7B3-86C3A8D39DAD-Aux[2]-NSStatusItemView] No matching scene to invalidate for this identity.
error	20:31:02.362785-0500	Nexy	Unhandled disconnected scene <private>
error	20:31:02.362884-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	20:31:02.362971-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	20:31:02.363012-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:31:02.363043-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	20:31:03.363341-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:03.363383-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:03.363481-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> attempting immediate handshake from activate
default	20:31:03.363513-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> sent handshake
default	20:31:03.363852-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:3CE1B0A6-79CB-41FD-9CA2-29E77A8C8823> from com.apple.controlcenter.statusitems
default	20:31:03.364156-0500	Nexy	Request for <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:3CE1B0A6-79CB-41FD-9CA2-29E77A8C8823> complete!
default	20:31:03.364499-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> was invalidated
default	20:31:03.364533-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:31:03.364587-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:03.364607-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:03.364655-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1220 <private>> attempting immediate handshake from activate
default	20:31:03.364677-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1220 <private>> sent handshake
error	20:31:03.364747-0500	Nexy	Error creating <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:3CE1B0A6-79CB-41FD-9CA2-29E77A8C8823>: <NSError: 0x8dec03c60; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:03.364768-0500	Nexy	No scene exists for identity: com.apple.controlcenter:3CE1B0A6-79CB-41FD-9CA2-29E77A8C8823
default	20:31:03.364844-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0780; com.apple.controlcenter:3CE1B0A6-79CB-41FD-9CA2-29E77A8C8823-Aux[3]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:31:03.365051-0500	Nexy	Request for <FBSScene: 0x8dd0c0780; com.apple.controlcenter:3CE1B0A6-79CB-41FD-9CA2-29E77A8C8823-Aux[3]-NSStatusItemView> complete!
default	20:31:03.365226-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1220 <private>> was invalidated
default	20:31:03.365271-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:31:03.365335-0500	Nexy	Error creating <FBSScene: 0x8dd0c0780; com.apple.controlcenter:3CE1B0A6-79CB-41FD-9CA2-29E77A8C8823-Aux[3]-NSStatusItemView>: <NSError: 0x8dec03ba0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:03.365354-0500	Nexy	No scene exists for identity: com.apple.controlcenter:3CE1B0A6-79CB-41FD-9CA2-29E77A8C8823-Aux[3]-NSStatusItemView
default	20:31:03.365655-0500	Nexy	[com.apple.controlcenter:3CE1B0A6-79CB-41FD-9CA2-29E77A8C8823-Aux[3]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	20:31:03.365917-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:03.365936-0500	Nexy	[com.apple.controlcenter:3CE1B0A6-79CB-41FD-9CA2-29E77A8C8823] No matching scene to invalidate for this identity.
error	20:31:03.365967-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:03.365986-0500	Nexy	[com.apple.controlcenter:3CE1B0A6-79CB-41FD-9CA2-29E77A8C8823-Aux[3]-NSStatusItemView] No matching scene to invalidate for this identity.
error	20:31:03.366503-0500	Nexy	Unhandled disconnected scene <private>
error	20:31:03.366590-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	20:31:03.366662-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	20:31:03.366698-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:31:04.367597-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:04.367655-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:04.367801-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> attempting immediate handshake from activate
default	20:31:04.367851-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> sent handshake
default	20:31:04.368324-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:9A936F5F-707C-4A35-9375-CBC277EB9D72> from com.apple.controlcenter.statusitems
default	20:31:04.368737-0500	Nexy	Request for <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:9A936F5F-707C-4A35-9375-CBC277EB9D72> complete!
default	20:31:04.369285-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> was invalidated
default	20:31:04.369323-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:31:04.369379-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:04.369401-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:04.369462-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1220 <private>> attempting immediate handshake from activate
default	20:31:04.369488-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1220 <private>> sent handshake
error	20:31:04.369561-0500	Nexy	Error creating <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:9A936F5F-707C-4A35-9375-CBC277EB9D72>: <NSError: 0x8dec03b10; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:04.369586-0500	Nexy	No scene exists for identity: com.apple.controlcenter:9A936F5F-707C-4A35-9375-CBC277EB9D72
default	20:31:04.369657-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:9A936F5F-707C-4A35-9375-CBC277EB9D72-Aux[4]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:31:04.369869-0500	Nexy	Request for <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:9A936F5F-707C-4A35-9375-CBC277EB9D72-Aux[4]-NSStatusItemView> complete!
default	20:31:04.370042-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1220 <private>> was invalidated
default	20:31:04.370080-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:31:04.370145-0500	Nexy	Error creating <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:9A936F5F-707C-4A35-9375-CBC277EB9D72-Aux[4]-NSStatusItemView>: <NSError: 0x8dec038d0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:04.370167-0500	Nexy	No scene exists for identity: com.apple.controlcenter:9A936F5F-707C-4A35-9375-CBC277EB9D72-Aux[4]-NSStatusItemView
default	20:31:04.370440-0500	Nexy	[com.apple.controlcenter:9A936F5F-707C-4A35-9375-CBC277EB9D72-Aux[4]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	20:31:04.370682-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:04.370706-0500	Nexy	[com.apple.controlcenter:9A936F5F-707C-4A35-9375-CBC277EB9D72] No matching scene to invalidate for this identity.
error	20:31:04.370738-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:04.370757-0500	Nexy	[com.apple.controlcenter:9A936F5F-707C-4A35-9375-CBC277EB9D72-Aux[4]-NSStatusItemView] No matching scene to invalidate for this identity.
error	20:31:04.371225-0500	Nexy	Unhandled disconnected scene <private>
error	20:31:04.371309-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	20:31:04.371377-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	20:31:04.371417-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:31:05.278064-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	20:31:05.335654-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	20:31:05.372323-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:05.372385-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:05.372525-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> attempting immediate handshake from activate
default	20:31:05.372579-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> sent handshake
default	20:31:05.373056-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:A7616002-E7A5-4C63-ACB9-58601F128DB2> from com.apple.controlcenter.statusitems
default	20:31:05.373481-0500	Nexy	Request for <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:A7616002-E7A5-4C63-ACB9-58601F128DB2> complete!
default	20:31:05.374027-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> was invalidated
default	20:31:05.374080-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:31:05.374170-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:05.374206-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:05.374296-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1220 <private>> attempting immediate handshake from activate
default	20:31:05.374336-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1220 <private>> sent handshake
error	20:31:05.374450-0500	Nexy	Error creating <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:A7616002-E7A5-4C63-ACB9-58601F128DB2>: <NSError: 0x8dec03660; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:05.374489-0500	Nexy	No scene exists for identity: com.apple.controlcenter:A7616002-E7A5-4C63-ACB9-58601F128DB2
default	20:31:05.374613-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0780; com.apple.controlcenter:A7616002-E7A5-4C63-ACB9-58601F128DB2-Aux[5]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:31:05.374953-0500	Nexy	Request for <FBSScene: 0x8dd0c0780; com.apple.controlcenter:A7616002-E7A5-4C63-ACB9-58601F128DB2-Aux[5]-NSStatusItemView> complete!
default	20:31:05.375284-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1220 <private>> was invalidated
default	20:31:05.375334-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:31:05.375442-0500	Nexy	Error creating <FBSScene: 0x8dd0c0780; com.apple.controlcenter:A7616002-E7A5-4C63-ACB9-58601F128DB2-Aux[5]-NSStatusItemView>: <NSError: 0x8dec03ba0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:05.375478-0500	Nexy	No scene exists for identity: com.apple.controlcenter:A7616002-E7A5-4C63-ACB9-58601F128DB2-Aux[5]-NSStatusItemView
default	20:31:05.375727-0500	Nexy	[com.apple.controlcenter:A7616002-E7A5-4C63-ACB9-58601F128DB2-Aux[5]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	20:31:05.376041-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:05.376064-0500	Nexy	[com.apple.controlcenter:A7616002-E7A5-4C63-ACB9-58601F128DB2] No matching scene to invalidate for this identity.
error	20:31:05.376096-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:05.376113-0500	Nexy	[com.apple.controlcenter:A7616002-E7A5-4C63-ACB9-58601F128DB2-Aux[5]-NSStatusItemView] No matching scene to invalidate for this identity.
error	20:31:05.376570-0500	Nexy	Unhandled disconnected scene <private>
error	20:31:05.376667-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	20:31:05.376732-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	20:31:05.376770-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:31:05.885411-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	20:31:05.885886-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5059","name":"Nexy(34055)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:31:05.886055-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 90 stopping playing
default	20:31:05.886142-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:31:05.886219-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:31:05.886344-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 90, PID = 34055, Name = sid:0x1c5059, Nexy(34055), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:31:05.886491-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:31:05.886579-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1c5059 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":34055}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1c5059, sessionType: 'prim', isRecording: false }, 
]
default	20:31:05.886720-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:31:05.886745-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:31:05.886761-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:31:05.886854-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:31:05.886898-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:31:06.101084-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=34075.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=34075, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:31:06.102365-0500	tccd	AUTHREQ_SUBJECT: msgID=34075.1, subject=com.nexy.assistant,
default	20:31:06.102925-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974300 at /Applications/Nexy.app
default	20:31:06.119029-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2769, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=34055, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=34075, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:31:06.119867-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2769, subject=com.nexy.assistant,
default	20:31:06.120408-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974300 at /Applications/Nexy.app
default	20:31:06.153918-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976100 at /Applications/Nexy.app
default	20:31:06.171739-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 33579: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b9860100 d66c0400 };
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
default	20:31:06.183070-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:31:06.377198-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:06.377232-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:06.377329-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0f00 <private>> attempting immediate handshake from activate
default	20:31:06.377360-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0f00 <private>> sent handshake
default	20:31:06.377652-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:C2BBDC1F-17C5-4C9A-9708-7AD25D59F751> from com.apple.controlcenter.statusitems
default	20:31:06.377912-0500	Nexy	Request for <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:C2BBDC1F-17C5-4C9A-9708-7AD25D59F751> complete!
default	20:31:06.378241-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0f00 <private>> was invalidated
default	20:31:06.378269-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:31:06.378340-0500	Nexy	Error creating <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:C2BBDC1F-17C5-4C9A-9708-7AD25D59F751>: <NSError: 0x8dec03e40; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:06.378356-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C2BBDC1F-17C5-4C9A-9708-7AD25D59F751
default	20:31:06.378391-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0780; com.apple.controlcenter:C2BBDC1F-17C5-4C9A-9708-7AD25D59F751-Aux[6]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	20:31:06.378489-0500	Nexy	Error creating <FBSScene: 0x8dd0c0780; com.apple.controlcenter:C2BBDC1F-17C5-4C9A-9708-7AD25D59F751-Aux[6]-NSStatusItemView>: <NSError: 0x8dec03de0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	20:31:06.378526-0500	Nexy	Request for <FBSScene: 0x8dd0c0780; com.apple.controlcenter:C2BBDC1F-17C5-4C9A-9708-7AD25D59F751-Aux[6]-NSStatusItemView> complete!
error	20:31:06.378679-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:06.378695-0500	Nexy	[com.apple.controlcenter:C2BBDC1F-17C5-4C9A-9708-7AD25D59F751] No matching scene to invalidate for this identity.
error	20:31:06.378717-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:06.378740-0500	Nexy	Unhandled disconnected scene <private>
error	20:31:06.378803-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:31:07.379730-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:07.379765-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:07.379853-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> attempting immediate handshake from activate
default	20:31:07.379885-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> sent handshake
default	20:31:07.380171-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:72CA62F9-A793-42F7-A28F-96C478A208FA> from com.apple.controlcenter.statusitems
default	20:31:07.380414-0500	Nexy	Request for <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:72CA62F9-A793-42F7-A28F-96C478A208FA> complete!
default	20:31:07.380686-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> was invalidated
default	20:31:07.380711-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:31:07.380753-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:07.380768-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:07.380809-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1040 <private>> attempting immediate handshake from activate
default	20:31:07.380826-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1040 <private>> sent handshake
error	20:31:07.380881-0500	Nexy	Error creating <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:72CA62F9-A793-42F7-A28F-96C478A208FA>: <NSError: 0x8dec03870; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:07.380899-0500	Nexy	No scene exists for identity: com.apple.controlcenter:72CA62F9-A793-42F7-A28F-96C478A208FA
default	20:31:07.380964-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:72CA62F9-A793-42F7-A28F-96C478A208FA-Aux[7]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:31:07.381112-0500	Nexy	Request for <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:72CA62F9-A793-42F7-A28F-96C478A208FA-Aux[7]-NSStatusItemView> complete!
default	20:31:07.381259-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c1040 <private>> was invalidated
default	20:31:07.381280-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:31:07.381326-0500	Nexy	Error creating <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:72CA62F9-A793-42F7-A28F-96C478A208FA-Aux[7]-NSStatusItemView>: <NSError: 0x8dec03a80; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:07.381340-0500	Nexy	No scene exists for identity: com.apple.controlcenter:72CA62F9-A793-42F7-A28F-96C478A208FA-Aux[7]-NSStatusItemView
default	20:31:07.381583-0500	Nexy	[com.apple.controlcenter:72CA62F9-A793-42F7-A28F-96C478A208FA-Aux[7]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	20:31:07.381772-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:07.381791-0500	Nexy	[com.apple.controlcenter:72CA62F9-A793-42F7-A28F-96C478A208FA] No matching scene to invalidate for this identity.
error	20:31:07.381814-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:07.381824-0500	Nexy	[com.apple.controlcenter:72CA62F9-A793-42F7-A28F-96C478A208FA-Aux[7]-NSStatusItemView] No matching scene to invalidate for this identity.
error	20:31:07.382178-0500	Nexy	Unhandled disconnected scene <private>
error	20:31:07.382247-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	20:31:07.382296-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	20:31:07.382322-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:31:07.899790-0500	Nexy	NSApplication._react(to:) dock
default	20:31:07.899806-0500	Nexy	NSApplication._react(to:) reactions=83
default	20:31:08.383311-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:08.383363-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:08.383471-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> attempting immediate handshake from activate
default	20:31:08.383519-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> sent handshake
default	20:31:08.383898-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:CD1C4173-DDBD-4FBF-BC94-E4B51563B2B9> from com.apple.controlcenter.statusitems
default	20:31:08.384234-0500	Nexy	Request for <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:CD1C4173-DDBD-4FBF-BC94-E4B51563B2B9> complete!
default	20:31:08.384483-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c10e0 <private>> was invalidated
default	20:31:08.384535-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:31:08.384648-0500	Nexy	Error creating <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:CD1C4173-DDBD-4FBF-BC94-E4B51563B2B9>: <NSError: 0x8dec03c30; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:08.384685-0500	Nexy	No scene exists for identity: com.apple.controlcenter:CD1C4173-DDBD-4FBF-BC94-E4B51563B2B9
default	20:31:08.384752-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:08.384780-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:08.384867-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> attempting immediate handshake from activate
default	20:31:08.384905-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> sent handshake
default	20:31:08.385159-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0d20; com.apple.controlcenter:CD1C4173-DDBD-4FBF-BC94-E4B51563B2B9-Aux[8]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:31:08.385467-0500	Nexy	Request for <FBSScene: 0x8dd0c0d20; com.apple.controlcenter:CD1C4173-DDBD-4FBF-BC94-E4B51563B2B9-Aux[8]-NSStatusItemView> complete!
default	20:31:08.385726-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0780 <private>> was invalidated
default	20:31:08.385771-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:31:08.385869-0500	Nexy	Error creating <FBSScene: 0x8dd0c0d20; com.apple.controlcenter:CD1C4173-DDBD-4FBF-BC94-E4B51563B2B9-Aux[8]-NSStatusItemView>: <NSError: 0x8dec03f90; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:08.385899-0500	Nexy	No scene exists for identity: com.apple.controlcenter:CD1C4173-DDBD-4FBF-BC94-E4B51563B2B9-Aux[8]-NSStatusItemView
default	20:31:08.386137-0500	Nexy	[com.apple.controlcenter:CD1C4173-DDBD-4FBF-BC94-E4B51563B2B9-Aux[8]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	20:31:08.386432-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:08.386457-0500	Nexy	[com.apple.controlcenter:CD1C4173-DDBD-4FBF-BC94-E4B51563B2B9] No matching scene to invalidate for this identity.
error	20:31:08.386497-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:08.386516-0500	Nexy	[com.apple.controlcenter:CD1C4173-DDBD-4FBF-BC94-E4B51563B2B9-Aux[8]-NSStatusItemView] No matching scene to invalidate for this identity.
error	20:31:08.386972-0500	Nexy	Unhandled disconnected scene <private>
error	20:31:08.387068-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	20:31:08.387135-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	20:31:08.387182-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	20:31:09.387676-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:09.387723-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:09.387850-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0d20 <private>> attempting immediate handshake from activate
default	20:31:09.387891-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0d20 <private>> sent handshake
default	20:31:09.388273-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:0C72BA04-3B7A-4C4F-A138-923402CE6185> from com.apple.controlcenter.statusitems
default	20:31:09.388607-0500	Nexy	Request for <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:0C72BA04-3B7A-4C4F-A138-923402CE6185> complete!
default	20:31:09.389106-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0d20 <private>> was invalidated
default	20:31:09.389157-0500	Nexy	FBSWorkspace unregistering source: <private>
default	20:31:09.389245-0500	Nexy	FBSWorkspace registering source: <private>
default	20:31:09.389280-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:31:09.389369-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0f00 <private>> attempting immediate handshake from activate
default	20:31:09.389406-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0f00 <private>> sent handshake
error	20:31:09.389512-0500	Nexy	Error creating <FBSScene: 0x8dd0c0dc0; com.apple.controlcenter:0C72BA04-3B7A-4C4F-A138-923402CE6185>: <NSError: 0x8dec02d90; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:09.389547-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0C72BA04-3B7A-4C4F-A138-923402CE6185
default	20:31:09.389662-0500	Nexy	Requesting scene <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:0C72BA04-3B7A-4C4F-A138-923402CE6185-Aux[9]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:31:09.389970-0500	Nexy	Request for <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:0C72BA04-3B7A-4C4F-A138-923402CE6185-Aux[9]-NSStatusItemView> complete!
default	20:31:09.390198-0500	Nexy	<FBSWorkspaceScenesClient:0x8dd0c0f00 <private>> was invalidated
default	20:31:09.390218-0500	Nexy	FBSWorkspace unregistering source: <private>
error	20:31:09.390264-0500	Nexy	Error creating <FBSScene: 0x8dd0c10e0; com.apple.controlcenter:0C72BA04-3B7A-4C4F-A138-923402CE6185-Aux[9]-NSStatusItemView>: <NSError: 0x8dec03810; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	20:31:09.390278-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0C72BA04-3B7A-4C4F-A138-923402CE6185-Aux[9]-NSStatusItemView
default	20:31:09.390408-0500	Nexy	[com.apple.controlcenter:0C72BA04-3B7A-4C4F-A138-923402CE6185-Aux[9]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	20:31:09.390604-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:09.390623-0500	Nexy	[com.apple.controlcenter:0C72BA04-3B7A-4C4F-A138-923402CE6185] No matching scene to invalidate for this identity.
error	20:31:09.390645-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	20:31:09.390656-0500	Nexy	[com.apple.controlcenter:0C72BA04-3B7A-4C4F-A138-923402CE6185-Aux[9]-NSStatusItemView] No matching scene to invalidate for this identity.
error	20:31:09.391041-0500	Nexy	Unhandled disconnected scene <private>
error	20:31:09.391160-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	20:31:09.391239-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	20:31:09.391321-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
