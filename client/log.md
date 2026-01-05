default	13:25:49.966833-0500	dmd	Requested application com.nexy.assistant has policy OK, associated categories:DH1005 associated sites:(null) equivalent bundle identifiers:com.nexy.assistant
default	13:25:50.043977-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:25:50.044162-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:25:50.045985-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:25:50.060769-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:25:50.060944-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87251 target:app<application.com.nexy.assistant.38522673.38522682(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:25:50.061073-0500	runningboardd	Assertion 394-80102-87251 (target:app<application.com.nexy.assistant.38522673.38522682(501)>) will be created as active
default	13:25:50.066206-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:25:50.066281-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682(501)>
default	13:25:50.066351-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:25:50.066485-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.002980 ms (wallclock); resolved to {4294967295, (null)}
default	13:25:50.082931-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:25:50.156513-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] is not RunningBoard jetsam managed.
default	13:25:50.156563-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] This process will not be managed.
default	13:25:50.156584-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682(501)>:83616]
default	13:25:50.156771-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:25:50.166888-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682(501)>:83616] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83616" ID:394-357-87253 target:83616 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:25:50.167090-0500	runningboardd	Assertion 394-357-87253 (target:[app<application.com.nexy.assistant.38522673.38522682(501)>:83616]) will be created as active
default	13:25:50.172046-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:25:50.172605-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring jetsam update because this process is not memory-managed
default	13:25:50.171617-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:25:50.172660-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring suspend because this process is not lifecycle managed
default	13:25:50.172709-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring GPU update because this process is not GPU managed
default	13:25:50.173062-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring memory limit update because this process is not memory-managed
default	13:25:50.281979-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring jetsam update because this process is not memory-managed
default	13:25:50.282052-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring suspend because this process is not lifecycle managed
default	13:25:50.282095-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring GPU update because this process is not GPU managed
default	13:25:50.282186-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring memory limit update because this process is not memory-managed
default	13:25:50.514931-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=489.14, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=489, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	13:25:50.528213-0500	tccd	AUTHREQ_SUBJECT: msgID=489.14, subject=com.nexy.assistant,
default	13:25:50.564460-0500	kernel	Nexy[83616] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0x1cc02052d81a06c7. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:25:50.564488-0500	kernel	Nexy[83616] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0x1cc02052d81a06c7. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:25:50.846086-0500	Nexy	[0x10582e120] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:25:50.846178-0500	Nexy	[0x105835090] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	13:25:51.158063-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x7e6a08000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:25:51.158350-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x7e6a08000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:25:51.158585-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x7e6a08000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:25:51.158821-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x7e6a08000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:25:51.160586-0500	Nexy	[0x10582d710] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:25:51.161473-0500	Nexy	[0x7e6b48000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:25:51.161819-0500	Nexy	[0x7e6b48140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:25:51.162287-0500	Nexy	[0x7e6b48280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:25:51.164664-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:25:51.172952-0500	Nexy	Received configuration update from daemon (initial)
default	13:25:51.186866-0500	Nexy	[0x7e6b483c0] invalidated after the last release of the connection object
default	13:25:51.187282-0500	Nexy	server port 0x00003413, session port 0x00003413
default	13:25:51.188679-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.540, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:25:51.188708-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:25:51.191111-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:25:51.211340-0500	Nexy	New connection 0xf0a83 main
default	13:25:51.214216-0500	Nexy	CHECKIN: pid=83616
default	13:25:51.223025-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682(501)>:83616] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83616" ID:394-357-87268 target:83616 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:25:51.223119-0500	runningboardd	Assertion 394-357-87268 (target:[app<application.com.nexy.assistant.38522673.38522682(501)>:83616]) will be created as active
default	13:25:51.223694-0500	Nexy	CHECKEDIN: pid=83616 asn=0x0-0xf80f8 foreground=0
default	13:25:51.223522-0500	launchservicesd	CHECKIN:0x0-0xf80f8 83616 com.nexy.assistant
default	13:25:51.224102-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:25:51.223993-0500	Nexy	[0x7e6b483c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:25:51.224277-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:25:51.224076-0500	Nexy	[0x7e6b483c0] Connection returned listener port: 0x5003
default	13:25:51.224574-0500	Nexy	[0x7e6b58300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x7e6b483c0.peer[357].0x7e6b58300
default	13:25:51.229104-0500	Nexy	[0x7e6b483c0] Connection returned listener port: 0x5003
default	13:25:51.233743-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:25:51.234535-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:25:51.238403-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.38522673.38522682(501)>:83616] as ready
default	13:25:51.238683-0500	Nexy	[0x7e6b483c0] Connection returned listener port: 0x5003
default	13:25:51.243016-0500	Nexy	Handshake succeeded
default	13:25:51.243036-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.38522673.38522682(501)>
default	13:25:51.243108-0500	Nexy	[0x7e6b483c0] Connection returned listener port: 0x5003
default	13:25:51.247778-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:25:51.247822-0500	Nexy	[0x7e6b48a00] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:25:51.247952-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:25:51.248013-0500	Nexy	[0x7e6b488c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:25:52.502535-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid A54E5185-CD49-4F7B-BE9D-3BB99571F7FD flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63083,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x8991cc02 tp_proto=0x06"
default	13:25:52.502594-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63083<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533180 t_state: SYN_SENT process: Nexy:83616 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8c01b13c
default	13:25:52.502986-0500	kernel	tcp connected: [<IPv4-redacted>:63083<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533180 t_state: ESTABLISHED process: Nexy:83616 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8c01b13c
default	13:25:52.503263-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63083<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533180 t_state: FIN_WAIT_1 process: Nexy:83616 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8c01b13c
default	13:25:52.503273-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63083<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533180 t_state: FIN_WAIT_1 process: Nexy:83616 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:25:52.586359-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:25:52.587390-0500	Nexy	[0x7e6b48c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:25:52.588984-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4012","name":"Nexy(83616)"}, "details":{"PID":83616,"session_type":"Primary"} }
default	13:25:52.589066-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":83616}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4012, sessionType: 'prim', isRecording: false }, 
]
default	13:25:52.589812-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 83616, name = Nexy
default	13:25:52.590136-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x7e6be7960 with ID: 0x1f4012
default	13:25:52.590681-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:25:52.591809-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:25:52.594039-0500	Nexy	[0x7e6b48dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:25:52.597312-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682 AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682>
default	13:25:52.602027-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:25:52.603837-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:25:52.603988-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:25:52.604140-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:25:52.604152-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:25:52.604187-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:25:52.604335-0500	Nexy	[0x7e6b48f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:25:52.604855-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83616.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:25:52.605247-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:25:52.610970-0500	tccd	AUTHREQ_SUBJECT: msgID=83616.2, subject=com.nexy.assistant,
default	13:25:52.611646-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190c00 at /Applications/Nexy.app
default	13:25:52.627497-0500	Nexy	[0x7e6b48f00] invalidated after the last release of the connection object
default	13:25:52.627547-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:25:52.630894-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	13:25:52.631953-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.308, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:25:52.632796-0500	tccd	AUTHREQ_SUBJECT: msgID=395.308, subject=com.nexy.assistant,
default	13:25:52.633368-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190c00 at /Applications/Nexy.app
error	13:25:52.645692-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:25:52.646590-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.310, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:25:52.647402-0500	tccd	AUTHREQ_SUBJECT: msgID=395.310, subject=com.nexy.assistant,
default	13:25:52.647969-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190c00 at /Applications/Nexy.app
default	13:25:52.662126-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:25:52.662719-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x7e5480620> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:25:52.676039-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:25:52.677663-0500	Nexy	[0x7e6b48f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:25:52.677994-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=359127985422337 }
default	13:25:52.678611-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:25:52.679105-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:25:52.679133-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:25:52.690818-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:25:52.725687-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:25:52.725712-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:25:52.732621-0500	Nexy	[0x7e6b49040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:25:53.235945-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7e7990040) Selecting device 71 from constructor
default	13:25:53.235960-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7e7990040)
default	13:25:53.235968-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7e7990040) not already running
default	13:25:53.236356-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7e7990040) nothing to teardown
default	13:25:53.236361-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7e7990040) connecting device 71
default	13:25:53.236505-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7e7990040) Device ID: 71 (Input:No | Output:Yes): true
default	13:25:53.236620-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7e7990040) created ioproc 0xa for device 71
default	13:25:53.236747-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990040) adding 7 device listeners to device 71
default	13:25:53.236943-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990040) adding 0 device delegate listeners to device 71
default	13:25:53.236953-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7e7990040)
default	13:25:53.237032-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:25:53.237041-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:25:53.237046-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:25:53.237063-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:25:53.237076-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:25:53.237173-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7e7990040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:25:53.237183-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7e7990040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:25:53.237190-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:25:53.237194-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990040) removing 0 device listeners from device 0
default	13:25:53.237199-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990040) removing 0 device delegate listeners from device 0
default	13:25:53.237202-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7e7990040)
default	13:25:53.237287-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:25:53.237740-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:25:53.239507-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:25:53.239582-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:25:53.239782-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7e5e08180, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:25:53.239842-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:25:53.242290-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:25:53.242536-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:25:53.248123-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:25:53.248363-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:25:53.250341-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7e54a14d0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:25:53.250365-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:25:53.250703-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:25:53.251406-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7e54a14a0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:25:53.251420-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x7e54a14a0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:25:53.251426-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:25:53.251427-0500	Nexy	AudioConverter -> 0x7e54a14a0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:25:53.251439-0500	Nexy	AudioConverter -> 0x7e54a14a0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:25:53.251445-0500	Nexy	AudioConverter -> 0x7e54a14a0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:25:53.252584-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7e54a14d0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:25:53.252593-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x7e54a14d0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:25:53.252600-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:25:53.252599-0500	Nexy	AudioConverter -> 0x7e54a14d0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:25:53.252608-0500	Nexy	AudioConverter -> 0x7e54a14d0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:25:53.252614-0500	Nexy	AudioConverter -> 0x7e54a14d0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:25:53.252746-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x7e54a14d0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:25:53.333338-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7e7990740) Selecting device 71 from constructor
default	13:25:53.333348-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7e7990740)
default	13:25:53.333355-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7e7990740) not already running
default	13:25:53.333359-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7e7990740) nothing to teardown
default	13:25:53.333364-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7e7990740) connecting device 71
default	13:25:53.333445-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7e7990740) Device ID: 71 (Input:No | Output:Yes): true
default	13:25:53.333544-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7e7990740) created ioproc 0xb for device 71
default	13:25:53.333641-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 7 device listeners to device 71
default	13:25:53.333801-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 0 device delegate listeners to device 71
default	13:25:53.333810-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7e7990740)
default	13:25:53.333873-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:25:53.333883-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:25:53.333888-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:25:53.333894-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:25:53.333901-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:25:53.333981-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7e7990740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:25:53.333992-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7e7990740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:25:53.333997-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:25:53.334001-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 0 device listeners from device 0
default	13:25:53.334006-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 0 device delegate listeners from device 0
default	13:25:53.334008-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7e7990740)
default	13:25:53.334022-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:25:53.334064-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x7e7990740) caller requesting device change from 71 to 78
default	13:25:53.334069-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7e7990740)
default	13:25:53.334074-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7e7990740) not already running
default	13:25:53.334076-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x7e7990740) disconnecting device 71
default	13:25:53.334080-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x7e7990740) destroying ioproc 0xb for device 71
default	13:25:53.334137-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xb}
default	13:25:53.334203-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:25:53.334269-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7e7990740) connecting device 78
default	13:25:53.334331-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7e7990740) Device ID: 78 (Input:Yes | Output:No): true
default	13:25:53.335670-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.311, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:25:53.336846-0500	tccd	AUTHREQ_SUBJECT: msgID=395.311, subject=com.nexy.assistant,
default	13:25:53.337510-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190c00 at /Applications/Nexy.app
default	13:25:53.355180-0500	tccd	AUTHREQ_PROMPTING: msgID=395.311, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	13:25:55.163633-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    474 = "<TCCDEventSubscriber: token=474, state=Initial, csid=(null)>";
    472 = "<TCCDEventSubscriber: token=472, state=Initial, csid=(null)>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
}
default	13:25:55.164277-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7e7990740) created ioproc 0xa for device 78
default	13:25:55.164560-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 7 device listeners to device 78
default	13:25:55.164908-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 0 device delegate listeners to device 78
default	13:25:55.164922-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7e7990740)
default	13:25:55.164940-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	13:25:55.164958-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:25:55.165242-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	13:25:55.165256-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	13:25:55.165265-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	13:25:55.165422-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7e7990740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:25:55.165446-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7e7990740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:25:55.165453-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:25:55.165535-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 7 device listeners from device 71
default	13:25:55.165796-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 0 device delegate listeners from device 71
default	13:25:55.165807-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7e7990740)
default	13:25:55.166361-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:25:55.166788-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	13:25:55.167872-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.312, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:25:55.169369-0500	tccd	AUTHREQ_SUBJECT: msgID=395.312, subject=com.nexy.assistant,
default	13:25:55.172358-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190c00 at /Applications/Nexy.app
default	13:25:55.194288-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7e54a1350, from  1 ch,  48000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	13:25:55.194541-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:25:55.195838-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.313, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:25:55.198215-0500	tccd	AUTHREQ_SUBJECT: msgID=395.313, subject=com.nexy.assistant,
default	13:25:55.199410-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190c00 at /Applications/Nexy.app
default	13:25:55.218987-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.314, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:25:55.219875-0500	tccd	AUTHREQ_SUBJECT: msgID=395.314, subject=com.nexy.assistant,
default	13:25:55.220489-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190c00 at /Applications/Nexy.app
default	13:25:55.237476-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:25:55.238601-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:25:55.238626-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682(501)>:83616] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-87294 target:83616 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:25:55.238693-0500	runningboardd	Assertion 394-328-87294 (target:[app<application.com.nexy.assistant.38522673.38522682(501)>:83616]) will be created as active
default	13:25:55.238944-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring jetsam update because this process is not memory-managed
default	13:25:55.238954-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring suspend because this process is not lifecycle managed
default	13:25:55.238970-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring GPU update because this process is not GPU managed
default	13:25:55.239037-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring memory limit update because this process is not memory-managed
default	13:25:55.241084-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:25:55.241126-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:25:55.241652-0500	gamepolicyd	Received state update for 83616 (app<application.com.nexy.assistant.38522673.38522682(501)>, running-active-NotVisible
default	13:25:55.262574-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xa}
default	13:25:55.263756-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4012","name":"Nexy(83616)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:25:55.263843-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:25:55.264209-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:25:55.264267-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f4012, Nexy(83616), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:25:55.264312-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:55.264342-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:25:55.264370-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:25:55.264432-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:25:55.264437-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:55.264445-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4012, Nexy(83616), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 19 starting recording
default	13:25:55.264482-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:55.264534-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:55.264566-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:55.264703-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:55.265044-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:25:55.265073-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:25:55.265093-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4012, Nexy(83616), 'prim'', displayID:'com.nexy.assistant'}
default	13:25:55.265149-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:55.265168-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	13:25:55.265182-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:25:55.265268-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:55.265290-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:55.265304-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	13:25:55.265315-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	13:25:55.265321-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	13:25:55.265348-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
fault	13:25:55.265361-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682 AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682>
fault	13:25:55.267069-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682 AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682>
error	13:25:55.268444-0500	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	13:25:55.277173-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:25:55.277235-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:25:55.277262-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:25:55.279819-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.279834-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.279855-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:55.279861-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.279870-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:55.279875-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:25:55.280410-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:25:55.283262-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.283274-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.283286-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:55.283293-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.283299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:55.283305-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:25:55.283396-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:25:55.284493-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.284503-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.284512-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:55.284518-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.284524-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:55.284531-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:25:55.284961-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:25:55.298816-0500	runningboardd	Assertion did invalidate due to timeout: 394-394-87252 (target:[app<application.com.nexy.assistant.38522673.38522682(501)>:83616])
default	13:25:55.321297-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	13:25:55.321414-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4012","name":"Nexy(83616)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:25:55.321477-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:25:55.321511-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:25:55.321537-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4012, Nexy(83616), 'prim'', displayID:'com.nexy.assistant'}
default	13:25:55.321579-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4012, Nexy(83616), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 19 stopping recording
default	13:25:55.321600-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:25:55.321629-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:25:55.321630-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:55.321659-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:25:55.321736-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:55.321746-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:25:55.321757-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:25:55.321774-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:55.321836-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:55.321866-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:25:55.321913-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:55.321955-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:25:55.321975-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:55.321986-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:25:55.326282-0500	runningboardd	Invalidating assertion 394-328-87294 (target:[app<application.com.nexy.assistant.38522673.38522682(501)>:83616]) from originator [osservice<com.apple.powerd>:328]
default	13:25:55.327182-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:25:55.327642-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.327656-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.327667-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:55.327675-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:55.327682-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:55.327688-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:25:55.327769-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:25:55.423408-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7e7990740) Selecting device 0 from destructor
default	13:25:55.423422-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7e7990740)
default	13:25:55.423429-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7e7990740) not already running
default	13:25:55.423435-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x7e7990740) disconnecting device 78
default	13:25:55.423441-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x7e7990740) destroying ioproc 0xa for device 78
default	13:25:55.423471-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	13:25:55.423504-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:25:55.423660-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x7e7990740) nothing to setup
default	13:25:55.423676-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 0 device listeners to device 0
default	13:25:55.423682-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 0 device delegate listeners to device 0
default	13:25:55.423691-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 7 device listeners from device 78
default	13:25:55.423887-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 0 device delegate listeners from device 78
default	13:25:55.423901-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7e7990740)
default	13:25:55.499402-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring jetsam update because this process is not memory-managed
default	13:25:55.499413-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring suspend because this process is not lifecycle managed
default	13:25:55.499423-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring GPU update because this process is not GPU managed
default	13:25:55.499439-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring memory limit update because this process is not memory-managed
default	13:25:55.501763-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:25:55.505243-0500	gamepolicyd	Received state update for 83616 (app<application.com.nexy.assistant.38522673.38522682(501)>, running-active-NotVisible
default	13:25:55.852775-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83628.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83628, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83628, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:25:55.854403-0500	tccd	AUTHREQ_SUBJECT: msgID=83628.1, subject=com.nexy.assistant,
default	13:25:55.855144-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:25:55.871048-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83628.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83628, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83628, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:25:55.871972-0500	tccd	AUTHREQ_SUBJECT: msgID=83628.2, subject=com.nexy.assistant,
default	13:25:55.872658-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:25:55.907540-0500	Nexy	[0x7e6b49400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:25:55.908328-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83616.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:25:55.909651-0500	tccd	AUTHREQ_SUBJECT: msgID=83616.3, subject=com.nexy.assistant,
default	13:25:55.910398-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:25:55.924518-0500	Nexy	[0x7e6b49400] invalidated after the last release of the connection object
default	13:25:55.929826-0500	Nexy	[0x7e6b49540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:25:55.930305-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83616.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:25:55.931175-0500	tccd	AUTHREQ_SUBJECT: msgID=83616.4, subject=com.nexy.assistant,
default	13:25:55.931806-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:25:55.945679-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[83616], responsiblePID[83616], responsiblePath: /Applications/Nexy.app to UID: 501
default	13:25:55.945931-0500	Nexy	[0x7e6b49540] invalidated after the last release of the connection object
default	13:25:55.991754-0500	Nexy	[0x7e6b49680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:25:55.992428-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:25:55.992623-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83616.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:25:55.993861-0500	tccd	AUTHREQ_SUBJECT: msgID=83616.5, subject=com.nexy.assistant,
default	13:25:55.994724-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:25:56.125494-0500	Nexy	[0x7e6b49680] invalidated after the last release of the connection object
default	13:25:56.125613-0500	Nexy	[0x7e6b49680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:25:56.133162-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254000 at /Applications/Nexy.app
error	13:25:56.138919-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:25:56.139100-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83616.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:25:56.140248-0500	tccd	AUTHREQ_SUBJECT: msgID=83616.6, subject=com.nexy.assistant,
default	13:25:56.141052-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254c00 at /Applications/Nexy.app
default	13:25:56.159094-0500	Nexy	[0x7e6b49680] invalidated after the last release of the connection object
default	13:25:56.159163-0500	Nexy	[0x7e6b49680] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:25:56.159245-0500	Nexy	[0x7e6b49680] invalidated after the last release of the connection object
default	13:25:56.159508-0500	Nexy	[0x7e6b49540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:25:56.160015-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83616.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:25:56.161185-0500	tccd	AUTHREQ_SUBJECT: msgID=83616.7, subject=com.nexy.assistant,
default	13:25:56.163060-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	13:25:56.164727-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:25:56.174834-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:25:56.187829-0500	Nexy	[0x7e6b49540] invalidated after the last release of the connection object
default	13:25:56.188071-0500	Nexy	server port 0x00013d0f, session port 0x00003413
default	13:25:56.188800-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.547, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:25:56.188827-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:25:56.189718-0500	tccd	AUTHREQ_SUBJECT: msgID=387.547, subject=com.nexy.assistant,
default	13:25:56.190434-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255500 at /Applications/Nexy.app
default	13:25:56.268799-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:25:56.288902-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254000 at /Applications/Nexy.app
default	13:25:56.292918-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:25:56.374474-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:25:56.970540-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	13:25:56.975754-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:25:56.989839-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7e7990740) Selecting device 71 from constructor
default	13:25:56.989856-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7e7990740)
default	13:25:56.989866-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7e7990740) not already running
default	13:25:56.989871-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7e7990740) nothing to teardown
default	13:25:56.989877-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7e7990740) connecting device 71
default	13:25:56.990026-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7e7990740) Device ID: 71 (Input:No | Output:Yes): true
default	13:25:56.990187-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7e7990740) created ioproc 0xc for device 71
default	13:25:56.990329-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 7 device listeners to device 71
default	13:25:56.990596-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 0 device delegate listeners to device 71
default	13:25:56.990607-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7e7990740)
default	13:25:56.990734-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:25:56.990746-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:25:56.990755-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:25:56.990766-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:25:56.990776-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:25:56.990911-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7e7990740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:25:56.990928-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7e7990740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:25:56.990937-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:25:56.990945-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 0 device listeners from device 0
default	13:25:56.990951-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 0 device delegate listeners from device 0
default	13:25:56.990957-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7e7990740)
default	13:25:56.990977-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:25:56.991053-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x7e7990740) caller requesting device change from 71 to 78
default	13:25:56.991061-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7e7990740)
default	13:25:56.991082-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7e7990740) not already running
default	13:25:56.991087-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x7e7990740) disconnecting device 71
default	13:25:56.991094-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x7e7990740) destroying ioproc 0xc for device 71
default	13:25:56.991128-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xc}
default	13:25:56.991172-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:25:56.991280-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7e7990740) connecting device 78
default	13:25:56.991396-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7e7990740) Device ID: 78 (Input:Yes | Output:No): true
default	13:25:56.993554-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.315, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:25:56.995304-0500	tccd	AUTHREQ_SUBJECT: msgID=395.315, subject=com.nexy.assistant,
default	13:25:56.996507-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190c00 at /Applications/Nexy.app
default	13:25:56.998378-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 2 UUID(s) for com.nexy.assistant
default	13:25:57.020180-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7e7990740) created ioproc 0xb for device 78
default	13:25:57.020358-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 7 device listeners to device 78
default	13:25:57.020549-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 0 device delegate listeners to device 78
default	13:25:57.020558-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7e7990740)
default	13:25:57.020567-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	13:25:57.020581-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:25:57.020747-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	13:25:57.020760-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	13:25:57.020766-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	13:25:57.020868-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7e7990740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:25:57.020876-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7e7990740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:25:57.020883-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:25:57.020888-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 7 device listeners from device 71
default	13:25:57.021058-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 0 device delegate listeners from device 71
default	13:25:57.021064-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7e7990740)
default	13:25:57.021081-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	13:25:57.021466-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:25:57.022711-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.316, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:25:57.023791-0500	tccd	AUTHREQ_SUBJECT: msgID=395.316, subject=com.nexy.assistant,
default	13:25:57.024449-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190c00 at /Applications/Nexy.app
default	13:25:57.041002-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7e54a1cb0, from  1 ch,  48000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	13:25:57.041213-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:25:57.042180-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.317, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:25:57.043045-0500	tccd	AUTHREQ_SUBJECT: msgID=395.317, subject=com.nexy.assistant,
default	13:25:57.043647-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190c00 at /Applications/Nexy.app
default	13:25:57.061544-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.318, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83616, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:25:57.062438-0500	tccd	AUTHREQ_SUBJECT: msgID=395.318, subject=com.nexy.assistant,
default	13:25:57.063050-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190c00 at /Applications/Nexy.app
default	13:25:57.080573-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682(501)>:83616] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-87308 target:83616 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:25:57.080694-0500	runningboardd	Assertion 394-328-87308 (target:[app<application.com.nexy.assistant.38522673.38522682(501)>:83616]) will be created as active
default	13:25:57.081077-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring jetsam update because this process is not memory-managed
default	13:25:57.081088-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring suspend because this process is not lifecycle managed
default	13:25:57.081099-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring GPU update because this process is not GPU managed
default	13:25:57.081125-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring memory limit update because this process is not memory-managed
default	13:25:57.084212-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:25:57.084744-0500	gamepolicyd	Received state update for 83616 (app<application.com.nexy.assistant.38522673.38522682(501)>, running-active-NotVisible
default	13:25:57.105153-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xb}
error	13:25:57.105834-0500	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	13:25:57.105849-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4012","name":"Nexy(83616)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:25:57.105946-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:25:57.105979-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f4012, Nexy(83616), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	13:25:57.106008-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:25:57.106076-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f4012, Nexy(83616), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:25:57.106108-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:57.106117-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:25:57.106153-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:25:57.106203-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:25:57.106209-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:57.106219-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4012, Nexy(83616), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 19 starting recording
default	13:25:57.106298-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:25:57.106281-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:57.106343-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:57.106329-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:25:57.106380-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:57.106359-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4012, Nexy(83616), 'prim'', displayID:'com.nexy.assistant'}
default	13:25:57.106462-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	13:25:57.106492-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:57.106482-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:25:57.106537-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:57.106420-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:57.106583-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:57.106596-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	13:25:57.106605-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	13:25:57.106625-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	13:25:57.106699-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:25:57.113029-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:25:57.113123-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:25:57.113182-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:25:57.113689-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.113703-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.113717-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:57.113724-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.113732-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:57.113740-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:25:57.113756-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.113768-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.113776-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:57.113785-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.113811-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:57.113832-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:25:57.114005-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:25:57.114568-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.114581-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.114589-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:57.114597-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.114604-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:57.114612-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:25:57.114679-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:25:57.159596-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	13:25:57.159735-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4012","name":"Nexy(83616)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:25:57.159813-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:25:57.159981-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:25:57.160022-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4012, Nexy(83616), 'prim'', displayID:'com.nexy.assistant'}
default	13:25:57.160095-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:57.160104-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4012, Nexy(83616), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 19 stopping recording
default	13:25:57.160130-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:25:57.160156-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:25:57.160187-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:25:57.160248-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:57.160295-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:25:57.160306-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:25:57.160233-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:57.160307-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:25:57.160357-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:25:57.160381-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:57.160476-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:25:57.160495-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:57.160506-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:25:57.165664-0500	runningboardd	Invalidating assertion 394-328-87308 (target:[app<application.com.nexy.assistant.38522673.38522682(501)>:83616]) from originator [osservice<com.apple.powerd>:328]
default	13:25:57.167082-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:25:57.167881-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.167896-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.167912-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:57.167921-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:25:57.167941-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:25:57.167948-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:25:57.168180-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:25:57.261617-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7e7990740) Selecting device 0 from destructor
default	13:25:57.261635-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7e7990740)
default	13:25:57.261642-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7e7990740) not already running
default	13:25:57.261647-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x7e7990740) disconnecting device 78
default	13:25:57.261668-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x7e7990740) destroying ioproc 0xb for device 78
default	13:25:57.261710-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	13:25:57.261753-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:25:57.261931-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x7e7990740) nothing to setup
default	13:25:57.261946-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 0 device listeners to device 0
default	13:25:57.261954-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7e7990740) adding 0 device delegate listeners to device 0
default	13:25:57.261960-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 7 device listeners from device 78
default	13:25:57.262173-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7e7990740) removing 0 device delegate listeners from device 78
default	13:25:57.262191-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7e7990740)
default	13:25:57.270204-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring jetsam update because this process is not memory-managed
default	13:25:57.270221-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring suspend because this process is not lifecycle managed
default	13:25:57.270232-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring GPU update because this process is not GPU managed
default	13:25:57.270251-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] Ignoring memory limit update because this process is not memory-managed
default	13:25:57.273166-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:25:57.273825-0500	gamepolicyd	Received state update for 83616 (app<application.com.nexy.assistant.38522673.38522682(501)>, running-active-NotVisible
default	13:25:58.318368-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f4012","name":"Nexy(83616)"}, "details":null }
default	13:25:58.318420-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f4012 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":83616})
default	13:25:58.318444-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":83616})
default	13:25:58.318806-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:25:58.318909-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 19, PID = 83616, Name = sid:0x1f4012, Nexy(83616), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:25:58.317981-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0xf80f8 (Nexy) connectionID: F0A83 pid: 83616 in session 0x101
default	13:25:58.318044-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0xf80f8 (Nexy) acq:0xb6c360100 count:1
default	13:25:58.319009-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:58.319272-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:58.319175-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:58.319344-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:58.319371-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:58.319494-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:25:58.320247-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0xf80f8 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0xf80f8 (Nexy)"
)}
default	13:25:58.323009-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x146a0 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0xf80f8 (Nexy)"
)}
default	13:25:58.332802-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682(501)>:83616]
default	13:25:58.337826-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682(501)>:83616] termination reported by launchd (0, 0, 0)
default	13:25:58.337858-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682(501)>:83616]
default	13:25:58.338082-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682(501)>:83616]
default	13:25:58.338280-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682(501)>:83616]
default	13:25:58.338326-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682(501)>:83616]
default	13:25:58.345143-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682(501)>: none (role: None) (endowments: (null))
default	13:25:58.345434-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682(501)>: none (role: None) (endowments: (null))
default	13:25:58.345580-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 83616, name = Nexy
default	13:25:58.348128-0500	launchservicesd	Hit the server for a process handle 11f203e8000146a0 that resolved to: [app<application.com.nexy.assistant.38522673.38522682(501)>:83616]
default	13:25:58.348500-0500	gamepolicyd	Received state update for 83616 (app<application.com.nexy.assistant.38522673.38522682(501)>, none-NotVisible
default	13:25:58.350241-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0xf80f8} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:25:58.350272-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 3
default	13:25:58.350291-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:25:58.353270-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 4
default	13:25:58.353283-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
error	13:26:00.752099-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	13:26:00.754538-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	13:26:00.755096-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	13:26:00.758188-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	13:26:00.855587-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	13:26:00.856381-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	13:26:01.544646-0500	runningboardd	Assertion 394-80102-87381 (target:app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>) will be created as active
default	13:26:01.552309-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:26:01.552373-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>
default	13:26:01.552526-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:26:01.552670-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:26:01.571795-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] is not RunningBoard jetsam managed.
default	13:26:01.571811-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] This process will not be managed.
default	13:26:01.571882-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671]
default	13:26:01.572681-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:01.588988-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671]
default	13:26:01.589210-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] from originator [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87382 target:83671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:26:01.589581-0500	runningboardd	Assertion 394-394-87382 (target:[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671]) will be created as active
default	13:26:01.590512-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] Ignoring jetsam update because this process is not memory-managed
default	13:26:01.590591-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] Ignoring suspend because this process is not lifecycle managed
default	13:26:01.590636-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] Set darwin role to: UserInteractive
default	13:26:01.590677-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] Ignoring GPU update because this process is not GPU managed
default	13:26:01.590775-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] Ignoring memory limit update because this process is not memory-managed
default	13:26:01.590924-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] reported to RB as running
default	13:26:01.595144-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83671" ID:394-357-87383 target:83671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:01.595316-0500	runningboardd	Assertion 394-357-87383 (target:[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671]) will be created as active
default	13:26:01.599934-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] Ignoring GPU update because this process is not GPU managed
default	13:26:01.600003-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] Ignoring memory limit update because this process is not memory-managed
default	13:26:01.597744-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:01.597995-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a61c0: Nexy> state 2
default	13:26:01.598064-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:01.606239-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:01.626274-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:01.657773-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] Ignoring jetsam update because this process is not memory-managed
default	13:26:01.657828-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] Ignoring suspend because this process is not lifecycle managed
default	13:26:01.657874-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] Ignoring GPU update because this process is not GPU managed
default	13:26:01.658107-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] Ignoring memory limit update because this process is not memory-managed
default	13:26:01.707658-0500	Nexy	[0x105be4f40] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:26:01.707804-0500	Nexy	[0x105be5480] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:26:01.717583-0500	logger	detected new pid 83671 for /Applications/Nexy.app/Contents/MacOS/Nexy
error	13:26:01.873600-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x9004d0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:26:01.880420-0500	Nexy	[0x9006743c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:01.917069-0500	Nexy	[0x9006743c0] invalidated after the last release of the connection object
default	13:26:01.917475-0500	Nexy	server port 0x0000330b, session port 0x0000330b
default	13:26:01.922126-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257000 at /Applications/Nexy.app
default	13:26:01.955459-0500	Nexy	New connection 0xf0a93 main
default	13:26:01.970022-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:01.970125-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:01.975867-0500	Nexy	BringForward: pid=83671 asn=0x0-0x103103 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:26:01.976383-0500	Nexy	BringFrontModifier: pid=83671 asn=0x0-0x103103 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:26:01.977068-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:26:01.988153-0500	Nexy	Handshake succeeded
default	13:26:01.988178-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>
default	13:26:01.989012-0500	Nexy	[0x9006743c0] Connection returned listener port: 0x4203
default	13:26:01.993870-0500	Nexy	[0x9006743c0] Connection returned listener port: 0x4203
default	13:26:02.016318-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:26:02.016335-0500	Nexy	[0x900674500] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:26:02.017108-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:26:02.017163-0500	Nexy	[0x900674a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:02.021214-0500	Nexy	[0x900674a00] Connection returned listener port: 0x6a03
default	13:26:02.025501-0500	Nexy	Registered process with identifier 83671-162158
default	13:26:02.089833-0500	gamepolicyd	Hit the server for a process handle 1d4f3238000146d7 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671]
default	13:26:02.090070-0500	gamepolicyd	Received state update for 83671 (app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>, running-active-NotVisible
default	13:26:02.090898-0500	gamepolicyd	Received state update for 83671 (app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>, running-active-NotVisible
default	13:26:03.102118-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 44FCCA70-175C-42C0-85C3-EC114982C670 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63091,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc5f99852 tp_proto=0x06"
default	13:26:03.102189-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63091<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533281 t_state: SYN_SENT process: Nexy:83671 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9e257588
default	13:26:03.102545-0500	kernel	tcp connected: [<IPv4-redacted>:63091<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533281 t_state: ESTABLISHED process: Nexy:83671 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9e257588
default	13:26:03.102906-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63091<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533281 t_state: FIN_WAIT_1 process: Nexy:83671 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x9e257588
default	13:26:03.102926-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63091<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533281 t_state: FIN_WAIT_1 process: Nexy:83671 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:26:03.150578-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:26:03.151196-0500	Nexy	[0x900674c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:26:03.152554-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4013","name":"Nexy(83671)"}, "details":{"PID":83671,"session_type":"Primary"} }
default	13:26:03.152658-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":83671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4013, sessionType: 'prim', isRecording: false }, 
]
default	13:26:03.155297-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:26:03.157046-0500	Nexy	[0x900674dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	13:26:03.173563-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:26:03.185091-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:03.217744-0500	Nexy	[0x900674f00] invalidated after the last release of the connection object
default	13:26:03.218012-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:03.218080-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:03.218436-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:26:03.223069-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:03.251287-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.321, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:03.253057-0500	tccd	AUTHREQ_SUBJECT: msgID=395.321, subject=com.nexy.assistant,
default	13:26:03.279330-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
default	13:26:03.297683-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:03.299747-0500	Nexy	[0x900674f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:26:03.300394-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=359364208623617 }
default	13:26:03.300560-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:26:03.300609-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:26:03.300638-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:26:03.318166-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:26:03.362627-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:26:03.362656-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:26:03.381891-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x105bf7e40) adding 7 device listeners to device 71
default	13:26:03.382080-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x105bf7e40) adding 0 device delegate listeners to device 71
default	13:26:03.382090-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x105bf7e40)
default	13:26:03.382173-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:03.382181-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:26:03.382186-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:03.382208-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:26:03.382217-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:26:03.382345-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x105bf7e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:26:03.382360-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x105bf7e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:26:03.382366-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:26:03.382373-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x105bf7e40) removing 0 device listeners from device 0
default	13:26:03.382376-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x105bf7e40) removing 0 device delegate listeners from device 0
default	13:26:03.382381-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x105bf7e40)
default	13:26:03.382431-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:26:03.382853-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:03.384321-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:26:03.384382-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:26:03.384531-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8ff9efa80, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:03.384557-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:03.388267-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:03.388505-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:03.389859-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8ff9efa20, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:03.389877-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:03.390237-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:03.391098-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8ff9efe70, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:03.391110-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8ff9efe70: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:03.391119-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:03.391114-0500	Nexy	AudioConverter -> 0x8ff9efe70: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:03.391129-0500	Nexy	AudioConverter -> 0x8ff9efe70: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:03.391136-0500	Nexy	AudioConverter -> 0x8ff9efe70: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:03.392103-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8ff9efa20, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:03.392115-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8ff9efa20: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:03.392122-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:03.392121-0500	Nexy	AudioConverter -> 0x8ff9efa20: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:03.392128-0500	Nexy	AudioConverter -> 0x8ff9efa20: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:03.392133-0500	Nexy	AudioConverter -> 0x8ff9efa20: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:03.392302-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8ff9efa20: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:03.442938-0500	Nexy	[0x900675180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:03.443562-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:03.443770-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83671.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:03.444999-0500	tccd	AUTHREQ_SUBJECT: msgID=83671.3, subject=com.nexy.assistant,
default	13:26:03.470084-0500	Nexy	[0x900675180] invalidated after the last release of the connection object
default	13:26:03.470211-0500	Nexy	[0x900675180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:03.470777-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:03.470968-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83671.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:03.472023-0500	tccd	AUTHREQ_SUBJECT: msgID=83671.4, subject=com.nexy.assistant,
default	13:26:03.472726-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:03.496913-0500	Nexy	[0x900675180] invalidated after the last release of the connection object
default	13:26:03.497018-0500	Nexy	[0x900675180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:26:03.497160-0500	Nexy	[0x900675180] invalidated after the last release of the connection object
default	13:26:03.832961-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83684.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83684, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83684, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:03.834383-0500	tccd	AUTHREQ_SUBJECT: msgID=83684.1, subject=com.nexy.assistant,
default	13:26:03.835212-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:03.855690-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83684.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83671, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83684, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83684, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:03.856605-0500	tccd	AUTHREQ_SUBJECT: msgID=83684.2, subject=com.nexy.assistant,
default	13:26:03.857245-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:03.892462-0500	Nexy	[0x900675540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:03.893074-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83671.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:03.899149-0500	tccd	AUTHREQ_SUBJECT: msgID=83671.5, subject=com.nexy.assistant,
default	13:26:03.899787-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:03.917393-0500	Nexy	[0x900675540] invalidated after the last release of the connection object
default	13:26:03.946326-0500	Nexy	server port 0x00011003, session port 0x0000330b
default	13:26:04.828608-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256a00 at /Applications/Nexy.app
default	13:26:04.848848-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:04.859379-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	13:26:05.013473-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	13:26:05.013854-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	13:26:05.015269-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	13:26:05.015791-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	13:26:05.049526-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	13:26:05.049916-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	13:26:05.972451-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x103103 (Nexy) connectionID: F0A93 pid: 83671 in session 0x101
default	13:26:05.972516-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x103103 (Nexy) acq:0xb6c363fa0 count:1
default	13:26:05.973347-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f4013","name":"Nexy(83671)"}, "details":null }
default	13:26:05.973414-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f4013 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":83671})
default	13:26:05.973438-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":83671})
default	13:26:05.973764-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 20, PID = 83671, Name = sid:0x1f4013, Nexy(83671), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:26:05.973963-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 20, PID = 83671, Name = sid:0x1f4013, Nexy(83671), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:26:05.974292-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:05.974451-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:05.974519-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x103103 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x103103 (Nexy)"
)}
default	13:26:05.974628-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:05.974725-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:05.974853-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:05.974941-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:05.975500-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x146d7 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x103103 (Nexy)"
)}
default	13:26:05.988037-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671]
default	13:26:05.994734-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671] termination reported by launchd (0, 0, 0)
default	13:26:05.994790-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671]
default	13:26:05.995078-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671]
default	13:26:05.995311-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671]
default	13:26:05.995373-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671]
default	13:26:06.001435-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>: none (role: None) (endowments: (null))
default	13:26:06.001718-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>: none (role: None) (endowments: (null))
default	13:26:06.001842-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 83671, name = Nexy
default	13:26:06.002521-0500	gamepolicyd	Received state update for 83671 (app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>, none-NotVisible
default	13:26:06.002624-0500	launchservicesd	Hit the server for a process handle 1d4f3238000146d7 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.E667CB0C-1B7B-45BE-B1FC-FA9A5CFF3794(501)>:83671]
default	13:26:06.004760-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x103103} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:26:06.004798-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a61c0: Nexy> state 3
default	13:26:06.004816-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:06.007261-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a61c0: Nexy> state 4
default	13:26:06.007275-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:09.059396-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:26:09.144618-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:26:09.144782-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:26:09.146500-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:26:09.148840-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:26:09.150592-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:26:09.150657-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87425 target:app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:09.150722-0500	runningboardd	Assertion 394-80102-87425 (target:app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>) will be created as active
default	13:26:09.153548-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:26:09.153574-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>
default	13:26:09.153588-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:26:09.153670-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:26:09.162776-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] is not RunningBoard jetsam managed.
default	13:26:09.162791-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] This process will not be managed.
default	13:26:09.162800-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]
default	13:26:09.162940-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:09.163470-0500	gamepolicyd	Hit the server for a process handle 116963c6000146fa that resolved to: [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]
default	13:26:09.163502-0500	gamepolicyd	Received state update for 83706 (app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>, running-active-NotVisible
default	13:26:09.165591-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]
default	13:26:09.165654-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] from originator [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87426 target:83706 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:26:09.165776-0500	runningboardd	Assertion 394-394-87426 (target:[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]) will be created as active
default	13:26:09.165955-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring jetsam update because this process is not memory-managed
default	13:26:09.165970-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring suspend because this process is not lifecycle managed
default	13:26:09.165991-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Set darwin role to: UserInteractive
default	13:26:09.166004-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring GPU update because this process is not GPU managed
default	13:26:09.166029-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring memory limit update because this process is not memory-managed
default	13:26:09.166111-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] reported to RB as running
default	13:26:09.167360-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83706" ID:394-357-87427 target:83706 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:09.167479-0500	runningboardd	Assertion 394-357-87427 (target:[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]) will be created as active
default	13:26:09.167656-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x105105 com.nexy.assistant starting stopped process.
default	13:26:09.168212-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring jetsam update because this process is not memory-managed
default	13:26:09.168252-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring suspend because this process is not lifecycle managed
default	13:26:09.168287-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring GPU update because this process is not GPU managed
default	13:26:09.168407-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:09.168343-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring memory limit update because this process is not memory-managed
default	13:26:09.168555-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 2
default	13:26:09.168581-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:09.168524-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]
default	13:26:09.170090-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:09.170404-0500	runningboardd	Invalidating assertion 394-80102-87425 (target:app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:26:09.170439-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring jetsam update because this process is not memory-managed
default	13:26:09.170481-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring suspend because this process is not lifecycle managed
default	13:26:09.170540-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring GPU update because this process is not GPU managed
default	13:26:09.170428-0500	gamepolicyd	Received state update for 83706 (app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>, running-active-NotVisible
default	13:26:09.170607-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring memory limit update because this process is not memory-managed
default	13:26:09.173089-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:09.179673-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:09.211579-0500	logger	detected new pid 83706 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:09.240422-0500	Nexy	[0x1026390c0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:26:09.240495-0500	Nexy	[0x102639680] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:26:09.276376-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring jetsam update because this process is not memory-managed
default	13:26:09.276390-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring suspend because this process is not lifecycle managed
default	13:26:09.276400-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring GPU update because this process is not GPU managed
default	13:26:09.276420-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] Ignoring memory limit update because this process is not memory-managed
default	13:26:09.276546-0500	gamepolicyd	Received state update for 83706 (app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>, running-active-NotVisible
default	13:26:09.278759-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:09.279100-0500	gamepolicyd	Received state update for 83706 (app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>, running-active-NotVisible
error	13:26:09.352524-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x9f80c0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:09.352750-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x9f80c0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:09.352958-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x9f80c0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:09.353157-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x9f80c0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:26:09.354329-0500	Nexy	[0x102631650] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:26:09.354939-0500	Nexy	[0x9f8288000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:26:09.355206-0500	Nexy	[0x9f8288140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:26:09.355552-0500	Nexy	[0x9f8288280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:26:09.355674-0500	Nexy	Received configuration update from daemon (initial)
default	13:26:09.357436-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:26:09.357742-0500	Nexy	[0x9f82883c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:09.358295-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83706.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:09.359702-0500	tccd	AUTHREQ_SUBJECT: msgID=83706.1, subject=com.nexy.assistant,
default	13:26:09.360403-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:09.378745-0500	Nexy	[0x9f82883c0] invalidated after the last release of the connection object
default	13:26:09.386411-0500	Nexy	server port 0x0000310f, session port 0x0000310f
default	13:26:09.387355-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.568, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:26:09.387378-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:09.388353-0500	tccd	AUTHREQ_SUBJECT: msgID=387.568, subject=com.nexy.assistant,
default	13:26:09.389523-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:09.409838-0500	Nexy	New connection 0xf20e3 main
default	13:26:09.412337-0500	Nexy	CHECKIN: pid=83706
default	13:26:09.423151-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83706" ID:394-357-87428 target:83706 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:09.423227-0500	runningboardd	Assertion 394-357-87428 (target:[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]) will be created as active
default	13:26:09.423634-0500	Nexy	CHECKEDIN: pid=83706 asn=0x0-0x105105 foreground=0
default	13:26:09.423625-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:09.423692-0500	runningboardd	Invalidating assertion 394-357-87427 (target:[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:26:09.423722-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:09.423496-0500	launchservicesd	CHECKIN:0x0-0x105105 83706 com.nexy.assistant
default	13:26:09.423872-0500	Nexy	[0x9f82883c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:09.423881-0500	Nexy	[0x9f82883c0] Connection returned listener port: 0x4e03
default	13:26:09.424305-0500	Nexy	[0x9f82b8300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x9f82883c0.peer[357].0x9f82b8300
default	13:26:09.426270-0500	Nexy	FRONTLOGGING: version 1
default	13:26:09.426306-0500	Nexy	Registered, pid=83706 ASN=0x0,0x105105
default	13:26:09.426738-0500	WindowServer	f20e3[CreateApplication]: Process creation: 0x0-0x105105 (Nexy) connectionID: F20E3 pid: 83706 in session 0x101
default	13:26:09.427131-0500	Nexy	[0x9f8288500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:26:09.428663-0500	Nexy	[0x9f82883c0] Connection returned listener port: 0x4e03
default	13:26:09.430664-0500	Nexy	BringForward: pid=83706 asn=0x0-0x105105 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:26:09.431077-0500	Nexy	BringFrontModifier: pid=83706 asn=0x0-0x105105 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:26:09.432410-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:26:09.434004-0500	Nexy	No persisted cache on this platform.
default	13:26:09.435034-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:26:09.435812-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:26:09.438596-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:26:09.438607-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:26:09.438668-0500	Nexy	Initializing connection
default	13:26:09.438707-0500	Nexy	Removing all cached process handles
default	13:26:09.439230-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] as ready
default	13:26:09.438735-0500	Nexy	Sending handshake request attempt #1 to server
default	13:26:09.438756-0500	Nexy	Creating connection to com.apple.runningboard
default	13:26:09.438766-0500	Nexy	[0x9f8288640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:26:09.440042-0500	Nexy	Handshake succeeded
default	13:26:09.440056-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>
default	13:26:09.440395-0500	Nexy	[0x9f82883c0] Connection returned listener port: 0x4e03
default	13:26:09.441596-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 83706
default	13:26:09.443908-0500	Nexy	[0x9f82883c0] Connection returned listener port: 0x4e03
default	13:26:09.454087-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:26:09.454106-0500	Nexy	[0x9f82888c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:26:09.454252-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:26:09.454339-0500	Nexy	[0x9f8288a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:10.258621-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D80FA825-DF12-40EB-9E94-FE4E4E7BAD34 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63103,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x6aa2d7d5 tp_proto=0x06"
default	13:26:10.258702-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63103<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533356 t_state: SYN_SENT process: Nexy:83706 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa7170937
default	13:26:10.259411-0500	kernel	tcp connected: [<IPv4-redacted>:63103<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533356 t_state: ESTABLISHED process: Nexy:83706 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa7170937
default	13:26:10.259699-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63103<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533356 t_state: FIN_WAIT_1 process: Nexy:83706 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xa7170937
default	13:26:10.259706-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63103<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533356 t_state: FIN_WAIT_1 process: Nexy:83706 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:26:10.300884-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:26:10.301589-0500	Nexy	[0x9f8288c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:26:10.302838-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4014","name":"Nexy(83706)"}, "details":{"PID":83706,"session_type":"Primary"} }
default	13:26:10.302922-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":83706}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4014, sessionType: 'prim', isRecording: false }, 
]
default	13:26:10.303730-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 83706, name = Nexy
default	13:26:10.304135-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x9f8317740 with ID: 0x1f4014
default	13:26:10.304424-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:26:10.305249-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:26:10.306664-0500	Nexy	[0x9f8288dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:26:10.309185-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A>
default	13:26:10.313821-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:26:10.315480-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:10.315676-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:10.315907-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:26:10.315918-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:26:10.315956-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:10.316112-0500	Nexy	[0x9f8288f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:26:10.316247-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:26:10.316726-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83706.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:10.324486-0500	tccd	AUTHREQ_SUBJECT: msgID=83706.2, subject=com.nexy.assistant,
default	13:26:10.325186-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:10.341716-0500	Nexy	[0x9f8288f00] invalidated after the last release of the connection object
default	13:26:10.341866-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:10.341912-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:10.342123-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:26:10.343224-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.322, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:10.344094-0500	tccd	AUTHREQ_SUBJECT: msgID=395.322, subject=com.nexy.assistant,
default	13:26:10.344671-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:26:10.360491-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:26:10.361422-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.324, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:10.362354-0500	tccd	AUTHREQ_SUBJECT: msgID=395.324, subject=com.nexy.assistant,
default	13:26:10.362929-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:10.376986-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:26:10.377001-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x9f6d30680> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:26:10.390039-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:10.390796-0500	Nexy	[0x9f8288f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:26:10.391144-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=359514532478977 }
default	13:26:10.391223-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:26:10.391263-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:26:10.391299-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:26:10.401618-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:26:10.434389-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:26:10.434413-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:26:10.438348-0500	Nexy	[0x9f8289040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:26:10.447585-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9f9684040) Selecting device 71 from constructor
default	13:26:10.447593-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9f9684040)
default	13:26:10.447598-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9f9684040) not already running
default	13:26:10.447603-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9f9684040) nothing to teardown
default	13:26:10.447607-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9f9684040) connecting device 71
default	13:26:10.447690-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9f9684040) Device ID: 71 (Input:No | Output:Yes): true
default	13:26:10.447767-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9f9684040) created ioproc 0xa for device 71
default	13:26:10.447860-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9f9684040) adding 7 device listeners to device 71
default	13:26:10.448004-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9f9684040) adding 0 device delegate listeners to device 71
default	13:26:10.448012-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9f9684040)
default	13:26:10.448069-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:10.448076-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:26:10.448084-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:10.448091-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:26:10.448098-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:26:10.448174-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9f9684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:26:10.448183-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9f9684040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:26:10.448187-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:26:10.448190-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9f9684040) removing 0 device listeners from device 0
default	13:26:10.448194-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9f9684040) removing 0 device delegate listeners from device 0
default	13:26:10.448198-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9f9684040)
default	13:26:10.448236-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:26:10.448468-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:10.449412-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:26:10.449453-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:26:10.449573-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9f6d78330, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:10.449595-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:10.450851-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:10.451019-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:10.452687-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:10.452853-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:10.453828-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9f6d782d0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:10.453840-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:10.454113-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:10.454765-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9f6d78720, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:10.454773-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9f6d78720: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:10.454776-0500	Nexy	AudioConverter -> 0x9f6d78720: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:10.454778-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:10.454785-0500	Nexy	AudioConverter -> 0x9f6d78720: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:10.454791-0500	Nexy	AudioConverter -> 0x9f6d78720: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:10.455502-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9f6d782d0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:10.455508-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9f6d782d0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:10.455511-0500	Nexy	AudioConverter -> 0x9f6d782d0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:10.455513-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:10.455519-0500	Nexy	AudioConverter -> 0x9f6d782d0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:10.455528-0500	Nexy	AudioConverter -> 0x9f6d782d0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:10.455643-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9f6d782d0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:10.489429-0500	Nexy	[0x9f8289180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:10.489943-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:10.490123-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83706.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:10.491092-0500	tccd	AUTHREQ_SUBJECT: msgID=83706.3, subject=com.nexy.assistant,
default	13:26:10.491751-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:10.510085-0500	Nexy	[0x9f8289180] invalidated after the last release of the connection object
default	13:26:10.510169-0500	Nexy	[0x9f8289180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:10.510582-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:10.510746-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83706.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:10.511604-0500	tccd	AUTHREQ_SUBJECT: msgID=83706.4, subject=com.nexy.assistant,
default	13:26:10.512204-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:10.529793-0500	Nexy	[0x9f8289180] invalidated after the last release of the connection object
default	13:26:10.529856-0500	Nexy	[0x9f8289180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:26:10.529938-0500	Nexy	[0x9f8289180] invalidated after the last release of the connection object
default	13:26:10.773463-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83716.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83716, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83716, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:10.775079-0500	tccd	AUTHREQ_SUBJECT: msgID=83716.1, subject=com.nexy.assistant,
default	13:26:10.775762-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:10.796154-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83716.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83716, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83716, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:10.797008-0500	tccd	AUTHREQ_SUBJECT: msgID=83716.2, subject=com.nexy.assistant,
default	13:26:10.797610-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:10.837564-0500	Nexy	[0x9f8289540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:10.838311-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83706.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83706, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:10.845185-0500	tccd	AUTHREQ_SUBJECT: msgID=83706.5, subject=com.nexy.assistant,
default	13:26:10.845843-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:10.863606-0500	Nexy	[0x9f8289540] invalidated after the last release of the connection object
default	13:26:10.893667-0500	Nexy	server port 0x00011203, session port 0x0000310f
default	13:26:12.224711-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	13:26:12.937570-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x105105 (Nexy) connectionID: F20E3 pid: 83706 in session 0x101
default	13:26:12.938019-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f4014","name":"Nexy(83706)"}, "details":null }
default	13:26:12.937627-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x105105 (Nexy) acq:0xb6c3625a0 count:1
default	13:26:12.938071-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f4014 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":83706})
default	13:26:12.938096-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":83706})
default	13:26:12.938638-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 21, PID = 83706, Name = sid:0x1f4014, Nexy(83706), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:26:12.938930-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 21, PID = 83706, Name = sid:0x1f4014, Nexy(83706), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:26:12.939651-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:12.939743-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:12.943372-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x105105 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x105105 (Nexy)"
)}
default	13:26:12.945298-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x146fa removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x105105 (Nexy)"
)}
default	13:26:12.939269-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:12.939503-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:12.939922-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:12.939986-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:12.952975-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706] termination reported by launchd (0, 0, 0)
default	13:26:12.953035-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]
default	13:26:12.953345-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]
default	13:26:12.953578-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]
default	13:26:12.953627-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]
default	13:26:12.954796-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]
default	13:26:12.957659-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>: none (role: None) (endowments: (null))
default	13:26:12.957866-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>: none (role: None) (endowments: (null))
default	13:26:12.957974-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 83706, name = Nexy
default	13:26:12.958566-0500	launchservicesd	Hit the server for a process handle 116963c6000146fa that resolved to: [app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>:83706]
default	13:26:12.958756-0500	gamepolicyd	Received state update for 83706 (app<application.com.nexy.assistant.38522673.38522682.875151E2-401C-4049-831F-5D25E725367A(501)>, none-NotVisible
default	13:26:12.960437-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x105105} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:26:12.960488-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 3
default	13:26:12.960505-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:12.962665-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 4
default	13:26:12.962677-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:16.021558-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:26:16.111670-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:26:16.111859-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:26:16.113565-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:26:16.116756-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:26:16.118947-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:26:16.119060-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87443 target:app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:16.119162-0500	runningboardd	Assertion 394-80102-87443 (target:app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>) will be created as active
default	13:26:16.121835-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:26:16.121876-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>
default	13:26:16.121890-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:26:16.121984-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:26:16.137018-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] is not RunningBoard jetsam managed.
default	13:26:16.137034-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] This process will not be managed.
default	13:26:16.137044-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]
default	13:26:16.137183-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:16.140974-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]
default	13:26:16.141071-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] from originator [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87444 target:83736 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:26:16.141249-0500	runningboardd	Assertion 394-394-87444 (target:[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]) will be created as active
default	13:26:16.141458-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring jetsam update because this process is not memory-managed
default	13:26:16.141472-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring suspend because this process is not lifecycle managed
default	13:26:16.141486-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Set darwin role to: UserInteractive
default	13:26:16.141495-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring GPU update because this process is not GPU managed
default	13:26:16.141570-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring memory limit update because this process is not memory-managed
default	13:26:16.141805-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] reported to RB as running
default	13:26:16.143059-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring jetsam update because this process is not memory-managed
default	13:26:16.143091-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring suspend because this process is not lifecycle managed
default	13:26:16.143114-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring GPU update because this process is not GPU managed
default	13:26:16.143177-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring memory limit update because this process is not memory-managed
default	13:26:16.143359-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]
default	13:26:16.144304-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83736" ID:394-357-87445 target:83736 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:16.144388-0500	runningboardd	Assertion 394-357-87445 (target:[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]) will be created as active
default	13:26:16.144987-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x106106 com.nexy.assistant starting stopped process.
default	13:26:16.147481-0500	kernel	Nexy[83736] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0xb996138472df45d1. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:26:16.147499-0500	kernel	Nexy[83736] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0xb996138472df45d1. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:26:16.148273-0500	gamepolicyd	Hit the server for a process handle 13541d7a00014718 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]
default	13:26:16.148196-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:16.148355-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 2
default	13:26:16.148334-0500	gamepolicyd	Received state update for 83736 (app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>, running-active-NotVisible
default	13:26:16.148375-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:16.149302-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:16.149679-0500	runningboardd	Invalidating assertion 394-80102-87443 (target:app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:26:16.149713-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring jetsam update because this process is not memory-managed
default	13:26:16.149754-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring suspend because this process is not lifecycle managed
default	13:26:16.149787-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring GPU update because this process is not GPU managed
default	13:26:16.149838-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring memory limit update because this process is not memory-managed
default	13:26:16.149811-0500	gamepolicyd	Received state update for 83736 (app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>, running-active-NotVisible
default	13:26:16.153740-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:16.161320-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:16.196646-0500	logger	detected new pid 83736 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:16.220343-0500	Nexy	[0x106264980] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:26:16.220422-0500	Nexy	[0x106264ec0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:26:16.253232-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring jetsam update because this process is not memory-managed
default	13:26:16.253243-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring suspend because this process is not lifecycle managed
default	13:26:16.253253-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring GPU update because this process is not GPU managed
default	13:26:16.253390-0500	gamepolicyd	Received state update for 83736 (app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>, running-active-NotVisible
default	13:26:16.253273-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] Ignoring memory limit update because this process is not memory-managed
default	13:26:16.255805-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:16.256078-0500	gamepolicyd	Received state update for 83736 (app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>, running-active-NotVisible
error	13:26:16.332071-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xbe04dc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:16.332297-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xbe04dc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:16.332496-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xbe04dc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:16.332698-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xbe04dc000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:26:16.334106-0500	Nexy	[0x106271180] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:26:16.334842-0500	Nexy	[0xbe0680000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:26:16.335136-0500	Nexy	[0xbe0680140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:26:16.335546-0500	Nexy	[0xbe0680280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:26:16.335692-0500	Nexy	Received configuration update from daemon (initial)
default	13:26:16.337477-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:26:16.337830-0500	Nexy	[0xbe06803c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:16.338510-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83736.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:16.340118-0500	tccd	AUTHREQ_SUBJECT: msgID=83736.1, subject=com.nexy.assistant,
default	13:26:16.340903-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:16.359787-0500	Nexy	[0xbe06803c0] invalidated after the last release of the connection object
default	13:26:16.360060-0500	Nexy	server port 0x00003413, session port 0x00003413
default	13:26:16.360945-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.569, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:26:16.360971-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:16.361788-0500	tccd	AUTHREQ_SUBJECT: msgID=387.569, subject=com.nexy.assistant,
default	13:26:16.362479-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:16.386830-0500	Nexy	New connection 0x9914f main
default	13:26:16.389719-0500	Nexy	CHECKIN: pid=83736
default	13:26:16.400196-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83736" ID:394-357-87448 target:83736 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:16.400302-0500	runningboardd	Assertion 394-357-87448 (target:[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]) will be created as active
default	13:26:16.400355-0500	Nexy	CHECKEDIN: pid=83736 asn=0x0-0x106106 foreground=0
default	13:26:16.400240-0500	launchservicesd	CHECKIN:0x0-0x106106 83736 com.nexy.assistant
default	13:26:16.400960-0500	runningboardd	Invalidating assertion 394-357-87445 (target:[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:26:16.400662-0500	Nexy	[0xbe06803c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:16.400696-0500	Nexy	[0xbe06803c0] Connection returned listener port: 0x4903
default	13:26:16.400868-0500	Nexy	[0xbe0694300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xbe06803c0.peer[357].0xbe0694300
default	13:26:16.403127-0500	Nexy	FRONTLOGGING: version 1
default	13:26:16.403156-0500	Nexy	Registered, pid=83736 ASN=0x0,0x106106
default	13:26:16.403520-0500	WindowServer	9914f[CreateApplication]: Process creation: 0x0-0x106106 (Nexy) connectionID: 9914F pid: 83736 in session 0x101
default	13:26:16.402632-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:16.402791-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:16.406857-0500	Nexy	[0xbe06803c0] Connection returned listener port: 0x4903
default	13:26:16.407499-0500	Nexy	[0xbe0680500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:26:16.408952-0500	Nexy	BringForward: pid=83736 asn=0x0-0x106106 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:26:16.409342-0500	Nexy	BringFrontModifier: pid=83736 asn=0x0-0x106106 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:26:16.410273-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:26:16.411962-0500	Nexy	No persisted cache on this platform.
default	13:26:16.413338-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:26:16.414000-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:26:16.418597-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:26:16.418607-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:26:16.418685-0500	Nexy	Initializing connection
default	13:26:16.418736-0500	Nexy	Removing all cached process handles
default	13:26:16.418781-0500	Nexy	Sending handshake request attempt #1 to server
default	13:26:16.418791-0500	Nexy	Creating connection to com.apple.runningboard
default	13:26:16.418802-0500	Nexy	[0xbe0680640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:26:16.419630-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] as ready
default	13:26:16.420514-0500	Nexy	Handshake succeeded
default	13:26:16.420533-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>
default	13:26:16.420686-0500	Nexy	[0xbe06803c0] Connection returned listener port: 0x4903
default	13:26:16.422076-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 83736
default	13:26:16.425192-0500	Nexy	[0xbe06803c0] Connection returned listener port: 0x4903
default	13:26:16.430124-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:26:16.430198-0500	Nexy	[0xbe0680780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:26:16.430386-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:26:16.430569-0500	Nexy	[0xbe0680a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:17.239861-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6AECD316-68AA-4402-AB91-56E2482C0CFB flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63115,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xce7519ef tp_proto=0x06"
default	13:26:17.239905-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63115<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533434 t_state: SYN_SENT process: Nexy:83736 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8e15b522
default	13:26:17.240396-0500	kernel	tcp connected: [<IPv4-redacted>:63115<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533434 t_state: ESTABLISHED process: Nexy:83736 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8e15b522
default	13:26:17.240693-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63115<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533434 t_state: FIN_WAIT_1 process: Nexy:83736 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8e15b522
default	13:26:17.240701-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63115<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533434 t_state: FIN_WAIT_1 process: Nexy:83736 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:26:17.276446-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:26:17.276947-0500	Nexy	[0xbe0680c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:26:17.277744-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4015","name":"Nexy(83736)"}, "details":{"PID":83736,"session_type":"Primary"} }
default	13:26:17.277820-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":83736}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4015, sessionType: 'prim', isRecording: false }, 
]
default	13:26:17.278400-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 83736, name = Nexy
default	13:26:17.278681-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xbe06f79a0 with ID: 0x1f4015
default	13:26:17.278940-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:26:17.279583-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:26:17.280889-0500	Nexy	[0xbe0680dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:26:17.282757-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0 AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0>
default	13:26:17.286984-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:26:17.288445-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:17.288819-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:17.288964-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:26:17.288975-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:26:17.289001-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:17.289124-0500	Nexy	[0xbe0680f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:26:17.289207-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:26:17.289563-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83736.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:17.297049-0500	tccd	AUTHREQ_SUBJECT: msgID=83736.2, subject=com.nexy.assistant,
default	13:26:17.297709-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:17.316406-0500	Nexy	[0xbe0680f00] invalidated after the last release of the connection object
default	13:26:17.316567-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:17.316617-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:17.316859-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:26:17.318053-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.325, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:17.318960-0500	tccd	AUTHREQ_SUBJECT: msgID=395.325, subject=com.nexy.assistant,
default	13:26:17.319538-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:26:17.335928-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:26:17.336781-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.327, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:17.337636-0500	tccd	AUTHREQ_SUBJECT: msgID=395.327, subject=com.nexy.assistant,
default	13:26:17.338186-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:17.352586-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:26:17.352605-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xbdf050600> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:26:17.366203-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:17.367055-0500	Nexy	[0xbe0680f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:26:17.367420-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=359643381497857 }
default	13:26:17.367522-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:26:17.367559-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:26:17.367590-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:26:17.377175-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:26:17.414251-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:26:17.414277-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:26:17.417880-0500	Nexy	[0xbe0681040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:26:17.426506-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbe19dc040) Selecting device 71 from constructor
default	13:26:17.426517-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbe19dc040)
default	13:26:17.426522-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbe19dc040) not already running
default	13:26:17.426527-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbe19dc040) nothing to teardown
default	13:26:17.426532-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbe19dc040) connecting device 71
default	13:26:17.426598-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbe19dc040) Device ID: 71 (Input:No | Output:Yes): true
default	13:26:17.426661-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbe19dc040) created ioproc 0xa for device 71
default	13:26:17.426749-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbe19dc040) adding 7 device listeners to device 71
default	13:26:17.426877-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbe19dc040) adding 0 device delegate listeners to device 71
default	13:26:17.426882-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbe19dc040)
default	13:26:17.426940-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:17.426947-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:26:17.426958-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:17.426963-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:26:17.426970-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:26:17.427042-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbe19dc040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:26:17.427052-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbe19dc040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:26:17.427057-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:26:17.427061-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbe19dc040) removing 0 device listeners from device 0
default	13:26:17.427063-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbe19dc040) removing 0 device delegate listeners from device 0
default	13:26:17.427067-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbe19dc040)
default	13:26:17.427109-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:26:17.427340-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:17.428240-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:26:17.428277-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:26:17.428404-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbdfbd1f20, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:17.428423-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:17.429642-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:17.429822-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:17.431253-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:17.431420-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:17.432420-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbdfbd1ec0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:17.432430-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:17.432692-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:17.433386-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbdfbd2310, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:17.433397-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xbdfbd2310: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:17.433402-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:17.433403-0500	Nexy	AudioConverter -> 0xbdfbd2310: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:17.433413-0500	Nexy	AudioConverter -> 0xbdfbd2310: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:17.433418-0500	Nexy	AudioConverter -> 0xbdfbd2310: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:17.434144-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xbdfbd1ec0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:17.434154-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xbdfbd1ec0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:17.434158-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:17.434159-0500	Nexy	AudioConverter -> 0xbdfbd1ec0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:17.434166-0500	Nexy	AudioConverter -> 0xbdfbd1ec0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:17.434176-0500	Nexy	AudioConverter -> 0xbdfbd1ec0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:17.434284-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xbdfbd1ec0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:17.468106-0500	Nexy	[0xbe0681180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:17.468624-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:17.468794-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83736.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:17.469769-0500	tccd	AUTHREQ_SUBJECT: msgID=83736.3, subject=com.nexy.assistant,
default	13:26:17.470597-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:17.490343-0500	Nexy	[0xbe0681180] invalidated after the last release of the connection object
default	13:26:17.490422-0500	Nexy	[0xbe0681180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:17.490777-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:17.490945-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83736.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:17.491683-0500	tccd	AUTHREQ_SUBJECT: msgID=83736.4, subject=com.nexy.assistant,
default	13:26:17.492294-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:17.509607-0500	Nexy	[0xbe0681180] invalidated after the last release of the connection object
default	13:26:17.509669-0500	Nexy	[0xbe0681180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:26:17.509752-0500	Nexy	[0xbe0681180] invalidated after the last release of the connection object
default	13:26:17.756217-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83746.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83746, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83746, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:17.757852-0500	tccd	AUTHREQ_SUBJECT: msgID=83746.1, subject=com.nexy.assistant,
default	13:26:17.758546-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:17.779552-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83746.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83746, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83746, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:17.780344-0500	tccd	AUTHREQ_SUBJECT: msgID=83746.2, subject=com.nexy.assistant,
default	13:26:17.780955-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:17.819751-0500	Nexy	[0xbe0681540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:17.820497-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83736.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83736, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:17.827281-0500	tccd	AUTHREQ_SUBJECT: msgID=83736.5, subject=com.nexy.assistant,
default	13:26:17.827959-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:17.845696-0500	Nexy	[0xbe0681540] invalidated after the last release of the connection object
default	13:26:17.874377-0500	Nexy	server port 0x00014703, session port 0x00003413
default	13:26:19.921802-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x106106 (Nexy) connectionID: 9914F pid: 83736 in session 0x101
default	13:26:19.921849-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x106106 (Nexy) acq:0xb6c361aa0 count:1
default	13:26:19.922049-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f4015","name":"Nexy(83736)"}, "details":null }
default	13:26:19.922080-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f4015 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":83736})
default	13:26:19.922094-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":83736})
default	13:26:19.922297-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 22, PID = 83736, Name = sid:0x1f4015, Nexy(83736), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:26:19.922369-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 22, PID = 83736, Name = sid:0x1f4015, Nexy(83736), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:26:19.922509-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:19.922651-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:19.922766-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:19.922832-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:19.922857-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:19.922985-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:19.922951-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x106106 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x106106 (Nexy)"
)}
default	13:26:19.923324-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x14718 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x106106 (Nexy)"
)}
default	13:26:19.928678-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]
default	13:26:19.939078-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736] termination reported by launchd (0, 0, 0)
default	13:26:19.939129-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]
default	13:26:19.939426-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]
default	13:26:19.939655-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]
default	13:26:19.939697-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]
default	13:26:19.943937-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>: none (role: None) (endowments: (null))
default	13:26:19.944135-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>: none (role: None) (endowments: (null))
default	13:26:19.944252-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 83736, name = Nexy
default	13:26:19.944700-0500	launchservicesd	Hit the server for a process handle 13541d7a00014718 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>:83736]
default	13:26:19.944982-0500	gamepolicyd	Received state update for 83736 (app<application.com.nexy.assistant.38522673.38522682.42E117E8-C6E5-41CF-A72A-7FFEC68EAFF0(501)>, none-NotVisible
default	13:26:19.946480-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x106106} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:26:19.946512-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 3
default	13:26:19.946532-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:19.948054-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 4
default	13:26:19.948065-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:23.005465-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:26:23.103655-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:26:23.103846-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:26:23.105451-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:26:23.107742-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:26:23.112198-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:26:23.112354-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87463 target:app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:23.112472-0500	runningboardd	Assertion 394-80102-87463 (target:app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>) will be created as active
default	13:26:23.115333-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:26:23.115389-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>
default	13:26:23.115401-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:26:23.115559-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:26:23.133513-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] is not RunningBoard jetsam managed.
default	13:26:23.133553-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] This process will not be managed.
default	13:26:23.133568-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]
default	13:26:23.133791-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:23.138991-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]
default	13:26:23.139101-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] from originator [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87464 target:83766 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:26:23.139296-0500	runningboardd	Assertion 394-394-87464 (target:[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]) will be created as active
default	13:26:23.139586-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring jetsam update because this process is not memory-managed
default	13:26:23.139601-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring suspend because this process is not lifecycle managed
default	13:26:23.139620-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Set darwin role to: UserInteractive
default	13:26:23.139636-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring GPU update because this process is not GPU managed
default	13:26:23.139652-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring memory limit update because this process is not memory-managed
default	13:26:23.139775-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] reported to RB as running
default	13:26:23.141041-0500	gamepolicyd	Hit the server for a process handle 116fa43100014736 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]
default	13:26:23.141120-0500	gamepolicyd	Received state update for 83766 (app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>, running-active-NotVisible
default	13:26:23.141851-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring jetsam update because this process is not memory-managed
default	13:26:23.141896-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring suspend because this process is not lifecycle managed
default	13:26:23.141927-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring GPU update because this process is not GPU managed
default	13:26:23.142002-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring memory limit update because this process is not memory-managed
default	13:26:23.142124-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]
default	13:26:23.142643-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83766" ID:394-357-87465 target:83766 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:23.142759-0500	runningboardd	Assertion 394-357-87465 (target:[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]) will be created as active
default	13:26:23.143018-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x107107 com.nexy.assistant starting stopped process.
default	13:26:23.144185-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:23.144396-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 2
default	13:26:23.144423-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:23.145649-0500	kernel	Nexy[83766] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0x8aa3385217993207. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:26:23.145673-0500	kernel	Nexy[83766] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0x8aa3385217993207. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:26:23.145476-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:23.146092-0500	runningboardd	Invalidating assertion 394-80102-87463 (target:app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:26:23.146157-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring jetsam update because this process is not memory-managed
default	13:26:23.146199-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring suspend because this process is not lifecycle managed
default	13:26:23.146234-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring GPU update because this process is not GPU managed
default	13:26:23.146281-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring memory limit update because this process is not memory-managed
default	13:26:23.150223-0500	gamepolicyd	Received state update for 83766 (app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>, running-active-NotVisible
default	13:26:23.150002-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:23.165244-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:23.214006-0500	logger	detected new pid 83766 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:23.231694-0500	Nexy	[0x103b349e0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:26:23.231764-0500	Nexy	[0x103b34f20] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:26:23.251476-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring jetsam update because this process is not memory-managed
default	13:26:23.251488-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring suspend because this process is not lifecycle managed
default	13:26:23.251499-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring GPU update because this process is not GPU managed
default	13:26:23.251519-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] Ignoring memory limit update because this process is not memory-managed
default	13:26:23.251661-0500	gamepolicyd	Received state update for 83766 (app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>, running-active-NotVisible
default	13:26:23.254232-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:23.254750-0500	gamepolicyd	Received state update for 83766 (app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>, running-active-NotVisible
error	13:26:23.363898-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x8f6100000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:23.364132-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x8f6100000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:23.364336-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x8f6100000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:23.364532-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x8f6100000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:26:23.365761-0500	Nexy	[0x103b24800] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:26:23.366374-0500	Nexy	[0x8f627c000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:26:23.366653-0500	Nexy	[0x8f627c140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:26:23.366981-0500	Nexy	[0x8f627c280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:26:23.368807-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:26:23.369148-0500	Nexy	[0x8f627c3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:23.369415-0500	Nexy	Received configuration update from daemon (initial)
default	13:26:23.369752-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83766.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:23.371655-0500	tccd	AUTHREQ_SUBJECT: msgID=83766.1, subject=com.nexy.assistant,
default	13:26:23.373034-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:23.394170-0500	Nexy	[0x8f627c3c0] invalidated after the last release of the connection object
default	13:26:23.394383-0500	Nexy	server port 0x0000370f, session port 0x0000370f
default	13:26:23.395230-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.570, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:26:23.395253-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:23.396186-0500	tccd	AUTHREQ_SUBJECT: msgID=387.570, subject=com.nexy.assistant,
default	13:26:23.397293-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:23.433770-0500	Nexy	[0x8f627c3c0] Connection returned listener port: 0x4703
default	13:26:23.433985-0500	Nexy	[0x8f6294300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x8f627c3c0.peer[357].0x8f6294300
default	13:26:23.438636-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:26:23.440330-0500	Nexy	No persisted cache on this platform.
default	13:26:23.441479-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:26:23.446640-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:26:23.446650-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:26:23.446711-0500	Nexy	Initializing connection
default	13:26:23.446752-0500	Nexy	Removing all cached process handles
default	13:26:23.446774-0500	Nexy	Sending handshake request attempt #1 to server
default	13:26:23.446783-0500	Nexy	Creating connection to com.apple.runningboard
default	13:26:23.446790-0500	Nexy	[0x8f627c8c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:26:23.447309-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] as ready
default	13:26:23.455312-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:26:23.455338-0500	Nexy	[0x8f627c640] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:26:23.455434-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:26:23.455522-0500	Nexy	[0x8f627ca00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:24.261574-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0BA7BFF5-0157-4019-9A90-231DABC4C573 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63132,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x74e4f37f tp_proto=0x06"
default	13:26:24.261650-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63132<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533552 t_state: SYN_SENT process: Nexy:83766 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x958ab82a
default	13:26:24.262243-0500	kernel	tcp connected: [<IPv4-redacted>:63132<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533552 t_state: ESTABLISHED process: Nexy:83766 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x958ab82a
default	13:26:24.262532-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63132<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533552 t_state: FIN_WAIT_1 process: Nexy:83766 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x958ab82a
default	13:26:24.262543-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63132<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533552 t_state: FIN_WAIT_1 process: Nexy:83766 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:26:24.299674-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:26:24.300321-0500	Nexy	[0x8f627cc80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:26:24.301429-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4016","name":"Nexy(83766)"}, "details":{"PID":83766,"session_type":"Primary"} }
default	13:26:24.301512-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":83766}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4016, sessionType: 'prim', isRecording: false }, 
]
default	13:26:24.302274-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 83766, name = Nexy
default	13:26:24.302628-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x8f62ff680 with ID: 0x1f4016
default	13:26:24.302925-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:26:24.303711-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:26:24.305094-0500	Nexy	[0x8f627cdc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:26:24.307353-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5 AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5>
default	13:26:24.311930-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:26:24.313519-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:24.313700-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:24.313858-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:26:24.313870-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:26:24.313900-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:24.314035-0500	Nexy	[0x8f627cf00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:26:24.314178-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:26:24.314558-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83766.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:24.322864-0500	tccd	AUTHREQ_SUBJECT: msgID=83766.2, subject=com.nexy.assistant,
default	13:26:24.323718-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:24.340055-0500	Nexy	[0x8f627cf00] invalidated after the last release of the connection object
default	13:26:24.340195-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:24.340239-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:24.340428-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:26:24.341469-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.328, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:24.342242-0500	tccd	AUTHREQ_SUBJECT: msgID=395.328, subject=com.nexy.assistant,
default	13:26:24.342777-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:26:24.358513-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:26:24.359374-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.330, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:24.360192-0500	tccd	AUTHREQ_SUBJECT: msgID=395.330, subject=com.nexy.assistant,
default	13:26:24.360761-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:24.374804-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:26:24.374821-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x8f52c46a0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:26:24.387686-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:24.388541-0500	Nexy	[0x8f627cf00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:26:24.388884-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=359772230516737 }
default	13:26:24.388964-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:26:24.389008-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:26:24.389048-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:26:24.398647-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:26:24.432090-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:26:24.432111-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:26:24.435647-0500	Nexy	[0x8f627d040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:26:24.444618-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x8f7e0aa40) Selecting device 71 from constructor
default	13:26:24.444628-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x8f7e0aa40)
default	13:26:24.444633-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x8f7e0aa40) not already running
default	13:26:24.444639-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x8f7e0aa40) nothing to teardown
default	13:26:24.444643-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x8f7e0aa40) connecting device 71
default	13:26:24.444713-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x8f7e0aa40) Device ID: 71 (Input:No | Output:Yes): true
default	13:26:24.444788-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x8f7e0aa40) created ioproc 0xa for device 71
default	13:26:24.444875-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x8f7e0aa40) adding 7 device listeners to device 71
default	13:26:24.445023-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x8f7e0aa40) adding 0 device delegate listeners to device 71
default	13:26:24.445029-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x8f7e0aa40)
default	13:26:24.445086-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:24.445095-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:26:24.445100-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:24.445110-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:26:24.445116-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:26:24.445192-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x8f7e0aa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:26:24.445199-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x8f7e0aa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:26:24.445204-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:26:24.445208-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x8f7e0aa40) removing 0 device listeners from device 0
default	13:26:24.445211-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x8f7e0aa40) removing 0 device delegate listeners from device 0
default	13:26:24.445214-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x8f7e0aa40)
default	13:26:24.445250-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:26:24.445472-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:24.446363-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:26:24.446404-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:26:24.446522-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8f52ec180, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:24.446543-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:24.447689-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:24.447858-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:24.449502-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:24.449668-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:24.450601-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8f52ec120, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:24.450613-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:24.450864-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:24.451471-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8f52ec570, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:24.451478-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8f52ec570: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:24.451483-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:24.451484-0500	Nexy	AudioConverter -> 0x8f52ec570: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:24.451493-0500	Nexy	AudioConverter -> 0x8f52ec570: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:24.451498-0500	Nexy	AudioConverter -> 0x8f52ec570: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:24.452189-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8f52ec120, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:24.452198-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8f52ec120: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:24.452199-0500	Nexy	AudioConverter -> 0x8f52ec120: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:24.452203-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:24.452208-0500	Nexy	AudioConverter -> 0x8f52ec120: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:24.452212-0500	Nexy	AudioConverter -> 0x8f52ec120: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:24.452325-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8f52ec120: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:24.485404-0500	Nexy	[0x8f627d180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:24.485873-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:24.486035-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83766.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:24.486958-0500	tccd	AUTHREQ_SUBJECT: msgID=83766.3, subject=com.nexy.assistant,
default	13:26:24.487574-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:24.505670-0500	Nexy	[0x8f627d180] invalidated after the last release of the connection object
default	13:26:24.505748-0500	Nexy	[0x8f627d180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:24.506089-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:24.506238-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83766.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:24.506948-0500	tccd	AUTHREQ_SUBJECT: msgID=83766.4, subject=com.nexy.assistant,
default	13:26:24.507533-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:24.525033-0500	Nexy	[0x8f627d180] invalidated after the last release of the connection object
default	13:26:24.525096-0500	Nexy	[0x8f627d180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:26:24.525177-0500	Nexy	[0x8f627d180] invalidated after the last release of the connection object
default	13:26:24.776264-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83776.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83776, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83776, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:24.777887-0500	tccd	AUTHREQ_SUBJECT: msgID=83776.1, subject=com.nexy.assistant,
default	13:26:24.778592-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:24.800143-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83776.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83776, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83776, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:24.801198-0500	tccd	AUTHREQ_SUBJECT: msgID=83776.2, subject=com.nexy.assistant,
default	13:26:24.802232-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:24.840146-0500	Nexy	[0x8f627d540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:24.840792-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83766.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83766, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:24.847603-0500	tccd	AUTHREQ_SUBJECT: msgID=83766.5, subject=com.nexy.assistant,
default	13:26:24.848292-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:24.866142-0500	Nexy	[0x8f627d540] invalidated after the last release of the connection object
default	13:26:24.896565-0500	Nexy	server port 0x00014203, session port 0x0000370f
default	13:26:26.808654-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	13:26:26.940486-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f4016","name":"Nexy(83766)"}, "details":null }
default	13:26:26.940519-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f4016 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":83766})
default	13:26:26.940531-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":83766})
default	13:26:26.940293-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x107107 (Nexy) connectionID: 5D1AF pid: 83766 in session 0x101
default	13:26:26.940355-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x107107 (Nexy) acq:0xb6c361b60 count:1
default	13:26:26.940759-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 23, PID = 83766, Name = sid:0x1f4016, Nexy(83766), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:26:26.940844-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 23, PID = 83766, Name = sid:0x1f4016, Nexy(83766), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:26:26.940979-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:26.941162-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:26.941226-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:26.941282-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:26.941303-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:26.941407-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:26.941580-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x107107 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x107107 (Nexy)"
)}
default	13:26:26.941852-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x14736 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x107107 (Nexy)"
)}
default	13:26:26.954467-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]
default	13:26:26.957478-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766] termination reported by launchd (0, 0, 0)
default	13:26:26.957597-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]
default	13:26:26.957837-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]
default	13:26:26.958067-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]
default	13:26:26.958115-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]
default	13:26:26.962639-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>: none (role: None) (endowments: (null))
default	13:26:26.962867-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>: none (role: None) (endowments: (null))
default	13:26:26.963015-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 83766, name = Nexy
default	13:26:26.963985-0500	launchservicesd	Hit the server for a process handle 116fa43100014736 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>:83766]
default	13:26:26.964073-0500	gamepolicyd	Received state update for 83766 (app<application.com.nexy.assistant.38522673.38522682.492FFAAB-8B01-4900-8508-30757777D9B5(501)>, none-NotVisible
default	13:26:26.966643-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x107107} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:26:26.966676-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 3
default	13:26:26.966694-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:26.969834-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 4
default	13:26:26.969851-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:30.032567-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:26:30.126245-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:26:30.126416-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:26:30.128528-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:26:30.130842-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:26:30.133008-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:26:30.133100-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87497 target:app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:30.133183-0500	runningboardd	Assertion 394-80102-87497 (target:app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>) will be created as active
default	13:26:30.135864-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:26:30.135898-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>
default	13:26:30.135910-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:26:30.135999-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:26:30.149287-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] is not RunningBoard jetsam managed.
default	13:26:30.149302-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] This process will not be managed.
default	13:26:30.149312-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]
default	13:26:30.149507-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:30.150130-0500	gamepolicyd	Hit the server for a process handle e965dd500014759 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]
default	13:26:30.150172-0500	gamepolicyd	Received state update for 83801 (app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>, running-active-NotVisible
default	13:26:30.152309-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]
default	13:26:30.152378-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] from originator [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87498 target:83801 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:26:30.152504-0500	runningboardd	Assertion 394-394-87498 (target:[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]) will be created as active
default	13:26:30.152699-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring jetsam update because this process is not memory-managed
default	13:26:30.152726-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring suspend because this process is not lifecycle managed
default	13:26:30.152749-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Set darwin role to: UserInteractive
default	13:26:30.152765-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring GPU update because this process is not GPU managed
default	13:26:30.152797-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring memory limit update because this process is not memory-managed
default	13:26:30.152859-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] reported to RB as running
default	13:26:30.154021-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring jetsam update because this process is not memory-managed
default	13:26:30.154050-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring suspend because this process is not lifecycle managed
default	13:26:30.154084-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring GPU update because this process is not GPU managed
default	13:26:30.154148-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring memory limit update because this process is not memory-managed
default	13:26:30.154247-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]
default	13:26:30.154361-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83801" ID:394-357-87499 target:83801 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:30.154432-0500	runningboardd	Assertion 394-357-87499 (target:[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]) will be created as active
default	13:26:30.154499-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x108108 com.nexy.assistant starting stopped process.
default	13:26:30.155342-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:30.155544-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 2
default	13:26:30.155570-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:30.156744-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:30.157048-0500	runningboardd	Invalidating assertion 394-80102-87497 (target:app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:26:30.157098-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring jetsam update because this process is not memory-managed
default	13:26:30.157116-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring suspend because this process is not lifecycle managed
default	13:26:30.157147-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring GPU update because this process is not GPU managed
default	13:26:30.157258-0500	gamepolicyd	Received state update for 83801 (app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>, running-active-NotVisible
default	13:26:30.157221-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring memory limit update because this process is not memory-managed
default	13:26:30.159842-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:30.167377-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:30.205579-0500	logger	detected new pid 83801 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:30.230391-0500	Nexy	[0x1057e58d0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:26:30.230468-0500	Nexy	[0x1057e5a10] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:26:30.262298-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring jetsam update because this process is not memory-managed
default	13:26:30.262310-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring suspend because this process is not lifecycle managed
default	13:26:30.262324-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring GPU update because this process is not GPU managed
default	13:26:30.262345-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] Ignoring memory limit update because this process is not memory-managed
default	13:26:30.262599-0500	gamepolicyd	Received state update for 83801 (app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>, running-active-NotVisible
default	13:26:30.265256-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:30.265645-0500	gamepolicyd	Received state update for 83801 (app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>, running-active-NotVisible
error	13:26:30.347311-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x9cc4e8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:30.347537-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x9cc4e8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:30.347748-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x9cc4e8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:30.347961-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x9cc4e8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:26:30.349440-0500	Nexy	[0x1057e1070] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:26:30.350152-0500	Nexy	[0x9cc668000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:26:30.350445-0500	Nexy	[0x9cc668140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:26:30.350894-0500	Nexy	[0x9cc668280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:26:30.351119-0500	Nexy	Received configuration update from daemon (initial)
default	13:26:30.353123-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:26:30.353478-0500	Nexy	[0x9cc6683c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:30.354181-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83801.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:30.355833-0500	tccd	AUTHREQ_SUBJECT: msgID=83801.1, subject=com.nexy.assistant,
default	13:26:30.356590-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:30.375741-0500	Nexy	[0x9cc6683c0] invalidated after the last release of the connection object
default	13:26:30.376080-0500	Nexy	server port 0x0000360b, session port 0x0000360b
default	13:26:30.377085-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.571, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:26:30.377115-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:30.377945-0500	tccd	AUTHREQ_SUBJECT: msgID=387.571, subject=com.nexy.assistant,
default	13:26:30.378660-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:30.400682-0500	Nexy	New connection 0x8dbe7 main
default	13:26:30.403281-0500	Nexy	CHECKIN: pid=83801
default	13:26:30.412267-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83801" ID:394-357-87502 target:83801 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:30.412358-0500	runningboardd	Assertion 394-357-87502 (target:[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]) will be created as active
default	13:26:30.412724-0500	Nexy	CHECKEDIN: pid=83801 asn=0x0-0x108108 foreground=0
default	13:26:30.412774-0500	runningboardd	Invalidating assertion 394-357-87499 (target:[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:26:30.412899-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:30.413022-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:30.412545-0500	launchservicesd	CHECKIN:0x0-0x108108 83801 com.nexy.assistant
default	13:26:30.412975-0500	Nexy	[0x9cc6683c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:30.412983-0500	Nexy	[0x9cc6683c0] Connection returned listener port: 0x4f03
default	13:26:30.413449-0500	Nexy	[0x9cc678300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x9cc6683c0.peer[357].0x9cc678300
default	13:26:30.421366-0500	Nexy	No persisted cache on this platform.
default	13:26:30.425192-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:26:30.425200-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:26:30.425261-0500	Nexy	Initializing connection
default	13:26:30.425306-0500	Nexy	Removing all cached process handles
default	13:26:30.425329-0500	Nexy	Sending handshake request attempt #1 to server
default	13:26:30.425340-0500	Nexy	Creating connection to com.apple.runningboard
default	13:26:30.425348-0500	Nexy	[0x9cc668640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:26:30.425745-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] as ready
default	13:26:30.437802-0500	Nexy	Registered process with identifier 83801-162410
default	13:26:31.198704-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid A5DBA5F9-ED3A-4731-A53C-81395EAFB561 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63140,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x5a748491 tp_proto=0x06"
default	13:26:31.198762-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63140<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533593 t_state: SYN_SENT process: Nexy:83801 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xabae88aa
default	13:26:31.199457-0500	kernel	tcp connected: [<IPv4-redacted>:63140<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533593 t_state: ESTABLISHED process: Nexy:83801 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xabae88aa
default	13:26:31.199754-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63140<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533593 t_state: FIN_WAIT_1 process: Nexy:83801 Duration: 0.002 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xabae88aa
default	13:26:31.199765-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63140<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533593 t_state: FIN_WAIT_1 process: Nexy:83801 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:26:31.236560-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:26:31.237206-0500	Nexy	[0x9cc668c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:26:31.238260-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4017","name":"Nexy(83801)"}, "details":{"PID":83801,"session_type":"Primary"} }
default	13:26:31.238346-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":83801}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4017, sessionType: 'prim', isRecording: false }, 
]
default	13:26:31.239079-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 83801, name = Nexy
default	13:26:31.239404-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x9cc6e3900 with ID: 0x1f4017
default	13:26:31.239689-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:26:31.240407-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:26:31.241964-0500	Nexy	[0x9cc668dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:26:31.244175-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035 AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035>
default	13:26:31.248481-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:26:31.250061-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:31.250248-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:31.250395-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:26:31.250406-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:26:31.250435-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:31.250570-0500	Nexy	[0x9cc668f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:26:31.250695-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:26:31.251106-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83801.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:31.257805-0500	tccd	AUTHREQ_SUBJECT: msgID=83801.2, subject=com.nexy.assistant,
default	13:26:31.258483-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:31.274821-0500	Nexy	[0x9cc668f00] invalidated after the last release of the connection object
default	13:26:31.274955-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:31.274992-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:31.275275-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:26:31.276530-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.331, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:31.277400-0500	tccd	AUTHREQ_SUBJECT: msgID=395.331, subject=com.nexy.assistant,
default	13:26:31.277995-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:26:31.294116-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:26:31.295007-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.333, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:31.295749-0500	tccd	AUTHREQ_SUBJECT: msgID=395.333, subject=com.nexy.assistant,
default	13:26:31.296305-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:31.310877-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:26:31.310895-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x9cb2f7e00> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:26:31.324362-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:31.325273-0500	Nexy	[0x9cc668f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:26:31.325676-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=359922554372097 }
default	13:26:31.325788-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:26:31.325819-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:26:31.325849-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:26:31.336755-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:26:31.371026-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:26:31.371048-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:26:31.374557-0500	Nexy	[0x9cc669040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:26:31.383229-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9cde16a40) Selecting device 71 from constructor
default	13:26:31.383238-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9cde16a40)
default	13:26:31.383243-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9cde16a40) not already running
default	13:26:31.383248-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9cde16a40) nothing to teardown
default	13:26:31.383250-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9cde16a40) connecting device 71
default	13:26:31.383322-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9cde16a40) Device ID: 71 (Input:No | Output:Yes): true
default	13:26:31.383398-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9cde16a40) created ioproc 0xa for device 71
default	13:26:31.383480-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9cde16a40) adding 7 device listeners to device 71
default	13:26:31.383606-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9cde16a40) adding 0 device delegate listeners to device 71
default	13:26:31.383614-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9cde16a40)
default	13:26:31.383671-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:31.383677-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:26:31.383688-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:31.383693-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:26:31.383701-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:26:31.383769-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9cde16a40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:26:31.383776-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9cde16a40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:26:31.383780-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:26:31.383785-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9cde16a40) removing 0 device listeners from device 0
default	13:26:31.383789-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9cde16a40) removing 0 device delegate listeners from device 0
default	13:26:31.383791-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9cde16a40)
default	13:26:31.383831-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:26:31.384061-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:31.384958-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:26:31.384996-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:26:31.385107-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9cbb7e850, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:31.385126-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:31.386305-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:31.386472-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:31.387906-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:31.388070-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:31.389034-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9cbb7e7f0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:31.389046-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:31.389328-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:31.389985-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9cbb7ec40, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:31.389993-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9cbb7ec40: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:31.389997-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:31.390000-0500	Nexy	AudioConverter -> 0x9cbb7ec40: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:31.390008-0500	Nexy	AudioConverter -> 0x9cbb7ec40: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:31.390012-0500	Nexy	AudioConverter -> 0x9cbb7ec40: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:31.390726-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9cbb7e7f0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:31.390733-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9cbb7e7f0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:31.390738-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:31.390738-0500	Nexy	AudioConverter -> 0x9cbb7e7f0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:31.390746-0500	Nexy	AudioConverter -> 0x9cbb7e7f0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:31.390754-0500	Nexy	AudioConverter -> 0x9cbb7e7f0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:31.390857-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x9cbb7e7f0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:31.424211-0500	Nexy	[0x9cc669180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:31.424730-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:31.424904-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83801.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:31.425848-0500	tccd	AUTHREQ_SUBJECT: msgID=83801.3, subject=com.nexy.assistant,
default	13:26:31.426721-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:31.448977-0500	Nexy	[0x9cc669180] invalidated after the last release of the connection object
default	13:26:31.449109-0500	Nexy	[0x9cc669180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:31.449460-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:31.449615-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83801.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:31.450400-0500	tccd	AUTHREQ_SUBJECT: msgID=83801.4, subject=com.nexy.assistant,
default	13:26:31.450984-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:31.469562-0500	Nexy	[0x9cc669180] invalidated after the last release of the connection object
default	13:26:31.469644-0500	Nexy	[0x9cc669180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:26:31.469726-0500	Nexy	[0x9cc669180] invalidated after the last release of the connection object
default	13:26:31.719424-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83812.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83812, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83812, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:31.721049-0500	tccd	AUTHREQ_SUBJECT: msgID=83812.1, subject=com.nexy.assistant,
default	13:26:31.721734-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:31.742691-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83812.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83812, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83812, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:31.743510-0500	tccd	AUTHREQ_SUBJECT: msgID=83812.2, subject=com.nexy.assistant,
default	13:26:31.744124-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:31.786247-0500	Nexy	[0x9cc669540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:31.787036-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83801.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83801, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:31.794063-0500	tccd	AUTHREQ_SUBJECT: msgID=83801.5, subject=com.nexy.assistant,
default	13:26:31.794722-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:31.812423-0500	Nexy	[0x9cc669540] invalidated after the last release of the connection object
default	13:26:31.842569-0500	Nexy	server port 0x00014803, session port 0x0000360b
default	13:26:33.885118-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x108108 (Nexy) connectionID: 8DBE7 pid: 83801 in session 0x101
default	13:26:33.885510-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f4017","name":"Nexy(83801)"}, "details":null }
default	13:26:33.885207-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x108108 (Nexy) acq:0xb6c360120 count:1
default	13:26:33.885567-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f4017 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":83801})
default	13:26:33.885591-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":83801})
default	13:26:33.885972-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 24, PID = 83801, Name = sid:0x1f4017, Nexy(83801), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:26:33.886270-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 24, PID = 83801, Name = sid:0x1f4017, Nexy(83801), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:26:33.886646-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:33.886989-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:33.887104-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:33.887140-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:33.886816-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:33.887367-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:33.890036-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x108108 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x108108 (Nexy)"
)}
default	13:26:33.890527-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x14759 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x108108 (Nexy)"
)}
default	13:26:33.902247-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]
default	13:26:33.905016-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801] termination reported by launchd (0, 0, 0)
default	13:26:33.905092-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]
default	13:26:33.905371-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]
default	13:26:33.906050-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]
default	13:26:33.906105-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]
default	13:26:33.911529-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>: none (role: None) (endowments: (null))
default	13:26:33.911761-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>: none (role: None) (endowments: (null))
default	13:26:33.911890-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 83801, name = Nexy
default	13:26:33.913000-0500	launchservicesd	Hit the server for a process handle e965dd500014759 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>:83801]
default	13:26:33.913258-0500	gamepolicyd	Received state update for 83801 (app<application.com.nexy.assistant.38522673.38522682.F1FE0EC5-7059-4616-914B-E1D8EA294035(501)>, none-NotVisible
default	13:26:33.915278-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x108108} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:26:33.915314-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 3
default	13:26:33.915333-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:33.918153-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 4
default	13:26:33.918171-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:36.979620-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:26:37.073391-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:26:37.073566-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:26:37.075258-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:26:37.078427-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:26:37.079722-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:26:37.079813-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87537 target:app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:37.079895-0500	runningboardd	Assertion 394-80102-87537 (target:app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>) will be created as active
default	13:26:37.082622-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:26:37.082655-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>
default	13:26:37.082667-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:26:37.082756-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:26:37.095386-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] is not RunningBoard jetsam managed.
default	13:26:37.095406-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] This process will not be managed.
default	13:26:37.095416-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]
default	13:26:37.095629-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:37.096265-0500	gamepolicyd	Hit the server for a process handle 1efeb96c0001477c that resolved to: [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]
default	13:26:37.096304-0500	gamepolicyd	Received state update for 83836 (app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>, running-active-NotVisible
default	13:26:37.098433-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]
default	13:26:37.098498-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] from originator [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87538 target:83836 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:26:37.098619-0500	runningboardd	Assertion 394-394-87538 (target:[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]) will be created as active
default	13:26:37.098833-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring jetsam update because this process is not memory-managed
default	13:26:37.098850-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring suspend because this process is not lifecycle managed
default	13:26:37.098870-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Set darwin role to: UserInteractive
default	13:26:37.098881-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring GPU update because this process is not GPU managed
default	13:26:37.098897-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring memory limit update because this process is not memory-managed
default	13:26:37.098958-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] reported to RB as running
default	13:26:37.100114-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring jetsam update because this process is not memory-managed
default	13:26:37.100138-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring suspend because this process is not lifecycle managed
default	13:26:37.100166-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring GPU update because this process is not GPU managed
default	13:26:37.100218-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring memory limit update because this process is not memory-managed
default	13:26:37.100317-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]
default	13:26:37.100471-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83836" ID:394-357-87539 target:83836 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:37.100562-0500	runningboardd	Assertion 394-357-87539 (target:[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]) will be created as active
default	13:26:37.100737-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x109109 com.nexy.assistant starting stopped process.
default	13:26:37.101675-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:37.101885-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 2
default	13:26:37.101912-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:37.102917-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:37.103085-0500	kernel	Nexy[83836] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0x461371725ac5e9fd. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:26:37.103107-0500	kernel	Nexy[83836] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0x461371725ac5e9fd. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:26:37.103240-0500	runningboardd	Invalidating assertion 394-80102-87537 (target:app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:26:37.103281-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring jetsam update because this process is not memory-managed
default	13:26:37.103344-0500	gamepolicyd	Received state update for 83836 (app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>, running-active-NotVisible
default	13:26:37.103353-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring suspend because this process is not lifecycle managed
default	13:26:37.103389-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring GPU update because this process is not GPU managed
default	13:26:37.103457-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring memory limit update because this process is not memory-managed
default	13:26:37.106244-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:37.114111-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:37.151200-0500	logger	detected new pid 83836 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:37.179666-0500	Nexy	[0x103fd0ff0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:26:37.179739-0500	Nexy	[0x103fd1f30] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:26:37.209762-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring jetsam update because this process is not memory-managed
default	13:26:37.209778-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring suspend because this process is not lifecycle managed
default	13:26:37.209789-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring GPU update because this process is not GPU managed
default	13:26:37.209810-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] Ignoring memory limit update because this process is not memory-managed
default	13:26:37.209973-0500	gamepolicyd	Received state update for 83836 (app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>, running-active-NotVisible
default	13:26:37.212673-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:37.212981-0500	gamepolicyd	Received state update for 83836 (app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>, running-active-NotVisible
error	13:26:37.296367-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xc70510000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:37.296595-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xc70510000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:37.296799-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xc70510000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:37.297005-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xc70510000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:26:37.298480-0500	Nexy	[0x103fc03f0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:26:37.299267-0500	Nexy	[0xc70630000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:26:37.299576-0500	Nexy	[0xc70630140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:26:37.300019-0500	Nexy	[0xc70630280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:26:37.301006-0500	Nexy	Received configuration update from daemon (initial)
default	13:26:37.302278-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:26:37.302654-0500	Nexy	[0xc706303c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:37.303335-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83836.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:37.304954-0500	tccd	AUTHREQ_SUBJECT: msgID=83836.1, subject=com.nexy.assistant,
default	13:26:37.305726-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:37.324995-0500	Nexy	[0xc706303c0] invalidated after the last release of the connection object
default	13:26:37.325330-0500	Nexy	server port 0x0000370b, session port 0x0000370b
default	13:26:37.326309-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.572, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:26:37.326334-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:37.327141-0500	tccd	AUTHREQ_SUBJECT: msgID=387.572, subject=com.nexy.assistant,
default	13:26:37.327847-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:37.353050-0500	Nexy	New connection 0x5bf03 main
default	13:26:37.355726-0500	Nexy	CHECKIN: pid=83836
default	13:26:37.366342-0500	Nexy	FRONTLOGGING: version 1
default	13:26:37.366388-0500	Nexy	Registered, pid=83836 ASN=0x0,0x109109
default	13:26:37.366874-0500	WindowServer	5bf03[CreateApplication]: Process creation: 0x0-0x109109 (Nexy) connectionID: 5BF03 pid: 83836 in session 0x101
default	13:26:37.367156-0500	Nexy	[0xc70630500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:26:37.370177-0500	Nexy	BringForward: pid=83836 asn=0x0-0x109109 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:26:37.370577-0500	Nexy	BringFrontModifier: pid=83836 asn=0x0-0x109109 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:26:37.374392-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:26:37.378231-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] as ready
default	13:26:37.378925-0500	Nexy	Handshake succeeded
default	13:26:37.378942-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>
default	13:26:37.386956-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:26:37.386979-0500	Nexy	[0xc70630640] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:26:37.387105-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:26:37.387200-0500	Nexy	[0xc70630a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:38.163193-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 1D5823BB-69DD-4DB7-AE13-647F90551185 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63150,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc16a130a tp_proto=0x06"
default	13:26:38.163248-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63150<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533658 t_state: SYN_SENT process: Nexy:83836 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9e9ab23e
default	13:26:38.163731-0500	kernel	tcp connected: [<IPv4-redacted>:63150<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533658 t_state: ESTABLISHED process: Nexy:83836 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9e9ab23e
default	13:26:38.164005-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63150<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533658 t_state: FIN_WAIT_1 process: Nexy:83836 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x9e9ab23e
default	13:26:38.164016-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63150<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533658 t_state: FIN_WAIT_1 process: Nexy:83836 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:26:38.200588-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:26:38.201217-0500	Nexy	[0xc70630c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:26:38.202294-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4018","name":"Nexy(83836)"}, "details":{"PID":83836,"session_type":"Primary"} }
default	13:26:38.202382-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":83836}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4018, sessionType: 'prim', isRecording: false }, 
]
default	13:26:38.203138-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 83836, name = Nexy
default	13:26:38.203502-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xc706d3940 with ID: 0x1f4018
default	13:26:38.203763-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:26:38.204488-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:26:38.205926-0500	Nexy	[0xc70630dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:26:38.208283-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB>
default	13:26:38.212884-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:26:38.214443-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:38.214617-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:38.214766-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:26:38.214776-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:26:38.214807-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:38.214935-0500	Nexy	[0xc70630f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:26:38.215090-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:26:38.215467-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83836.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:38.222337-0500	tccd	AUTHREQ_SUBJECT: msgID=83836.2, subject=com.nexy.assistant,
default	13:26:38.223324-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:38.239718-0500	Nexy	[0xc70630f00] invalidated after the last release of the connection object
default	13:26:38.239869-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:38.239905-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:38.240214-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:26:38.241488-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.334, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:38.242396-0500	tccd	AUTHREQ_SUBJECT: msgID=395.334, subject=com.nexy.assistant,
default	13:26:38.243020-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:26:38.259114-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:26:38.260020-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.336, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:38.260793-0500	tccd	AUTHREQ_SUBJECT: msgID=395.336, subject=com.nexy.assistant,
default	13:26:38.261358-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:38.275795-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:26:38.275825-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xc6fbbc5e0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:26:38.289190-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:38.290222-0500	Nexy	[0xc70630f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:26:38.290626-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=360072878227457 }
default	13:26:38.290740-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:26:38.290777-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:26:38.290818-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:26:38.300951-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:26:38.334348-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:26:38.334372-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:26:38.338020-0500	Nexy	[0xc70631040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:26:38.347038-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xc71ed0040) Selecting device 71 from constructor
default	13:26:38.347048-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc71ed0040)
default	13:26:38.347053-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc71ed0040) not already running
default	13:26:38.347059-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc71ed0040) nothing to teardown
default	13:26:38.347062-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xc71ed0040) connecting device 71
default	13:26:38.347134-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc71ed0040) Device ID: 71 (Input:No | Output:Yes): true
default	13:26:38.347203-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xc71ed0040) created ioproc 0xa for device 71
default	13:26:38.347292-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc71ed0040) adding 7 device listeners to device 71
default	13:26:38.347440-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc71ed0040) adding 0 device delegate listeners to device 71
default	13:26:38.347450-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc71ed0040)
default	13:26:38.347510-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:38.347517-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:26:38.347527-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:38.347532-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:26:38.347539-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:26:38.347618-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc71ed0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:26:38.347626-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc71ed0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:26:38.347630-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:26:38.347635-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc71ed0040) removing 0 device listeners from device 0
default	13:26:38.347637-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc71ed0040) removing 0 device delegate listeners from device 0
default	13:26:38.347642-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc71ed0040)
default	13:26:38.347682-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:26:38.347902-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:38.348829-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:26:38.348867-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:26:38.348984-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc6fb21fb0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:38.349009-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:38.350182-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:38.350356-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:38.351984-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:38.352169-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:38.353143-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc6fb21f50, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:38.353157-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:38.353432-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:38.354080-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc6fb223a0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:38.354089-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc6fb223a0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:38.354093-0500	Nexy	AudioConverter -> 0xc6fb223a0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:38.354094-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:38.354099-0500	Nexy	AudioConverter -> 0xc6fb223a0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:38.354104-0500	Nexy	AudioConverter -> 0xc6fb223a0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:38.354821-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc6fb21f50, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:38.354830-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc6fb21f50: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:38.354835-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:38.354832-0500	Nexy	AudioConverter -> 0xc6fb21f50: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:38.354840-0500	Nexy	AudioConverter -> 0xc6fb21f50: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:38.354850-0500	Nexy	AudioConverter -> 0xc6fb21f50: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:38.354953-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc6fb21f50: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:38.388358-0500	Nexy	[0xc70631180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:38.388873-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:38.389045-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83836.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:38.390008-0500	tccd	AUTHREQ_SUBJECT: msgID=83836.3, subject=com.nexy.assistant,
default	13:26:38.390666-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:38.409188-0500	Nexy	[0xc70631180] invalidated after the last release of the connection object
default	13:26:38.409264-0500	Nexy	[0xc70631180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:38.409610-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:38.409769-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83836.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:38.410511-0500	tccd	AUTHREQ_SUBJECT: msgID=83836.4, subject=com.nexy.assistant,
default	13:26:38.411115-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:38.428634-0500	Nexy	[0xc70631180] invalidated after the last release of the connection object
default	13:26:38.428695-0500	Nexy	[0xc70631180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:26:38.428771-0500	Nexy	[0xc70631180] invalidated after the last release of the connection object
default	13:26:38.671127-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83846.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83846, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83846, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:38.672475-0500	tccd	AUTHREQ_SUBJECT: msgID=83846.1, subject=com.nexy.assistant,
default	13:26:38.673115-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:38.693361-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83846.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83846, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83846, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:38.694211-0500	tccd	AUTHREQ_SUBJECT: msgID=83846.2, subject=com.nexy.assistant,
default	13:26:38.695086-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:38.730168-0500	Nexy	[0xc70631540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:38.730811-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83836.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83836, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:38.737086-0500	tccd	AUTHREQ_SUBJECT: msgID=83836.5, subject=com.nexy.assistant,
default	13:26:38.737725-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:38.755510-0500	Nexy	[0xc70631540] invalidated after the last release of the connection object
default	13:26:38.779833-0500	Nexy	server port 0x00014003, session port 0x0000370b
default	13:26:40.820244-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	13:26:40.824201-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x109109 (Nexy) connectionID: 5BF03 pid: 83836 in session 0x101
default	13:26:40.824244-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x109109 (Nexy) acq:0xb6c361e40 count:1
default	13:26:40.824570-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f4018","name":"Nexy(83836)"}, "details":null }
default	13:26:40.824604-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f4018 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":83836})
default	13:26:40.824614-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":83836})
default	13:26:40.825012-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 25, PID = 83836, Name = sid:0x1f4018, Nexy(83836), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:26:40.825076-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 25, PID = 83836, Name = sid:0x1f4018, Nexy(83836), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:26:40.825156-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:40.825377-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:40.825440-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:40.825455-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:40.825273-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:40.825521-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x109109 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x109109 (Nexy)"
)}
default	13:26:40.825548-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:40.825817-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x1477c removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x109109 (Nexy)"
)}
default	13:26:40.832746-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]
default	13:26:40.839529-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836] termination reported by launchd (0, 0, 0)
default	13:26:40.839593-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]
default	13:26:40.839869-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]
default	13:26:40.840096-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]
default	13:26:40.840145-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]
default	13:26:40.844367-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>: none (role: None) (endowments: (null))
default	13:26:40.844556-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>: none (role: None) (endowments: (null))
default	13:26:40.844683-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 83836, name = Nexy
default	13:26:40.845133-0500	launchservicesd	Hit the server for a process handle 1efeb96c0001477c that resolved to: [app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>:83836]
default	13:26:40.845371-0500	gamepolicyd	Received state update for 83836 (app<application.com.nexy.assistant.38522673.38522682.579DE8ED-5AF8-4F36-B2C8-88594F5B2EFB(501)>, none-NotVisible
default	13:26:40.846990-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x109109} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:26:40.847024-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 3
default	13:26:40.847043-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:40.849592-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 4
default	13:26:40.849605-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:43.900430-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:26:44.012840-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:26:44.013068-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:26:44.015067-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:26:44.017534-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:26:44.019951-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:26:44.020776-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87589 target:app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:44.020872-0500	runningboardd	Assertion 394-80102-87589 (target:app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>) will be created as active
default	13:26:44.026277-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:26:44.026313-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>
default	13:26:44.026324-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:26:44.026420-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000954 ms (wallclock); resolved to {4294967295, (null)}
default	13:26:44.046953-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] is not RunningBoard jetsam managed.
default	13:26:44.046997-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] This process will not be managed.
default	13:26:44.047064-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]
default	13:26:44.051424-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:44.052436-0500	gamepolicyd	Hit the server for a process handle 28f3a8c0001479a that resolved to: [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]
default	13:26:44.052478-0500	gamepolicyd	Received state update for 83866 (app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>, running-active-NotVisible
default	13:26:44.055248-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]
default	13:26:44.055361-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] from originator [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87594 target:83866 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:26:44.055532-0500	runningboardd	Assertion 394-394-87594 (target:[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]) will be created as active
default	13:26:44.055803-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] Ignoring jetsam update because this process is not memory-managed
default	13:26:44.055830-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] Ignoring suspend because this process is not lifecycle managed
default	13:26:44.055855-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] Set darwin role to: UserInteractive
default	13:26:44.055872-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] Ignoring GPU update because this process is not GPU managed
default	13:26:44.055903-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] Ignoring memory limit update because this process is not memory-managed
default	13:26:44.056019-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] reported to RB as running
default	13:26:44.057921-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83866" ID:394-357-87595 target:83866 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:44.058060-0500	runningboardd	Assertion 394-357-87595 (target:[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]) will be created as active
default	13:26:44.062715-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 2
default	13:26:44.092024-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:44.150793-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] Ignoring jetsam update because this process is not memory-managed
default	13:26:44.150810-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] Ignoring suspend because this process is not lifecycle managed
default	13:26:44.150826-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] Ignoring GPU update because this process is not GPU managed
default	13:26:44.150854-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] Ignoring memory limit update because this process is not memory-managed
default	13:26:44.157248-0500	Nexy	[0x105c917d0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:26:44.157334-0500	Nexy	[0x105c91d90] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:26:44.161201-0500	logger	detected new pid 83866 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:44.167150-0500	gamepolicyd	Received state update for 83866 (app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>, running-active-NotVisible
error	13:26:44.365883-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x7bc514000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:44.366231-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x7bc514000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:44.366688-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x7bc514000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:44.367166-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x7bc514000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:26:44.368700-0500	Nexy	[0x105c80800] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:26:44.373126-0500	Nexy	[0x7bc684000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:26:44.373574-0500	Nexy	[0x7bc684140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:26:44.376693-0500	Nexy	[0x7bc684280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:26:44.381031-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:26:44.383156-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83866.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:44.382081-0500	Nexy	[0x7bc6843c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:44.388887-0500	tccd	AUTHREQ_SUBJECT: msgID=83866.1, subject=com.nexy.assistant,
default	13:26:44.452819-0500	Nexy	[0x7bc6843c0] invalidated after the last release of the connection object
default	13:26:44.457385-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.577, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:26:44.457420-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:44.465446-0500	tccd	AUTHREQ_SUBJECT: msgID=387.577, subject=com.nexy.assistant,
default	13:26:44.467222-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:44.487574-0500	Nexy	Received configuration update from daemon (initial)
default	13:26:44.505090-0500	Nexy	New connection 0xf9eb3 main
default	13:26:44.509849-0500	Nexy	CHECKIN: pid=83866
default	13:26:44.523304-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:83866" ID:394-357-87604 target:83866 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:44.523425-0500	runningboardd	Assertion 394-357-87604 (target:[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]) will be created as active
default	13:26:44.523591-0500	Nexy	CHECKEDIN: pid=83866 asn=0x0-0x10a10a foreground=0
default	13:26:44.523925-0500	runningboardd	Invalidating assertion 394-357-87595 (target:[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:26:44.523411-0500	launchservicesd	CHECKIN:0x0-0x10a10a 83866 com.nexy.assistant
default	13:26:44.524075-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:44.524235-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:44.524013-0500	Nexy	[0x7bc6843c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:44.524053-0500	Nexy	[0x7bc6843c0] Connection returned listener port: 0x4403
default	13:26:44.524354-0500	Nexy	[0x7bccc8300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x7bc6843c0.peer[357].0x7bccc8300
default	13:26:44.528599-0500	Nexy	[0x7bc6843c0] Connection returned listener port: 0x4403
default	13:26:44.529144-0500	Nexy	[0x7bc684500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:26:44.529644-0500	Nexy	BringForward: pid=83866 asn=0x0-0x10a10a bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:26:44.529824-0500	Nexy	BringFrontModifier: pid=83866 asn=0x0-0x10a10a Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:26:44.537195-0500	Nexy	No persisted cache on this platform.
default	13:26:44.542264-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:26:44.547384-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:26:44.556638-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 83866
default	13:26:44.559607-0500	Nexy	[0x7bc6843c0] Connection returned listener port: 0x4403
default	13:26:44.566189-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:26:44.566225-0500	Nexy	[0x7bc684780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:26:44.566370-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:26:44.566507-0500	Nexy	[0x7bc684a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:44.567907-0500	Nexy	[0x7bc684a00] Connection returned listener port: 0x6a03
default	13:26:45.739757-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 82C51441-0ABC-40EF-ADF9-A01F0E22C302 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63166,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x065ac034 tp_proto=0x06"
default	13:26:45.739849-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63166<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533927 t_state: SYN_SENT process: Nexy:83866 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x84b0b4fe
default	13:26:45.740020-0500	kernel	tcp connected: [<IPv4-redacted>:63166<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533927 t_state: ESTABLISHED process: Nexy:83866 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x84b0b4fe
default	13:26:45.740276-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63166<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533927 t_state: FIN_WAIT_1 process: Nexy:83866 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x84b0b4fe
default	13:26:45.740286-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63166<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 533927 t_state: FIN_WAIT_1 process: Nexy:83866 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:26:45.776550-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:26:45.777097-0500	Nexy	[0x7bc684c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:26:45.778702-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4019","name":"Nexy(83866)"}, "details":{"PID":83866,"session_type":"Primary"} }
default	13:26:45.778795-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":83866}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4019, sessionType: 'prim', isRecording: false }, 
]
default	13:26:45.779572-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 83866, name = Nexy
default	13:26:45.780205-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x7bc6d7380 with ID: 0x1f4019
default	13:26:45.780466-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:26:45.781153-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:26:45.782542-0500	Nexy	[0x7bc684dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:26:45.784887-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB>
default	13:26:45.789664-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:26:45.791177-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:45.791344-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:45.791493-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:26:45.791505-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:26:45.791532-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:45.791659-0500	Nexy	[0x7bc684f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:26:45.791826-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:26:45.792268-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83866.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:45.798470-0500	tccd	AUTHREQ_SUBJECT: msgID=83866.2, subject=com.nexy.assistant,
default	13:26:45.799174-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:45.816214-0500	Nexy	[0x7bc684f00] invalidated after the last release of the connection object
default	13:26:45.816369-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:45.816409-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:45.816644-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:26:45.818507-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.337, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:45.819386-0500	tccd	AUTHREQ_SUBJECT: msgID=395.337, subject=com.nexy.assistant,
default	13:26:45.819958-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:26:45.835835-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:26:45.836678-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.339, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:45.837469-0500	tccd	AUTHREQ_SUBJECT: msgID=395.339, subject=com.nexy.assistant,
default	13:26:45.838027-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:45.852897-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:26:45.852912-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x7bb4ce240> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:26:45.866421-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:45.867202-0500	Nexy	[0x7bc684f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:26:45.867542-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=360201727246337 }
default	13:26:45.867621-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:26:45.867659-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:26:45.867691-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:26:45.877691-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:26:45.915172-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:26:45.915263-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:26:45.920101-0500	Nexy	[0x7bc685040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:26:45.930175-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7bd740040) Selecting device 71 from constructor
default	13:26:45.930191-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7bd740040)
default	13:26:45.930197-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7bd740040) not already running
default	13:26:45.930203-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bd740040) nothing to teardown
default	13:26:45.930207-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7bd740040) connecting device 71
default	13:26:45.930311-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7bd740040) Device ID: 71 (Input:No | Output:Yes): true
default	13:26:45.930402-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7bd740040) created ioproc 0xa for device 71
default	13:26:45.930530-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7bd740040) adding 7 device listeners to device 71
default	13:26:45.930701-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7bd740040) adding 0 device delegate listeners to device 71
default	13:26:45.930710-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7bd740040)
default	13:26:45.930778-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:45.930790-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:26:45.930804-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:45.930810-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:26:45.930819-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:26:45.930922-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7bd740040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:26:45.930936-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7bd740040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:26:45.930943-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:26:45.930947-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7bd740040) removing 0 device listeners from device 0
default	13:26:45.930951-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7bd740040) removing 0 device delegate listeners from device 0
default	13:26:45.930954-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7bd740040)
default	13:26:45.931008-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:26:45.931293-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:45.932347-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:26:45.932404-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:26:45.932554-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7bbe8a880, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:45.932574-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:45.933904-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:45.934097-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:45.935903-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:45.936098-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:45.937171-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7bbe8a820, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:45.937184-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:45.937491-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:45.938193-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7bbe8ac70, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:45.938201-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x7bbe8ac70: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:45.938206-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:45.938206-0500	Nexy	AudioConverter -> 0x7bbe8ac70: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:45.938215-0500	Nexy	AudioConverter -> 0x7bbe8ac70: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:45.938219-0500	Nexy	AudioConverter -> 0x7bbe8ac70: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:45.938987-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7bbe8a820, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:45.938997-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x7bbe8a820: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:45.939002-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:45.939018-0500	Nexy	AudioConverter -> 0x7bbe8a820: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:45.939024-0500	Nexy	AudioConverter -> 0x7bbe8a820: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:45.939034-0500	Nexy	AudioConverter -> 0x7bbe8a820: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:45.939141-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x7bbe8a820: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:45.973781-0500	Nexy	[0x7bc685180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:45.974298-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:45.974473-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83866.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:45.975662-0500	tccd	AUTHREQ_SUBJECT: msgID=83866.3, subject=com.nexy.assistant,
default	13:26:45.976377-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:45.995182-0500	Nexy	[0x7bc685180] invalidated after the last release of the connection object
default	13:26:45.995265-0500	Nexy	[0x7bc685180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:45.995665-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:45.995837-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83866.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:45.996715-0500	tccd	AUTHREQ_SUBJECT: msgID=83866.4, subject=com.nexy.assistant,
default	13:26:45.997325-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:46.015191-0500	Nexy	[0x7bc685180] invalidated after the last release of the connection object
default	13:26:46.015256-0500	Nexy	[0x7bc685180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:26:46.015345-0500	Nexy	[0x7bc685180] invalidated after the last release of the connection object
default	13:26:46.262236-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83998.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83998, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83998, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:46.263907-0500	tccd	AUTHREQ_SUBJECT: msgID=83998.1, subject=com.nexy.assistant,
default	13:26:46.265008-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:46.285892-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83998.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=83998, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=83998, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:46.286766-0500	tccd	AUTHREQ_SUBJECT: msgID=83998.2, subject=com.nexy.assistant,
default	13:26:46.287390-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255800 at /Applications/Nexy.app
default	13:26:46.328485-0500	Nexy	[0x7bc685540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:46.329107-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=83866.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=83866, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:46.336059-0500	tccd	AUTHREQ_SUBJECT: msgID=83866.5, subject=com.nexy.assistant,
default	13:26:46.337356-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257000 at /Applications/Nexy.app
default	13:26:46.358726-0500	Nexy	[0x7bc685540] invalidated after the last release of the connection object
default	13:26:46.401412-0500	Nexy	server port 0x00014303, session port 0x00003207
default	13:26:48.435229-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f4019","name":"Nexy(83866)"}, "details":null }
default	13:26:48.435262-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f4019 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":83866})
default	13:26:48.435273-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":83866})
default	13:26:48.435519-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 26, PID = 83866, Name = sid:0x1f4019, Nexy(83866), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:26:48.435621-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 26, PID = 83866, Name = sid:0x1f4019, Nexy(83866), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:26:48.435755-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:48.436018-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:48.436074-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:48.436093-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:48.434782-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x10a10a (Nexy) connectionID: F9EB3 pid: 83866 in session 0x101
default	13:26:48.434824-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x10a10a (Nexy) acq:0xb6c3627c0 count:1
default	13:26:48.435949-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:48.438582-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x10a10a removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10a10a (Nexy)"
)}
default	13:26:48.437299-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:48.443747-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x1479a removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10a10a (Nexy)"
)}
default	13:26:48.491765-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866] termination reported by launchd (0, 0, 0)
default	13:26:48.492387-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]
default	13:26:48.492661-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]
default	13:26:48.492885-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]
default	13:26:48.492918-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]
default	13:26:48.495723-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]
default	13:26:48.499607-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>: none (role: None) (endowments: (null))
default	13:26:48.499784-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>: none (role: None) (endowments: (null))
default	13:26:48.499895-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 83866, name = Nexy
default	13:26:48.500303-0500	launchservicesd	Hit the server for a process handle 28f3a8c0001479a that resolved to: [app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>:83866]
default	13:26:48.500323-0500	gamepolicyd	Received state update for 83866 (app<application.com.nexy.assistant.38522673.38522682.A6FA158D-67E2-46C0-B15B-D8DE51B315FB(501)>, none-NotVisible
default	13:26:48.505053-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x10a10a} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:26:48.505084-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 3
default	13:26:48.505103-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:48.523015-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a73e0: Nexy> state 4
default	13:26:48.523027-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:51.538696-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:26:51.630448-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:26:51.630614-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:26:51.632400-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:26:51.636753-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:26:51.637152-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:26:51.637232-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87645 target:app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:51.637314-0500	runningboardd	Assertion 394-80102-87645 (target:app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>) will be created as active
default	13:26:51.640073-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:26:51.640113-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>
default	13:26:51.640125-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:26:51.640208-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.001073 ms (wallclock); resolved to {4294967295, (null)}
default	13:26:51.657291-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] is not RunningBoard jetsam managed.
default	13:26:51.657365-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] This process will not be managed.
default	13:26:51.657413-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]
default	13:26:51.657735-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:51.662404-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]
default	13:26:51.662481-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] from originator [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87647 target:84273 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:26:51.662621-0500	runningboardd	Assertion 394-394-87647 (target:[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]) will be created as active
default	13:26:51.662853-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring jetsam update because this process is not memory-managed
default	13:26:51.662919-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring suspend because this process is not lifecycle managed
default	13:26:51.662938-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Set darwin role to: UserInteractive
default	13:26:51.662947-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring GPU update because this process is not GPU managed
default	13:26:51.663100-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring memory limit update because this process is not memory-managed
default	13:26:51.663227-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] reported to RB as running
default	13:26:51.665277-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring jetsam update because this process is not memory-managed
default	13:26:51.665324-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring suspend because this process is not lifecycle managed
default	13:26:51.665390-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring GPU update because this process is not GPU managed
default	13:26:51.665457-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring memory limit update because this process is not memory-managed
default	13:26:51.665628-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]
default	13:26:51.665846-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84273" ID:394-357-87648 target:84273 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:51.665977-0500	runningboardd	Assertion 394-357-87648 (target:[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]) will be created as active
default	13:26:51.666460-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x10b10b com.nexy.assistant starting stopped process.
default	13:26:51.666820-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:51.666989-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 2
default	13:26:51.667013-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:51.670172-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:51.670732-0500	runningboardd	Invalidating assertion 394-80102-87645 (target:app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:26:51.670773-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring jetsam update because this process is not memory-managed
default	13:26:51.670806-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring suspend because this process is not lifecycle managed
default	13:26:51.670834-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring GPU update because this process is not GPU managed
default	13:26:51.670911-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring memory limit update because this process is not memory-managed
default	13:26:51.674253-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:51.674319-0500	gamepolicyd	Hit the server for a process handle ddef23e00014931 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]
default	13:26:51.674371-0500	gamepolicyd	Received state update for 84273 (app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>, running-active-NotVisible
default	13:26:51.674599-0500	gamepolicyd	Received state update for 84273 (app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>, running-active-NotVisible
default	13:26:51.688497-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:51.759124-0500	Nexy	[0x103f10b50] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:26:51.759200-0500	Nexy	[0x103f11090] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:26:51.769942-0500	logger	detected new pid 84273 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:51.772737-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring jetsam update because this process is not memory-managed
default	13:26:51.772749-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring suspend because this process is not lifecycle managed
default	13:26:51.772761-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring GPU update because this process is not GPU managed
default	13:26:51.772896-0500	gamepolicyd	Received state update for 84273 (app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>, running-active-NotVisible
default	13:26:51.772778-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] Ignoring memory limit update because this process is not memory-managed
default	13:26:51.775458-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:51.775799-0500	gamepolicyd	Received state update for 84273 (app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>, running-active-NotVisible
error	13:26:51.877171-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x84e538000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:51.877417-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x84e538000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:51.877631-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x84e538000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:51.877835-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x84e538000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:26:51.879455-0500	Nexy	[0x103f003f0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:26:51.880258-0500	Nexy	[0x84e700000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:26:51.880646-0500	Nexy	[0x84e700140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:26:51.881247-0500	Nexy	[0x84e700280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:26:51.882735-0500	Nexy	Received configuration update from daemon (initial)
default	13:26:51.883380-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:26:51.883747-0500	Nexy	[0x84e7003c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:51.884516-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84273.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:51.886281-0500	tccd	AUTHREQ_SUBJECT: msgID=84273.1, subject=com.nexy.assistant,
default	13:26:51.887253-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:51.912178-0500	Nexy	[0x84e7003c0] invalidated after the last release of the connection object
default	13:26:51.914402-0500	Nexy	server port 0x00003507, session port 0x00003507
default	13:26:51.915508-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.581, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:26:51.915608-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:51.917526-0500	tccd	AUTHREQ_SUBJECT: msgID=387.581, subject=com.nexy.assistant,
default	13:26:51.918885-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:51.942393-0500	Nexy	New connection 0xe1bab main
default	13:26:51.954377-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84273" ID:394-357-87653 target:84273 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:51.954477-0500	runningboardd	Assertion 394-357-87653 (target:[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]) will be created as active
default	13:26:51.955085-0500	Nexy	CHECKEDIN: pid=84273 asn=0x0-0x10b10b foreground=0
default	13:26:51.954874-0500	runningboardd	Invalidating assertion 394-357-87648 (target:[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:26:51.954852-0500	launchservicesd	CHECKIN:0x0-0x10b10b 84273 com.nexy.assistant
default	13:26:51.955204-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:51.970657-0500	Nexy	[0x84e700500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:26:51.981935-0500	Nexy	BringForward: pid=84273 asn=0x0-0x10b10b bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:26:51.986280-0500	Nexy	No persisted cache on this platform.
default	13:26:51.995932-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:26:51.995948-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:26:51.996047-0500	Nexy	Initializing connection
default	13:26:51.996109-0500	Nexy	Removing all cached process handles
default	13:26:51.996145-0500	Nexy	Sending handshake request attempt #1 to server
default	13:26:51.996174-0500	Nexy	Creating connection to com.apple.runningboard
default	13:26:51.996189-0500	Nexy	[0x84e700640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:26:51.996792-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] as ready
default	13:26:52.000629-0500	Nexy	[0x84e7003c0] Connection returned listener port: 0x4303
default	13:26:52.001976-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 84273
default	13:26:52.017966-0500	Nexy	[0x84e700a00] Connection returned listener port: 0x6c03
default	13:26:52.926126-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 012F7190-1377-41F7-BFE5-3FD48C78BC02 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63183,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x6e32753e tp_proto=0x06"
default	13:26:52.926249-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63183<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534268 t_state: SYN_SENT process: Nexy:84273 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbcca412e
default	13:26:52.927057-0500	kernel	tcp connected: [<IPv4-redacted>:63183<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534268 t_state: ESTABLISHED process: Nexy:84273 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbcca412e
default	13:26:52.927489-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63183<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534268 t_state: FIN_WAIT_1 process: Nexy:84273 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xbcca412e
default	13:26:52.927499-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63183<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534268 t_state: FIN_WAIT_1 process: Nexy:84273 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:26:52.996588-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:26:52.997895-0500	Nexy	[0x84e700c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:26:53.000413-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f401a","name":"Nexy(84273)"}, "details":{"PID":84273,"session_type":"Primary"} }
default	13:26:53.000515-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":84273}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f401a, sessionType: 'prim', isRecording: false }, 
]
default	13:26:53.002456-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x84e7bb4e0 with ID: 0x1f401a
default	13:26:53.001712-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 84273, name = Nexy
default	13:26:53.003304-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:26:53.005003-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:26:53.007491-0500	Nexy	[0x84e700dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:26:53.019304-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A>
default	13:26:53.028553-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:26:53.031203-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:53.031570-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:26:53.031806-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:26:53.031822-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:26:53.031866-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:53.032094-0500	Nexy	[0x84e700f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:26:53.032258-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:26:53.032900-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84273.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:53.042751-0500	tccd	AUTHREQ_SUBJECT: msgID=84273.2, subject=com.nexy.assistant,
default	13:26:53.043747-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:53.063157-0500	Nexy	[0x84e700f00] invalidated after the last release of the connection object
default	13:26:53.063390-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:53.063457-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:26:53.063790-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:26:53.065232-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.340, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:53.066318-0500	tccd	AUTHREQ_SUBJECT: msgID=395.340, subject=com.nexy.assistant,
default	13:26:53.066953-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:26:53.083710-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:26:53.084635-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.342, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:26:53.085510-0500	tccd	AUTHREQ_SUBJECT: msgID=395.342, subject=com.nexy.assistant,
default	13:26:53.086285-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:26:53.103151-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:26:53.103171-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x84cd93900> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:26:53.120140-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:26:53.121186-0500	Nexy	[0x84e700f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:26:53.121650-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=361949778935809 }
default	13:26:53.121814-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:26:53.121857-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:26:53.121887-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:26:53.132735-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:26:53.170172-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:26:53.170201-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:26:53.174911-0500	Nexy	[0x84e701040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:26:53.184128-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x84f6d8040) Selecting device 71 from constructor
default	13:26:53.184139-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x84f6d8040)
default	13:26:53.184144-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x84f6d8040) not already running
default	13:26:53.184149-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x84f6d8040) nothing to teardown
default	13:26:53.184154-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x84f6d8040) connecting device 71
default	13:26:53.184226-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x84f6d8040) Device ID: 71 (Input:No | Output:Yes): true
default	13:26:53.184300-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x84f6d8040) created ioproc 0xa for device 71
default	13:26:53.184382-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x84f6d8040) adding 7 device listeners to device 71
default	13:26:53.184525-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x84f6d8040) adding 0 device delegate listeners to device 71
default	13:26:53.184531-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x84f6d8040)
default	13:26:53.184588-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:53.184596-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:26:53.184606-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:26:53.184612-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:26:53.184618-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:26:53.184691-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x84f6d8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:26:53.184700-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x84f6d8040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:26:53.184704-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:26:53.184708-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x84f6d8040) removing 0 device listeners from device 0
default	13:26:53.184710-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x84f6d8040) removing 0 device delegate listeners from device 0
default	13:26:53.184714-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x84f6d8040)
default	13:26:53.184756-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:26:53.184989-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:53.185939-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:26:53.185980-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:26:53.186115-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x84cdc9740, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:53.186141-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:53.187427-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:53.187593-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:53.189270-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:53.189438-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:53.190412-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x84cdc96e0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:53.190424-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:53.190690-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:53.191378-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x84cdc9b30, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:53.191386-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x84cdc9b30: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:53.191390-0500	Nexy	AudioConverter -> 0x84cdc9b30: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:53.191392-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:53.191399-0500	Nexy	AudioConverter -> 0x84cdc9b30: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:53.191404-0500	Nexy	AudioConverter -> 0x84cdc9b30: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:53.192116-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x84cdc96e0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:26:53.192125-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x84cdc96e0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:53.192126-0500	Nexy	AudioConverter -> 0x84cdc96e0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:26:53.192130-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:26:53.192132-0500	Nexy	AudioConverter -> 0x84cdc96e0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:26:53.192142-0500	Nexy	AudioConverter -> 0x84cdc96e0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:26:53.192255-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x84cdc96e0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:26:53.226732-0500	Nexy	[0x84e701180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:53.227250-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:53.227417-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84273.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:53.228420-0500	tccd	AUTHREQ_SUBJECT: msgID=84273.3, subject=com.nexy.assistant,
default	13:26:53.229082-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:53.248039-0500	Nexy	[0x84e701180] invalidated after the last release of the connection object
default	13:26:53.248126-0500	Nexy	[0x84e701180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:26:53.248534-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:26:53.248696-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84273.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:53.249552-0500	tccd	AUTHREQ_SUBJECT: msgID=84273.4, subject=com.nexy.assistant,
default	13:26:53.250159-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:53.267585-0500	Nexy	[0x84e701180] invalidated after the last release of the connection object
default	13:26:53.267661-0500	Nexy	[0x84e701180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:26:53.267754-0500	Nexy	[0x84e701180] invalidated after the last release of the connection object
default	13:26:53.538660-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84283.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84283, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84283, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:53.540386-0500	tccd	AUTHREQ_SUBJECT: msgID=84283.1, subject=com.nexy.assistant,
default	13:26:53.541116-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:53.565525-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84283.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84283, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84283, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:26:53.567194-0500	tccd	AUTHREQ_SUBJECT: msgID=84283.2, subject=com.nexy.assistant,
default	13:26:53.568331-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:53.614958-0500	Nexy	[0x84e701540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:53.616051-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84273.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84273, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:53.623670-0500	tccd	AUTHREQ_SUBJECT: msgID=84273.5, subject=com.nexy.assistant,
default	13:26:53.624355-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257000 at /Applications/Nexy.app
default	13:26:53.644016-0500	Nexy	[0x84e701540] invalidated after the last release of the connection object
default	13:26:53.676528-0500	Nexy	server port 0x00010e03, session port 0x00003507
default	13:26:54.708530-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	13:26:55.721376-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x10b10b (Nexy) connectionID: E1BAB pid: 84273 in session 0x101
default	13:26:55.721422-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x10b10b (Nexy) acq:0xb6c363160 count:1
default	13:26:55.722140-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f401a","name":"Nexy(84273)"}, "details":null }
default	13:26:55.722177-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f401a from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":84273})
default	13:26:55.722202-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":84273})
default	13:26:55.722521-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 27, PID = 84273, Name = sid:0x1f401a, Nexy(84273), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:26:55.722625-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 27, PID = 84273, Name = sid:0x1f401a, Nexy(84273), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:26:55.723190-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:55.723289-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:55.723402-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:55.723486-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:55.722882-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:55.723042-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:26:55.726207-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x10b10b removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10b10b (Nexy)"
)}
default	13:26:55.726883-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x14931 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10b10b (Nexy)"
)}
default	13:26:55.733597-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]
default	13:26:55.736913-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273] termination reported by launchd (0, 0, 0)
default	13:26:55.736958-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]
default	13:26:55.737221-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]
default	13:26:55.737463-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]
default	13:26:55.737509-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]
default	13:26:55.742053-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>: none (role: None) (endowments: (null))
default	13:26:55.742266-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>: none (role: None) (endowments: (null))
default	13:26:55.742391-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 84273, name = Nexy
default	13:26:55.743366-0500	launchservicesd	Hit the server for a process handle ddef23e00014931 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>:84273]
default	13:26:55.743832-0500	gamepolicyd	Received state update for 84273 (app<application.com.nexy.assistant.38522673.38522682.FEA570FF-79CD-4E76-823F-B59513E5E05A(501)>, none-NotVisible
default	13:26:55.745744-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x10b10b} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:26:55.745781-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 3
default	13:26:55.745806-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:55.747612-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 4
default	13:26:55.747626-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:26:58.804784-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:26:58.892498-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:26:58.892668-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:26:58.894711-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:26:58.896431-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:26:58.899295-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:26:58.899358-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87709 target:app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:58.899425-0500	runningboardd	Assertion 394-80102-87709 (target:app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>) will be created as active
default	13:26:58.901911-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:26:58.901941-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>
default	13:26:58.901952-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:26:58.902015-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:26:58.912604-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] is not RunningBoard jetsam managed.
default	13:26:58.912620-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] This process will not be managed.
default	13:26:58.912631-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]
default	13:26:58.917762-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:58.919821-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]
default	13:26:58.919872-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] from originator [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87710 target:84310 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:26:58.919981-0500	runningboardd	Assertion 394-394-87710 (target:[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]) will be created as active
default	13:26:58.920164-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring jetsam update because this process is not memory-managed
default	13:26:58.920185-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring suspend because this process is not lifecycle managed
default	13:26:58.920202-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Set darwin role to: UserInteractive
default	13:26:58.920212-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring GPU update because this process is not GPU managed
default	13:26:58.920229-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring memory limit update because this process is not memory-managed
default	13:26:58.920285-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] reported to RB as running
default	13:26:58.921364-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring jetsam update because this process is not memory-managed
default	13:26:58.921397-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring suspend because this process is not lifecycle managed
default	13:26:58.921422-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring GPU update because this process is not GPU managed
default	13:26:58.921552-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring memory limit update because this process is not memory-managed
default	13:26:58.921715-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84310" ID:394-357-87711 target:84310 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:58.921720-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]
default	13:26:58.921798-0500	runningboardd	Assertion 394-357-87711 (target:[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]) will be created as active
default	13:26:58.921840-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x10c10c com.nexy.assistant starting stopped process.
default	13:26:58.922771-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:58.922936-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 2
default	13:26:58.922959-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:58.923854-0500	kernel	Nexy[84310] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0xc4d206ef1cb2d53f. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:26:58.923866-0500	kernel	Nexy[84310] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0xc4d206ef1cb2d53f. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:26:58.924835-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:58.925139-0500	runningboardd	Invalidating assertion 394-80102-87709 (target:app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:26:58.925156-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring jetsam update because this process is not memory-managed
default	13:26:58.925203-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring suspend because this process is not lifecycle managed
default	13:26:58.925240-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring GPU update because this process is not GPU managed
default	13:26:58.925285-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring memory limit update because this process is not memory-managed
default	13:26:58.927731-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:58.927795-0500	gamepolicyd	Hit the server for a process handle 1213984d00014956 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]
default	13:26:58.927917-0500	gamepolicyd	Received state update for 84310 (app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>, running-active-NotVisible
default	13:26:58.934072-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:58.967946-0500	logger	detected new pid 84310 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:58.993149-0500	Nexy	[0x10225c940] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:26:58.993212-0500	Nexy	[0x10225ce80] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:26:59.027692-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring jetsam update because this process is not memory-managed
default	13:26:59.027707-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring suspend because this process is not lifecycle managed
default	13:26:59.027718-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring GPU update because this process is not GPU managed
default	13:26:59.027858-0500	gamepolicyd	Received state update for 84310 (app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>, running-active-NotVisible
default	13:26:59.027739-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] Ignoring memory limit update because this process is not memory-managed
default	13:26:59.030334-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:26:59.030600-0500	gamepolicyd	Received state update for 84310 (app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>, running-active-NotVisible
error	13:26:59.108053-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xb8a4e0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:59.108275-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xb8a4e0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:59.108480-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xb8a4e0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:26:59.108684-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xb8a4e0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:26:59.110163-0500	Nexy	[0x10226a1d0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:26:59.110944-0500	Nexy	[0xb8a65c000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:26:59.111263-0500	Nexy	[0xb8a65c140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:26:59.111696-0500	Nexy	[0xb8a65c280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:26:59.111967-0500	Nexy	Received configuration update from daemon (initial)
default	13:26:59.114053-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:26:59.114418-0500	Nexy	[0xb8a65c3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:26:59.115140-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84310.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:26:59.116754-0500	tccd	AUTHREQ_SUBJECT: msgID=84310.1, subject=com.nexy.assistant,
default	13:26:59.117526-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:59.136734-0500	Nexy	[0xb8a65c3c0] invalidated after the last release of the connection object
default	13:26:59.137084-0500	Nexy	server port 0x0000350b, session port 0x0000350b
default	13:26:59.138142-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.582, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:26:59.138168-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:26:59.139031-0500	tccd	AUTHREQ_SUBJECT: msgID=387.582, subject=com.nexy.assistant,
default	13:26:59.139764-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:26:59.160825-0500	Nexy	New connection 0xa8a63 main
default	13:26:59.163680-0500	Nexy	CHECKIN: pid=84310
default	13:26:59.174083-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84310" ID:394-357-87712 target:84310 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:26:59.174184-0500	runningboardd	Assertion 394-357-87712 (target:[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]) will be created as active
default	13:26:59.174637-0500	Nexy	CHECKEDIN: pid=84310 asn=0x0-0x10c10c foreground=0
default	13:26:59.174633-0500	runningboardd	Invalidating assertion 394-357-87711 (target:[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:26:59.174487-0500	launchservicesd	CHECKIN:0x0-0x10c10c 84310 com.nexy.assistant
default	13:26:59.174724-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:26:59.174864-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:26:59.174891-0500	Nexy	[0xb8a65c3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:59.174935-0500	Nexy	[0xb8a65c3c0] Connection returned listener port: 0x5003
default	13:26:59.175265-0500	Nexy	[0xb8a670300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xb8a65c3c0.peer[357].0xb8a670300
default	13:26:59.177726-0500	Nexy	FRONTLOGGING: version 1
default	13:26:59.177792-0500	Nexy	Registered, pid=84310 ASN=0x0,0x10c10c
default	13:26:59.178302-0500	WindowServer	a8a63[CreateApplication]: Process creation: 0x0-0x10c10c (Nexy) connectionID: A8A63 pid: 84310 in session 0x101
default	13:26:59.178651-0500	Nexy	[0xb8a65c640] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:26:59.180751-0500	Nexy	[0xb8a65c3c0] Connection returned listener port: 0x5003
default	13:26:59.182351-0500	Nexy	BringForward: pid=84310 asn=0x0-0x10c10c bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:26:59.182760-0500	Nexy	BringFrontModifier: pid=84310 asn=0x0-0x10c10c Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:26:59.183574-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:26:59.185034-0500	Nexy	No persisted cache on this platform.
default	13:26:59.186234-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:26:59.186762-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:26:59.189363-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:26:59.189373-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:26:59.189430-0500	Nexy	Initializing connection
default	13:26:59.189471-0500	Nexy	Removing all cached process handles
default	13:26:59.189502-0500	Nexy	Sending handshake request attempt #1 to server
default	13:26:59.189518-0500	Nexy	Creating connection to com.apple.runningboard
default	13:26:59.189527-0500	Nexy	[0xb8a65c500] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:26:59.190022-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] as ready
default	13:26:59.190648-0500	Nexy	Handshake succeeded
default	13:26:59.190664-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>
default	13:26:59.191138-0500	Nexy	[0xb8a65c3c0] Connection returned listener port: 0x5003
default	13:26:59.192257-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 84310
default	13:26:59.195256-0500	Nexy	[0xb8a65c3c0] Connection returned listener port: 0x5003
default	13:26:59.200148-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:26:59.200161-0500	Nexy	[0xb8a65c8c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:26:59.200305-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:26:59.200371-0500	Nexy	[0xb8a65ca00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:26:59.203732-0500	Nexy	[0xb8a65ca00] Connection returned listener port: 0x7003
default	13:26:59.984935-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 5C31604D-6CF1-46ED-A9CF-C7FF84A61D60 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63194,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xe8fbc19b tp_proto=0x06"
default	13:26:59.985011-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63194<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534417 t_state: SYN_SENT process: Nexy:84310 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8a72d9dd
default	13:26:59.985605-0500	kernel	tcp connected: [<IPv4-redacted>:63194<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534417 t_state: ESTABLISHED process: Nexy:84310 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8a72d9dd
default	13:26:59.985927-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63194<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534417 t_state: FIN_WAIT_1 process: Nexy:84310 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8a72d9dd
default	13:26:59.985937-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63194<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534417 t_state: FIN_WAIT_1 process: Nexy:84310 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:27:00.022308-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:27:00.023066-0500	Nexy	[0xb8a65cc80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:27:00.024219-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f401b","name":"Nexy(84310)"}, "details":{"PID":84310,"session_type":"Primary"} }
default	13:27:00.024302-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":84310}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f401b, sessionType: 'prim', isRecording: false }, 
]
default	13:27:00.025193-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 84310, name = Nexy
default	13:27:00.025618-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xb8a6db920 with ID: 0x1f401b
default	13:27:00.025942-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:27:00.026758-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:27:00.028330-0500	Nexy	[0xb8a65cdc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:27:00.030253-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C>
default	13:27:00.034517-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:27:00.036046-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:00.036226-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:00.036369-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:27:00.036379-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:27:00.036407-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:00.036539-0500	Nexy	[0xb8a65cf00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:27:00.036665-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:27:00.037067-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84310.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:00.043653-0500	tccd	AUTHREQ_SUBJECT: msgID=84310.2, subject=com.nexy.assistant,
default	13:27:00.044301-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:00.060080-0500	Nexy	[0xb8a65cf00] invalidated after the last release of the connection object
default	13:27:00.060208-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:00.060241-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:00.060488-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:27:00.061719-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.343, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:00.062572-0500	tccd	AUTHREQ_SUBJECT: msgID=395.343, subject=com.nexy.assistant,
default	13:27:00.063163-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:27:00.079102-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:27:00.079993-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.345, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:00.080744-0500	tccd	AUTHREQ_SUBJECT: msgID=395.345, subject=com.nexy.assistant,
default	13:27:00.081315-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:00.095514-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:27:00.095530-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xb891f8ce0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:27:00.109014-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:00.109920-0500	Nexy	[0xb8a65cf00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:27:00.110305-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=362108692725761 }
default	13:27:00.110410-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:27:00.110450-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:27:00.110481-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:27:00.120398-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:27:00.153877-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:27:00.153898-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:27:00.157342-0500	Nexy	[0xb8a65d040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:27:00.166017-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb8be66a40) Selecting device 71 from constructor
default	13:27:00.166024-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xb8be66a40)
default	13:27:00.166029-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xb8be66a40) not already running
default	13:27:00.166035-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb8be66a40) nothing to teardown
default	13:27:00.166038-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xb8be66a40) connecting device 71
default	13:27:00.166114-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xb8be66a40) Device ID: 71 (Input:No | Output:Yes): true
default	13:27:00.166186-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xb8be66a40) created ioproc 0xa for device 71
default	13:27:00.166264-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb8be66a40) adding 7 device listeners to device 71
default	13:27:00.166426-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb8be66a40) adding 0 device delegate listeners to device 71
default	13:27:00.166433-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xb8be66a40)
default	13:27:00.166492-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:00.166498-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:27:00.166507-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:00.166513-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:27:00.166520-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:27:00.166594-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xb8be66a40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:27:00.166603-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xb8be66a40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:27:00.166606-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:27:00.166610-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb8be66a40) removing 0 device listeners from device 0
default	13:27:00.166614-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb8be66a40) removing 0 device delegate listeners from device 0
default	13:27:00.166616-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xb8be66a40)
default	13:27:00.166652-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:27:00.166887-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:00.167778-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:27:00.167819-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:27:00.167932-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb893095c0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:00.167952-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:00.169096-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:00.169265-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:00.170761-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:00.170948-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:00.171937-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb89309560, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:00.171951-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:00.172241-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:00.172861-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb893099b0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:00.172869-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xb893099b0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:00.172874-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:00.172875-0500	Nexy	AudioConverter -> 0xb893099b0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:00.172888-0500	Nexy	AudioConverter -> 0xb893099b0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:00.172892-0500	Nexy	AudioConverter -> 0xb893099b0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:00.173609-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb89309560, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:00.173618-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xb89309560: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:00.173623-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:00.173624-0500	Nexy	AudioConverter -> 0xb89309560: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:00.173630-0500	Nexy	AudioConverter -> 0xb89309560: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:00.173640-0500	Nexy	AudioConverter -> 0xb89309560: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:00.173748-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xb89309560: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:00.207366-0500	Nexy	[0xb8a65d180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:00.207905-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:00.208076-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84310.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:00.209043-0500	tccd	AUTHREQ_SUBJECT: msgID=84310.3, subject=com.nexy.assistant,
default	13:27:00.209686-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:00.227989-0500	Nexy	[0xb8a65d180] invalidated after the last release of the connection object
default	13:27:00.228075-0500	Nexy	[0xb8a65d180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:00.228456-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:00.228617-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84310.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:00.229434-0500	tccd	AUTHREQ_SUBJECT: msgID=84310.4, subject=com.nexy.assistant,
default	13:27:00.230065-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:00.247555-0500	Nexy	[0xb8a65d180] invalidated after the last release of the connection object
default	13:27:00.247621-0500	Nexy	[0xb8a65d180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:27:00.247708-0500	Nexy	[0xb8a65d180] invalidated after the last release of the connection object
default	13:27:00.487889-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84321.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84321, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84321, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:00.489448-0500	tccd	AUTHREQ_SUBJECT: msgID=84321.1, subject=com.nexy.assistant,
default	13:27:00.490176-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:00.511605-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84321.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84321, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84321, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:00.512447-0500	tccd	AUTHREQ_SUBJECT: msgID=84321.2, subject=com.nexy.assistant,
default	13:27:00.513077-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:00.551606-0500	Nexy	[0xb8a65d540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:27:00.552330-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84310.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84310, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:00.559190-0500	tccd	AUTHREQ_SUBJECT: msgID=84310.5, subject=com.nexy.assistant,
default	13:27:00.559854-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257000 at /Applications/Nexy.app
default	13:27:00.578171-0500	Nexy	[0xb8a65d540] invalidated after the last release of the connection object
default	13:27:00.606729-0500	Nexy	server port 0x00013e03, session port 0x0000350b
default	13:27:02.654594-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x10c10c (Nexy) connectionID: A8A63 pid: 84310 in session 0x101
default	13:27:02.654656-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x10c10c (Nexy) acq:0xb6c3604e0 count:1
default	13:27:02.655072-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f401b","name":"Nexy(84310)"}, "details":null }
default	13:27:02.655128-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f401b from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":84310})
default	13:27:02.655152-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":84310})
default	13:27:02.655617-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 28, PID = 84310, Name = sid:0x1f401b, Nexy(84310), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:27:02.656042-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:02.655697-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 28, PID = 84310, Name = sid:0x1f401b, Nexy(84310), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:27:02.656105-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:02.656131-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:02.655796-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:02.656253-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:02.655930-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:02.658538-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x10c10c removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10c10c (Nexy)"
)}
default	13:27:02.659205-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x14956 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10c10c (Nexy)"
)}
default	13:27:02.667138-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]
default	13:27:02.669742-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310] termination reported by launchd (0, 0, 0)
default	13:27:02.669790-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]
default	13:27:02.670057-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]
default	13:27:02.670286-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]
default	13:27:02.670332-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]
default	13:27:02.675028-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>: none (role: None) (endowments: (null))
default	13:27:02.675247-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>: none (role: None) (endowments: (null))
default	13:27:02.675374-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 84310, name = Nexy
default	13:27:02.675832-0500	launchservicesd	Hit the server for a process handle 1213984d00014956 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>:84310]
default	13:27:02.676007-0500	gamepolicyd	Received state update for 84310 (app<application.com.nexy.assistant.38522673.38522682.6D10D7AB-9521-4DB7-93CE-7644178E486C(501)>, none-NotVisible
default	13:27:02.677776-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x10c10c} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:27:02.677812-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 3
default	13:27:02.677828-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:27:02.679665-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 4
default	13:27:02.679678-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:27:05.735549-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:27:05.824461-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:27:05.824647-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:27:05.871443-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:27:05.873564-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:27:05.876193-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:27:05.876280-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87738 target:app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:05.876375-0500	runningboardd	Assertion 394-80102-87738 (target:app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>) will be created as active
default	13:27:05.879883-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:27:05.879919-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>
default	13:27:05.879930-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:27:05.880021-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:27:05.893632-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] is not RunningBoard jetsam managed.
default	13:27:05.893650-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] This process will not be managed.
default	13:27:05.893661-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]
default	13:27:05.893877-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:05.894577-0500	gamepolicyd	Hit the server for a process handle c27fcd000014976 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]
default	13:27:05.894624-0500	gamepolicyd	Received state update for 84342 (app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>, running-active-NotVisible
default	13:27:05.896847-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]
default	13:27:05.896917-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] from originator [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87739 target:84342 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:27:05.897039-0500	runningboardd	Assertion 394-394-87739 (target:[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]) will be created as active
default	13:27:05.897265-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring jetsam update because this process is not memory-managed
default	13:27:05.897284-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring suspend because this process is not lifecycle managed
default	13:27:05.897308-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Set darwin role to: UserInteractive
default	13:27:05.897325-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring GPU update because this process is not GPU managed
default	13:27:05.897356-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring memory limit update because this process is not memory-managed
default	13:27:05.897401-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] reported to RB as running
default	13:27:05.898555-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring jetsam update because this process is not memory-managed
default	13:27:05.898566-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring suspend because this process is not lifecycle managed
default	13:27:05.898605-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring GPU update because this process is not GPU managed
default	13:27:05.898670-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring memory limit update because this process is not memory-managed
default	13:27:05.898783-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]
default	13:27:05.898843-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84342" ID:394-357-87740 target:84342 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:05.898936-0500	runningboardd	Assertion 394-357-87740 (target:[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]) will be created as active
default	13:27:05.899003-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x10d10d com.nexy.assistant starting stopped process.
default	13:27:05.899996-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:27:05.900187-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 2
default	13:27:05.900213-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:27:05.901381-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:05.901654-0500	runningboardd	Invalidating assertion 394-80102-87738 (target:app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:27:05.901711-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring jetsam update because this process is not memory-managed
default	13:27:05.901755-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring suspend because this process is not lifecycle managed
default	13:27:05.901850-0500	gamepolicyd	Received state update for 84342 (app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>, running-active-NotVisible
default	13:27:05.901787-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring GPU update because this process is not GPU managed
default	13:27:05.901840-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring memory limit update because this process is not memory-managed
default	13:27:05.904858-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:05.907216-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring jetsam update because this process is not memory-managed
default	13:27:05.907229-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring suspend because this process is not lifecycle managed
default	13:27:05.907239-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring GPU update because this process is not GPU managed
default	13:27:05.907258-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] Ignoring memory limit update because this process is not memory-managed
default	13:27:05.910135-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:05.914654-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:05.952116-0500	logger	detected new pid 84342 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:05.976743-0500	Nexy	[0x101855210] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:27:05.976810-0500	Nexy	[0x101855750] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:27:06.006571-0500	gamepolicyd	Received state update for 84342 (app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>, running-active-NotVisible
error	13:27:06.094084-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x7a0528000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:06.094320-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x7a0528000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:06.094527-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x7a0528000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:06.094732-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x7a0528000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:27:06.096276-0500	Nexy	[0x101844370] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:27:06.097040-0500	Nexy	[0x7a06f0000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:27:06.097341-0500	Nexy	[0x7a06f0140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:27:06.097779-0500	Nexy	[0x7a06f0280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:27:06.098007-0500	Nexy	Received configuration update from daemon (initial)
default	13:27:06.099817-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:27:06.100163-0500	Nexy	[0x7a06f03c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:27:06.100871-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84342.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:06.102722-0500	tccd	AUTHREQ_SUBJECT: msgID=84342.1, subject=com.nexy.assistant,
default	13:27:06.103669-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:06.124427-0500	Nexy	[0x7a06f03c0] invalidated after the last release of the connection object
default	13:27:06.124840-0500	Nexy	server port 0x0000300b, session port 0x0000300b
default	13:27:06.126029-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.583, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:27:06.126056-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:06.127079-0500	tccd	AUTHREQ_SUBJECT: msgID=387.583, subject=com.nexy.assistant,
default	13:27:06.127866-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:06.155080-0500	Nexy	New connection 0xe079f main
default	13:27:06.157922-0500	Nexy	CHECKIN: pid=84342
default	13:27:06.167103-0500	Nexy	CHECKEDIN: pid=84342 asn=0x0-0x10d10d foreground=0
default	13:27:06.167087-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84342" ID:394-357-87741 target:84342 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:06.167186-0500	runningboardd	Assertion 394-357-87741 (target:[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]) will be created as active
default	13:27:06.166943-0500	launchservicesd	CHECKIN:0x0-0x10d10d 84342 com.nexy.assistant
default	13:27:06.167668-0500	runningboardd	Invalidating assertion 394-357-87740 (target:[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:27:06.167395-0500	Nexy	[0x7a06f03c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:27:06.168334-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:27:06.167443-0500	Nexy	[0x7a06f03c0] Connection returned listener port: 0x4503
default	13:27:06.168462-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:27:06.167841-0500	Nexy	[0x7a0700300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x7a06f03c0.peer[357].0x7a0700300
default	13:27:06.170430-0500	Nexy	FRONTLOGGING: version 1
default	13:27:06.170497-0500	Nexy	Registered, pid=84342 ASN=0x0,0x10d10d
default	13:27:06.171019-0500	WindowServer	e079f[CreateApplication]: Process creation: 0x0-0x10d10d (Nexy) connectionID: E079F pid: 84342 in session 0x101
default	13:27:06.171324-0500	Nexy	[0x7a06f0500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:27:06.173599-0500	Nexy	[0x7a06f03c0] Connection returned listener port: 0x4503
default	13:27:06.175148-0500	Nexy	BringForward: pid=84342 asn=0x0-0x10d10d bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:27:06.175720-0500	Nexy	BringFrontModifier: pid=84342 asn=0x0-0x10d10d Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:27:06.176532-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:27:06.177860-0500	Nexy	No persisted cache on this platform.
default	13:27:06.180084-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:27:06.182776-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:27:06.182786-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:27:06.182847-0500	Nexy	Initializing connection
default	13:27:06.182888-0500	Nexy	Removing all cached process handles
default	13:27:06.182910-0500	Nexy	Sending handshake request attempt #1 to server
default	13:27:06.182920-0500	Nexy	Creating connection to com.apple.runningboard
default	13:27:06.182929-0500	Nexy	[0x7a06f0640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:27:06.183356-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] as ready
default	13:27:06.183990-0500	Nexy	Handshake succeeded
default	13:27:06.184005-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>
default	13:27:06.978653-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D240962A-ADBC-4D2E-B04F-25D1AB882569 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63210,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x3d87e886 tp_proto=0x06"
default	13:27:06.978733-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63210<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534511 t_state: SYN_SENT process: Nexy:84342 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8a2a9e9b
default	13:27:06.979274-0500	kernel	tcp connected: [<IPv4-redacted>:63210<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534511 t_state: ESTABLISHED process: Nexy:84342 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8a2a9e9b
default	13:27:06.979542-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63210<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534511 t_state: FIN_WAIT_1 process: Nexy:84342 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8a2a9e9b
default	13:27:06.979552-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63210<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534511 t_state: FIN_WAIT_1 process: Nexy:84342 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:27:07.016529-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:27:07.017174-0500	Nexy	[0x7a06f0c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:27:07.018153-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f401c","name":"Nexy(84342)"}, "details":{"PID":84342,"session_type":"Primary"} }
default	13:27:07.018235-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":84342}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f401c, sessionType: 'prim', isRecording: false }, 
]
default	13:27:07.018965-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 84342, name = Nexy
default	13:27:07.019298-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x7a07638a0 with ID: 0x1f401c
default	13:27:07.019658-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:27:07.020428-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:27:07.021866-0500	Nexy	[0x7a06f0dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:27:07.024107-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630 AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630>
default	13:27:07.028565-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:27:07.030052-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:07.030226-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:07.030380-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:27:07.030391-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:27:07.030424-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:07.030554-0500	Nexy	[0x7a06f0f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:27:07.030677-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:27:07.031089-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84342.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:07.037812-0500	tccd	AUTHREQ_SUBJECT: msgID=84342.2, subject=com.nexy.assistant,
default	13:27:07.038481-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:07.054630-0500	Nexy	[0x7a06f0f00] invalidated after the last release of the connection object
default	13:27:07.054768-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:07.054806-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:07.055080-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:27:07.056371-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.346, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:07.057265-0500	tccd	AUTHREQ_SUBJECT: msgID=395.346, subject=com.nexy.assistant,
default	13:27:07.057897-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:27:07.074073-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:27:07.075050-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.348, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:07.075906-0500	tccd	AUTHREQ_SUBJECT: msgID=395.348, subject=com.nexy.assistant,
default	13:27:07.076519-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:07.090590-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:27:07.090606-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x79ec7cd00> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:27:07.104007-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:07.104912-0500	Nexy	[0x7a06f0f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:27:07.105317-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=362246131679233 }
default	13:27:07.105417-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:27:07.105453-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:27:07.105489-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:27:07.115468-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:27:07.148766-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:27:07.148788-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:27:07.152270-0500	Nexy	[0x7a06f1040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:27:07.158936-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7a1718040) Selecting device 71 from constructor
default	13:27:07.158946-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7a1718040)
default	13:27:07.158952-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7a1718040) not already running
default	13:27:07.158957-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7a1718040) nothing to teardown
default	13:27:07.158961-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7a1718040) connecting device 71
default	13:27:07.159028-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7a1718040) Device ID: 71 (Input:No | Output:Yes): true
default	13:27:07.159092-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7a1718040) created ioproc 0xa for device 71
default	13:27:07.159184-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7a1718040) adding 7 device listeners to device 71
default	13:27:07.159318-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7a1718040) adding 0 device delegate listeners to device 71
default	13:27:07.159326-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7a1718040)
default	13:27:07.159392-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:07.159401-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:27:07.159413-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:07.159419-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:27:07.159425-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:27:07.159507-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7a1718040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:27:07.159519-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7a1718040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:27:07.159523-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:27:07.159528-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7a1718040) removing 0 device listeners from device 0
default	13:27:07.159532-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7a1718040) removing 0 device delegate listeners from device 0
default	13:27:07.159534-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7a1718040)
default	13:27:07.159568-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:27:07.159802-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:07.160692-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:27:07.160731-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:27:07.160845-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x79edcd5f0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:07.160870-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:07.162005-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:07.162173-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:07.163577-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:07.163748-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:07.164753-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x79edcd590, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:07.164766-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:07.165030-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:07.165724-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x79edcd9e0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:07.165735-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x79edcd9e0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:07.165740-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:07.165739-0500	Nexy	AudioConverter -> 0x79edcd9e0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:07.165746-0500	Nexy	AudioConverter -> 0x79edcd9e0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:07.165751-0500	Nexy	AudioConverter -> 0x79edcd9e0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:07.166505-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x79edcd590, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:07.166513-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x79edcd590: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:07.166518-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:07.166520-0500	Nexy	AudioConverter -> 0x79edcd590: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:07.166528-0500	Nexy	AudioConverter -> 0x79edcd590: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:07.166538-0500	Nexy	AudioConverter -> 0x79edcd590: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:07.166645-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x79edcd590: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:07.200017-0500	Nexy	[0x7a06f1180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:07.200524-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:07.200699-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84342.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:07.201661-0500	tccd	AUTHREQ_SUBJECT: msgID=84342.3, subject=com.nexy.assistant,
default	13:27:07.202286-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:07.220777-0500	Nexy	[0x7a06f1180] invalidated after the last release of the connection object
default	13:27:07.220861-0500	Nexy	[0x7a06f1180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:07.221270-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:07.221438-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84342.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:07.222305-0500	tccd	AUTHREQ_SUBJECT: msgID=84342.4, subject=com.nexy.assistant,
default	13:27:07.222953-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:07.241007-0500	Nexy	[0x7a06f1180] invalidated after the last release of the connection object
default	13:27:07.241075-0500	Nexy	[0x7a06f1180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:27:07.241166-0500	Nexy	[0x7a06f1180] invalidated after the last release of the connection object
default	13:27:07.485867-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84352.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84352, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84352, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:07.487540-0500	tccd	AUTHREQ_SUBJECT: msgID=84352.1, subject=com.nexy.assistant,
default	13:27:07.488231-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:07.509299-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84352.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84352, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84352, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:07.510143-0500	tccd	AUTHREQ_SUBJECT: msgID=84352.2, subject=com.nexy.assistant,
default	13:27:07.510766-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:07.549969-0500	Nexy	[0x7a06f1540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:27:07.550652-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84342.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84342, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:07.557225-0500	tccd	AUTHREQ_SUBJECT: msgID=84342.5, subject=com.nexy.assistant,
default	13:27:07.557881-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257000 at /Applications/Nexy.app
default	13:27:07.576028-0500	Nexy	[0x7a06f1540] invalidated after the last release of the connection object
default	13:27:07.604969-0500	Nexy	server port 0x00014003, session port 0x0000300b
default	13:27:09.580925-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	13:27:09.643248-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x10d10d (Nexy) connectionID: E079F pid: 84342 in session 0x101
default	13:27:09.643306-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x10d10d (Nexy) acq:0xb6c363e40 count:1
default	13:27:09.643551-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f401c","name":"Nexy(84342)"}, "details":null }
default	13:27:09.643605-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f401c from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":84342})
default	13:27:09.643630-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":84342})
default	13:27:09.644056-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 29, PID = 84342, Name = sid:0x1f401c, Nexy(84342), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:27:09.644176-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 29, PID = 84342, Name = sid:0x1f401c, Nexy(84342), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:27:09.644711-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:09.644783-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:09.644808-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:09.644390-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:09.644546-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:09.644932-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:09.645597-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x10d10d removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10d10d (Nexy)"
)}
default	13:27:09.647018-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x14976 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10d10d (Nexy)"
)}
default	13:27:09.653388-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]
default	13:27:09.658129-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342] termination reported by launchd (0, 0, 0)
default	13:27:09.658179-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]
default	13:27:09.658458-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]
default	13:27:09.658675-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]
default	13:27:09.658723-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]
default	13:27:09.663922-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>: none (role: None) (endowments: (null))
default	13:27:09.664130-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>: none (role: None) (endowments: (null))
default	13:27:09.664264-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 84342, name = Nexy
default	13:27:09.664706-0500	launchservicesd	Hit the server for a process handle c27fcd000014976 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>:84342]
default	13:27:09.664839-0500	gamepolicyd	Received state update for 84342 (app<application.com.nexy.assistant.38522673.38522682.8E41A90B-D389-4D76-B1F4-EBBA91D17630(501)>, none-NotVisible
default	13:27:09.666512-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x10d10d} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:27:09.666553-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 3
default	13:27:09.666569-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:27:09.668124-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 4
default	13:27:09.668137-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:27:12.730215-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:27:12.823156-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:27:12.823333-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:27:12.825285-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:27:12.827243-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:27:12.829679-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:27:12.829770-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87764 target:app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:12.829852-0500	runningboardd	Assertion 394-80102-87764 (target:app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>) will be created as active
default	13:27:12.832499-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:27:12.832529-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>
default	13:27:12.832545-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:27:12.832619-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:27:12.846056-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] is not RunningBoard jetsam managed.
default	13:27:12.846074-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] This process will not be managed.
default	13:27:12.846082-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]
default	13:27:12.846302-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:12.846957-0500	gamepolicyd	Hit the server for a process handle bb3d1b700014994 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]
default	13:27:12.846998-0500	gamepolicyd	Received state update for 84372 (app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>, running-active-NotVisible
default	13:27:12.849081-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]
default	13:27:12.849142-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] from originator [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87765 target:84372 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:27:12.849255-0500	runningboardd	Assertion 394-394-87765 (target:[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]) will be created as active
default	13:27:12.849446-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring jetsam update because this process is not memory-managed
default	13:27:12.849466-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring suspend because this process is not lifecycle managed
default	13:27:12.849487-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Set darwin role to: UserInteractive
default	13:27:12.849503-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring GPU update because this process is not GPU managed
default	13:27:12.849538-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring memory limit update because this process is not memory-managed
default	13:27:12.849590-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] reported to RB as running
default	13:27:12.850755-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring jetsam update because this process is not memory-managed
default	13:27:12.850779-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring suspend because this process is not lifecycle managed
default	13:27:12.850806-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring GPU update because this process is not GPU managed
default	13:27:12.850867-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring memory limit update because this process is not memory-managed
default	13:27:12.850953-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]
default	13:27:12.851026-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84372" ID:394-357-87766 target:84372 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:12.851180-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x10e10e com.nexy.assistant starting stopped process.
default	13:27:12.851136-0500	runningboardd	Assertion 394-357-87766 (target:[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]) will be created as active
default	13:27:12.852139-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:27:12.852345-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 2
default	13:27:12.852374-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:27:12.853631-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:12.853630-0500	kernel	Nexy[84372] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0xe9d3a15b9f2cff51. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:27:12.853650-0500	kernel	Nexy[84372] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0xe9d3a15b9f2cff51. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:27:12.853929-0500	runningboardd	Invalidating assertion 394-80102-87764 (target:app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:27:12.853992-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring jetsam update because this process is not memory-managed
default	13:27:12.854054-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring suspend because this process is not lifecycle managed
default	13:27:12.854088-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring GPU update because this process is not GPU managed
default	13:27:12.854187-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring memory limit update because this process is not memory-managed
default	13:27:12.854089-0500	gamepolicyd	Received state update for 84372 (app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>, running-active-NotVisible
default	13:27:12.856853-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:12.864445-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:12.903376-0500	logger	detected new pid 84372 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:12.927938-0500	Nexy	[0x103a11990] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:27:12.928019-0500	Nexy	[0x103a0cd90] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:27:12.955250-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring jetsam update because this process is not memory-managed
default	13:27:12.955265-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring suspend because this process is not lifecycle managed
default	13:27:12.955276-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring GPU update because this process is not GPU managed
default	13:27:12.955451-0500	gamepolicyd	Received state update for 84372 (app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>, running-active-NotVisible
default	13:27:12.955297-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] Ignoring memory limit update because this process is not memory-managed
default	13:27:12.958206-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:12.958513-0500	gamepolicyd	Received state update for 84372 (app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>, running-active-NotVisible
error	13:27:13.042391-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x8d24e8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:13.042608-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x8d24e8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:13.042809-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x8d24e8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:13.043009-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x8d24e8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:27:13.044435-0500	Nexy	[0x103a17190] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:27:13.045172-0500	Nexy	[0x8d2664000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:27:13.045468-0500	Nexy	[0x8d2664140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:27:13.045912-0500	Nexy	[0x8d2664280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:27:13.046101-0500	Nexy	Received configuration update from daemon (initial)
default	13:27:13.048229-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:27:13.048582-0500	Nexy	[0x8d26643c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:27:13.049283-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84372.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:13.050910-0500	tccd	AUTHREQ_SUBJECT: msgID=84372.1, subject=com.nexy.assistant,
default	13:27:13.051692-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:13.071151-0500	Nexy	[0x8d26643c0] invalidated after the last release of the connection object
default	13:27:13.071481-0500	Nexy	server port 0x0000320f, session port 0x0000320f
default	13:27:13.072520-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.584, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:27:13.072549-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:13.073365-0500	tccd	AUTHREQ_SUBJECT: msgID=387.584, subject=com.nexy.assistant,
default	13:27:13.074084-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:13.098026-0500	Nexy	New connection 0x8db2b main
default	13:27:13.101033-0500	Nexy	CHECKIN: pid=84372
default	13:27:13.110460-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84372" ID:394-357-87767 target:84372 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:13.110557-0500	runningboardd	Assertion 394-357-87767 (target:[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]) will be created as active
default	13:27:13.110937-0500	runningboardd	Invalidating assertion 394-357-87766 (target:[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:27:13.111164-0500	Nexy	CHECKEDIN: pid=84372 asn=0x0-0x10e10e foreground=0
default	13:27:13.111027-0500	launchservicesd	CHECKIN:0x0-0x10e10e 84372 com.nexy.assistant
default	13:27:13.111397-0500	Nexy	[0x8d26643c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:27:13.111212-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:27:13.111444-0500	Nexy	[0x8d26643c0] Connection returned listener port: 0x5003
default	13:27:13.111334-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:27:13.111738-0500	Nexy	[0x8d2678300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x8d26643c0.peer[357].0x8d2678300
default	13:27:13.118597-0500	Nexy	FRONTLOGGING: version 1
default	13:27:13.118653-0500	Nexy	Registered, pid=84372 ASN=0x0,0x10e10e
default	13:27:13.119208-0500	WindowServer	8db2b[CreateApplication]: Process creation: 0x0-0x10e10e (Nexy) connectionID: 8DB2B pid: 84372 in session 0x101
default	13:27:13.119595-0500	Nexy	[0x8d2664500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:27:13.124114-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:27:13.132091-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 84372
default	13:27:13.942858-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0F257149-1BFD-48A1-8D51-7007784C7B64 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63217,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x3725b932 tp_proto=0x06"
default	13:27:13.942914-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63217<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534540 t_state: SYN_SENT process: Nexy:84372 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbfa5fbc4
default	13:27:13.943572-0500	kernel	tcp connected: [<IPv4-redacted>:63217<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534540 t_state: ESTABLISHED process: Nexy:84372 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbfa5fbc4
default	13:27:13.943854-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63217<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534540 t_state: FIN_WAIT_1 process: Nexy:84372 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xbfa5fbc4
default	13:27:13.943862-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63217<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534540 t_state: FIN_WAIT_1 process: Nexy:84372 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:27:13.981431-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:27:13.982076-0500	Nexy	[0x8d2664c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:27:13.983232-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f401d","name":"Nexy(84372)"}, "details":{"PID":84372,"session_type":"Primary"} }
default	13:27:13.983319-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":84372}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f401d, sessionType: 'prim', isRecording: false }, 
]
default	13:27:13.984354-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 84372, name = Nexy
default	13:27:13.984766-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x8d26e3940 with ID: 0x1f401d
default	13:27:13.985100-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:27:13.986102-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:27:13.987566-0500	Nexy	[0x8d2664dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:27:13.989940-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC>
default	13:27:13.994935-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:27:13.996440-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:13.996623-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:13.996774-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:27:13.996788-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:27:13.996819-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:13.996953-0500	Nexy	[0x8d2664f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:27:13.997085-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:27:13.997515-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84372.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:14.005146-0500	tccd	AUTHREQ_SUBJECT: msgID=84372.2, subject=com.nexy.assistant,
default	13:27:14.005863-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:14.022428-0500	Nexy	[0x8d2664f00] invalidated after the last release of the connection object
default	13:27:14.022629-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:14.022691-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:14.022993-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:27:14.024451-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.349, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:14.025381-0500	tccd	AUTHREQ_SUBJECT: msgID=395.349, subject=com.nexy.assistant,
default	13:27:14.026019-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:27:14.042357-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:27:14.043354-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.351, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:14.044229-0500	tccd	AUTHREQ_SUBJECT: msgID=395.351, subject=com.nexy.assistant,
default	13:27:14.044831-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:14.058958-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:27:14.058976-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x8d12c46a0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:27:14.072434-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:14.073363-0500	Nexy	[0x8d2664f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:27:14.073780-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=362374980698113 }
default	13:27:14.073893-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:27:14.073932-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:27:14.073967-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:27:14.083678-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:27:14.117477-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:27:14.117497-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:27:14.121129-0500	Nexy	[0x8d2665040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:27:14.127819-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x8d3e1ea40) Selecting device 71 from constructor
default	13:27:14.127827-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x8d3e1ea40)
default	13:27:14.127831-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x8d3e1ea40) not already running
default	13:27:14.127837-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x8d3e1ea40) nothing to teardown
default	13:27:14.127840-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x8d3e1ea40) connecting device 71
default	13:27:14.127908-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x8d3e1ea40) Device ID: 71 (Input:No | Output:Yes): true
default	13:27:14.127974-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x8d3e1ea40) created ioproc 0xa for device 71
default	13:27:14.128070-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x8d3e1ea40) adding 7 device listeners to device 71
default	13:27:14.128221-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x8d3e1ea40) adding 0 device delegate listeners to device 71
default	13:27:14.128228-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x8d3e1ea40)
default	13:27:14.128293-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:14.128300-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:27:14.128312-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:14.128317-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:27:14.128324-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:27:14.128401-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x8d3e1ea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:27:14.128407-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x8d3e1ea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:27:14.128411-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:27:14.128415-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x8d3e1ea40) removing 0 device listeners from device 0
default	13:27:14.128417-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x8d3e1ea40) removing 0 device delegate listeners from device 0
default	13:27:14.128422-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x8d3e1ea40)
default	13:27:14.128467-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:27:14.128700-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:14.129688-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:27:14.129731-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:27:14.129848-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8d12b7900, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:14.129868-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:14.131006-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:14.131206-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:14.132738-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:14.132920-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:14.133955-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8d12b78a0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:14.133969-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:14.134227-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:14.134864-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8d12b7cf0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:14.134872-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8d12b7cf0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:14.134879-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:14.134880-0500	Nexy	AudioConverter -> 0x8d12b7cf0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:14.134890-0500	Nexy	AudioConverter -> 0x8d12b7cf0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:14.134893-0500	Nexy	AudioConverter -> 0x8d12b7cf0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:14.135672-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x8d12b78a0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:14.135679-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8d12b78a0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:14.135684-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:14.135687-0500	Nexy	AudioConverter -> 0x8d12b78a0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:14.135694-0500	Nexy	AudioConverter -> 0x8d12b78a0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:14.135704-0500	Nexy	AudioConverter -> 0x8d12b78a0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:14.135816-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x8d12b78a0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:14.169456-0500	Nexy	[0x8d2665180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:14.169981-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:14.170157-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84372.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:14.171175-0500	tccd	AUTHREQ_SUBJECT: msgID=84372.3, subject=com.nexy.assistant,
default	13:27:14.172003-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:14.190360-0500	Nexy	[0x8d2665180] invalidated after the last release of the connection object
default	13:27:14.190445-0500	Nexy	[0x8d2665180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:14.190862-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:14.191028-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84372.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:14.191817-0500	tccd	AUTHREQ_SUBJECT: msgID=84372.4, subject=com.nexy.assistant,
default	13:27:14.192404-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:14.210225-0500	Nexy	[0x8d2665180] invalidated after the last release of the connection object
default	13:27:14.210288-0500	Nexy	[0x8d2665180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:27:14.210376-0500	Nexy	[0x8d2665180] invalidated after the last release of the connection object
default	13:27:14.459312-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84382.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84382, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84382, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:14.460998-0500	tccd	AUTHREQ_SUBJECT: msgID=84382.1, subject=com.nexy.assistant,
default	13:27:14.461685-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:14.484724-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84382.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84382, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84382, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:14.485786-0500	tccd	AUTHREQ_SUBJECT: msgID=84382.2, subject=com.nexy.assistant,
default	13:27:14.486458-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:14.532337-0500	Nexy	[0x8d2665540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:27:14.533560-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84372.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84372, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:14.541084-0500	tccd	AUTHREQ_SUBJECT: msgID=84372.5, subject=com.nexy.assistant,
default	13:27:14.541789-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257000 at /Applications/Nexy.app
default	13:27:14.561319-0500	Nexy	[0x8d2665540] invalidated after the last release of the connection object
default	13:27:14.590377-0500	Nexy	server port 0x00011003, session port 0x0000320f
default	13:27:16.636554-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x10e10e (Nexy) connectionID: 8DB2B pid: 84372 in session 0x101
default	13:27:16.636615-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x10e10e (Nexy) acq:0xb6c362660 count:1
default	13:27:16.636935-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f401d","name":"Nexy(84372)"}, "details":null }
default	13:27:16.636992-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f401d from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":84372})
default	13:27:16.637016-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":84372})
default	13:27:16.637376-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 30, PID = 84372, Name = sid:0x1f401d, Nexy(84372), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:27:16.637491-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 30, PID = 84372, Name = sid:0x1f401d, Nexy(84372), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:27:16.637985-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:16.638075-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:16.638180-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:16.638253-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:16.637648-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:16.637824-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:16.642941-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x10e10e removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10e10e (Nexy)"
)}
default	13:27:16.645540-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x14994 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10e10e (Nexy)"
)}
default	13:27:16.651901-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]
default	13:27:16.657195-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372] termination reported by launchd (0, 0, 0)
default	13:27:16.657291-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]
default	13:27:16.657551-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]
default	13:27:16.657764-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]
default	13:27:16.657816-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]
default	13:27:16.662879-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>: none (role: None) (endowments: (null))
default	13:27:16.663137-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>: none (role: None) (endowments: (null))
default	13:27:16.663300-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 84372, name = Nexy
default	13:27:16.664881-0500	launchservicesd	Hit the server for a process handle bb3d1b700014994 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>:84372]
default	13:27:16.665055-0500	gamepolicyd	Received state update for 84372 (app<application.com.nexy.assistant.38522673.38522682.DC506E14-0E77-4862-A8BD-1F526A41CBCC(501)>, none-NotVisible
default	13:27:16.666691-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x10e10e} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:27:16.666726-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 3
default	13:27:16.666744-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:27:16.668149-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 4
default	13:27:16.668160-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:27:19.710805-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:27:19.803102-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:27:19.803275-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:27:19.804915-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:27:19.807488-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:27:19.809752-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:27:19.809844-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87794 target:app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:19.809931-0500	runningboardd	Assertion 394-80102-87794 (target:app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>) will be created as active
default	13:27:19.812608-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:27:19.812638-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>
default	13:27:19.812655-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:27:19.812793-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000954 ms (wallclock); resolved to {4294967295, (null)}
default	13:27:19.825529-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] is not RunningBoard jetsam managed.
default	13:27:19.825545-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] This process will not be managed.
default	13:27:19.825556-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]
default	13:27:19.825753-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:19.826534-0500	gamepolicyd	Hit the server for a process handle 506e701000149b3 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]
default	13:27:19.826574-0500	gamepolicyd	Received state update for 84403 (app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>, running-active-NotVisible
default	13:27:19.828677-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]
default	13:27:19.828744-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] from originator [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87795 target:84403 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:27:19.828866-0500	runningboardd	Assertion 394-394-87795 (target:[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]) will be created as active
default	13:27:19.829061-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring jetsam update because this process is not memory-managed
default	13:27:19.829077-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring suspend because this process is not lifecycle managed
default	13:27:19.829101-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Set darwin role to: UserInteractive
default	13:27:19.829118-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring GPU update because this process is not GPU managed
default	13:27:19.829153-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring memory limit update because this process is not memory-managed
default	13:27:19.829210-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] reported to RB as running
default	13:27:19.830694-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring jetsam update because this process is not memory-managed
default	13:27:19.830754-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring suspend because this process is not lifecycle managed
default	13:27:19.830782-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring GPU update because this process is not GPU managed
default	13:27:19.830871-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring memory limit update because this process is not memory-managed
default	13:27:19.830971-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]
default	13:27:19.831073-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84403" ID:394-357-87796 target:84403 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:19.831151-0500	runningboardd	Assertion 394-357-87796 (target:[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]) will be created as active
default	13:27:19.831343-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x10f10f com.nexy.assistant starting stopped process.
default	13:27:19.832366-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:27:19.832607-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 2
default	13:27:19.832634-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:27:19.833578-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:19.833863-0500	runningboardd	Invalidating assertion 394-80102-87794 (target:app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:27:19.833904-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring jetsam update because this process is not memory-managed
default	13:27:19.833995-0500	gamepolicyd	Received state update for 84403 (app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>, running-active-NotVisible
default	13:27:19.833920-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring suspend because this process is not lifecycle managed
default	13:27:19.833936-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring GPU update because this process is not GPU managed
default	13:27:19.834049-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring memory limit update because this process is not memory-managed
default	13:27:19.834369-0500	kernel	Nexy[84403] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0xd102a1ce6ff5a02d. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:27:19.834393-0500	kernel	Nexy[84403] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0xd102a1ce6ff5a02d. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:27:19.836905-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:19.844871-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:19.884852-0500	logger	detected new pid 84403 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:19.912959-0500	Nexy	[0x104041990] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:27:19.913034-0500	Nexy	[0x10403cd90] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:27:19.937918-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring jetsam update because this process is not memory-managed
default	13:27:19.937935-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring suspend because this process is not lifecycle managed
default	13:27:19.937947-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring GPU update because this process is not GPU managed
default	13:27:19.938112-0500	gamepolicyd	Received state update for 84403 (app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>, running-active-NotVisible
default	13:27:19.937968-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] Ignoring memory limit update because this process is not memory-managed
default	13:27:19.940862-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:19.941193-0500	gamepolicyd	Received state update for 84403 (app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>, running-active-NotVisible
error	13:27:20.031868-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x8024e0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:20.032104-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x8024e0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:20.032311-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x8024e0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:20.032516-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x8024e0000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:27:20.033967-0500	Nexy	[0x104047190] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:27:20.034724-0500	Nexy	[0x80265c000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:27:20.035020-0500	Nexy	[0x80265c140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:27:20.035429-0500	Nexy	[0x80265c280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:27:20.037388-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:27:20.037739-0500	Nexy	[0x80265c3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:27:20.037765-0500	Nexy	Received configuration update from daemon (initial)
default	13:27:20.038429-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84403.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:20.040043-0500	tccd	AUTHREQ_SUBJECT: msgID=84403.1, subject=com.nexy.assistant,
default	13:27:20.040961-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:20.060482-0500	Nexy	[0x80265c3c0] invalidated after the last release of the connection object
default	13:27:20.060987-0500	Nexy	server port 0x0000360f, session port 0x0000360f
default	13:27:20.061935-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.585, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:27:20.061963-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:20.062784-0500	tccd	AUTHREQ_SUBJECT: msgID=387.585, subject=com.nexy.assistant,
default	13:27:20.063494-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:20.088732-0500	Nexy	New connection 0xa8a53 main
default	13:27:20.091520-0500	Nexy	CHECKIN: pid=84403
default	13:27:20.100904-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84403" ID:394-357-87798 target:84403 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:20.101008-0500	runningboardd	Assertion 394-357-87798 (target:[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]) will be created as active
default	13:27:20.101191-0500	Nexy	CHECKEDIN: pid=84403 asn=0x0-0x10f10f foreground=0
default	13:27:20.101028-0500	launchservicesd	CHECKIN:0x0-0x10f10f 84403 com.nexy.assistant
default	13:27:20.101434-0500	runningboardd	Invalidating assertion 394-357-87796 (target:[app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:27:20.101464-0500	Nexy	[0x80265c3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:27:20.101533-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:27:20.101511-0500	Nexy	[0x80265c3c0] Connection returned listener port: 0x4903
default	13:27:20.101651-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:27:20.102164-0500	Nexy	[0x802670300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x80265c3c0.peer[357].0x802670300
default	13:27:20.104706-0500	Nexy	FRONTLOGGING: version 1
default	13:27:20.104779-0500	Nexy	Registered, pid=84403 ASN=0x0,0x10f10f
default	13:27:20.105309-0500	WindowServer	a8a53[CreateApplication]: Process creation: 0x0-0x10f10f (Nexy) connectionID: A8A53 pid: 84403 in session 0x101
default	13:27:20.105681-0500	Nexy	[0x80265c500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:27:20.108971-0500	Nexy	BringForward: pid=84403 asn=0x0-0x10f10f bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:27:20.109461-0500	Nexy	BringFrontModifier: pid=84403 asn=0x0-0x10f10f Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:27:20.113531-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:27:20.114372-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:27:20.118221-0500	Nexy	Handshake succeeded
default	13:27:20.118236-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>
default	13:27:20.118662-0500	Nexy	[0x80265c3c0] Connection returned listener port: 0x4903
default	13:27:21.078247-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 535B0E08-1ABC-4E56-87DF-47B60EB14484 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63228,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x788a6d28 tp_proto=0x06"
default	13:27:21.078330-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63228<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534652 t_state: SYN_SENT process: Nexy:84403 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9b03d017
default	13:27:21.078860-0500	kernel	tcp connected: [<IPv4-redacted>:63228<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534652 t_state: ESTABLISHED process: Nexy:84403 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9b03d017
default	13:27:21.079124-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63228<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534652 t_state: FIN_WAIT_1 process: Nexy:84403 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x9b03d017
default	13:27:21.079134-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63228<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534652 t_state: FIN_WAIT_1 process: Nexy:84403 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:27:21.117017-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:27:21.117660-0500	Nexy	[0x80265cc80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:27:21.118901-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f401e","name":"Nexy(84403)"}, "details":{"PID":84403,"session_type":"Primary"} }
default	13:27:21.118987-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":84403}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f401e, sessionType: 'prim', isRecording: false }, 
]
default	13:27:21.119719-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 84403, name = Nexy
default	13:27:21.120109-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x8026db880 with ID: 0x1f401e
default	13:27:21.120412-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:27:21.121200-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:27:21.122649-0500	Nexy	[0x80265cdc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:27:21.124917-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151 AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151>
default	13:27:21.129595-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:27:21.131215-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:21.131395-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:21.131547-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:27:21.131560-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:27:21.131591-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:21.131726-0500	Nexy	[0x80265cf00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:27:21.131861-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:27:21.132257-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84403.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:21.139507-0500	tccd	AUTHREQ_SUBJECT: msgID=84403.2, subject=com.nexy.assistant,
default	13:27:21.141093-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:21.157381-0500	Nexy	[0x80265cf00] invalidated after the last release of the connection object
default	13:27:21.157510-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:21.157548-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:21.157759-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:27:21.158942-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.352, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:21.159742-0500	tccd	AUTHREQ_SUBJECT: msgID=395.352, subject=com.nexy.assistant,
default	13:27:21.160295-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:27:21.190486-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:27:21.192697-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.354, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:21.202176-0500	tccd	AUTHREQ_SUBJECT: msgID=395.354, subject=com.nexy.assistant,
default	13:27:21.208173-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:21.256736-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:27:21.256788-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x8012a4020> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:27:21.287962-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:21.288785-0500	Nexy	[0x80265cf00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:27:21.289187-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=362508124684289 }
default	13:27:21.289300-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:27:21.289344-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:27:21.289374-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:27:21.300256-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:27:21.334892-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:27:21.334923-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:27:21.339168-0500	Nexy	[0x80265d040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:27:21.348778-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x803deaa40) Selecting device 71 from constructor
default	13:27:21.348790-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x803deaa40)
default	13:27:21.348795-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x803deaa40) not already running
default	13:27:21.348802-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x803deaa40) nothing to teardown
default	13:27:21.348804-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x803deaa40) connecting device 71
default	13:27:21.348881-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x803deaa40) Device ID: 71 (Input:No | Output:Yes): true
default	13:27:21.348956-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x803deaa40) created ioproc 0xa for device 71
default	13:27:21.349042-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x803deaa40) adding 7 device listeners to device 71
default	13:27:21.349189-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x803deaa40) adding 0 device delegate listeners to device 71
default	13:27:21.349196-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x803deaa40)
default	13:27:21.349257-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:21.349266-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:27:21.349276-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:21.349282-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:27:21.349288-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:27:21.349364-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x803deaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:27:21.349375-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x803deaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:27:21.349379-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:27:21.349383-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x803deaa40) removing 0 device listeners from device 0
default	13:27:21.349385-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x803deaa40) removing 0 device delegate listeners from device 0
default	13:27:21.349390-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x803deaa40)
default	13:27:21.349426-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:27:21.349663-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:21.350645-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:27:21.350684-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:27:21.350816-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x80129bed0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:21.350836-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:21.352051-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:21.352221-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:21.353898-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:21.354090-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:21.355108-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x80130c240, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:21.355120-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:21.355386-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:21.356070-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x80130c210, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:21.356079-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x80130c210: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:21.356081-0500	Nexy	AudioConverter -> 0x80130c210: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:21.356085-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:21.356089-0500	Nexy	AudioConverter -> 0x80130c210: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:21.356092-0500	Nexy	AudioConverter -> 0x80130c210: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:21.356817-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x80130c240, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:21.356826-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x80130c240: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:21.356827-0500	Nexy	AudioConverter -> 0x80130c240: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:21.356831-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:21.356834-0500	Nexy	AudioConverter -> 0x80130c240: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:21.356843-0500	Nexy	AudioConverter -> 0x80130c240: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:21.356956-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x80130c240: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:21.391510-0500	Nexy	[0x80265d180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:21.392075-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:21.392249-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84403.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:21.393299-0500	tccd	AUTHREQ_SUBJECT: msgID=84403.3, subject=com.nexy.assistant,
default	13:27:21.393975-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:21.412786-0500	Nexy	[0x80265d180] invalidated after the last release of the connection object
default	13:27:21.412877-0500	Nexy	[0x80265d180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:21.413317-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:21.413496-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84403.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:21.414416-0500	tccd	AUTHREQ_SUBJECT: msgID=84403.4, subject=com.nexy.assistant,
default	13:27:21.415113-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:21.432940-0500	Nexy	[0x80265d180] invalidated after the last release of the connection object
default	13:27:21.433007-0500	Nexy	[0x80265d180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:27:21.433098-0500	Nexy	[0x80265d180] invalidated after the last release of the connection object
default	13:27:21.677506-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84467.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84467, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84467, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:21.679553-0500	tccd	AUTHREQ_SUBJECT: msgID=84467.1, subject=com.nexy.assistant,
default	13:27:21.680466-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:21.709115-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84467.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84467, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84467, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:21.710329-0500	tccd	AUTHREQ_SUBJECT: msgID=84467.2, subject=com.nexy.assistant,
default	13:27:21.711069-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:21.754352-0500	Nexy	[0x80265d540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:27:21.755074-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84403.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84403, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:21.761751-0500	tccd	AUTHREQ_SUBJECT: msgID=84403.5, subject=com.nexy.assistant,
default	13:27:21.762434-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257000 at /Applications/Nexy.app
default	13:27:21.780404-0500	Nexy	[0x80265d540] invalidated after the last release of the connection object
default	13:27:21.808320-0500	Nexy	server port 0x00014703, session port 0x0000360f
default	13:27:23.513792-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	13:27:23.848893-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x10f10f (Nexy) connectionID: A8A53 pid: 84403 in session 0x101
default	13:27:23.849311-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f401e","name":"Nexy(84403)"}, "details":null }
default	13:27:23.849342-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f401e from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":84403})
default	13:27:23.849350-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":84403})
default	13:27:23.849632-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 31, PID = 84403, Name = sid:0x1f401e, Nexy(84403), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:27:23.849749-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 31, PID = 84403, Name = sid:0x1f401e, Nexy(84403), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:27:23.848936-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x10f10f (Nexy) acq:0xb6c3601c0 count:1
default	13:27:23.850260-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:23.850322-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:23.850342-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:23.849975-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:23.850071-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:23.850426-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:23.855786-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x10f10f removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10f10f (Nexy)"
)}
default	13:27:23.857508-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x149b3 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10f10f (Nexy)"
)}
default	13:27:23.869971-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]
default	13:27:23.870017-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]
default	13:27:23.880148-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>: none (role: None) (endowments: (null))
default	13:27:23.880669-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 84403, name = Nexy
default	13:27:23.880530-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>: none (role: None) (endowments: (null))
default	13:27:23.883549-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]
default	13:27:23.884027-0500	gamepolicyd	Received state update for 84403 (app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>, none-NotVisible
default	13:27:23.884274-0500	launchservicesd	Hit the server for a process handle 506e701000149b3 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.D4C730A7-9EFA-441C-86C0-DCD435C04151(501)>:84403]
default	13:27:23.893131-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 4
default	13:27:23.893146-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:27:26.946158-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:27:27.044219-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:27:27.044394-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:27:27.046142-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:27:27.048360-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:27:27.051028-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:27:27.051120-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87851 target:app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:27.051208-0500	runningboardd	Assertion 394-80102-87851 (target:app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>) will be created as active
default	13:27:27.053869-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:27:27.053905-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>
default	13:27:27.053925-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:27:27.054004-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000954 ms (wallclock); resolved to {4294967295, (null)}
default	13:27:27.067166-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] is not RunningBoard jetsam managed.
default	13:27:27.067183-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] This process will not be managed.
default	13:27:27.067193-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]
default	13:27:27.067394-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:27.068114-0500	gamepolicyd	Hit the server for a process handle 1be0828900014a07 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]
default	13:27:27.068165-0500	gamepolicyd	Received state update for 84487 (app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>, running-active-NotVisible
default	13:27:27.070106-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]
default	13:27:27.070167-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] from originator [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87852 target:84487 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:27:27.070285-0500	runningboardd	Assertion 394-394-87852 (target:[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]) will be created as active
default	13:27:27.070493-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring jetsam update because this process is not memory-managed
default	13:27:27.070513-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring suspend because this process is not lifecycle managed
default	13:27:27.070533-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Set darwin role to: UserInteractive
default	13:27:27.070552-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring GPU update because this process is not GPU managed
default	13:27:27.070584-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring memory limit update because this process is not memory-managed
default	13:27:27.070672-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] reported to RB as running
default	13:27:27.071979-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring jetsam update because this process is not memory-managed
default	13:27:27.072061-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring suspend because this process is not lifecycle managed
default	13:27:27.072103-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring GPU update because this process is not GPU managed
default	13:27:27.072216-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring memory limit update because this process is not memory-managed
default	13:27:27.072278-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84487" ID:394-357-87853 target:84487 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:27.072350-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]
default	13:27:27.072421-0500	runningboardd	Assertion 394-357-87853 (target:[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]) will be created as active
default	13:27:27.072779-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x110110 com.nexy.assistant starting stopped process.
default	13:27:27.074359-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:27:27.074630-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 2
default	13:27:27.074666-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:27:27.076508-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:27.076886-0500	runningboardd	Invalidating assertion 394-80102-87851 (target:app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:27:27.076945-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring jetsam update because this process is not memory-managed
default	13:27:27.077006-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring suspend because this process is not lifecycle managed
default	13:27:27.077071-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring GPU update because this process is not GPU managed
default	13:27:27.077152-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring memory limit update because this process is not memory-managed
default	13:27:27.076968-0500	gamepolicyd	Received state update for 84487 (app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>, running-active-NotVisible
default	13:27:27.081211-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:27.092746-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:27.134495-0500	logger	detected new pid 84487 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:27.154144-0500	Nexy	[0x101e661d0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:27:27.154228-0500	Nexy	[0x101e6d7a0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:27:27.178592-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring jetsam update because this process is not memory-managed
default	13:27:27.178608-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring suspend because this process is not lifecycle managed
default	13:27:27.178620-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring GPU update because this process is not GPU managed
default	13:27:27.178637-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] Ignoring memory limit update because this process is not memory-managed
default	13:27:27.178839-0500	gamepolicyd	Received state update for 84487 (app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>, running-active-NotVisible
default	13:27:27.181464-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:27.181894-0500	gamepolicyd	Received state update for 84487 (app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>, running-active-NotVisible
error	13:27:27.278702-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xab25a8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:27.278943-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xab25a8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:27.279150-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xab25a8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:27.279350-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xab25a8000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:27:27.281090-0500	Nexy	[0x101e6ab60] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:27:27.281898-0500	Nexy	[0xab2780000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:27:27.282222-0500	Nexy	[0xab2780140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:27:27.282684-0500	Nexy	[0xab2780280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:27:27.282876-0500	Nexy	Received configuration update from daemon (initial)
default	13:27:27.285105-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:27:27.285466-0500	Nexy	[0xab27803c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:27:27.286186-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84487.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:27.287890-0500	tccd	AUTHREQ_SUBJECT: msgID=84487.1, subject=com.nexy.assistant,
default	13:27:27.288748-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:27.309035-0500	Nexy	[0xab27803c0] invalidated after the last release of the connection object
default	13:27:27.309433-0500	Nexy	server port 0x00003607, session port 0x00003607
default	13:27:27.310643-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.586, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:27:27.310671-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:27.311680-0500	tccd	AUTHREQ_SUBJECT: msgID=387.586, subject=com.nexy.assistant,
default	13:27:27.312776-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:27.341186-0500	Nexy	New connection 0xf430b main
default	13:27:27.344249-0500	Nexy	CHECKIN: pid=84487
default	13:27:27.354811-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84487" ID:394-357-87856 target:84487 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:27.355006-0500	runningboardd	Assertion 394-357-87856 (target:[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]) will be created as active
default	13:27:27.354492-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:27:27.354413-0500	Nexy	[0xab27803c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:27:27.354639-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:27:27.354423-0500	Nexy	[0xab27803c0] Connection returned listener port: 0x4e03
default	13:27:27.359734-0500	Nexy	[0xab2780500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:27:27.364171-0500	runningboardd	Invalidating assertion 394-357-87853 (target:[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:27:27.367286-0500	Nexy	BringFrontModifier: pid=84487 asn=0x0-0x110110 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:27:27.367974-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:27:27.395431-0500	Nexy	[0xab2780a00] Connection returned listener port: 0x6603
default	13:27:27.396401-0500	Nexy	Registered process with identifier 84487-163448
default	13:27:28.179229-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid EA612EB6-5A3B-420D-A3D7-4BE6E4F9573C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63240,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x1d0ed753 tp_proto=0x06"
default	13:27:28.179280-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63240<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534748 t_state: SYN_SENT process: Nexy:84487 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9eb748fd
default	13:27:28.179831-0500	kernel	tcp connected: [<IPv4-redacted>:63240<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534748 t_state: ESTABLISHED process: Nexy:84487 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9eb748fd
default	13:27:28.180129-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63240<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534748 t_state: FIN_WAIT_1 process: Nexy:84487 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x9eb748fd
default	13:27:28.180139-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63240<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534748 t_state: FIN_WAIT_1 process: Nexy:84487 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:27:28.216917-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:27:28.217529-0500	Nexy	[0xab2780c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:27:28.218518-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f401f","name":"Nexy(84487)"}, "details":{"PID":84487,"session_type":"Primary"} }
default	13:27:28.218602-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":84487}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f401f, sessionType: 'prim', isRecording: false }, 
]
default	13:27:28.219336-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 84487, name = Nexy
default	13:27:28.219666-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xab27f3900 with ID: 0x1f401f
default	13:27:28.219939-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:27:28.220700-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:27:28.222086-0500	Nexy	[0xab2780dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:27:28.224409-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10 AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10>
default	13:27:28.228964-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:27:28.230657-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:28.230855-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:28.231005-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:27:28.231017-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:27:28.231045-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:28.231175-0500	Nexy	[0xab2780f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:27:28.231327-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:27:28.231746-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84487.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:28.238668-0500	tccd	AUTHREQ_SUBJECT: msgID=84487.2, subject=com.nexy.assistant,
default	13:27:28.239348-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:28.255512-0500	Nexy	[0xab2780f00] invalidated after the last release of the connection object
default	13:27:28.255666-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:28.255707-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:28.255991-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:27:28.257256-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.355, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:28.258080-0500	tccd	AUTHREQ_SUBJECT: msgID=395.355, subject=com.nexy.assistant,
default	13:27:28.258681-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:27:28.275357-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:27:28.276274-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.357, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:28.277132-0500	tccd	AUTHREQ_SUBJECT: msgID=395.357, subject=com.nexy.assistant,
default	13:27:28.277726-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:28.292433-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:27:28.292458-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xab0c90cc0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:27:28.308068-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:28.308958-0500	Nexy	[0xab2780f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:27:28.309390-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=362868901937153 }
default	13:27:28.309526-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:27:28.309565-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:27:28.309596-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:27:28.319725-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:27:28.353360-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:27:28.353384-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:27:28.356906-0500	Nexy	[0xab2781040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:27:28.366099-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xab36c0040) Selecting device 71 from constructor
default	13:27:28.366111-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xab36c0040)
default	13:27:28.366116-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xab36c0040) not already running
default	13:27:28.366125-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xab36c0040) nothing to teardown
default	13:27:28.366128-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xab36c0040) connecting device 71
default	13:27:28.366204-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xab36c0040) Device ID: 71 (Input:No | Output:Yes): true
default	13:27:28.366285-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xab36c0040) created ioproc 0xa for device 71
default	13:27:28.366379-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xab36c0040) adding 7 device listeners to device 71
default	13:27:28.366530-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xab36c0040) adding 0 device delegate listeners to device 71
default	13:27:28.366539-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xab36c0040)
default	13:27:28.366605-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:28.366612-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:27:28.366624-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:28.366630-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:27:28.366636-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:27:28.366718-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xab36c0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:27:28.366725-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xab36c0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:27:28.366730-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:27:28.366734-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xab36c0040) removing 0 device listeners from device 0
default	13:27:28.366738-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xab36c0040) removing 0 device delegate listeners from device 0
default	13:27:28.366743-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xab36c0040)
default	13:27:28.366782-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:27:28.367022-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:28.368226-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xab0cb2820, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:28.368252-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:28.372767-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xab0cb27c0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:28.372782-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:28.373056-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:28.373735-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xab0cb2c10, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:28.373745-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xab0cb2c10: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:28.373750-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:28.373750-0500	Nexy	AudioConverter -> 0xab0cb2c10: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:28.373771-0500	Nexy	AudioConverter -> 0xab0cb2c10: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:28.373776-0500	Nexy	AudioConverter -> 0xab0cb2c10: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:28.374593-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xab0cb27c0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:28.374603-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xab0cb27c0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:28.374604-0500	Nexy	AudioConverter -> 0xab0cb27c0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:28.374609-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:28.374623-0500	Nexy	AudioConverter -> 0xab0cb27c0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:28.374643-0500	Nexy	AudioConverter -> 0xab0cb27c0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:28.374779-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xab0cb27c0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:28.409233-0500	Nexy	[0xab2781180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:28.409787-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:28.409959-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84487.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:28.411006-0500	tccd	AUTHREQ_SUBJECT: msgID=84487.3, subject=com.nexy.assistant,
default	13:27:28.411973-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:28.431884-0500	Nexy	[0xab2781180] invalidated after the last release of the connection object
default	13:27:28.431976-0500	Nexy	[0xab2781180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:28.432363-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:28.432528-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84487.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:28.433335-0500	tccd	AUTHREQ_SUBJECT: msgID=84487.4, subject=com.nexy.assistant,
default	13:27:28.433937-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:28.452328-0500	Nexy	[0xab2781180] invalidated after the last release of the connection object
default	13:27:28.452397-0500	Nexy	[0xab2781180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:27:28.452491-0500	Nexy	[0xab2781180] invalidated after the last release of the connection object
default	13:27:28.697613-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84498.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84498, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84498, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:28.699019-0500	tccd	AUTHREQ_SUBJECT: msgID=84498.1, subject=com.nexy.assistant,
default	13:27:28.699667-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:28.719520-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84498.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84498, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84498, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:28.720297-0500	tccd	AUTHREQ_SUBJECT: msgID=84498.2, subject=com.nexy.assistant,
default	13:27:28.720887-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:28.756019-0500	Nexy	[0xab2781540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:27:28.756625-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84487.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84487, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:28.762763-0500	tccd	AUTHREQ_SUBJECT: msgID=84487.5, subject=com.nexy.assistant,
default	13:27:28.763390-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257000 at /Applications/Nexy.app
default	13:27:28.780879-0500	Nexy	[0xab2781540] invalidated after the last release of the connection object
default	13:27:28.808511-0500	Nexy	server port 0x00014403, session port 0x00003607
default	13:27:30.848846-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x110110 (Nexy) connectionID: F430B pid: 84487 in session 0x101
default	13:27:30.848917-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x110110 (Nexy) acq:0xb6c363e80 count:1
default	13:27:30.849569-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f401f","name":"Nexy(84487)"}, "details":null }
default	13:27:30.849610-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f401f from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":84487})
default	13:27:30.849625-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":84487})
default	13:27:30.849879-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 32, PID = 84487, Name = sid:0x1f401f, Nexy(84487), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:27:30.849966-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 32, PID = 84487, Name = sid:0x1f401f, Nexy(84487), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:27:30.850136-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:30.850265-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:30.850455-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:30.850532-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:30.850106-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x110110 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x110110 (Nexy)"
)}
default	13:27:30.850610-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:30.850548-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x14a07 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x110110 (Nexy)"
)}
default	13:27:30.850666-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:30.856942-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]
default	13:27:30.867469-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487] termination reported by launchd (0, 0, 0)
default	13:27:30.867590-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]
default	13:27:30.867849-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]
default	13:27:30.868079-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]
default	13:27:30.868129-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]
default	13:27:30.872843-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>: none (role: None) (endowments: (null))
default	13:27:30.873083-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>: none (role: None) (endowments: (null))
default	13:27:30.873188-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 84487, name = Nexy
default	13:27:30.873671-0500	launchservicesd	Hit the server for a process handle 1be0828900014a07 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>:84487]
default	13:27:30.873878-0500	gamepolicyd	Received state update for 84487 (app<application.com.nexy.assistant.38522673.38522682.5467C80E-1AEA-4819-86B8-BDDFB755CE10(501)>, none-NotVisible
default	13:27:30.875659-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x110110} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:27:30.875699-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 3
default	13:27:30.875722-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:27:30.877249-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 4
default	13:27:30.877260-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:27:33.928549-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:27:34.024507-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:27:34.024682-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:27:34.026796-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:27:34.031928-0500	runningboardd	Launch request for app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:27:34.032032-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:80102] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-80102-87905 target:app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:34.032119-0500	runningboardd	Assertion 394-80102-87905 (target:app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>) will be created as active
default	13:27:34.032650-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:27:34.034780-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:27:34.034811-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>
default	13:27:34.034826-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:27:34.034957-0500	runningboardd	app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:27:34.049603-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] is not RunningBoard jetsam managed.
default	13:27:34.049619-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] This process will not be managed.
default	13:27:34.049629-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]
default	13:27:34.049849-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:34.050595-0500	gamepolicyd	Hit the server for a process handle 1d494f1e00014a41 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]
default	13:27:34.050635-0500	gamepolicyd	Received state update for 84545 (app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>, running-active-NotVisible
default	13:27:34.053005-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]
default	13:27:34.053072-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] from originator [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-87906 target:84545 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:27:34.053194-0500	runningboardd	Assertion 394-394-87906 (target:[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]) will be created as active
default	13:27:34.053396-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring jetsam update because this process is not memory-managed
default	13:27:34.053414-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring suspend because this process is not lifecycle managed
default	13:27:34.053436-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Set darwin role to: UserInteractive
default	13:27:34.053452-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring GPU update because this process is not GPU managed
default	13:27:34.053503-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring memory limit update because this process is not memory-managed
default	13:27:34.053553-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] reported to RB as running
default	13:27:34.054730-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring jetsam update because this process is not memory-managed
default	13:27:34.054770-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring suspend because this process is not lifecycle managed
default	13:27:34.054815-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring GPU update because this process is not GPU managed
default	13:27:34.054888-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring memory limit update because this process is not memory-managed
default	13:27:34.055006-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84545" ID:394-357-87907 target:84545 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:34.055012-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]
default	13:27:34.055113-0500	runningboardd	Assertion 394-357-87907 (target:[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]) will be created as active
default	13:27:34.055155-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x111111 com.nexy.assistant starting stopped process.
default	13:27:34.056152-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:27:34.056358-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 2
default	13:27:34.056385-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:27:34.057564-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:34.057573-0500	kernel	Nexy[84545] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0xa0b7da7b7d7220bf. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:27:34.057596-0500	kernel	Nexy[84545] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0xa0b7da7b7d7220bf. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:27:34.057862-0500	runningboardd	Invalidating assertion 394-80102-87905 (target:app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:80102]
default	13:27:34.057903-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring jetsam update because this process is not memory-managed
default	13:27:34.057918-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring suspend because this process is not lifecycle managed
default	13:27:34.057970-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring GPU update because this process is not GPU managed
default	13:27:34.058053-0500	gamepolicyd	Received state update for 84545 (app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>, running-active-NotVisible
default	13:27:34.058027-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring memory limit update because this process is not memory-managed
default	13:27:34.060920-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:34.069895-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:34.107793-0500	logger	detected new pid 84545 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:34.133542-0500	Nexy	[0x1021c6010] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:27:34.133632-0500	Nexy	[0x1021cd260] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:27:34.161397-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring jetsam update because this process is not memory-managed
default	13:27:34.161415-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring suspend because this process is not lifecycle managed
default	13:27:34.161427-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring GPU update because this process is not GPU managed
default	13:27:34.161598-0500	gamepolicyd	Received state update for 84545 (app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>, running-active-NotVisible
default	13:27:34.161475-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] Ignoring memory limit update because this process is not memory-managed
default	13:27:34.164351-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:27:34.164720-0500	gamepolicyd	Received state update for 84545 (app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>, running-active-NotVisible
error	13:27:34.248970-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xbaa110000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:34.249191-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xbaa110000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:34.249396-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xbaa110000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:27:34.249599-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xbaa110000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:27:34.251069-0500	Nexy	[0x1021c5650] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:27:34.251915-0500	Nexy	[0xbaa24c000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:27:34.252233-0500	Nexy	[0xbaa24c140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:27:34.252682-0500	Nexy	[0xbaa24c280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:27:34.252984-0500	Nexy	Received configuration update from daemon (initial)
default	13:27:34.254950-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:27:34.255311-0500	Nexy	[0xbaa24c3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:27:34.256068-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84545.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:34.257755-0500	tccd	AUTHREQ_SUBJECT: msgID=84545.1, subject=com.nexy.assistant,
default	13:27:34.258550-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:34.278315-0500	Nexy	[0xbaa24c3c0] invalidated after the last release of the connection object
default	13:27:34.278650-0500	Nexy	server port 0x00003607, session port 0x00003607
default	13:27:34.279716-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.587, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:27:34.279742-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:27:34.280555-0500	tccd	AUTHREQ_SUBJECT: msgID=387.587, subject=com.nexy.assistant,
default	13:27:34.281243-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:34.304050-0500	Nexy	New connection 0x924e7 main
default	13:27:34.306586-0500	Nexy	CHECKIN: pid=84545
default	13:27:34.315809-0500	launchservicesd	CHECKIN:0x0-0x111111 84545 com.nexy.assistant
default	13:27:34.315648-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:84545" ID:394-357-87908 target:84545 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:27:34.315741-0500	runningboardd	Assertion 394-357-87908 (target:[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]) will be created as active
default	13:27:34.315927-0500	Nexy	CHECKEDIN: pid=84545 asn=0x0-0x111111 foreground=0
default	13:27:34.316102-0500	runningboardd	Invalidating assertion 394-357-87907 (target:[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:27:34.316215-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:27:34.316198-0500	Nexy	[0xbaa24c3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:27:34.316348-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:27:34.316205-0500	Nexy	[0xbaa24c3c0] Connection returned listener port: 0x4203
default	13:27:34.316378-0500	Nexy	[0xbaa25c300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xbaa24c3c0.peer[357].0xbaa25c300
default	13:27:34.318798-0500	Nexy	FRONTLOGGING: version 1
default	13:27:34.318869-0500	Nexy	Registered, pid=84545 ASN=0x0,0x111111
default	13:27:34.319361-0500	WindowServer	924e7[CreateApplication]: Process creation: 0x0-0x111111 (Nexy) connectionID: 924E7 pid: 84545 in session 0x101
default	13:27:34.319653-0500	Nexy	[0xbaa24c500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:27:34.321907-0500	Nexy	[0xbaa24c3c0] Connection returned listener port: 0x4203
default	13:27:34.323393-0500	Nexy	BringForward: pid=84545 asn=0x0-0x111111 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:27:34.323926-0500	Nexy	BringFrontModifier: pid=84545 asn=0x0-0x111111 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:27:34.324740-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:27:34.326508-0500	Nexy	No persisted cache on this platform.
default	13:27:34.331237-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:27:34.331248-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:27:34.331310-0500	Nexy	Initializing connection
default	13:27:34.331355-0500	Nexy	Removing all cached process handles
default	13:27:34.343128-0500	Nexy	[0xbaa24ca00] Connection returned listener port: 0x6a03
default	13:27:35.138355-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid A540E19A-CA6C-4AC6-B1BE-F7D1D3A23AD9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63250,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xdf4b9650 tp_proto=0x06"
default	13:27:35.138433-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63250<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534844 t_state: SYN_SENT process: Nexy:84545 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8a5cffa7
default	13:27:35.139092-0500	kernel	tcp connected: [<IPv4-redacted>:63250<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534844 t_state: ESTABLISHED process: Nexy:84545 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8a5cffa7
default	13:27:35.139406-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63250<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534844 t_state: FIN_WAIT_1 process: Nexy:84545 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8a5cffa7
default	13:27:35.139417-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63250<-><IPv4-redacted>:53] interface: utun4 (skipped: 336)
so_gencnt: 534844 t_state: FIN_WAIT_1 process: Nexy:84545 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:27:35.177073-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:27:35.177740-0500	Nexy	[0xbaa24cc80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:27:35.178864-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4020","name":"Nexy(84545)"}, "details":{"PID":84545,"session_type":"Primary"} }
default	13:27:35.178956-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":84545}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4020, sessionType: 'prim', isRecording: false }, 
]
default	13:27:35.179704-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 84545, name = Nexy
default	13:27:35.180062-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xbaa2eb920 with ID: 0x1f4020
default	13:27:35.180335-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:27:35.181104-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:27:35.182570-0500	Nexy	[0xbaa24cdc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:27:35.184855-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF AUID=501> and <type=Application identifier=application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF>
default	13:27:35.189349-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:27:35.190922-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:35.191099-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:27:35.191253-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:27:35.191267-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:27:35.191298-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:35.191430-0500	Nexy	[0xbaa24cf00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:27:35.191557-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:27:35.191977-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84545.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:35.198867-0500	tccd	AUTHREQ_SUBJECT: msgID=84545.2, subject=com.nexy.assistant,
default	13:27:35.200556-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:35.216981-0500	Nexy	[0xbaa24cf00] invalidated after the last release of the connection object
default	13:27:35.217117-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:35.217159-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:27:35.217498-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:27:35.218673-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.358, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:35.219471-0500	tccd	AUTHREQ_SUBJECT: msgID=395.358, subject=com.nexy.assistant,
default	13:27:35.220057-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
error	13:27:35.235773-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:27:35.236675-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.360, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:27:35.237425-0500	tccd	AUTHREQ_SUBJECT: msgID=395.360, subject=com.nexy.assistant,
default	13:27:35.237998-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x723190300 at /Applications/Nexy.app
default	13:27:35.252168-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:27:35.252191-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xba9798840> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:27:35.265659-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:27:35.266567-0500	Nexy	[0xbaa24cf00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:27:35.266968-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=363118010040321 }
default	13:27:35.267076-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:27:35.267113-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	13:27:35.267142-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	13:27:35.277704-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 113
default	13:27:35.312536-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:27:35.312577-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:27:35.316427-0500	Nexy	[0xbaa24d040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:27:35.326165-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbab900040) Selecting device 71 from constructor
default	13:27:35.326175-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbab900040)
default	13:27:35.326181-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbab900040) not already running
default	13:27:35.326186-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbab900040) nothing to teardown
default	13:27:35.326190-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbab900040) connecting device 71
default	13:27:35.326277-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbab900040) Device ID: 71 (Input:No | Output:Yes): true
default	13:27:35.326354-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbab900040) created ioproc 0xa for device 71
default	13:27:35.326436-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbab900040) adding 7 device listeners to device 71
default	13:27:35.326586-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbab900040) adding 0 device delegate listeners to device 71
default	13:27:35.326592-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbab900040)
default	13:27:35.326653-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:35.326661-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:27:35.326670-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:27:35.326675-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:27:35.326683-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:27:35.326756-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbab900040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:27:35.326766-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbab900040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:27:35.326771-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:27:35.326775-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbab900040) removing 0 device listeners from device 0
default	13:27:35.326778-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbab900040) removing 0 device delegate listeners from device 0
default	13:27:35.326781-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbab900040)
default	13:27:35.326827-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:27:35.327080-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:35.328028-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:27:35.328082-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:27:35.328207-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xba96a27f0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:35.328233-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:35.329649-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:35.329857-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:35.331592-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:35.331804-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:35.333017-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xba96a2790, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:35.333029-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:35.333363-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:35.334139-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xba96a2be0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:35.334147-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xba96a2be0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:35.334153-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:35.334151-0500	Nexy	AudioConverter -> 0xba96a2be0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:35.334161-0500	Nexy	AudioConverter -> 0xba96a2be0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:35.334165-0500	Nexy	AudioConverter -> 0xba96a2be0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:35.335016-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xba96a2790, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:27:35.335025-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xba96a2790: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:35.335031-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:27:35.335031-0500	Nexy	AudioConverter -> 0xba96a2790: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:27:35.335037-0500	Nexy	AudioConverter -> 0xba96a2790: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:27:35.335047-0500	Nexy	AudioConverter -> 0xba96a2790: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:27:35.335167-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xba96a2790: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:27:35.370234-0500	Nexy	[0xbaa24d180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:35.370811-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:35.370992-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84545.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:35.372061-0500	tccd	AUTHREQ_SUBJECT: msgID=84545.3, subject=com.nexy.assistant,
default	13:27:35.373099-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:35.394937-0500	Nexy	[0xbaa24d180] invalidated after the last release of the connection object
default	13:27:35.395037-0500	Nexy	[0xbaa24d180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:27:35.395497-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:27:35.395663-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84545.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:35.396564-0500	tccd	AUTHREQ_SUBJECT: msgID=84545.4, subject=com.nexy.assistant,
default	13:27:35.397231-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:35.420639-0500	Nexy	[0xbaa24d180] invalidated after the last release of the connection object
default	13:27:35.420721-0500	Nexy	[0xbaa24d180] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:27:35.420830-0500	Nexy	[0xbaa24d180] invalidated after the last release of the connection object
default	13:27:35.704166-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84555.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84555, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84555, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:35.705950-0500	tccd	AUTHREQ_SUBJECT: msgID=84555.1, subject=com.nexy.assistant,
default	13:27:35.706696-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:35.732451-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84555.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.python3, pid=84555, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, requesting={TCCDProcess: identifier=com.apple.python3, pid=84555, auid=501, euid=501, binary_path=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python}, },
default	13:27:35.733484-0500	tccd	AUTHREQ_SUBJECT: msgID=84555.2, subject=com.nexy.assistant,
default	13:27:35.734154-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21256700 at /Applications/Nexy.app
default	13:27:35.774988-0500	Nexy	[0xbaa24d540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:27:35.775710-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84545.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84545, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:27:35.782748-0500	tccd	AUTHREQ_SUBJECT: msgID=84545.5, subject=com.nexy.assistant,
default	13:27:35.783432-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21257000 at /Applications/Nexy.app
default	13:27:35.802316-0500	Nexy	[0xbaa24d540] invalidated after the last release of the connection object
default	13:27:35.832870-0500	Nexy	server port 0x00014303, session port 0x00003607
default	13:27:37.075773-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	13:27:37.882205-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x111111 (Nexy) connectionID: 924E7 pid: 84545 in session 0x101
default	13:27:37.882253-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x111111 (Nexy) acq:0xb6c362ca0 count:1
default	13:27:37.882481-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f4020","name":"Nexy(84545)"}, "details":null }
default	13:27:37.882520-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f4020 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":84545})
default	13:27:37.882534-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":84545})
default	13:27:37.882896-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 33, PID = 84545, Name = sid:0x1f4020, Nexy(84545), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:27:37.882977-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 33, PID = 84545, Name = sid:0x1f4020, Nexy(84545), 'prim', BundleID = com.nexy.assistant, Category = SoloAmbientSound, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:27:37.883348-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:37.883440-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:37.883475-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:37.883076-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:37.883223-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:37.883665-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:27:37.884442-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x111111 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x111111 (Nexy)"
)}
default	13:27:37.886512-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x14a41 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x111111 (Nexy)"
)}
default	13:27:37.897056-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]
default	13:27:37.902064-0500	runningboardd	[app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545] termination reported by launchd (0, 0, 0)
default	13:27:37.902110-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]
default	13:27:37.902426-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]
default	13:27:37.902692-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]
default	13:27:37.902755-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]
default	13:27:37.908684-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>: none (role: None) (endowments: (null))
default	13:27:37.908890-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>: none (role: None) (endowments: (null))
default	13:27:37.909023-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 84545, name = Nexy
default	13:27:37.910136-0500	launchservicesd	Hit the server for a process handle 1d494f1e00014a41 that resolved to: [app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>:84545]
default	13:27:37.910547-0500	gamepolicyd	Received state update for 84545 (app<application.com.nexy.assistant.38522673.38522682.23BEDE9A-4A62-4306-BE39-356EBFB288BF(501)>, none-NotVisible
default	13:27:37.913336-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x111111} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:27:37.913373-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 3
default	13:27:37.913391-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:27:37.921574-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96c5a5360: Nexy> state 4
default	13:27:37.921588-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
