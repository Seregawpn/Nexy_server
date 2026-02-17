default	15:39:34.950321-0500	loginwindow	VoiceOverDebug: _ScreenReaderToggleEnabled with option 72
default	15:39:34.953594-0500	loginwindow	VoiceOverDebug: after boostrap_look_up succeeded
default	15:39:34.953663-0500	loginwindow	VoiceOverDebug: calling _SCRStartup returned 0
default	15:39:34.967076-0500	UIKitSystem	Application accessibility enabled: 1, (
	0   libAccessibility.dylib              0x00000001c22da16c _AXSApplicationAccessibilitySetEnabled + 84
	1   libAccessibility.dylib              0x00000001c22f2a40 _AXSVoiceOverTouchSetEnabled + 368
	2   FuseBoard                           0x00000002a09f742c -[FUAccessibilityServer _queue_applySettingWithKey:] + 696
	3   FuseBoard                           0x00000002a09f93ec __76-[FUAccessibilityServer _handleApplicationAccessibilityChangedNotification:]_block_invoke + 708
	4   libdispatch.dylib                   0x000000019c9a8b5c _dispatch_call_block_and_release + 32
	5   libdispatch.dylib                   0x000000019c9c2ad4 _dispatch_client_callout + 16
	6   libdispatch.dylib                   0x000000019c9b14e8 _dispatch_lane_serial_drain + 740
	7   libdispatch.dylib                   0x000000019c9b1ff8 _dispatch_lane_invoke + 440
	8   libdispatch.dylib                   0x000000019c9b3308 _dispatch_workloop_invoke + 1612
	9   libdispatch.dylib                   0x000000019c9bc474 _dispa
default	15:39:35.132958-0500	VoiceOver	Requesting app group container lookup; personaid = 4294967295, type = NOPERSONA, name = <unknown>, origin [pid = 0, personaid = 0], proximate [pid = 0, personaid = 0], identifier = <private>, euid = 501, uid = 501, platform = 1
default	15:39:35.139961-0500	VoiceOver	Consumed sandbox extension; path = [<private>], handle = 0
default	15:39:35.139982-0500	VoiceOver	container_create_or_lookup_app_group_path_by_app_group_identifier: success
default	15:39:35.410775-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=6832.10, attribution={responsible={TCCDProcess: identifier=com.apple.VoiceOver, pid=7274, auid=501, euid=501, responsible_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, accessing={TCCDProcess: identifier=com.apple.LegacyUserDefaultsConverter, pid=7275, auid=501, euid=501, binary_path=/System/Library/PrivateFrameworks/ScreenReaderCore.framework/Versions/A/Resources/LegacyUserDefaultsConverter}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=6832, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	15:39:35.418545-0500	tccd	AUTHREQ_SUBJECT: msgID=6832.10, subject=com.apple.VoiceOver,
error	15:39:35.425347-0500	kernel	System Policy: LegacyUserDefaultsConverter(7275) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences/com.apple.VoiceOver4
error	15:39:35.425414-0500	kernel	System Policy: LegacyUserDefaultsConverter(7275) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences
default	15:39:35.536511-0500	VoiceOver	container_create_or_lookup_app_group_path_by_app_group_identifier: success
default	15:39:35.608385-0500	VoiceOver	[0xc2ec683c0] activating connection: mach=false listener=false peer=false name=com.apple.carboncore.csnameddata
default	15:39:35.650063-0500	VoiceOver	VoiceOverDebug: ArgumentParser _initializeStartupOptions 72
default	15:39:35.652344-0500	VoiceOver	[0xc2ec68500] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	15:39:35.653151-0500	VoiceOver	[0xc2ec68640] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	15:39:35.663901-0500	VoiceOver	Received configuration update from daemon (initial)
default	15:39:35.673671-0500	VoiceOver	VoiceOverDebug: SCRWorkspace init
default	15:39:35.674417-0500	VoiceOver	[0xc2ec68a00] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	15:39:35.675385-0500	VoiceOver	[0xc2ec68b40] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	15:39:35.678917-0500	VoiceOver	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	15:39:35.679451-0500	VoiceOver	[0xc2ec68c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	15:39:35.680140-0500	VoiceOver	[0xc2ec68c80] invalidated after the last release of the connection object
default	15:39:35.680373-0500	VoiceOver	server port 0x0000480b, session port 0x0000480b
default	15:39:35.683749-0500	VoiceOver	New connection 0x10d457 main
default	15:39:35.686477-0500	VoiceOver	CHECKIN: pid=7274
default	15:39:35.692451-0500	runningboardd	Resolved pid 7274 to [osservice<com.apple.VoiceOver(501)>:7274]
default	15:39:35.692761-0500	runningboardd	_bundleMatchesProcessWithExecutablePath using realpath and comparing /System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver and /System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOverStarter
default	15:39:35.692878-0500	launchservicesd	CHECKIN:0x0-0x38e38e 7274 com.apple.VoiceOver
default	15:39:35.692996-0500	VoiceOver	CHECKEDIN: pid=7274 asn=0x0-0x38e38e foreground=0
default	15:39:35.693139-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] is not RunningBoard jetsam managed.
default	15:39:35.693156-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] This process will not be managed.
default	15:39:35.693169-0500	runningboardd	Now tracking process: [osservice<com.apple.VoiceOver(501)>:7274]
default	15:39:35.693454-0500	VoiceOver	[0xc2ec68c80] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	15:39:35.693674-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:7274" ID:394-357-107835 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	15:39:35.693773-0500	runningboardd	Assertion 394-357-107835 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:39:35.693722-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///System/Library/CoreServices/VoiceOver.app/
default	15:39:35.693809-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] reported to RB as running
default	15:39:35.694021-0500	loginwindow	-[Application setState:] | enter: <Application: 0xae8a1aa80: VoiceOver> state 2
default	15:39:35.693888-0500	VoiceOver	[0xc2ec68dc0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	15:39:35.693896-0500	VoiceOver	[0xc2ec68dc0] Connection returned listener port: 0x7903
default	15:39:35.694150-0500	VoiceOver	[0xc2f4a5680] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xc2ec68dc0.peer[357].0xc2f4a5680
default	15:39:35.694324-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : VoiceOver
default	15:39:35.694164-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:7274" ID:394-357-107836 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	15:39:35.694194-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring jetsam update because this process is not memory-managed
default	15:39:35.694308-0500	runningboardd	Assertion 394-357-107836 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:39:35.694315-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring suspend because this process is not lifecycle managed
default	15:39:35.694497-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Set darwin role to: UserInteractive
default	15:39:35.694600-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring GPU update because this process is not GPU managed
default	15:39:35.694736-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring memory limit update because this process is not memory-managed
default	15:39:35.694775-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Skipping AppNap state - not lifecycle managed
default	15:39:35.697606-0500	runningboardd	Invalidating assertion 394-357-107835 (target:[osservice<com.apple.VoiceOver(501)>:7274]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	15:39:35.697813-0500	gamepolicyd	Hit the server for a process handle 19864b200001c6a that resolved to: [osservice<com.apple.VoiceOver(501)>:7274]
default	15:39:35.697855-0500	gamepolicyd	Received state update for 7274 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	15:39:35.698149-0500	VoiceOver	FRONTLOGGING: version 1
default	15:39:35.698159-0500	VoiceOver	Registered, pid=7274 ASN=0x0,0x38e38e
default	15:39:35.699177-0500	WindowServer	10d457[CreateApplication]: Process creation: 0x0-0x38e38e (VoiceOver) connectionID: 10D457 pid: 7274 in session 0x101
default	15:39:35.712034-0500	VoiceOver	[0xc2ec68dc0] Connection returned listener port: 0x7903
default	15:39:35.712610-0500	VoiceOver	BringForward: pid=7274 asn=0x0-0x38e38e bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	15:39:35.713983-0500	VoiceOver	Current system appearance, (HLTB: 1), (SLS: 0)
default	15:39:35.715339-0500	VoiceOver	No persisted cache on this platform.
default	15:39:35.716046-0500	VoiceOver	Current system appearance, (HLTB: 1), (SLS: 0)
default	15:39:35.716548-0500	VoiceOver	Post-registration system appearance: (HLTB: 1)
default	15:39:35.716553-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 7274
default	15:39:35.716973-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 7274
default	15:39:35.719105-0500	VoiceOver	[0xc2ec68f00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	15:39:35.722453-0500	VoiceOver	FBSWorkspace: endpoint monitoring is disabled.
default	15:39:35.722465-0500	VoiceOver	FBSWorkspace: default shell endpoint is disabled.
default	15:39:35.722523-0500	VoiceOver	Initializing connection
default	15:39:35.722567-0500	VoiceOver	Removing all cached process handles
default	15:39:35.722589-0500	VoiceOver	Sending handshake request attempt #1 to server
default	15:39:35.722599-0500	VoiceOver	Creating connection to com.apple.runningboard
default	15:39:35.722604-0500	VoiceOver	[0xc2ec69040] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	15:39:35.723117-0500	runningboardd	Setting client for [osservice<com.apple.VoiceOver(501)>:7274] as ready
default	15:39:35.723798-0500	VoiceOver	Handshake succeeded
default	15:39:35.723814-0500	VoiceOver	Identity resolved as osservice<com.apple.VoiceOver(501)>
default	15:39:35.729351-0500	VoiceOver	[0xc2ec68dc0] Connection returned listener port: 0x7903
default	15:39:35.731462-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.apple.VoiceOver token: 1e0000001d pid: 7274
default	15:39:35.731673-0500	VoiceOver	[0xc2ec69180] activating connection: mach=true listener=false peer=false name=com.apple.bird.token
default	15:39:35.734121-0500	VoiceOver	[0xc2ec68dc0] Connection returned listener port: 0x7903
default	15:39:35.741203-0500	VoiceOver	[0xc2ec69180] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	15:39:35.742094-0500	VoiceOver	[0xc2ec69540] activating connection: mach=true listener=false peer=false name=com.apple.AccessibilityVisualsAgent
default	15:39:35.742500-0500	VoiceOver	[0xc2ec69180] activating connection: mach=true listener=false peer=false name=com.apple.bird
default	15:39:35.736361-0500	VoiceOver	Created a new Process Instance Registry XPC connection (inactive)
default	15:39:35.746946-0500	VoiceOver	[0xc2ec692c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	15:39:35.747117-0500	VoiceOver	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	15:39:35.747250-0500	VoiceOver	[0xc2ec69680] activating connection: mach=false listener=true peer=false name=(anonymous)
default	15:39:35.747956-0500	VoiceOver	[0xc2ec69680] Connection returned listener port: 0x9c03
default	15:39:35.749828-0500	VoiceOver	Registered process with identifier 7274-1375057
default	15:39:35.759004-0500	VoiceOver	[C:1] Alloc <private>
default	15:39:35.759069-0500	VoiceOver	[0xc2ec69900] activating connection: mach=false listener=false peer=false name=(anonymous)
default	15:39:35.763386-0500	WindowManager	Connection activated | (7274) VoiceOver
default	15:39:35.777312-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.apple.VoiceOver token: 2100000023 pid: 7274
default	15:39:35.777466-0500	VoiceOver	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xc2f0550e0
 (
    "<NSAquaAppearance: 0xc2f055220>",
    "<NSSystemAppearance: 0xc2f055180>"
)>
default	15:39:35.782670-0500	VoiceOver	[0xc2ec69e00] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	15:39:35.787820-0500	VoiceOver	[0xc2ec69f40] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	15:39:35.823174-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 7277
default	15:39:35.823601-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 7277
default	15:39:35.829292-0500	VoiceOver	[0xc2ec6a800] activating connection: mach=true listener=false peer=false name=com.apple.inputanalyticsd
default	15:39:35.874577-0500	VoiceOver	New connection 0xeabeb secondary
default	15:39:35.878278-0500	distnoted	register name: kVoiceOverSpeechBecameActiveNotification object: kCFNotificationAnyObject token: 270000002a pid: 7274
default	15:39:35.878375-0500	distnoted	register name: kVoiceOverSpeechBecameIdleNotification object: kCFNotificationAnyObject token: 2800000029 pid: 7274
default	15:39:35.879498-0500	VoiceOver	[0xc2ec6b200] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	15:39:35.889039-0500	VoiceOver	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	15:39:35.890013-0500	VoiceOver	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.apple.VoiceOver (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	15:39:35.891495-0500	VoiceOver	[0xc2ec6b340] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	15:39:35.894222-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver>
default	15:39:35.899295-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	15:39:35.901079-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/VoiceOver/AUVoiceIOChatFlavor, translatedBundleID VoiceOver, bundleIDs {(
    "com.apple.VoiceOver"
)}
default	15:39:35.901213-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/VoiceOver/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID VoiceOver, bundleIDs {(
    "com.apple.VoiceOver"
)}
default	15:39:35.901341-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	15:39:35.901352-0500	VoiceOver	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	15:39:35.901813-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	15:39:35.901923-0500	VoiceOver	[0xc2ec6b480] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	15:39:35.902745-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=7274.2, attribution={requesting={TCCDProcess: identifier=com.apple.VoiceOver, pid=7274, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, },
default	15:39:35.909370-0500	tccd	AUTHREQ_SUBJECT: msgID=7274.2, subject=com.apple.VoiceOver,
default	15:39:35.912039-0500	VoiceOver	[0xc2ec6b480] invalidated after the last release of the connection object
default	15:39:35.912064-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	15:39:35.913933-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.2494, attribution={accessing={TCCDProcess: identifier=com.apple.VoiceOver, pid=7274, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	15:39:35.914361-0500	tccd	AUTHREQ_SUBJECT: msgID=399.2494, subject=com.apple.VoiceOver,
default	15:39:35.914911-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.apple.VoiceOver, type: 0: 0x7d90c2a00 at /System/Library/CoreServices/VoiceOver.app
error	15:39:35.919013-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.apple.VoiceOver, pid=7274, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=399, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	15:39:35.920023-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.2496, attribution={accessing={TCCDProcess: identifier=com.apple.VoiceOver, pid=7274, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	15:39:35.920526-0500	tccd	AUTHREQ_SUBJECT: msgID=399.2496, subject=com.apple.VoiceOver,
default	15:39:35.921071-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.apple.VoiceOver, type: 0: 0x7d90c2a00 at /System/Library/CoreServices/VoiceOver.app
default	15:39:35.928824-0500	VoiceOver	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	15:39:35.929028-0500	VoiceOver	AddInstanceForFactory: No factory registered for id <CFUUID 0xc2f738b40> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	15:39:35.944967-0500	VoiceOver	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	15:39:35.944977-0500	VoiceOver	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	15:39:35.945545-0500	VoiceOver	     HALC_ProxyObject.cpp:1456   HALC_Object_PropertyListener: not initialized
default	15:39:35.948784-0500	coreaudiod	>>> SIMULATE [com.apple.VoiceOver]
default	15:39:35.948929-0500	coreaudiod	<<< SIMULATE [com.apple.VoiceOver]
default	15:39:35.953140-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	15:39:35.953610-0500	VoiceOver	                AUHAL.cpp:420   AUHAL: (0x104aec090) Selecting device 85 from constructor
default	15:39:35.953624-0500	VoiceOver	                AUHAL.cpp:629   SelectDevice: -> (0x104aec090)
default	15:39:35.953634-0500	VoiceOver	                AUHAL.cpp:681   SelectDevice: (0x104aec090) not already running
default	15:39:35.954186-0500	VoiceOver	                AUHAL.cpp:757   SelectDevice: (0x104aec090) nothing to teardown
default	15:39:35.954191-0500	VoiceOver	                AUHAL.cpp:762   SelectDevice: (0x104aec090) connecting device 85
default	15:39:35.954266-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x104aec090) Device ID: 85 (Input:No | Output:Yes): true
default	15:39:35.954346-0500	VoiceOver	                AUHAL.cpp:774   SelectDevice: (0x104aec090) created ioproc 0xa for device 85
default	15:39:35.954447-0500	VoiceOver	                AUHAL.cpp:863   SelectDevice: (0x104aec090) adding 7 device listeners to device 85
default	15:39:35.954597-0500	VoiceOver	                AUHAL.cpp:863   SelectDevice: (0x104aec090) adding 0 device delegate listeners to device 85
default	15:39:35.954603-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x104aec090)
default	15:39:35.954668-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	15:39:35.954678-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	15:39:35.954683-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	15:39:35.954698-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	15:39:35.954705-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	15:39:35.954792-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104aec090) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	15:39:35.954799-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104aec090) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	15:39:35.954803-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	15:39:35.954807-0500	VoiceOver	                AUHAL.cpp:900   SelectDevice: (0x104aec090) removing 0 device listeners from device 0
default	15:39:35.954812-0500	VoiceOver	                AUHAL.cpp:900   SelectDevice: (0x104aec090) removing 0 device delegate listeners from device 0
default	15:39:35.954817-0500	VoiceOver	                AUHAL.cpp:916   SelectDevice: <- (0x104aec090)
default	15:39:35.970295-0500	VoiceOver	                AUHAL.cpp:2303  SetProperty: (0x104aec090) caller requesting device change from 85 to 85
default	15:39:35.970304-0500	VoiceOver	                AUHAL.cpp:629   SelectDevice: -> (0x104aec090)
default	15:39:35.970309-0500	VoiceOver	                AUHAL.cpp:664   SelectDevice: <- (0x104aec090) exiting with nothing to do
default	15:39:35.975240-0500	VoiceOver	[0xc2e510870] Session created.
default	15:39:35.975250-0500	VoiceOver	[0xc2e510870] Session created with Mach Service: <private>
default	15:39:35.975269-0500	VoiceOver	[0xc2ec6b480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	15:39:35.975337-0500	VoiceOver	[0xc2e510870] Session activated
default	15:39:36.739976-0500	VoiceOver	[0xc2e510f00] Session created.
default	15:39:36.739989-0500	VoiceOver	[0xc2e510f00] Session created with Mach Service: <private>
default	15:39:36.739999-0500	VoiceOver	[0xc2e0bf200] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	15:39:36.740109-0500	VoiceOver	[0xc2e510f00] Session activated
default	15:39:36.758471-0500	VoiceOver	[0xc2e510f50] Session created.
default	15:39:36.758481-0500	VoiceOver	[0xc2e510f50] Session created with Mach Service: <private>
default	15:39:36.758487-0500	VoiceOver	[0xc2e0a4140] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	15:39:36.758558-0500	VoiceOver	[0xc2e510f50] Session activated
error	15:39:36.868432-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	15:39:36.875649-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	15:39:36.875689-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	15:39:36.879831-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	15:39:36.879859-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	15:39:36.960567-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	15:39:36.960594-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	15:39:37.011840-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	15:39:37.011879-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
default	15:39:37.026993-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	15:39:37.028722-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	15:39:37.029370-0500	VoiceOver	       ACv2Workarounds.mm:51    com.apple.VoiceOver: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	15:39:37.029424-0500	VoiceOver	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	15:39:37.029571-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2e113270, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	15:39:37.029618-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	15:39:37.030158-0500	VoiceOver	[0xc2e0b0280] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	15:39:37.034677-0500	VoiceOver	LFSMCopySessionAgentEndpoint: enter
default	15:39:37.034847-0500	VoiceOver	[0xc2e0b0000] activating connection: mach=true listener=false peer=false name=com.apple.logind
default	15:39:37.036195-0500	VoiceOver	LFSMCopySessionAgentEndpoint: exit: result = 0
default	15:39:37.036339-0500	VoiceOver	[0xc2e0b0500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	15:39:37.037574-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:39:37.039158-0500	VoiceOver	[SCROBrailleClient setDelegate:<SCROutputBrailleComponent: 0xc2f059000>]
default	15:39:37.039308-0500	VoiceOver	-[SCROBrailleClient _registerDelegate] Register callback: 'Display Configuration Changed'
default	15:39:37.039612-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:39:37.041110-0500	VoiceOver	[0xc2e0b0640] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	15:39:37.042289-0500	VoiceOver	[0xc2e0b08c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	15:39:37.042998-0500	VoiceOver	[0xc2e0b08c0] invalidated after the last release of the connection object
default	15:39:37.043149-0500	VoiceOver	server port 0x00016b07, session port 0x0000480b
default	15:39:37.044903-0500	VoiceOver	[0xc2e0b08c0] activating connection: mach=true listener=false peer=false name=com.apple.backlightd
default	15:39:37.051103-0500	WindowServer	Connection added: IOHIDEventSystemConnection uuid:BF09BD03-1F48-49F1-91E6-DF19AB5BE0AB pid:7274 process:VoiceOver type:Rate Controlled entitlements:0xa caller:ScreenReader: -[SCREventFactory completeInitialization] + 1196 attributes:(null) state:0x0 events:0 mask:0x0 dropped:0 dropStatus:0 droppedMask:0x0 lastDroppedTime:NONE
default	15:39:37.053925-0500	VoiceOver	SASSessionStateForUser:1280: enter
default	15:39:37.054007-0500	VoiceOver	SASSessionStateForUser:1300: SA: currentState: 2
default	15:39:37.054017-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:39:37.054635-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:39:37.054728-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:39:37.059329-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 6700000061 pid: 7274
default	15:39:37.059928-0500	VoiceOver	SASSessionStateForUser:1280: enter
default	15:39:37.059995-0500	VoiceOver	SASSessionStateForUser:1300: SA: currentState: 2
default	15:39:37.060009-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:39:37.060532-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:39:37.060606-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:39:37.060880-0500	VoiceOver	'Dock' is running
default	15:39:37.061074-0500	VoiceOver	'Setup Assistant' is not running
default	15:39:37.064060-0500	VoiceOver	                AUHAL.cpp:2303  SetProperty: (0x104aec090) caller requesting device change from 85 to 85
default	15:39:37.064069-0500	VoiceOver	                AUHAL.cpp:629   SelectDevice: -> (0x104aec090)
default	15:39:37.064078-0500	VoiceOver	                AUHAL.cpp:664   SelectDevice: <- (0x104aec090) exiting with nothing to do
error	15:39:37.069438-0500	kernel	1 duplicate report for System Policy: LegacyUserDefaultsConverter(7275) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences
default	15:39:37.080360-0500	VoiceOver	[0xc2e0b3980] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	15:39:37.081578-0500	VoiceOver	[0xc2e0b3980] invalidated after the last release of the connection object
default	15:39:37.106709-0500	VoiceOver	[0xc2ec68dc0] Connection returned listener port: 0x7903
default	15:39:37.107232-0500	VoiceOver	[0xc2e0b3980] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	15:39:37.107615-0500	VoiceOver	SignalReady: pid=7274 asn=0x0-0x38e38e
default	15:39:37.108047-0500	VoiceOver	SIGNAL: pid=7274 asn=0x0x-0x38e38e
default	15:39:37.108690-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///System/Library/CoreServices/VoiceOver.app/
default	15:39:37.120894-0500	distnoted	register name: AXSSVoiceOverPunctuationCloudKitUpdateNotification object: kCFNotificationAnyObject token: 6800000060 pid: 7274
default	15:39:37.121807-0500	VoiceOver	CloudKit integration setup failed with error:
Error Domain=AXCloudKitErrorDomain Code=0 "Current process can't use cloud kit" UserInfo={NSLocalizedFailureReason=Current process can't use cloud kit}
default	15:39:37.121828-0500	VoiceOver	CloudKit integration setup failed with error:
Error Domain=AXCloudKitErrorDomain Code=0 "Current process can't use cloud kit" UserInfo={NSLocalizedFailureReason=Current process can't use cloud kit}
default	15:39:37.131233-0500	VoiceOver	[0xc2ec68dc0] Connection returned listener port: 0x7903
default	15:39:37.170648-0500	VoiceOver	[SCROBrailleClient handleCallback:] for key CallbackConnect
default	15:39:37.170880-0500	VoiceOver	-[SCROBrailleClient _registerDelegate] Register callback: 'Display Configuration Changed'
default	15:39:37.224736-0500	VoiceOver	IOMainPort returned 0
default	15:39:37.225200-0500	VoiceOver	-[SCROBrailleClient handleCallback:] Call delegate's config change handler; Delegate wants == 1, isConfigured == 1
default	15:39:37.225230-0500	VoiceOver	-[SCROBrailleClient handleCallback:] Call delegate's config change handler; Delegate wants == 1, isConfigured == 1
default	15:39:37.235743-0500	VoiceOver	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	15:39:37.235749-0500	VoiceOver	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	15:39:37.235781-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	15:39:37.235872-0500	VoiceOver	[0xc2e0b1b80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	15:39:37.236193-0500	VoiceOver	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	15:39:37.250624-0500	VoiceOver	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	15:39:37.251221-0500	VoiceOver	void _NSEnableAutomaticTerminationAndLog(NSString *) No windows open yet
default	15:39:37.258316-0500	VoiceOver	sConnectionName: com.apple.spotlight.IndexAgent
default	15:39:37.258353-0500	VoiceOver	Start service name com.apple.spotlight.IndexAgent
default	15:39:37.258409-0500	VoiceOver	[0xc2e0b1540] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	15:39:37.260483-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppDrawing" ID:394-387-107842 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	15:39:37.260669-0500	runningboardd	Assertion 394-387-107842 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:39:37.262448-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring jetsam update because this process is not memory-managed
default	15:39:37.262548-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring suspend because this process is not lifecycle managed
default	15:39:37.262636-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring GPU update because this process is not GPU managed
default	15:39:37.262749-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring memory limit update because this process is not memory-managed
default	15:39:37.262804-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Skipping AppNap state - not lifecycle managed
default	15:39:37.268521-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppVisible" ID:394-387-107843 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	15:39:37.268589-0500	runningboardd	Assertion 394-387-107843 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:39:37.268861-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring jetsam update because this process is not memory-managed
default	15:39:37.268871-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring suspend because this process is not lifecycle managed
default	15:39:37.268881-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring GPU update because this process is not GPU managed
default	15:39:37.268985-0500	gamepolicyd	Received state update for 7274 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	15:39:37.268910-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring memory limit update because this process is not memory-managed
default	15:39:37.268940-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Skipping AppNap state - not lifecycle managed
default	15:39:37.274358-0500	VoiceOver	registering darwin observer for name: com.apple.gms.availability.notification
default	15:39:37.274389-0500	VoiceOver	registering darwin observer for name: com.apple.os-eligibility-domain.change.greymatter
default	15:39:37.274409-0500	VoiceOver	registering darwin observer for name: com.apple.language.changed
default	15:39:37.274435-0500	VoiceOver	isAvailable value changed: isMDMAllowed = true, gmAvailable (current) = true
default	15:39:37.271414-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.apple.VoiceOver: <private>
default	15:39:37.366786-0500	VoiceOver	No list of permitted front apps returned
default	15:39:37.367332-0500	VoiceOver	No list of permitted front apps returned
default	15:39:37.367405-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:39:37.368021-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:39:37.368175-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:39:37.370923-0500	gamepolicyd	Received state update for 7274 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	15:39:37.402884-0500	VoiceOver	[0xc2ddc0140] Session created.
default	15:39:37.402896-0500	VoiceOver	[0xc2ddc0140] Session created with Mach Service: <private>
default	15:39:37.402906-0500	VoiceOver	[0xc2e0b0b40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	15:39:37.403064-0500	VoiceOver	[0xc2ddc0140] Session activated
default	15:39:37.425415-0500	VoiceOver	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	15:39:37.426943-0500	VoiceOver	Start service name com.apple.spotlightknowledged
default	15:39:37.432564-0500	VoiceOver	[GMS] availability notification token 321
default	15:39:37.571208-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2edf9b30, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	15:39:37.571255-0500	VoiceOver	AudioConverter -> 0xc2edf9b30: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	15:39:37.571265-0500	VoiceOver	AudioConverter -> 0xc2edf9b30: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	15:39:37.571933-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:37.572936-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.VoiceOver(501)>:7274] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-7274-107844 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	15:39:37.573009-0500	runningboardd	Assertion 394-7274-107844 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:39:37.574012-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring jetsam update because this process is not memory-managed
default	15:39:37.574013-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-107845 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	15:39:37.574024-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring suspend because this process is not lifecycle managed
default	15:39:37.574059-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring GPU update because this process is not GPU managed
default	15:39:37.574080-0500	runningboardd	Assertion 394-328-107845 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:39:37.574110-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring memory limit update because this process is not memory-managed
default	15:39:37.574141-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Skipping AppNap state - not lifecycle managed
default	15:39:37.575582-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:37.577430-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring jetsam update because this process is not memory-managed
default	15:39:37.577441-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring suspend because this process is not lifecycle managed
default	15:39:37.577450-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring GPU update because this process is not GPU managed
default	15:39:37.577569-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring memory limit update because this process is not memory-managed
default	15:39:37.577595-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Skipping AppNap state - not lifecycle managed
default	15:39:37.588198-0500	gamepolicyd	Received state update for 7274 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	15:39:37.591747-0500	gamepolicyd	Received state update for 7274 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	15:39:37.611129-0500	VoiceOver	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	15:39:37.612545-0500	VoiceOver	[0xc2e0b03c0] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	15:39:37.615598-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ea080","name":"VoiceOver(7274)"}, "details":{"PID":7274,"session_type":"Primary"} }
default	15:39:37.615698-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] VoiceOver","pid":7274}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea080, sessionType: 'prim', isRecording: false }, 
]
default	15:39:37.616787-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 7274, name = VoiceOver
default	15:39:37.617412-0500	VoiceOver	    SessionCore_Create.mm:99    Created session 0xc2dcb5100 with ID: 0x1ea080
error	15:39:37.618691-0500	VoiceOver	Reporter disconnected. { function=sendMessage, reporterID=31241592111106 }
default	15:39:37.618726-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	15:39:37.621150-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea080","name":"VoiceOver(7274)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	15:39:37.621249-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	15:39:37.621607-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	15:39:37.621691-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	15:39:37.621748-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 128 starting playing
default	15:39:37.622020-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ea080, VoiceOver(7274), 'prim'', AudioCategory changed to 'MediaPlayback'
default	15:39:37.622414-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	15:39:37.622555-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	15:39:37.622638-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea07f, Python(7253), 'prim'', displayID:'org.python.python'}, secondSession={clientName:'sid:0x1ea080, VoiceOver(7274), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	15:39:37.622817-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea080 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":7274}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea080, sessionType: 'prim', isRecording: false }, 
]
default	15:39:37.623038-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	15:39:37.624830-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x19BF0001 category Not set
default	15:39:37.625798-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	15:39:37.625580-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	15:39:37.625741-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	15:39:37.625843-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	15:39:37.625936-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	15:39:37.626085-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	15:39:37.626226-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 2
default	15:39:37.626236-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:39:37.626293-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:39:37.626302-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	15:39:37.626715-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	15:39:37.627264-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	15:39:37.645960-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2ddb5710, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	15:39:37.646217-0500	VoiceOver	AudioConverter -> 0xc2ddb5710: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	15:39:37.646290-0500	VoiceOver	AudioConverter -> 0xc2ddb5710: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	15:39:37.673774-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2ddb6640, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	15:39:37.674022-0500	VoiceOver	AudioConverter -> 0xc2ddb6640: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	15:39:37.674047-0500	VoiceOver	AudioConverter -> 0xc2ddb6640: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	15:39:37.674833-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 7280
default	15:39:37.675383-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 7280
default	15:39:37.705920-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877140 [System: PrevIdle PrevDisp DeclUser kDisp]
default	15:39:37.714051-0500	VoiceOver	[0xc2ee241e0] Session created.
default	15:39:37.714086-0500	VoiceOver	[0xc2ee241e0] Session created with Mach Service: <private>
default	15:39:37.714104-0500	VoiceOver	[0xc2e0b0780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	15:39:37.714346-0500	VoiceOver	[0xc2ee241e0] Session activated
default	15:39:37.834777-0500	VoiceOver	AudioComponentPluginMgr.mm:114   registrationsChanged
default	15:39:37.837251-0500	VoiceOver	AudioComponentPluginMgr.mm:1117  component registrations changed
default	15:39:37.837274-0500	VoiceOver	AudioComponentPluginMgr.mm:906   First wildcard component search: 0/0/0
default	15:39:37.838232-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.843095-0500	VoiceOver	AudioComponentPluginMgr.mm:1117  component registrations changed
default	15:39:37.870037-0500	VoiceOver	[0xc2e0b1b80] invalidated after the last release of the connection object
default	15:39:37.870703-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.870898-0500	VoiceOver	[0xc2e0b1b80] invalidated after the last release of the connection object
default	15:39:37.870939-0500	VoiceOver	[0xc2e0b1680] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.871098-0500	VoiceOver	[0xc2e0b1680] invalidated after the last release of the connection object
default	15:39:37.871179-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.871329-0500	VoiceOver	[0xc2e0b1b80] invalidated after the last release of the connection object
default	15:39:37.871393-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.871625-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:37.871779-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.872035-0500	VoiceOver	[0xc2e0b1b80] invalidated after the last release of the connection object
default	15:39:37.872081-0500	VoiceOver	[0xc2e0b1680] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.872255-0500	VoiceOver	[0xc2e0b1680] invalidated after the last release of the connection object
default	15:39:37.872356-0500	VoiceOver	[0xc2e0b1680] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.872611-0500	VoiceOver	[0xc2e0b1680] invalidated after the last release of the connection object
default	15:39:37.872673-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.872915-0500	VoiceOver	[0xc2e0b1b80] invalidated after the last release of the connection object
default	15:39:37.873094-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.873344-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:37.873444-0500	VoiceOver	[0xc2e0b1680] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.873660-0500	VoiceOver	[0xc2e0b1680] invalidated after the last release of the connection object
default	15:39:37.873774-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.873938-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.874017-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.874285-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.874377-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.874535-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:37.874593-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.874752-0500	VoiceOver	[0xc2e0b1b80] invalidated after the last release of the connection object
default	15:39:37.874799-0500	VoiceOver	[0xc2e0b1680] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.874972-0500	VoiceOver	[0xc2e0b1680] invalidated after the last release of the connection object
default	15:39:37.875020-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.875169-0500	VoiceOver	[0xc2e0b1b80] invalidated after the last release of the connection object
default	15:39:37.875215-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.875366-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.875418-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.875581-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:37.875622-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.875791-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.875833-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.875988-0500	VoiceOver	[0xc2e0b1b80] invalidated after the last release of the connection object
default	15:39:37.876055-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.876204-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.876250-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.876374-0500	VoiceOver	[0xc2e0b1b80] invalidated after the last release of the connection object
default	15:39:37.876395-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.876530-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:37.876573-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.877468-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.877649-0500	VoiceOver	[0xc2e0b1680] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.877886-0500	VoiceOver	[0xc2e0b1680] invalidated after the last release of the connection object
default	15:39:37.877954-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.878331-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.878446-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.878623-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.878662-0500	VoiceOver	[0xc2e0b1a40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.878925-0500	VoiceOver	[0xc2e0b1a40] invalidated after the last release of the connection object
default	15:39:37.878964-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.879113-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.879153-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.879419-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.879455-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.879678-0500	VoiceOver	[0xc2e0b1b80] invalidated after the last release of the connection object
default	15:39:37.879698-0500	VoiceOver	[0xc2e0b1e00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.879882-0500	VoiceOver	[0xc2e0b1e00] invalidated after the last release of the connection object
default	15:39:37.879909-0500	VoiceOver	[0xc2e0b1e00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.880038-0500	VoiceOver	[0xc2e0b1e00] invalidated after the last release of the connection object
default	15:39:37.880059-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.880357-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.880378-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.880876-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.881086-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.881355-0500	VoiceOver	[0xc2e0b1b80] invalidated after the last release of the connection object
default	15:39:37.881388-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.881573-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.881645-0500	VoiceOver	[0xc2e0b1e00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.881880-0500	VoiceOver	[0xc2e0b1e00] invalidated after the last release of the connection object
default	15:39:37.881911-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.882261-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.882333-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.882545-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.882576-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.882813-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.882848-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.883003-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.883033-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.883187-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.883223-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.883346-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.883371-0500	VoiceOver	[0xc2e0b1e00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.883485-0500	VoiceOver	[0xc2e0b1e00] invalidated after the last release of the connection object
default	15:39:37.883557-0500	VoiceOver	[0xc2e0b1e00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.883683-0500	VoiceOver	[0xc2e0b1e00] invalidated after the last release of the connection object
default	15:39:37.883718-0500	VoiceOver	[0xc2e0b1e00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.883846-0500	VoiceOver	[0xc2e0b1e00] invalidated after the last release of the connection object
default	15:39:37.883899-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.884047-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.884072-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.884206-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.884236-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.884372-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.884399-0500	VoiceOver	[0xc2e0b1e00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.884572-0500	VoiceOver	[0xc2e0b1e00] invalidated after the last release of the connection object
default	15:39:37.884594-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.884731-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.884758-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.884872-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.884896-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.885019-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.885055-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.885242-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.885371-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.885552-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.885617-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.885757-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.885798-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.886006-0500	VoiceOver	[0xc2e0b17c0] invalidated after the last release of the connection object
default	15:39:37.886229-0500	VoiceOver	Class EXGetExtensionClass(void) returning EXConcreteExtension
default	15:39:37.886267-0500	VoiceOver	[0xc2e0b17c0] activating connection: mach=true listener=false peer=false name=com.apple.pluginkit.pkd
default	15:39:37.886439-0500	VoiceOver	[d <private>] <PKHost:0xc2de00300> Beginning discovery for flags: 1024, point: (null)
default	15:39:37.888051-0500	VoiceOver	[d <private>] <PKHost:0xc2de00300> Completed discovery. Final # of matches: 1
default	15:39:37.889197-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.889370-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.889420-0500	VoiceOver	[d <private>] <PKHost:0xc2de00300> Beginning discovery for flags: 1024, point: (null)
default	15:39:37.890423-0500	VoiceOver	[d <private>] <PKHost:0xc2de00300> Completed discovery. Final # of matches: 1
default	15:39:37.891985-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.892205-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.892266-0500	VoiceOver	[d <private>] <PKHost:0xc2de00300> Beginning discovery for flags: 1024, point: (null)
default	15:39:37.893277-0500	VoiceOver	[d <private>] <PKHost:0xc2de00300> Completed discovery. Final # of matches: 1
default	15:39:37.894731-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.894926-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.895050-0500	VoiceOver	[d <private>] <PKHost:0xc2de00300> Beginning discovery for flags: 1024, point: (null)
default	15:39:37.895992-0500	VoiceOver	[d <private>] <PKHost:0xc2de00300> Completed discovery. Final # of matches: 1
default	15:39:37.897686-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.897897-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.897957-0500	VoiceOver	[d <private>] <PKHost:0xc2de00300> Beginning discovery for flags: 1024, point: (null)
default	15:39:37.898789-0500	VoiceOver	[d <private>] <PKHost:0xc2de00300> Completed discovery. Final # of matches: 1
default	15:39:37.899929-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.900177-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.909090-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.909480-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.913376-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.913665-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.913726-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.913897-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.918315-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.918512-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.918545-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.918687-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:37.918737-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	15:39:37.918874-0500	VoiceOver	[0xc2e0b1900] invalidated after the last release of the connection object
default	15:39:37.920409-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Ready plugins sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	15:39:37.934771-0500	runningboardd	Launch request for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}[0] is using uid 501 (divined from auid 501 euid 501)
default	15:39:37.934830-0500	runningboardd	Executing launch request for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]} (Launching extension com.apple.ax.MauiTTSSupport.MauiAUSP(14844CB3-B750-5F5A-987A-D4BBC31613B5) for host 7274) from requestor: [osservice<com.apple.pluginkit.pkd(501)>:4824]
default	15:39:37.934897-0500	runningboardd	Creating and launching job for: xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}
default	15:39:37.935046-0500	runningboardd	'(null)' Submitting extension overlay (host PID 7274, path /System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/Versions/A/PlugIns/MauiAUSP.appex/Contents/MacOS/MauiAUSP):
<dictionary: 0x7bd306a60> { count = 3, transaction: 0, voucher = 0x0, contents =
	"XPCService" => <dictionary: 0x7bd304d80> { count = 11, transaction: 0, voucher = 0x0, contents =
		"_ManagedBy" => <string: 0x7bd833120> { string cache = 0x0, length = 22, contents = "com.apple.runningboard" }
		"RunLoopType" => <string: 0x7bd832af0> { string cache = 0x0, length = 9, contents = "NSRunLoop" }
		"Platform" => <int64: 0x8a1fe6cfd66b5eff>: 1
		"JoinExistingSession" => <bool: 0x20b06f830>: true
		"_SandboxProfile" => <string: 0x7bd8313e0> { string cache = 0x0, length = 6, contents = "plugin" }
		"_AdditionalSubServices" => <dictionary: 0x7bd305c20> { count = 1, transaction: 0, voucher = 0x0, contents =
			"apple-extension-service" => <bool: 0x20b06f830>: true
		}
		"PersonaEnterprise" => <int64: 0x8a1fe6cfd66b41bf>: 1001
		"_AdditionalProperties" => <dictionary: 0x7bd306160> { count = 1, transaction: 0, voucher = 0x0, contents =
			"RunningBoard" => <dictionary: 0x7bd307480> { count = 2, transaction: 0, voucher = 0x0, contents =
				"RunningBoardLaunchedIdentity" => <dictionary: 0x7bd3a0b40> { count = 6, transaction: 0, voucher = 0x0, contents =
					"e" => <int64: 0x8a1fe6cfd66b515f>: 501
					"TYPE" => <int64: 0x8a1fe6cfd66b5ed7>: 4
					"h" => <int64: 0x8a1fe6cfd66bbda7>: 7274
					"i" => <string: 0x7bd8300c0> { string cache = 0x0, length = 36, contents = "com.apple.ax.MauiTTSSupport.MauiAUSP" }
					"r" => <int64: 0x8a1fe6cfd66b5ee7>: 2
					"H" => <dictionary: 0x7bdaede60> { count = 5, transaction: 0, voucher = 0x0, contents =
						"l" => <string: 0x7bd8314a0> { string cache = 0x0, length = 19, contents = "com.apple.VoiceOver" }
						"t" => <int64: 0x8a1fe6cfd66b5ee7>: 2
						"TYPE" => <int64: 0x8a1fe6cfd66b5ec7>: 6
						"a" => <int64: 0x8a1fe6cfd66b515f>: 501
						"p" => <int64: 0x8a1fe6cfd66b5ef7>: 0
					}
				}
				"RunningBoardLaunched" => <bool: 0x20b06f830>: true
			}
		}
		"_OmitSandboxParameters" => <bool: 0x20b06f830>: true
		"ServiceType" => <string: 0x7bd832490> { string cache = 0x0, length = 11, contents = "Application" }
		"ProgramArguments" => <array: 0x7bd832c40> { count = 3, capacity = 8, contents =
			0: <string: 0x7bd832340> { string cache = 0x0, length = 125, contents = "/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/Versions/A/PlugIns/MauiAUSP.appex/Contents/MacOS/MauiAUSP" }
			1: <string: 0x7bd831050> { string cache = 0x0, length = 15, contents = "-AppleLanguages" }
			2: <string: 0x7bd832f70> { string cache = 0x0, length = 27, contents = "("en-CA", "ru-CA", "fr-CA")" }
		}
	}
	"RunningBoard" => <dictionary: 0x7bd3053e0> { count = 1, transaction: 0, voucher = 0x0, contents =
		"Managed" => <bool: 0x20b06f830>: true
	}
	"CFBundlePackageType" => <string: 0x7bd832df0> { string cache = 0x0, length = 4, contents = "XPC!" }
}
default	15:39:37.962523-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] Memory Limits: active 0 inactive 0
 <private>
default	15:39:37.962544-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] This process will be managed.
error	15:39:37.962594-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] Memorystatus failed with unexpected error: Invalid argument (22)
default	15:39:37.963357-0500	runningboardd	Now tracking process: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284]
default	15:39:37.963577-0500	runningboardd	Calculated state for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}: running-suspended (role: None) (endowments: (null))
default	15:39:37.964026-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] reported to RB as running
default	15:39:37.965212-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] from originator [osservice<com.apple.VoiceOver(501)>:7274] with description <RBSAssertionDescriptor| "com.apple.extension.session" ID:394-7274-107848 target:7284 attributes:[
	<RBSLegacyAttribute| requestedReason:ViewService reason:ViewService flags:( AllowIdleSleep PreventTaskSuspend PreventTaskThrottleDown )>,
	<RBSAcquisitionCompletionAttribute| policy:AfterValidation>
	]>
default	15:39:37.965507-0500	runningboardd	Assertion 394-7274-107848 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284]) will be created as active
default	15:39:37.966125-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] Set jetsam priority to 40 [0] flag[1]
default	15:39:37.966202-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] Resuming task.
default	15:39:37.966279-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] Result 45 setting darwin role to UserInteractiveNonFocal: Operation not supported, falling back to setting priority
default	15:39:37.966487-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] Set darwin priority to: PRIO_DEFAULT
default	15:39:37.966737-0500	UIKitSystem	Hit the server for a process handle ccb8e8800001c74 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284]
default	15:39:37.966805-0500	UIKitSystem	Received state update for 7284 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	15:39:37.966265-0500	WindowServer	Hit the server for a process handle ccb8e8800001c74 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284]
default	15:39:37.966821-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] prevented from droping Memory Limits from 0 to -1
default	15:39:37.966376-0500	WindowServer	Received state update for 7284 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	15:39:37.964586-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] got pid from ready request: 7284
default	15:39:37.969914-0500	runningboardd	Calculated state for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}: running-active (role: UserInteractiveNonFocal) (endowments: (null))
default	15:39:37.970171-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] acquired startup assertion
default	15:39:37.970336-0500	WindowServer	Received state update for 7284 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	15:39:37.970396-0500	UIKitSystem	Received state update for 7284 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	15:39:37.970571-0500	VoiceOver	Creating side-channel connection to com.apple.runningboard
default	15:39:37.970583-0500	VoiceOver	[0xc2e0b1e00] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	15:39:37.971457-0500	VoiceOver	Hit the server for a process handle ccb8e8800001c74 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284]
default	15:39:37.971714-0500	VoiceOver	[0xc2e0b1900] activating connection: mach=false listener=false peer=false name=com.apple.ax.MauiTTSSupport.MauiAUSP
default	15:39:37.971838-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Prepare using sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	15:39:37.971864-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5] [<private>(<private>)] Sending prepareUsing to managed extension; this should launch it if not already running.
default	15:39:37.988862-0500	gamepolicyd	Hit the server for a process handle ccb8e8800001c74 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284]
default	15:39:37.988966-0500	gamepolicyd	Received state update for 7284 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	15:39:37.993365-0500	gamepolicyd	Received state update for 7284 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	15:39:38.003177-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	15:39:38.005539-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:38.007313-0500	VoiceOver	[0xc2e0b1180] invalidated after the last release of the connection object
default	15:39:38.025780-0500	runningboardd	Setting client for [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] as ready
default	15:39:38.027168-0500	MauiAUSP	Identity resolved as xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}
default	15:39:38.037683-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Begin using sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	15:39:38.038139-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] plugin loaded and ready for host
default	15:39:38.038649-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] from originator [osservice<com.apple.VoiceOver(501)>:7274] with description <RBSAssertionDescriptor| "com.apple.extension.session" ID:394-7274-107849 target:7284 attributes:[
	<RBSLegacyAttribute| requestedReason:ViewService reason:ViewService flags:( AllowIdleSleep PreventTaskSuspend PreventTaskThrottleDown WantsForegroundResourcePriority )>,
	<RBSAcquisitionCompletionAttribute| policy:AfterValidation>
	]>
default	15:39:38.038719-0500	runningboardd	Assertion 394-7274-107849 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284]) will be created as active
default	15:39:38.039192-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] Set jetsam priority to 100 [0] flag[1]
default	15:39:38.039294-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] prevented from droping Memory Limits from 0 to -1
default	15:39:38.042196-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] invalidating startup assertion
default	15:39:38.042383-0500	VoiceOver	Class EXGetExtensionContextInternalClass(void) returning EXExtensionContextImplementation
default	15:39:38.042438-0500	runningboardd	Invalidating assertion 394-7274-107848 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284]) from originator [osservice<com.apple.VoiceOver(501)>:7274]
default	15:39:38.051474-0500	VoiceOver	[0xc2e0b1180] activating connection: mach=false listener=true peer=false name=(anonymous)
default	15:39:38.051788-0500	VoiceOver	[0xc2f130f00] activating connection: mach=false listener=false peer=false name=com.apple.ax.MauiTTSSupport.MauiAUSP.apple-extension-service
default	15:39:38.052073-0500	VoiceOver	[0xc2e0b1180] Connection returned listener port: 0x36537
default	15:39:38.109407-0500	VoiceOver	[0xc2f131080] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xc2e0b1180.peer[7284].0xc2f131080
default	15:39:38.109803-0500	VoiceOver	[0xc2e0b1b80] activating connection: mach=false listener=false peer=false name=com.apple.audio.AUCrashHandlerService
default	15:39:38.121356-0500	VoiceOver	   AUOOPRenderPipePool.mm:167   Host obtained render pipe 29835449
default	15:39:38.121541-0500	VoiceOver	       AUOOPWorkgroups.mm:66    AUOOPWorkgroupManager: mutating workgroups.
default	15:39:38.121833-0500	VoiceOver	       AUOOPWorkgroups.mm:308   AUOOPWorkgroupManager: propagating workgroups.
default	15:39:38.121845-0500	VoiceOver	       AUOOPWorkgroups.mm:343   AUOOPWorkgroupManager: notifying workgroup listeners. Added :10, removed: 0
default	15:39:38.158474-0500	VoiceOver	[0xc2e0b1b80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
error	15:39:38.158509-0500	VoiceOver	        AUCrashHandler.mm:126   invalidated
default	15:39:38.412910-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284] with description <RBSAssertionDescriptor| "RunningBoardAssertedAssetSets" ID:394-7284-107851 target:7284 attributes:[
	<RBSDomainAttribute| domain:"com.apple.common" name:"FinishTaskUninterruptable" sourceEnvironment:"(null)">
	]>
default	15:39:38.412987-0500	runningboardd	Assertion 394-7284-107851 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284]) will be created as inactive as start-time-defining assertions exist
default	15:39:38.418486-0500	runningboardd	Invalidating assertion 394-7284-107851 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284]) from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:7274])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:7284]
default	15:39:38.556909-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2dd31050, from  1 ch,  22050 Hz, Float32 (actually:  1 ch,  22050 Hz, Float32) to  1 ch,  22050 Hz, Float32 (actually:  1 ch,  22050 Hz, Float32)
default	15:39:38.556956-0500	VoiceOver	     AudioQueueObject.cpp:487   AudioQueueObject: aq@0xc2ec88000: New output; format  1 ch,  22050 Hz, Float32 (passthrough? no)
default	15:39:38.557614-0500	VoiceOver	           HeadTracker.mm:110   HeadTrackerSession 0xc2ffe45a0 created for movie spatialization.
default	15:39:38.557621-0500	VoiceOver	           HeadTracker.mm:110   HeadTrackerSession 0xc2ffe4640 created for music spatialization.
default	15:39:38.558559-0500	VoiceOver	           AQMEIO_HAL.cpp:2218  [AddSpatialPropertiesListener] objectID=85
default	15:39:38.558624-0500	VoiceOver	           AQMEIO_HAL.cpp:2240  aqmeio@0xc2ea3aa18: [AddSpatialPropertiesListener] Installed listener 0xc2e862380
default	15:39:38.559144-0500	VoiceOver	          AQMixEngine.cpp:733   AQMEDevice (0xc2f144418) has neither a defaultOutStreamClient nor a defaultInStreamClient
default	15:39:38.559586-0500	VoiceOver	EnhanceDialogueProcessor.cpp:226   EnhanceDialogueProcessor() - Product does not support Enhance Dialogue
default	15:39:38.559627-0500	VoiceOver	EnhanceDialogueProcessor.cpp:226   EnhanceDialogueProcessor() - Product does not support Enhance Dialogue
default	15:39:38.559698-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2dd31170, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	15:39:38.562530-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xc2ec88000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	15:39:38.562551-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0xc2ec88000:
default	15:39:38.562577-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	15:39:38.562582-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	15:39:38.562592-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	15:39:38.563679-0500	VoiceOver	       LoudnessManager.mm:1257  GetHardwarePlatformKey: found acoustic ID: 37
default	15:39:38.563688-0500	VoiceOver	       LoudnessManager.mm:1387  GetHardwarePlatformKey: GetHardwarePlatformKey(): hardware platform key is Mac
default	15:39:38.563762-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	15:39:38.563777-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	15:39:38.570224-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:39:38.570760-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	15:39:38.570985-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:39:38.573235-0500	VoiceOver	SpatializationManager.cpp:1418  Loaded preset file /System/Library/Audio/Tunings/AID37/AU/aid37-aumx-3dem-appl.aupreset
default	15:39:38.573877-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	15:39:38.574047-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:39:38.574068-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	15:39:38.574095-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:39:38.574615-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
default	15:39:38.574709-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	15:39:38.574760-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:39:38.574965-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:39:38.574979-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xc2ea3aa18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	15:39:38.581871-0500	VoiceOver	           AQMEIO_HAL.cpp:1922  user headtracking mode for app com.apple.VoiceOver: 1
default	15:39:38.592386-0500	VoiceOver	AQSTL aq(0xc2ec88000) start time resolved to: 736092 ioTS st: 736092 ht: 73376.195892
error	15:39:38.696609-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	15:39:38.713875-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.pbs.fetch_services
default	15:39:38.740778-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:39.042668-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:39.042949-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:40.034451-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:40.034714-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:40.779489-0500	VoiceOver	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=0
default	15:39:41.007266-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	15:39:41.026662-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:41.026865-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:42.018708-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:42.018933-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:43.018879-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:43.019175-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:43.857825-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:43.858005-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:44.000760-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	15:39:45.031019-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:45.031260-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:45.772089-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:45.772430-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:46.744759-0500	VoiceOver	LSExceptions shared instance invalidated for timeout.
default	15:39:46.933749-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:46.933779-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:4990 called from <private>
default	15:39:46.935555-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
fault	15:39:46.935461-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:39:46.941030-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4990 called from <private>
default	15:39:46.944999-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4991)
default	15:39:46.941303-0500	runningboardd	Invalidating assertion 394-7274-107844 (target:[osservice<com.apple.VoiceOver(501)>:7274]) from originator [osservice<com.apple.VoiceOver(501)>:7274]
default	15:39:46.945030-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4991 called from <private>
default	15:39:46.945039-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4991 called from <private>
default	15:39:46.948553-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:39:46.948569-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:39:46.948770-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:46.948868-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4990 called from <private>
default	15:39:46.948982-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4990 called from <private>
default	15:39:46.956144-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:46.962245-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:46.963130-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:46.964962-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4990 called from <private>
default	15:39:46.964978-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4990 called from <private>
default	15:39:46.964997-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:39:46.965020-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:46.965033-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4990 called from <private>
default	15:39:46.968904-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.VoiceOver(501)>:7274] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-7274-107862 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	15:39:46.968987-0500	runningboardd	Assertion 394-7274-107862 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:39:46.971386-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4990 called from <private>
default	15:39:46.971451-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4990 called from <private>
error	15:39:46.971471-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	15:39:46.971482-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:46.971489-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:39:46.971497-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:39:46.971607-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:46.972426-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:46.972734-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:39:46.972748-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:46.973225-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:46.973303-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:46.973474-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4991)
default	15:39:46.973496-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4991 called from <private>
default	15:39:46.973505-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4991 called from <private>
default	15:39:47.007790-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	15:39:47.007859-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	15:39:47.007903-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	15:39:47.007951-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	15:39:47.008021-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	15:39:47.008909-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea07f, Python(7253), 'prim'', displayID:'org.python.python'}, secondSession={clientName:'sid:0x1ea080, VoiceOver(7274), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	15:39:47.009347-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea07f, Python(7253), 'prim'', displayID:'org.python.python'}, secondSession={clientName:'sid:0x1ea080, VoiceOver(7274), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	15:39:47.008791-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2eda8360, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	15:39:47.008907-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	15:39:47.009013-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	15:39:47.009764-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea07f, Python(7253), 'prim'', displayID:'org.python.python'}, secondSession={clientName:'sid:0x1ea080, VoiceOver(7274), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	15:39:47.009568-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:39:47.009696-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104aec090) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	15:39:47.009787-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104aec090) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	15:39:47.009865-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	15:39:47.020236-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	15:39:47.022072-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	15:39:47.092220-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea07f, Python(7253), 'prim'', displayID:'org.python.python'}, secondSession={clientName:'sid:0x1ea080, VoiceOver(7274), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	15:39:47.168559-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 7294
default	15:39:47.599981-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:09  id:21474877140 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:39:47.601579-0500	VoiceOver	HIDAnalytics Timer Send event com.apple.iokituser.hid.iohidpostevent
default	15:39:47.601589-0500	VoiceOver	HIDAnalytics Set Value Send event com.apple.iokituser.hid.iohidpostevent
default	15:39:47.601674-0500	VoiceOver	HIDAnalytics Unregister Send event com.apple.iokituser.hid.iohidpostevent
default	15:39:47.812637-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
fault	15:39:47.863507-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	15:39:47.864211-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	15:39:47.865652-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	15:39:47.866411-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:39:48.036287-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:48.036396-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:48.118848-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877318 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:39:48.119074-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	15:39:48.215420-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	15:39:48.755705-0500	VoiceOver	[0xc2e0b2080] activating connection: mach=true listener=false peer=false name=mul-xpc (Apple)_OpenStep
default	15:39:48.756112-0500	VoiceOver	[0xc2e0b1a40] activating connection: mach=true listener=false peer=false name=com.apple.naturallanguaged
default	15:39:49.042819-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:49.043132-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:50.003200-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	15:39:50.041682-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:50.041855-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:50.101927-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea07f, Python(7253), 'prim'', displayID:'org.python.python'}, secondSession={clientName:'sid:0x1ea080, VoiceOver(7274), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	15:39:50.102961-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:39:50.104315-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:39:50.104424-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:39:50.104545-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:39:51.034903-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:51.035011-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:52.029409-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:52.029639-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:52.233376-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:52.234710-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4991)
default	15:39:52.234743-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4991 called from <private>
fault	15:39:52.234776-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:39:52.234754-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4991 called from <private>
default	15:39:52.235791-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	15:39:52.238001-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4990 called from <private>
default	15:39:52.241393-0500	runningboardd	Invalidating assertion 394-7274-107865 (target:[osservice<com.apple.VoiceOver(501)>:7274]) from originator [osservice<com.apple.VoiceOver(501)>:7274]
default	15:39:52.238173-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4990 called from <private>
default	15:39:52.250889-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:39:52.250916-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:39:52.251034-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:52.251053-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4990 called from <private>
default	15:39:52.251059-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4990 called from <private>
default	15:39:52.252496-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4991)
default	15:39:52.252525-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4991 called from <private>
default	15:39:52.252532-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4991 called from <private>
default	15:39:52.254589-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:52.254839-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:52.255816-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:52.257314-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4990 called from <private>
default	15:39:52.257540-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4990 called from <private>
default	15:39:52.257797-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:39:52.257930-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:52.258188-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4990 called from <private>
default	15:39:52.258904-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4990 called from <private>
default	15:39:52.258997-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4990 called from <private>
error	15:39:52.259044-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	15:39:52.259113-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:52.259149-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:39:52.259171-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:39:52.259287-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:52.260664-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.VoiceOver(501)>:7274] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-7274-107882 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	15:39:52.260782-0500	runningboardd	Assertion 394-7274-107882 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:39:52.259635-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:52.259780-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:39:52.259812-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:52.262638-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:52.262746-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:52.265567-0500	runningboardd	Invalidating assertion 394-7274-107882 (target:[osservice<com.apple.VoiceOver(501)>:7274]) from originator [osservice<com.apple.VoiceOver(501)>:7274]
default	15:39:52.272770-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:39:52.272804-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:39:52.272943-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:52.279237-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:52.279437-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:39:52.279448-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:52.279519-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:39:52.279526-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:39:52.279532-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:39:52.279539-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:52.279596-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4990 called from <private>
default	15:39:52.279690-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x104aec090) Device ID: 85 (Input:No | Output:Yes): true
default	15:39:52.279767-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x104aec090)
default	15:39:52.280124-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	15:39:52.280189-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	15:39:52.280344-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	15:39:52.280913-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:52.280491-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
error	15:39:52.280961-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	15:39:52.280971-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	15:39:52.281032-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4990 called from <private>
default	15:39:52.281147-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4990 called from <private>
default	15:39:52.281197-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4990 called from <private>
default	15:39:52.281249-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:39:52.281387-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:39:52.281554-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:39:52.282109-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:52.282217-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4990 called from <private>
error	15:39:52.283009-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	15:39:52.291954-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
error	15:39:52.481272-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	15:39:52.950499-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	15:39:52.951584-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	15:39:52.996876-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:4990 called from <private>
default	15:39:52.997556-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2eda5530, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	15:39:52.997587-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	15:39:52.997684-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	15:39:52.998030-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:39:52.998150-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104aec090) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	15:39:52.998168-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104aec090) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	15:39:52.998178-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	15:39:52.998194-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xc2ea3aa18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	15:39:52.998204-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xc2ea3aa18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	15:39:52.998847-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2eda56b0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	15:39:52.999422-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:39:53.999691-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:39:53.000123-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	15:39:53.000458-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:39:53.000629-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	15:39:53.000899-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:39:53.000932-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	15:39:53.001301-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0xc2ec88000:
default	15:39:53.001358-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	15:39:53.001367-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	15:39:53.001384-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	15:39:53.001422-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	15:39:53.001449-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	15:39:53.001943-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:39:53.001996-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 0
default	15:39:53.002111-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0xc2ec88000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	15:39:53.002397-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:39:53.002593-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	15:39:53.002847-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:39:53.003097-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	15:39:53.003331-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:39:53.003355-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	15:39:53.003397-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:39:53.003559-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
default	15:39:53.003632-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	15:39:53.003674-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:39:53.003936-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:39:53.003953-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xc2ea3aa18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	15:39:53.038161-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:53.038265-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:53.156446-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:39:53.156495-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:39:53.156557-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea07f, Python(7253), 'prim'', displayID:'org.python.python'}, secondSession={clientName:'sid:0x1ea080, VoiceOver(7274), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	15:39:53.157119-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:39:53.157170-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:39:53.979031-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474877318 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:39:54.023412-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:54.023530-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:54.188543-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	15:39:54.578160-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	15:39:54.587877-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:39:54.587971-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 0
default	15:39:55.017263-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:55.017402-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:56.004878-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	15:39:56.034929-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:56.035145-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:56.687206-0500	VoiceOver	aqmeio@0xc2ea3aa18 Stop id=85
default	15:39:56.687222-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:39:56.687880-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:39:57.016465-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:57.016792-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:39:57.952397-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:57.953310-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4990 called from <private>
default	15:39:57.953387-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4990 called from <private>
default	15:39:57.957051-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4991)
default	15:39:57.957076-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4991 called from <private>
default	15:39:57.957082-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4991 called from <private>
default	15:39:57.960618-0500	runningboardd	Invalidating assertion 394-7274-107885 (target:[osservice<com.apple.VoiceOver(501)>:7274]) from originator [osservice<com.apple.VoiceOver(501)>:7274]
default	15:39:57.963670-0500	runningboardd	Invalidating assertion 394-328-107845 (target:[osservice<com.apple.VoiceOver(501)>:7274]) from originator [osservice<com.apple.powerd>:328]
default	15:39:57.957514-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	15:39:57.972512-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:39:57.972532-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:39:57.973074-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:57.973095-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4990 called from <private>
default	15:39:57.973103-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4990 called from <private>
default	15:39:57.978920-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:57.979229-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4990 called from <private>
default	15:39:57.979240-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4990 called from <private>
default	15:39:57.979254-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:39:57.979264-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:57.982742-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.VoiceOver(501)>:7274] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-7274-107893 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	15:39:57.982891-0500	runningboardd	Assertion 394-7274-107893 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:39:57.979346-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:57.979372-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4990 called from <private>
default	15:39:57.980767-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:57.987423-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4991)
default	15:39:57.987454-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4991 called from <private>
default	15:39:57.987464-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4991 called from <private>
default	15:39:57.989455-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4990 called from <private>
error	15:39:57.989517-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	15:39:57.989526-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:57.989537-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:39:57.990047-0500	runningboardd	Invalidating assertion 394-7274-107893 (target:[osservice<com.apple.VoiceOver(501)>:7274]) from originator [osservice<com.apple.VoiceOver(501)>:7274]
default	15:39:57.989543-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:39:57.989558-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:39:57.989911-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:57.989942-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4990 called from <private>
default	15:39:57.989969-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4990 called from <private>
default	15:39:57.990886-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:57.990911-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:39:57.990962-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:39:57.991906-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4990 called from <private>
default	15:39:57.991919-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4990 called from <private>
default	15:39:57.991930-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:39:57.991940-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:39:57.992577-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4990 called from <private>
default	15:39:58.039050-0500	runningboardd	Invalidating assertion 394-328-107897 (target:[osservice<com.apple.VoiceOver(501)>:7274]) from originator [osservice<com.apple.powerd>:328]
default	15:39:58.039161-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-107899 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	15:39:58.039244-0500	runningboardd	Assertion 394-328-107899 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:39:58.039803-0500	runningboardd	Invalidating assertion 394-328-107899 (target:[osservice<com.apple.VoiceOver(501)>:7274]) from originator [osservice<com.apple.powerd>:328]
default	15:39:58.058024-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x104aec090) Device ID: 85 (Input:No | Output:Yes): true
default	15:39:58.058051-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x104aec090)
default	15:39:58.058163-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	15:39:58.058177-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	15:39:58.058186-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	15:39:58.058206-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	15:39:59.037564-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:39:59.037807-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:00.038723-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:00.038947-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:01.032828-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:01.033082-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:02.043414-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:02.043571-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:03.032360-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:03.032601-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:03.034887-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:03.035037-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:03.347296-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:03.347522-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:03.476752-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:40:03.476809-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4990 called from <private>
default	15:40:03.476818-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4990 called from <private>
default	15:40:03.477421-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4991)
default	15:40:03.477446-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:4991 called from <private>
default	15:40:03.477456-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:4991 called from <private>
default	15:40:03.495088-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4991)
default	15:40:03.495136-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4991 called from <private>
default	15:40:03.495142-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4991 called from <private>
default	15:40:03.498985-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:40:03.499349-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:40:03.499370-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:40:03.513503-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:4990 called from <private>
default	15:40:03.513534-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:4990 called from <private>
default	15:40:03.513659-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:40:03.517340-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:40:03.517599-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:4990 called from <private>
default	15:40:03.517611-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:4990 called from <private>
default	15:40:03.517782-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:40:03.523027-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:40:03.523339-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:40:03.523350-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:40:03.523844-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:40:03.523854-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:40:03.523885-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:40:03.523895-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:40:03.523920-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:40:03.523978-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(4990)
default	15:40:03.524020-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:40:03.524202-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:40:03.524296-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:40:03.524348-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:40:03.524461-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:40:03.524599-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:40:03.524724-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:40:03.525017-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:4990 called from <private>
default	15:40:03.525121-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:4990 called from <private>
default	15:40:03.526586-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(4990)
default	15:40:03.526808-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:4990 called from <private>
default	15:40:03.527040-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:4990 called from <private>
default	15:40:03.527091-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x104aec090) Device ID: 85 (Input:No | Output:Yes): true
default	15:40:03.527137-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:4990 called from <private>
default	15:40:03.527175-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x104aec090)
default	15:40:03.527235-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:4990 called from <private>
default	15:40:03.527494-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	15:40:03.527546-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	15:40:03.527645-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	15:40:03.527817-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	15:40:03.527852-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	15:40:03.529160-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2eda5530, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	15:40:03.529251-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	15:40:03.530065-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104aec090) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	15:40:03.530131-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104aec090) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	15:40:03.530177-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	15:40:03.532286-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x104aec090) Device ID: 85 (Input:No | Output:Yes): true
default	15:40:03.532311-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x104aec090)
default	15:40:03.539206-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2eda5530, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	15:40:03.539235-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	15:40:03.539639-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x104aec090) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	15:40:03.539663-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x104aec090) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	15:40:03.539670-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	15:40:03.539707-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xc2ea3aa18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	15:40:03.539721-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0xc2ea3aa18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	15:40:04.024337-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:04.024488-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:04.252863-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	15:40:05.031533-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:05.031769-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:05.474494-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:05.474739-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:05.897815-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 7308
default	15:40:05.898309-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 7308
default	15:40:06.027884-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:06.027991-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:06.613902-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000007 pid: 7321
default	15:40:06.614331-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 7321
default	15:40:06.737499-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:06.737610-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:07.123766-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7324
default	15:40:07.123796-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7323
default	15:40:07.463656-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7325
default	15:40:07.516798-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7326
default	15:40:07.559729-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7328
default	15:40:07.637440-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 7327
default	15:40:07.651283-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 7327
default	15:40:07.676073-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7329
default	15:40:08.032056-0500	VoiceOver	[0xc2e0b12c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:08.032165-0500	VoiceOver	[0xc2e0b12c0] invalidated after the last release of the connection object
default	15:40:08.260380-0500	VoiceOver	No list of permitted front apps returned
default	15:40:08.260658-0500	VoiceOver	No list of permitted front apps returned
default	15:40:08.263968-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:08.264601-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:08.264754-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:08.324337-0500	VoiceOver	[0xc2e0b1f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:08.324446-0500	VoiceOver	[0xc2e0b1f40] invalidated after the last release of the connection object
default	15:40:08.327893-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7330
default	15:40:08.328248-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7331
default	15:40:08.557951-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7334
default	15:40:08.594101-0500	VoiceOver	No list of permitted front apps returned
default	15:40:08.594377-0500	VoiceOver	No list of permitted front apps returned
default	15:40:08.666806-0500	VoiceOver	[0xc2e0b1680] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:08.666994-0500	VoiceOver	[0xc2e0b1680] invalidated after the last release of the connection object
default	15:40:08.672588-0500	VoiceOver	[0xc2e0b1680] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:08.672986-0500	VoiceOver	[0xc2e0b1680] invalidated after the last release of the connection object
default	15:40:08.686889-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2eda7030, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	15:40:08.686923-0500	VoiceOver	AudioConverter -> 0xc2eda7030: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	15:40:08.686933-0500	VoiceOver	AudioConverter -> 0xc2eda7030: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	15:40:08.689045-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.VoiceOver(501)>:7274] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-7274-107939 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	15:40:08.689179-0500	runningboardd	Assertion 394-7274-107939 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:40:08.690207-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring jetsam update because this process is not memory-managed
default	15:40:08.690157-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-107940 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	15:40:08.690598-0500	runningboardd	Assertion 394-328-107940 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:40:08.690408-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring suspend because this process is not lifecycle managed
default	15:40:08.691056-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring GPU update because this process is not GPU managed
default	15:40:08.691868-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring memory limit update because this process is not memory-managed
default	15:40:08.691926-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Skipping AppNap state - not lifecycle managed
default	15:40:08.698273-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring jetsam update because this process is not memory-managed
default	15:40:08.698326-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring suspend because this process is not lifecycle managed
default	15:40:08.698393-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring GPU update because this process is not GPU managed
default	15:40:08.698477-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring memory limit update because this process is not memory-managed
default	15:40:08.698513-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Skipping AppNap state - not lifecycle managed
default	15:40:08.701148-0500	gamepolicyd	Received state update for 7274 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	15:40:08.702478-0500	gamepolicyd	Received state update for 7274 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	15:40:08.726414-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7336
default	15:40:08.726171-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	15:40:08.730612-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea080","name":"VoiceOver(7274)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	15:40:08.730802-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	15:40:08.730820-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 128 starting playing
default	15:40:08.730897-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	15:40:08.730962-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	15:40:08.730998-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea07f, Python(7253), 'prim'', displayID:'org.python.python'}, secondSession={clientName:'sid:0x1ea080, VoiceOver(7274), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	15:40:08.731123-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea080 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":7274}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea080, sessionType: 'prim', isRecording: false }, 
]
default	15:40:08.731244-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	15:40:08.731714-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7337
default	15:40:08.731159-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	15:40:08.731719-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x19BF0001 category Not set
default	15:40:08.732420-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	15:40:08.732007-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	15:40:08.732618-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	15:40:08.732637-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 2
default	15:40:08.732765-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:40:08.731255-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	15:40:08.732978-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:40:08.735377-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	15:40:08.766458-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877842 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:08.835747-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	15:40:08.836783-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	15:40:08.836889-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:08.837120-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:40:08.837151-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	15:40:08.837214-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:40:08.837658-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
fault	15:40:08.837516-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:08.837769-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	15:40:08.837877-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:40:08.838227-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:40:08.838253-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xc2ea3aa18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	15:40:08.895339-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	15:40:08.899621-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	15:40:08.909581-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:40:08.909657-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 0
default	15:40:08.912909-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877842 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:08.913404-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877843 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:08.949717-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:40:08.950356-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:08.950700-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	15:40:08.950751-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:08.950965-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:40:08.951000-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	15:40:08.951056-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:40:08.951252-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
default	15:40:08.951323-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	15:40:08.951371-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:40:08.951663-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:40:08.951687-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xc2ea3aa18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	15:40:08.968686-0500	VoiceOver	AQSTL aq(0xc2ec88000) start time resolved to: 1405874 ioTS st: 1405874 ht: 73406.571494
error	15:40:08.984915-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	15:40:09.837908-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:09.837116-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:09.840730-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:09.924985-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:09.924330-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:09.925348-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:10.119364-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877843 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:10.129239-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:10.129739-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:10.129607-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:10.155407-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7339
default	15:40:10.155980-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7340
default	15:40:10.185524-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:10.185139-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:10.185647-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:10.637953-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877845 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	15:40:10.903363-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	15:40:11.005527-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	15:40:12.066571-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	15:40:12.069139-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:40:12.069199-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 0
default	15:40:12.092715-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7343
default	15:40:12.099670-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877845 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:12.100354-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877848 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:12.143497-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877849 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:12.176728-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:40:12.177381-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:12.177500-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	15:40:12.177711-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:40:12.177733-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
fault	15:40:12.177746-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:12.177767-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:40:12.177974-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
default	15:40:12.178040-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	15:40:12.178066-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:40:12.178317-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:40:12.178332-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xc2ea3aa18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	15:40:12.188642-0500	VoiceOver	AQSTL aq(0xc2ec88000) start time resolved to: 1476875 ioTS st: 1476875 ht: 73409.791494
error	15:40:12.209477-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	15:40:12.995464-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7344
default	15:40:13.314311-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:13.314788-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:13.314888-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:13.454633-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:13.454214-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:13.454993-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:13.990130-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877849 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:14.143359-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	15:40:14.166537-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:40:14.166652-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:40:14.168533-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:40:14.168709-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:40:14.205977-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	15:40:14.419271-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:14.418431-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:14.419739-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:14.526154-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000007 pid: 7347
default	15:40:14.531863-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 7347
default	15:40:14.553885-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:14.553311-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:14.556132-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:14.589461-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	15:40:14.599432-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:40:14.599528-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 0
default	15:40:15.851941-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:15.851432-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:15.852194-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:15.988202-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:15.987724-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:15.988383-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:16.698849-0500	VoiceOver	aqmeio@0xc2ea3aa18 Stop id=85
default	15:40:16.698885-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:40:16.699357-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:40:17.999825-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 3
default	15:40:19.398619-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	15:40:19.399283-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea080","name":"VoiceOver(7274)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	15:40:19.399517-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 128 stopping playing
default	15:40:19.399607-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	15:40:19.399684-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	15:40:19.399899-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	15:40:19.400856-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	15:40:19.401298-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	15:40:19.400612-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea080 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":7274}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea080, sessionType: 'prim', isRecording: false }, 
]
default	15:40:19.401525-0500	runningboardd	Invalidating assertion 394-328-107940 (target:[osservice<com.apple.VoiceOver(501)>:7274]) from originator [osservice<com.apple.powerd>:328]
default	15:40:19.401021-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	15:40:19.401412-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	15:40:19.400887-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	15:40:19.401452-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 2
default	15:40:19.401715-0500	runningboardd	Invalidating assertion 394-7274-107939 (target:[osservice<com.apple.VoiceOver(501)>:7274]) from originator [osservice<com.apple.VoiceOver(501)>:7274]
default	15:40:19.508383-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring jetsam update because this process is not memory-managed
default	15:40:19.508409-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring suspend because this process is not lifecycle managed
default	15:40:19.508433-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring GPU update because this process is not GPU managed
default	15:40:19.508480-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring memory limit update because this process is not memory-managed
default	15:40:19.508570-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Skipping AppNap state - not lifecycle managed
default	15:40:19.515710-0500	gamepolicyd	Received state update for 7274 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	15:40:19.523068-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:19.522353-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:19.523654-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:19.670562-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:19.669910-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:19.670731-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:20.387070-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:20.386420-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:20.387389-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:20.512048-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:20.513263-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:20.512809-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:23.795813-0500	VoiceOver	No list of permitted front apps returned
default	15:40:23.897658-0500	VoiceOver	No list of permitted front apps returned
default	15:40:23.897998-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:23.898971-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:23.898802-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:24.017219-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877886 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:24.017607-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-107986 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	15:40:24.017674-0500	runningboardd	Assertion 394-328-107986 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:40:24.018003-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring jetsam update because this process is not memory-managed
default	15:40:24.018016-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring suspend because this process is not lifecycle managed
default	15:40:24.018026-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring GPU update because this process is not GPU managed
default	15:40:24.018059-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring memory limit update because this process is not memory-managed
default	15:40:24.018084-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Skipping AppNap state - not lifecycle managed
default	15:40:24.024457-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	15:40:24.031141-0500	gamepolicyd	Received state update for 7274 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	15:40:24.044354-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:40:24.044945-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:24.045048-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	15:40:24.045284-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:40:24.045308-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
fault	15:40:24.045303-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:24.045341-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:40:24.045574-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
default	15:40:24.045635-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	15:40:24.047075-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:7274] from originator [osservice<com.apple.VoiceOver(501)>:7274] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-7274-107987 target:7274 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	15:40:24.047147-0500	runningboardd	Assertion 394-7274-107987 (target:[osservice<com.apple.VoiceOver(501)>:7274]) will be created as active
default	15:40:24.047499-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring jetsam update because this process is not memory-managed
default	15:40:24.047544-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring suspend because this process is not lifecycle managed
default	15:40:24.047600-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring GPU update because this process is not GPU managed
default	15:40:24.047755-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Ignoring memory limit update because this process is not memory-managed
default	15:40:24.047791-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:7274] Skipping AppNap state - not lifecycle managed
default	15:40:24.051628-0500	VoiceOver	[0xc2e0b2800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:24.051753-0500	VoiceOver	[0xc2e0b2800] invalidated after the last release of the connection object
default	15:40:24.054433-0500	gamepolicyd	Received state update for 7274 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	15:40:24.083959-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:40:24.084872-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea080","name":"VoiceOver(7274)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	15:40:24.085047-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	15:40:24.085066-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 128 starting playing
default	15:40:24.085179-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	15:40:24.085232-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 128, PID = 7274, Name = sid:0x1ea080, VoiceOver(7274), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	15:40:24.085350-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	15:40:24.085369-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea080 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":7274}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea080, sessionType: 'prim', isRecording: false }, 
]
default	15:40:24.085432-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	15:40:24.085443-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	15:40:24.085458-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xc2ea3aa18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	15:40:24.085665-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x19BF0001 category Not set
default	15:40:24.085896-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	15:40:24.085985-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	15:40:24.086030-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	15:40:24.086045-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 3
default	15:40:24.086056-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:40:24.086129-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:40:24.108552-0500	VoiceOver	AQSTL aq(0xc2ec88000) start time resolved to: 1739712 ioTS st: 1739712 ht: 73421.711494
error	15:40:24.211617-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	15:40:24.212811-0500	VoiceOver	[0xc2e0b2580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:24.213079-0500	VoiceOver	[0xc2e0b2580] invalidated after the last release of the connection object
default	15:40:24.216937-0500	VoiceOver	[0xc2e0b2580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:24.217094-0500	VoiceOver	[0xc2e0b2580] invalidated after the last release of the connection object
default	15:40:24.224919-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2dda9230, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	15:40:24.224946-0500	VoiceOver	AudioConverter -> 0xc2dda9230: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	15:40:24.224958-0500	VoiceOver	AudioConverter -> 0xc2dda9230: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	15:40:24.225022-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	15:40:24.225424-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:40:24.225646-0500	VoiceOver	[0xc2e0b1680] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:24.225759-0500	VoiceOver	[0xc2e0b1680] invalidated after the last release of the connection object
default	15:40:24.244365-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	15:40:24.249104-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:40:24.249145-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 0
default	15:40:24.257385-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877886 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:24.257821-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877887 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:24.310872-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:40:24.311297-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	15:40:24.311585-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:24.311748-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	15:40:24.311964-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:40:24.311990-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	15:40:24.312031-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:40:24.312336-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
default	15:40:24.312398-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	15:40:24.312436-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:40:24.312638-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:40:24.312650-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xc2ea3aa18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	15:40:24.431107-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	15:40:26.006992-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	15:40:27.481863-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 7360
default	15:40:27.876435-0500	VoiceOver	No list of permitted front apps returned
default	15:40:27.876583-0500	VoiceOver	No list of permitted front apps returned
default	15:40:27.917651-0500	VoiceOver	[0xc2e0b2580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:27.917764-0500	VoiceOver	[0xc2e0b2580] invalidated after the last release of the connection object
default	15:40:27.979156-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	15:40:27.989639-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:40:27.989675-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 0
default	15:40:27.996917-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474877887 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:27.997378-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877888 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:28.049206-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:40:28.049763-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:28.049824-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	15:40:28.050017-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	15:40:28.050026-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:28.050040-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	15:40:28.050070-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:40:28.050213-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
default	15:40:28.050273-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	15:40:28.050302-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:40:28.050518-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:40:28.050534-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xc2ea3aa18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	15:40:28.068631-0500	VoiceOver	AQSTL aq(0xc2ec88000) start time resolved to: 1827031 ioTS st: 1827031 ht: 73425.671494
default	15:40:28.663646-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:28.664391-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:28.664530-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:28.690088-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	15:40:28.699109-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:40:28.699156-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 0
default	15:40:28.727000-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877888 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:28.727412-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877890 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:28.731353-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877890 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:28.738194-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877891 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:28.783205-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:40:28.783310-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:40:28.812163-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:40:28.812493-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:28.812788-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	15:40:28.812896-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:28.812980-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:40:28.813003-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	15:40:28.813030-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:40:28.813165-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
default	15:40:28.813230-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	15:40:28.813256-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:40:29.000159-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
error	15:40:29.016387-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	15:40:30.687103-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:40:30.687228-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:40:30.687443-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:40:30.687864-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:40:30.751804-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea003, Antigravity Help(3130), 'prim'', displayID:'com.google.antigravity.helper'}, secondSession={clientName:'sid:0x1ea080, VoiceOver(7274), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	15:40:30.752450-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	15:40:30.752509-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	15:40:30.774656-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:30.775017-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:30.775084-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:30.922679-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	15:40:30.929069-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:40:30.929112-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 0
default	15:40:30.952327-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474877891 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:30.953402-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877893 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:30.979274-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877893 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:30.980040-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877894 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:31.030194-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:40:31.030731-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:31.030818-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	15:40:31.031007-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:31.031011-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:40:31.031037-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	15:40:31.031069-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:40:31.031219-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
default	15:40:31.031270-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	15:40:31.031296-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:40:31.031482-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:40:31.031497-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xc2ea3aa18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	15:40:31.094182-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	15:40:32.003931-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
fault	15:40:33.134011-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:33.151854-0500	VoiceOver	No list of permitted front apps returned
default	15:40:33.252748-0500	VoiceOver	No list of permitted front apps returned
default	15:40:33.254455-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	15:40:33.254880-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 7274, name: VoiceOver
default	15:40:33.254945-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	15:40:33.262048-0500	VoiceOver	[0xc2e0b2940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:33.262187-0500	VoiceOver	[0xc2e0b2940] invalidated after the last release of the connection object
default	15:40:33.272483-0500	VoiceOver	[0xc2e0b30c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:33.272602-0500	VoiceOver	[0xc2e0b30c0] invalidated after the last release of the connection object
default	15:40:33.274020-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc2edac990, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	15:40:33.274044-0500	VoiceOver	AudioConverter -> 0xc2edac990: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	15:40:33.274051-0500	VoiceOver	AudioConverter -> 0xc2edac990: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	15:40:33.288819-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	15:40:33.299117-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:40:33.299171-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 0
default	15:40:33.302649-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474877894 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:33.303112-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877896 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:33.346923-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:40:33.347263-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:33.347578-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	15:40:33.347584-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:33.347848-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:40:33.347875-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	15:40:33.347909-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:40:33.348059-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
default	15:40:33.348119-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	15:40:33.348150-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:40:33.348393-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:40:33.348412-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xc2ea3aa18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	15:40:33.358637-0500	VoiceOver	AQSTL aq(0xc2ec88000) start time resolved to: 1943677 ioTS st: 1943677 ht: 73430.961494
error	15:40:33.453707-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	15:40:34.027221-0500	VoiceOver	[0xc2e0b2940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:34.027523-0500	VoiceOver	[0xc2e0b2940] invalidated after the last release of the connection object
default	15:40:34.575026-0500	VoiceOver	[0xc2e0b2940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:34.575299-0500	VoiceOver	[0xc2e0b2940] invalidated after the last release of the connection object
default	15:40:35.005726-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	15:40:35.085187-0500	VoiceOver	[0xc2e0b2940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:35.085423-0500	VoiceOver	[0xc2e0b2940] invalidated after the last release of the connection object
default	15:40:35.606211-0500	VoiceOver	[0xc2e0b2940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:35.606511-0500	VoiceOver	[0xc2e0b2940] invalidated after the last release of the connection object
default	15:40:36.569958-0500	VoiceOver	[0xc2e0b2940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:36.570095-0500	VoiceOver	[0xc2e0b2940] invalidated after the last release of the connection object
default	15:40:37.719578-0500	VoiceOver	[0xc2e0b2940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:37.719841-0500	VoiceOver	[0xc2e0b2940] invalidated after the last release of the connection object
default	15:40:38.005697-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	15:40:38.550219-0500	VoiceOver	[0xc2e0b2940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:38.550519-0500	VoiceOver	[0xc2e0b2940] invalidated after the last release of the connection object
default	15:40:38.635612-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 7497
default	15:40:38.636138-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 7497
default	15:40:38.804749-0500	VoiceOver	[0xc2e0b2940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:38.804951-0500	VoiceOver	[0xc2e0b2940] invalidated after the last release of the connection object
default	15:40:39.154791-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	15:40:39.159189-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	15:40:39.159235-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 0
default	15:40:39.162453-0500	powerd	Process VoiceOver.7274 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474877896 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	15:40:39.162805-0500	powerd	Process VoiceOver.7274 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877899 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	15:40:39.218324-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	15:40:39.218842-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:39.219050-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	15:40:39.219058-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	15:40:39.219255-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	15:40:39.219278-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
	App = VoiceOver
	Route = head-tracked headphones
	contentType = 'moov'
	isRunning = 1
	mSpatialMode = 1
	overrideSpatialMode = 0
	preferencesVersion = 1

	Spatial preferences: {
		prefersHeadTrackedSpatialization = 1
		prefersLossyAudioSources = 0
		maxSpatializableChannels = 16
		alwaysSpatialize = 0
		spatialAudioSourceCount = 3
		spatialAudioSources = [ 'mlti', 'binh', 'most' ]
	}
}
default	15:40:39.219305-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0xc2ec88000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	15:40:39.219443-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0xc2ec88000; ; [7274]; play>; running count now 1
default	15:40:39.219496-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	15:40:39.219521-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	15:40:39.219696-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	15:40:39.219710-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0xc2ea3aa18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	15:40:39.238586-0500	VoiceOver	AQSTL aq(0xc2ec88000) start time resolved to: 2073331 ioTS st: 2073331 ht: 73436.841494
error	15:40:39.456717-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	15:40:40.050061-0500	VoiceOver	[0xc2e0b2580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	15:40:40.050292-0500	VoiceOver	[0xc2e0b2580] invalidated after the last release of the connection object
