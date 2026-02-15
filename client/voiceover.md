default	12:53:27.729837-0500	loginwindow	VoiceOverDebug: _ScreenReaderToggleEnabled with option 72
default	12:53:27.735213-0500	loginwindow	VoiceOverDebug: after boostrap_look_up succeeded
default	12:53:27.735291-0500	loginwindow	VoiceOverDebug: calling _SCRStartup returned 0
default	12:53:27.769035-0500	UIKitSystem	Application accessibility enabled: 1, (
	0   libAccessibility.dylib              0x00000001bc4e216c _AXSApplicationAccessibilitySetEnabled + 84
	1   libAccessibility.dylib              0x00000001bc4faa40 _AXSVoiceOverTouchSetEnabled + 368
	2   FuseBoard                           0x000000029abff42c -[FUAccessibilityServer _queue_applySettingWithKey:] + 696
	3   FuseBoard                           0x000000029ac013ec __76-[FUAccessibilityServer _handleApplicationAccessibilityChangedNotification:]_block_invoke + 708
	4   libdispatch.dylib                   0x0000000196bb0b5c _dispatch_call_block_and_release + 32
	5   libdispatch.dylib                   0x0000000196bcaad4 _dispatch_client_callout + 16
	6   libdispatch.dylib                   0x0000000196bb94e8 _dispatch_lane_serial_drain + 740
	7   libdispatch.dylib                   0x0000000196bb9ff8 _dispatch_lane_invoke + 440
	8   libdispatch.dylib                   0x0000000196bbb308 _dispatch_workloop_invoke + 1612
	9   libdispatch.dylib                   0x0000000196bc4474 _dispa
default	12:53:27.985646-0500	VoiceOver	Requesting app group container lookup; personaid = 4294967295, type = NOPERSONA, name = <unknown>, origin [pid = 0, personaid = 0], proximate [pid = 0, personaid = 0], identifier = <private>, euid = 501, uid = 501, platform = 1
default	12:53:28.297368-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35997.16, attribution={responsible={TCCDProcess: identifier=com.apple.VoiceOver, pid=61431, auid=501, euid=501, responsible_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, accessing={TCCDProcess: identifier=com.apple.LegacyUserDefaultsConverter, pid=61432, auid=501, euid=501, binary_path=/System/Library/PrivateFrameworks/ScreenReaderCore.framework/Versions/A/Resources/LegacyUserDefaultsConverter}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=35997, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	12:53:28.310055-0500	tccd	AUTHREQ_SUBJECT: msgID=35997.16, subject=com.apple.VoiceOver,
error	12:53:28.318454-0500	kernel	System Policy: LegacyUserDefaultsConverter(61432) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences/com.apple.VoiceOver4
error	12:53:28.318586-0500	kernel	System Policy: LegacyUserDefaultsConverter(61432) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences
default	12:53:28.385915-0500	VoiceOver	container_create_or_lookup_app_group_path_by_app_group_identifier: success
default	12:53:28.453192-0500	VoiceOver	[0x7070503c0] activating connection: mach=false listener=false peer=false name=com.apple.carboncore.csnameddata
default	12:53:28.463648-0500	VoiceOver	VoiceOverDebug: ArgumentParser _initializeStartupOptions 72
default	12:53:28.465503-0500	VoiceOver	[0x707050500] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	12:53:28.466013-0500	VoiceOver	[0x707050640] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	12:53:28.466856-0500	VoiceOver	Received configuration update from daemon (initial)
default	12:53:28.485699-0500	VoiceOver	VoiceOverDebug: SCRWorkspace init
default	12:53:28.486284-0500	VoiceOver	[0x707050a00] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	12:53:28.487684-0500	VoiceOver	[0x707050b40] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	12:53:28.491405-0500	VoiceOver	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	12:53:28.491897-0500	VoiceOver	[0x707050c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	12:53:28.492444-0500	VoiceOver	[0x707050c80] invalidated after the last release of the connection object
default	12:53:28.492623-0500	VoiceOver	server port 0x00005607, session port 0x00005607
default	12:53:28.495425-0500	VoiceOver	New connection 0x7e33b main
default	12:53:28.497591-0500	VoiceOver	CHECKIN: pid=61431
default	12:53:28.503061-0500	runningboardd	Resolved pid 61431 to [osservice<com.apple.VoiceOver(501)>:61431]
default	12:53:28.503333-0500	runningboardd	_bundleMatchesProcessWithExecutablePath using realpath and comparing /System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver and /System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOverStarter
default	12:53:28.503504-0500	launchservicesd	CHECKIN:0x0-0x10b10b 61431 com.apple.VoiceOver
default	12:53:28.503621-0500	VoiceOver	CHECKEDIN: pid=61431 asn=0x0-0x10b10b foreground=0
default	12:53:28.503690-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] is not RunningBoard jetsam managed.
default	12:53:28.503705-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] This process will not be managed.
default	12:53:28.503715-0500	runningboardd	Now tracking process: [osservice<com.apple.VoiceOver(501)>:61431]
default	12:53:28.504035-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.coreservices.launchservicesd>:366] with description <RBSAssertionDescriptor| "uielement:61431" ID:404-366-22916 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	12:53:28.504092-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] reported to RB as running
default	12:53:28.504112-0500	runningboardd	Assertion 404-366-22916 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:53:28.504189-0500	VoiceOver	[0x707050c80] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	12:53:28.504384-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:53:28.504403-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.coreservices.launchservicesd>:366] with description <RBSAssertionDescriptor| "uielement:61431" ID:404-366-22917 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	12:53:28.504415-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:53:28.504458-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Set darwin role to: UserInteractive
default	12:53:28.504471-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:53:28.504507-0500	VoiceOver	[0x707050dc0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	12:53:28.504513-0500	VoiceOver	[0x707050dc0] Connection returned listener port: 0x5c03
default	12:53:28.504635-0500	VoiceOver	[0x7068cd680] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x707050dc0.peer[366].0x7068cd680
default	12:53:28.504492-0500	runningboardd	Assertion 404-366-22917 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:53:28.504519-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:53:28.504578-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:53:28.505938-0500	VoiceOver	FRONTLOGGING: version 1
default	12:53:28.505943-0500	VoiceOver	Registered, pid=61431 ASN=0x0,0x10b10b
default	12:53:28.506531-0500	WindowServer	7e33b[CreateApplication]: Process creation: 0x0-0x10b10b (VoiceOver) connectionID: 7E33B pid: 61431 in session 0x101
default	12:53:28.506872-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///System/Library/CoreServices/VoiceOver.app/
default	12:53:28.507807-0500	gamepolicyd	Hit the server for a process handle e52cc4c0000eff7 that resolved to: [osservice<com.apple.VoiceOver(501)>:61431]
default	12:53:28.507863-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:53:28.507805-0500	runningboardd	Invalidating assertion 404-366-22916 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.coreservices.launchservicesd>:366]
default	12:53:28.508121-0500	loginwindow	-[Application setState:] | enter: <Application: 0xaa0802620: VoiceOver> state 2
default	12:53:28.508219-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : VoiceOver
default	12:53:28.520154-0500	VoiceOver	[0x707050dc0] Connection returned listener port: 0x5c03
default	12:53:28.520768-0500	VoiceOver	BringForward: pid=61431 asn=0x0-0x10b10b bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	12:53:28.521243-0500	VoiceOver	Current system appearance, (HLTB: 1), (SLS: 0)
default	12:53:28.522547-0500	VoiceOver	No persisted cache on this platform.
default	12:53:28.523276-0500	VoiceOver	Current system appearance, (HLTB: 1), (SLS: 0)
default	12:53:28.523994-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 61431
default	12:53:28.524005-0500	VoiceOver	Post-registration system appearance: (HLTB: 1)
default	12:53:28.524384-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 61431
default	12:53:28.530539-0500	VoiceOver	[0x707051180] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	12:53:28.534225-0500	VoiceOver	FBSWorkspace: endpoint monitoring is disabled.
default	12:53:28.534238-0500	VoiceOver	FBSWorkspace: default shell endpoint is disabled.
default	12:53:28.534295-0500	VoiceOver	Initializing connection
default	12:53:28.534332-0500	VoiceOver	Removing all cached process handles
default	12:53:28.534349-0500	VoiceOver	Sending handshake request attempt #1 to server
default	12:53:28.534358-0500	VoiceOver	Creating connection to com.apple.runningboard
default	12:53:28.534363-0500	VoiceOver	[0x707051040] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	12:53:28.534821-0500	runningboardd	Setting client for [osservice<com.apple.VoiceOver(501)>:61431] as ready
default	12:53:28.535410-0500	VoiceOver	Handshake succeeded
default	12:53:28.535425-0500	VoiceOver	Identity resolved as osservice<com.apple.VoiceOver(501)>
default	12:53:28.546135-0500	VoiceOver	[0x707050dc0] Connection returned listener port: 0x5c03
default	12:53:28.547018-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.apple.VoiceOver token: 1e0000001d pid: 61431
default	12:53:28.547290-0500	VoiceOver	[0x7070512c0] activating connection: mach=true listener=false peer=false name=com.apple.bird.token
default	12:53:28.549114-0500	VoiceOver	[0x7070512c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	12:53:28.550568-0500	VoiceOver	[0x7070512c0] activating connection: mach=true listener=false peer=false name=com.apple.bird
default	12:53:28.551932-0500	VoiceOver	[0x707050dc0] Connection returned listener port: 0x5c03
default	12:53:28.558283-0500	VoiceOver	[0x707051540] activating connection: mach=true listener=false peer=false name=com.apple.AccessibilityVisualsAgent
default	12:53:28.554097-0500	VoiceOver	Created a new Process Instance Registry XPC connection (inactive)
default	12:53:28.561999-0500	VoiceOver	[0x707050f00] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	12:53:28.562057-0500	VoiceOver	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	12:53:28.562102-0500	VoiceOver	[0x707051680] activating connection: mach=false listener=true peer=false name=(anonymous)
default	12:53:28.562695-0500	VoiceOver	[0x707051680] Connection returned listener port: 0x8703
default	12:53:28.563657-0500	VoiceOver	Registered process with identifier 61431-844979
default	12:53:28.571185-0500	VoiceOver	[C:1] Alloc <private>
default	12:53:28.571243-0500	VoiceOver	[0x707051900] activating connection: mach=false listener=false peer=false name=(anonymous)
default	12:53:28.575042-0500	WindowManager	Connection activated | (61431) VoiceOver
default	12:53:28.587436-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.apple.VoiceOver token: 2100000023 pid: 61431
default	12:53:28.587594-0500	VoiceOver	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x706c5d040
 (
    "<NSAquaAppearance: 0x706c5d220>",
    "<NSSystemAppearance: 0x706c5d180>"
)>
default	12:53:28.591331-0500	VoiceOver	[0x707051e00] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	12:53:28.593697-0500	VoiceOver	[0x707051f40] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	12:53:28.624030-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 61433
default	12:53:28.646416-0500	VoiceOver	New connection 0xd8193 secondary
default	12:53:28.650254-0500	distnoted	register name: kVoiceOverSpeechBecameActiveNotification object: kCFNotificationAnyObject token: 270000002a pid: 61431
default	12:53:28.650336-0500	distnoted	register name: kVoiceOverSpeechBecameIdleNotification object: kCFNotificationAnyObject token: 2800000029 pid: 61431
default	12:53:28.651218-0500	VoiceOver	[0x707053200] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	12:53:28.665524-0500	VoiceOver	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	12:53:28.666620-0500	VoiceOver	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.apple.VoiceOver (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	12:53:28.668306-0500	VoiceOver	[0x707053340] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	12:53:28.672600-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver>
default	12:53:28.678845-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	12:53:28.681138-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/VoiceOver/AUVoiceIOChatFlavor, translatedBundleID VoiceOver, bundleIDs {(
    "com.apple.VoiceOver"
)}
default	12:53:28.681318-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/VoiceOver/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID VoiceOver, bundleIDs {(
    "com.apple.VoiceOver"
)}
default	12:53:28.681469-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	12:53:28.681480-0500	VoiceOver	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	12:53:28.681946-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	12:53:28.682075-0500	VoiceOver	[0x707053480] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	12:53:28.683195-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=61431.2, attribution={requesting={TCCDProcess: identifier=com.apple.VoiceOver, pid=61431, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, },
default	12:53:28.689677-0500	tccd	AUTHREQ_SUBJECT: msgID=61431.2, subject=com.apple.VoiceOver,
default	12:53:28.692459-0500	VoiceOver	[0x707053480] invalidated after the last release of the connection object
default	12:53:28.692500-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	12:53:28.694734-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.464, attribution={accessing={TCCDProcess: identifier=com.apple.VoiceOver, pid=61431, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:53:28.695213-0500	tccd	AUTHREQ_SUBJECT: msgID=409.464, subject=com.apple.VoiceOver,
default	12:53:28.695812-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.apple.VoiceOver, type: 0: 0x8fcd7c600 at /System/Library/CoreServices/VoiceOver.app
error	12:53:28.701421-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.apple.VoiceOver, pid=61431, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=409, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	12:53:28.702394-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=409.466, attribution={accessing={TCCDProcess: identifier=com.apple.VoiceOver, pid=61431, auid=501, euid=501, binary_path=/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=397, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	12:53:28.702927-0500	tccd	AUTHREQ_SUBJECT: msgID=409.466, subject=com.apple.VoiceOver,
default	12:53:28.703511-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.apple.VoiceOver, type: 0: 0x8fcd7c600 at /System/Library/CoreServices/VoiceOver.app
default	12:53:28.708977-0500	VoiceOver	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	12:53:28.709619-0500	VoiceOver	AddInstanceForFactory: No factory registered for id <CFUUID 0x707750f60> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	12:53:28.726550-0500	VoiceOver	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	12:53:28.726564-0500	VoiceOver	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	12:53:28.732177-0500	coreaudiod	>>> SIMULATE [com.apple.VoiceOver]
default	12:53:28.732358-0500	coreaudiod	<<< SIMULATE [com.apple.VoiceOver]
default	12:53:28.737062-0500	VoiceOver	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	12:53:28.737564-0500	VoiceOver	                AUHAL.cpp:420   AUHAL: (0x706be0040) Selecting device 85 from constructor
default	12:53:28.737581-0500	VoiceOver	                AUHAL.cpp:629   SelectDevice: -> (0x706be0040)
default	12:53:28.737590-0500	VoiceOver	                AUHAL.cpp:681   SelectDevice: (0x706be0040) not already running
default	12:53:28.737983-0500	VoiceOver	                AUHAL.cpp:757   SelectDevice: (0x706be0040) nothing to teardown
default	12:53:28.737988-0500	VoiceOver	                AUHAL.cpp:762   SelectDevice: (0x706be0040) connecting device 85
default	12:53:28.738059-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:53:28.738138-0500	VoiceOver	                AUHAL.cpp:774   SelectDevice: (0x706be0040) created ioproc 0xa for device 85
default	12:53:28.738240-0500	VoiceOver	                AUHAL.cpp:863   SelectDevice: (0x706be0040) adding 7 device listeners to device 85
default	12:53:28.738396-0500	VoiceOver	                AUHAL.cpp:863   SelectDevice: (0x706be0040) adding 0 device delegate listeners to device 85
default	12:53:28.738405-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:53:28.738475-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:53:28.738481-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:53:28.738487-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:53:28.738501-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:53:28.738512-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:53:28.738595-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:53:28.738605-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:53:28.738610-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:53:28.738614-0500	VoiceOver	                AUHAL.cpp:900   SelectDevice: (0x706be0040) removing 0 device listeners from device 0
default	12:53:28.738622-0500	VoiceOver	                AUHAL.cpp:900   SelectDevice: (0x706be0040) removing 0 device delegate listeners from device 0
default	12:53:28.738626-0500	VoiceOver	                AUHAL.cpp:916   SelectDevice: <- (0x706be0040)
default	12:53:28.773637-0500	VoiceOver	[0x7077b8820] Session created.
default	12:53:28.773646-0500	VoiceOver	[0x7077b8820] Session created with Mach Service: <private>
default	12:53:28.773682-0500	VoiceOver	[0x707053480] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	12:53:28.773775-0500	VoiceOver	[0x7077b8820] Session activated
error	12:53:28.792134-0500	kernel	1 duplicate report for System Policy: LegacyUserDefaultsConverter(61432) deny(1) file-read-data /Users/sergiyzasorin/Library/Group Containers/group.com.apple.VoiceOver/Library/Preferences
default	12:53:29.550229-0500	VoiceOver	[0x7077b8eb0] Session created.
default	12:53:29.550240-0500	VoiceOver	[0x7077b8eb0] Session created with Mach Service: <private>
default	12:53:29.550249-0500	VoiceOver	[0x707d7b200] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	12:53:29.550369-0500	VoiceOver	[0x7077b8eb0] Session activated
default	12:53:29.567367-0500	VoiceOver	[0x7077b8f00] Session created.
default	12:53:29.567377-0500	VoiceOver	[0x7077b8f00] Session created with Mach Service: <private>
default	12:53:29.567400-0500	VoiceOver	[0x707d60140] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	12:53:29.567468-0500	VoiceOver	[0x7077b8f00] Session activated
error	12:53:29.686466-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	12:53:29.696894-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	12:53:29.696937-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	12:53:29.701493-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	12:53:29.701520-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	12:53:29.784460-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	12:53:29.784490-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	12:53:29.837995-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
error	12:53:29.838038-0500	VoiceOver	-[AFLocalization outputVoiceDescriptorForOutputLanguageCode:voiceName:] No descriptor found for language code <private>, voice name <private>
default	12:53:29.851728-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:53:29.853513-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:53:29.854209-0500	VoiceOver	       ACv2Workarounds.mm:51    com.apple.VoiceOver: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	12:53:29.854265-0500	VoiceOver	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	12:53:29.854412-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x707e20510, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:53:29.854464-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:53:29.855087-0500	VoiceOver	[0x707d6c280] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	12:53:29.858959-0500	VoiceOver	LFSMCopySessionAgentEndpoint: enter
default	12:53:29.859160-0500	VoiceOver	[0x707d6c000] activating connection: mach=true listener=false peer=false name=com.apple.logind
default	12:53:29.860546-0500	VoiceOver	LFSMCopySessionAgentEndpoint: exit: result = 0
default	12:53:29.860680-0500	VoiceOver	[0x707d6c500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	12:53:29.860960-0500	VoiceOver	[SCROBrailleClient setDelegate:<SCROutputBrailleComponent: 0x706c61000>]
default	12:53:29.860997-0500	VoiceOver	-[SCROBrailleClient _registerDelegate] Register callback: 'Display Configuration Changed'
default	12:53:29.861629-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:53:29.862011-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:53:29.862529-0500	VoiceOver	[0x707d6c8c0] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	12:53:29.863776-0500	VoiceOver	[0x707d6c640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	12:53:29.864480-0500	VoiceOver	[0x707d6c640] invalidated after the last release of the connection object
default	12:53:29.867191-0500	VoiceOver	server port 0x0001ee0f, session port 0x00005607
default	12:53:29.869152-0500	VoiceOver	[0x707d6c640] activating connection: mach=true listener=false peer=false name=com.apple.backlightd
default	12:53:29.874010-0500	WindowServer	Connection added: IOHIDEventSystemConnection uuid:336206AB-338D-4D00-B12B-8E90A3232605 pid:61431 process:VoiceOver type:Rate Controlled entitlements:0xa caller:ScreenReader: -[SCREventFactory completeInitialization] + 1196 attributes:(null) state:0x0 events:0 mask:0x0 dropped:0 dropStatus:0 droppedMask:0x0 lastDroppedTime:NONE
default	12:53:29.877645-0500	VoiceOver	SASSessionStateForUser:1280: enter
default	12:53:29.877727-0500	VoiceOver	SASSessionStateForUser:1300: SA: currentState: 2
default	12:53:29.877743-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:53:29.878310-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:53:29.878417-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:53:29.883111-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 6700000061 pid: 61431
default	12:53:29.883790-0500	VoiceOver	SASSessionStateForUser:1280: enter
default	12:53:29.883850-0500	VoiceOver	SASSessionStateForUser:1300: SA: currentState: 2
default	12:53:29.883863-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:53:29.884407-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:53:29.884489-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:53:29.884783-0500	VoiceOver	'Dock' is running
default	12:53:29.884996-0500	VoiceOver	'Setup Assistant' is not running
default	12:53:29.887881-0500	VoiceOver	                AUHAL.cpp:2303  SetProperty: (0x706be0040) caller requesting device change from 85 to 85
default	12:53:29.887888-0500	VoiceOver	                AUHAL.cpp:629   SelectDevice: -> (0x706be0040)
default	12:53:29.887895-0500	VoiceOver	                AUHAL.cpp:664   SelectDevice: <- (0x706be0040) exiting with nothing to do
default	12:53:29.903665-0500	VoiceOver	[0x707d6d180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	12:53:29.904921-0500	VoiceOver	[0x707d6d180] invalidated after the last release of the connection object
default	12:53:29.934086-0500	VoiceOver	[0x707050dc0] Connection returned listener port: 0x5c03
default	12:53:29.934875-0500	VoiceOver	[0x707d6d180] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	12:53:29.935307-0500	VoiceOver	SignalReady: pid=61431 asn=0x0-0x10b10b
default	12:53:29.935762-0500	VoiceOver	SIGNAL: pid=61431 asn=0x0x-0x10b10b
default	12:53:29.936775-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///System/Library/CoreServices/VoiceOver.app/
default	12:53:29.949429-0500	distnoted	register name: AXSSVoiceOverPunctuationCloudKitUpdateNotification object: kCFNotificationAnyObject token: 6800000060 pid: 61431
default	12:53:29.951431-0500	VoiceOver	CloudKit integration setup failed with error:
Error Domain=AXCloudKitErrorDomain Code=0 "Current process can't use cloud kit" UserInfo={NSLocalizedFailureReason=Current process can't use cloud kit}
default	12:53:29.951455-0500	VoiceOver	CloudKit integration setup failed with error:
Error Domain=AXCloudKitErrorDomain Code=0 "Current process can't use cloud kit" UserInfo={NSLocalizedFailureReason=Current process can't use cloud kit}
default	12:53:29.962672-0500	VoiceOver	[0x707050dc0] Connection returned listener port: 0x5c03
default	12:53:30.010637-0500	VoiceOver	[SCROBrailleClient handleCallback:] for key CallbackConnect
default	12:53:30.012177-0500	VoiceOver	-[SCROBrailleClient _registerDelegate] Register callback: 'Display Configuration Changed'
default	12:53:30.058760-0500	VoiceOver	IOMainPort returned 0
default	12:53:30.060256-0500	VoiceOver	-[SCROBrailleClient handleCallback:] Call delegate's config change handler; Delegate wants == 1, isConfigured == 1
default	12:53:30.060364-0500	VoiceOver	-[SCROBrailleClient handleCallback:] Call delegate's config change handler; Delegate wants == 1, isConfigured == 1
default	12:53:30.071821-0500	VoiceOver	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	12:53:30.071835-0500	VoiceOver	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	12:53:30.071897-0500	VoiceOver	[0x707d6d680] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	12:53:30.072021-0500	VoiceOver	[0x707d6d680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	12:53:30.072736-0500	VoiceOver	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	12:53:30.087269-0500	VoiceOver	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	12:53:30.087904-0500	VoiceOver	void _NSEnableAutomaticTerminationAndLog(NSString *) No windows open yet
default	12:53:30.089020-0500	VoiceOver	sConnectionName: com.apple.spotlight.IndexAgent
default	12:53:30.089188-0500	VoiceOver	Start service name com.apple.spotlight.IndexAgent
default	12:53:30.089222-0500	VoiceOver	[0x707d6d540] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	12:53:30.110474-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.WindowServer(88)>:396] with description <RBSAssertionDescriptor| "AppDrawing" ID:404-396-22921 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:53:30.110584-0500	runningboardd	Assertion 404-396-22921 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:53:30.112463-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:53:30.112550-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:53:30.112644-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:53:30.112770-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:53:30.112782-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:53:30.118608-0500	VoiceOver	registering darwin observer for name: com.apple.gms.availability.notification
default	12:53:30.118653-0500	VoiceOver	registering darwin observer for name: com.apple.os-eligibility-domain.change.greymatter
default	12:53:30.118675-0500	VoiceOver	registering darwin observer for name: com.apple.language.changed
default	12:53:30.118742-0500	VoiceOver	isAvailable value changed: isMDMAllowed = true, gmAvailable (current) = true
default	12:53:30.136733-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.WindowServer(88)>:396] with description <RBSAssertionDescriptor| "AppVisible" ID:404-396-22922 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:53:30.136873-0500	runningboardd	Assertion 404-396-22922 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:53:30.137836-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:53:30.137849-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:53:30.137859-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:53:30.137917-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:53:30.137944-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:53:30.146619-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:53:30.276660-0500	VoiceOver	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	12:53:30.286523-0500	VoiceOver	Start service name com.apple.spotlightknowledged
default	12:53:30.307482-0500	VoiceOver	[GMS] availability notification token 310
default	12:53:32.692599-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.apple.VoiceOver: <private>
default	12:53:33.589705-0500	VoiceOver	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=0
default	12:53:34.047203-0500	VoiceOver	[0x708198aa0] Session created.
default	12:53:34.047219-0500	VoiceOver	[0x708198aa0] Session created with Mach Service: <private>
default	12:53:34.047235-0500	VoiceOver	[0x707d6cf00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	12:53:34.047415-0500	VoiceOver	[0x708198aa0] Session activated
default	12:53:34.447012-0500	VoiceOver	New connection 0xf4473 secondary
default	12:53:34.507098-0500	VoiceOver	No list of permitted front apps returned
default	12:53:34.525257-0500	VoiceOver	No list of permitted front apps returned
default	12:53:34.563412-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:53:34.570919-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:53:34.593728-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:53:34.727474-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873749 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:53:34.728195-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-22928 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:53:34.728302-0500	runningboardd	Assertion 404-337-22928 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:53:34.728831-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:53:34.728853-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:53:34.728925-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:53:34.728988-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:53:34.729022-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:53:34.731967-0500	VoiceOver	[0x70819a170] Session created.
default	12:53:34.732007-0500	VoiceOver	[0x70819a170] Session created with Mach Service: <private>
default	12:53:34.732086-0500	VoiceOver	[0x707d6c3c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.voices
default	12:53:34.732203-0500	VoiceOver	[0x70819a170] Session activated
default	12:53:34.802551-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:53:34.845756-0500	VoiceOver	AudioComponentPluginMgr.mm:114   registrationsChanged
default	12:53:34.849713-0500	VoiceOver	AudioComponentPluginMgr.mm:1117  component registrations changed
default	12:53:34.849766-0500	VoiceOver	AudioComponentPluginMgr.mm:906   First wildcard component search: 0/0/0
default	12:53:34.853703-0500	VoiceOver	AudioComponentPluginMgr.mm:1117  component registrations changed
default	12:53:34.854460-0500	VoiceOver	[0x707d6db80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.889314-0500	VoiceOver	[0x707d6db80] invalidated after the last release of the connection object
default	12:53:34.890227-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.890484-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.890552-0500	VoiceOver	[0x707d6ca00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.890748-0500	VoiceOver	[0x707d6ca00] invalidated after the last release of the connection object
default	12:53:34.891000-0500	VoiceOver	[0x707d6c780] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.891180-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:53:34.891283-0500	VoiceOver	[0x707d6cb40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.891536-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:53:34.891623-0500	VoiceOver	[0x707d6d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.891798-0500	VoiceOver	[0x707d6d400] invalidated after the last release of the connection object
default	12:53:34.891963-0500	VoiceOver	[0x707d6d7c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.892160-0500	VoiceOver	[0x707d6d7c0] invalidated after the last release of the connection object
default	12:53:34.892252-0500	VoiceOver	[0x707d6d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.892589-0500	VoiceOver	[0x707d6d900] invalidated after the last release of the connection object
default	12:53:34.892642-0500	VoiceOver	[0x707d6da40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.892818-0500	VoiceOver	[0x707d6da40] invalidated after the last release of the connection object
default	12:53:34.893210-0500	VoiceOver	[0x707d6de00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.893445-0500	VoiceOver	[0x707d6de00] invalidated after the last release of the connection object
default	12:53:34.893526-0500	VoiceOver	[0x707d6df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.893687-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:53:34.893770-0500	VoiceOver	[0x707d6e080] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.894308-0500	VoiceOver	[0x707d6e080] invalidated after the last release of the connection object
default	12:53:34.894383-0500	VoiceOver	[0x707d6c780] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.894639-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:53:34.894850-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.895076-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.895278-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.895607-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.895664-0500	VoiceOver	[0x707d6cb40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.895863-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:53:34.895957-0500	VoiceOver	[0x707d6d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.896136-0500	VoiceOver	[0x707d6d400] invalidated after the last release of the connection object
default	12:53:34.896188-0500	VoiceOver	[0x707d6d7c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.896599-0500	VoiceOver	[0x707d6d7c0] invalidated after the last release of the connection object
default	12:53:34.896657-0500	VoiceOver	[0x707d6d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.896816-0500	VoiceOver	[0x707d6d900] invalidated after the last release of the connection object
default	12:53:34.897145-0500	VoiceOver	[0x707d6df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.897381-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:53:34.897547-0500	VoiceOver	[0x707d6c780] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.897871-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:53:34.897965-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.898168-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.898228-0500	VoiceOver	[0x707d6db80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.898566-0500	VoiceOver	[0x707d6db80] invalidated after the last release of the connection object
default	12:53:34.898596-0500	VoiceOver	[0x707d6df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.898825-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:53:34.898909-0500	VoiceOver	[0x707d6d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.899110-0500	VoiceOver	[0x707d6d900] invalidated after the last release of the connection object
default	12:53:34.899177-0500	VoiceOver	[0x707d6d7c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.899380-0500	VoiceOver	[0x707d6d7c0] invalidated after the last release of the connection object
default	12:53:34.899410-0500	VoiceOver	[0x707d6df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.899573-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:53:34.899625-0500	VoiceOver	[0x707d6db80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.899787-0500	VoiceOver	[0x707d6db80] invalidated after the last release of the connection object
default	12:53:34.899840-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.900001-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.900053-0500	VoiceOver	[0x707d6c780] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.900260-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:53:34.900316-0500	VoiceOver	[0x707d6cb40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.900487-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:53:34.900531-0500	VoiceOver	[0x707d6d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.900690-0500	VoiceOver	[0x707d6d900] invalidated after the last release of the connection object
default	12:53:34.900718-0500	VoiceOver	[0x707d6d400] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.900943-0500	VoiceOver	[0x707d6d400] invalidated after the last release of the connection object
default	12:53:34.900975-0500	VoiceOver	[0x707d6df40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.901170-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:53:34.901201-0500	VoiceOver	[0x707d6da40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.901443-0500	VoiceOver	[0x707d6da40] invalidated after the last release of the connection object
default	12:53:34.901475-0500	VoiceOver	[0x707d6de00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.901634-0500	VoiceOver	[0x707d6de00] invalidated after the last release of the connection object
default	12:53:34.901720-0500	VoiceOver	[0x707d6e080] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.901870-0500	VoiceOver	[0x707d6e080] invalidated after the last release of the connection object
default	12:53:34.901897-0500	VoiceOver	[0x707d6ca00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.902053-0500	VoiceOver	[0x707d6ca00] invalidated after the last release of the connection object
default	12:53:34.902132-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.902544-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.902681-0500	VoiceOver	[0x707d6da40] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.902889-0500	VoiceOver	[0x707d6da40] invalidated after the last release of the connection object
default	12:53:34.902931-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.903080-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.903129-0500	VoiceOver	[0x707d6db80] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.903291-0500	VoiceOver	[0x707d6db80] invalidated after the last release of the connection object
default	12:53:34.903330-0500	VoiceOver	[0x707d6de00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.903502-0500	VoiceOver	[0x707d6de00] invalidated after the last release of the connection object
default	12:53:34.903542-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.903709-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.903753-0500	VoiceOver	[0x707d6e080] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.903903-0500	VoiceOver	[0x707d6e080] invalidated after the last release of the connection object
default	12:53:34.903933-0500	VoiceOver	[0x707d6ca00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.904090-0500	VoiceOver	[0x707d6ca00] invalidated after the last release of the connection object
default	12:53:34.904177-0500	VoiceOver	[0x707d6e080] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.904336-0500	VoiceOver	[0x707d6e080] invalidated after the last release of the connection object
default	12:53:34.904392-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.904546-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.904614-0500	VoiceOver	[0x707d6e080] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.904762-0500	VoiceOver	[0x707d6e080] invalidated after the last release of the connection object
default	12:53:34.904810-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.905013-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.905054-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.905190-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.905234-0500	VoiceOver	[0x707d6ca00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.905471-0500	VoiceOver	[0x707d6ca00] invalidated after the last release of the connection object
default	12:53:34.905497-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.905652-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.905689-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.905863-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.905977-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.906177-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.906225-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.906471-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.906522-0500	VoiceOver	[0x707d6ca00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.906810-0500	VoiceOver	[0x707d6ca00] invalidated after the last release of the connection object
default	12:53:34.906867-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.907078-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.907121-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.907388-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.907705-0500	VoiceOver	Class EXGetExtensionClass(void) returning EXConcreteExtension
default	12:53:34.907756-0500	VoiceOver	[0x707d6db80] activating connection: mach=true listener=false peer=false name=com.apple.pluginkit.pkd
default	12:53:34.907967-0500	VoiceOver	[d <private>] <PKHost:0x706295840> Beginning discovery for flags: 1024, point: (null)
default	12:53:34.910712-0500	VoiceOver	[d <private>] <PKHost:0x706295840> Completed discovery. Final # of matches: 1
default	12:53:34.912260-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.912524-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.912717-0500	VoiceOver	[d <private>] <PKHost:0x706295840> Beginning discovery for flags: 1024, point: (null)
default	12:53:34.914418-0500	VoiceOver	[d <private>] <PKHost:0x706295840> Completed discovery. Final # of matches: 1
default	12:53:34.917584-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.917982-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.918093-0500	VoiceOver	[d <private>] <PKHost:0x706295840> Beginning discovery for flags: 1024, point: (null)
default	12:53:34.920013-0500	VoiceOver	[d <private>] <PKHost:0x706295840> Completed discovery. Final # of matches: 1
default	12:53:34.922342-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.922590-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.922662-0500	VoiceOver	[d <private>] <PKHost:0x706295840> Beginning discovery for flags: 1024, point: (null)
default	12:53:34.923902-0500	VoiceOver	[d <private>] <PKHost:0x706295840> Completed discovery. Final # of matches: 1
default	12:53:34.925154-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.925369-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.925429-0500	VoiceOver	[d <private>] <PKHost:0x706295840> Beginning discovery for flags: 1024, point: (null)
default	12:53:34.926738-0500	VoiceOver	[d <private>] <PKHost:0x706295840> Completed discovery. Final # of matches: 1
default	12:53:34.926980-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	12:53:34.927926-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.928148-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.937726-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.938010-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.942975-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.943423-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.943484-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.943753-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.949811-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.950227-0500	VoiceOver	[0x707d6e580] invalidated after the last release of the connection object
default	12:53:34.950333-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.950639-0500	VoiceOver	[0x707d6d2c0] invalidated after the last release of the connection object
default	12:53:34.950700-0500	VoiceOver	[0x707d6ca00] activating connection: mach=false listener=false peer=false name=com.apple.audio.ComponentTagHelper
default	12:53:34.950895-0500	VoiceOver	[0x707d6ca00] invalidated after the last release of the connection object
default	12:53:34.954819-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Ready plugins sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	12:53:34.960603-0500	runningboardd	Launch request for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}[0] is using uid 501 (divined from auid 501 euid 501)
default	12:53:34.960675-0500	runningboardd	Executing launch request for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]} (Launching extension com.apple.ax.MauiTTSSupport.MauiAUSP(14844CB3-B750-5F5A-987A-D4BBC31613B5) for host 61431) from requestor: [osservice<com.apple.pluginkit.pkd(501)>:35537]
default	12:53:34.960773-0500	runningboardd	Creating and launching job for: xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}
default	12:53:34.960968-0500	runningboardd	'(null)' Submitting extension overlay (host PID 61431, path /System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/Versions/A/PlugIns/MauiAUSP.appex/Contents/MacOS/MauiAUSP):
<dictionary: 0xc9e877060> { count = 3, transaction: 0, voucher = 0x0, contents =
	"XPCService" => <dictionary: 0xc9efa1aa0> { count = 11, transaction: 0, voucher = 0x0, contents =
		"_ManagedBy" => <string: 0xc9f8232d0> { string cache = 0x0, length = 22, contents = "com.apple.runningboard" }
		"RunLoopType" => <string: 0xc9f2d7ae0> { string cache = 0x0, length = 9, contents = "NSRunLoop" }
		"Platform" => <int64: 0x914e65d49b1b40a7>: 1
		"JoinExistingSession" => <bool: 0x205277830>: true
		"_SandboxProfile" => <string: 0xc9f808420> { string cache = 0x0, length = 6, contents = "plugin" }
		"_AdditionalSubServices" => <dictionary: 0xc9efa21c0> { count = 1, transaction: 0, voucher = 0x0, contents =
			"apple-extension-service" => <bool: 0x205277830>: true
		}
		"PersonaEnterprise" => <int64: 0x914e65d49b1b5fe7>: 1001
		"_AdditionalProperties" => <dictionary: 0xc9efa0360> { count = 1, transaction: 0, voucher = 0x0, contents =
			"RunningBoard" => <dictionary: 0xc9efa0b40> { count = 2, transaction: 0, voucher = 0x0, contents =
				"RunningBoardLaunchedIdentity" => <dictionary: 0xc9efa0120> { count = 6, transaction: 0, voucher = 0x0, contents =
					"e" => <int64: 0x914e65d49b1b4f07>: 501
					"TYPE" => <int64: 0x914e65d49b1b408f>: 4
					"h" => <int64: 0x914e65d49b1c3f17>: 61431
					"i" => <string: 0xc9f883f30> { string cache = 0x0, length = 36, contents = "com.apple.ax.MauiTTSSupport.MauiAUSP" }
					"r" => <int64: 0x914e65d49b1b40bf>: 2
					"H" => <dictionary: 0xc9efa0cc0> { count = 5, transaction: 0, voucher = 0x0, contents =
						"l" => <string: 0xc9f823ae0> { string cache = 0x0, length = 19, contents = "com.apple.VoiceOver" }
						"t" => <int64: 0x914e65d49b1b40bf>: 2
						"TYPE" => <int64: 0x914e65d49b1b409f>: 6
						"a" => <int64: 0x914e65d49b1b4f07>: 501
						"p" => <int64: 0x914e65d49b1b40af>: 0
					}
				}
				"RunningBoardLaunched" => <bool: 0x205277830>: true
			}
		}
		"_OmitSandboxParameters" => <bool: 0x205277830>: true
		"ServiceType" => <string: 0xc9f2d79f0> { string cache = 0x0, length = 11, contents = "Application" }
		"ProgramArguments" => <array: 0xc9f80b120> { count = 3, capacity = 8, contents =
			0: <string: 0xc9f2d65e0> { string cache = 0x0, length = 125, contents = "/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/Versions/A/PlugIns/MauiAUSP.appex/Contents/MacOS/MauiAUSP" }
			1: <string: 0xc9f2d5500> { string cache = 0x0, length = 15, contents = "-AppleLanguages" }
			2: <string: 0xc9f2d4060> { string cache = 0x0, length = 27, contents = "("en-CA", "ru-CA", "fr-CA")" }
		}
	}
	"RunningBoard" => <dictionary: 0xc9e8750e0> { count = 1, transaction: 0, voucher = 0x0, contents =
		"Managed" => <bool: 0x205277830>: true
	}
	"CFBundlePackageType" => <string: 0xc9f2d6f10> { string cache = 0x0, length = 4, contents = "XPC!" }
}
default	12:53:34.996189-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] Memory Limits: active 0 inactive 0
 <private>
default	12:53:34.996215-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] This process will be managed.
error	12:53:34.996277-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] Memorystatus failed with unexpected error: Invalid argument (22)
default	12:53:34.996296-0500	runningboardd	Now tracking process: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]
default	12:53:34.996485-0500	runningboardd	Calculated state for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}: running-suspended (role: None) (endowments: (null))
default	12:53:34.997315-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] got pid from ready request: 61441
default	12:53:34.997649-0500	WindowServer	Hit the server for a process handle 1c860a530000f001 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]
default	12:53:34.996944-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] reported to RB as running
default	12:53:34.997898-0500	UIKitSystem	Hit the server for a process handle 1c860a530000f001 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]
default	12:53:34.997961-0500	UIKitSystem	Received state update for 61441 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	12:53:34.997713-0500	WindowServer	Received state update for 61441 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	12:53:34.998163-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "com.apple.extension.session" ID:404-61431-22929 target:61441 attributes:[
	<RBSLegacyAttribute| requestedReason:ViewService reason:ViewService flags:( AllowIdleSleep PreventTaskSuspend PreventTaskThrottleDown )>,
	<RBSAcquisitionCompletionAttribute| policy:AfterValidation>
	]>
default	12:53:34.998254-0500	runningboardd	Assertion 404-61431-22929 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]) will be created as active
default	12:53:34.998744-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] Set jetsam priority to 40 [0] flag[1]
default	12:53:34.998763-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] Resuming task.
default	12:53:34.998786-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] Result 45 setting darwin role to UserInteractiveNonFocal: Operation not supported, falling back to setting priority
default	12:53:34.998836-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] Set darwin priority to: PRIO_DEFAULT
default	12:53:34.999413-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] prevented from droping Memory Limits from 0 to -1
default	12:53:35.003156-0500	runningboardd	Calculated state for xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}: running-active (role: UserInteractiveNonFocal) (endowments: (null))
default	12:53:35.003439-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] acquired startup assertion
default	12:53:35.003680-0500	WindowServer	Received state update for 61441 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	12:53:35.003796-0500	UIKitSystem	Received state update for 61441 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	12:53:35.004050-0500	VoiceOver	Creating side-channel connection to com.apple.runningboard
default	12:53:35.004067-0500	VoiceOver	[0x707d6ca00] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	12:53:35.004920-0500	VoiceOver	Hit the server for a process handle 1c860a530000f001 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]
default	12:53:35.005166-0500	VoiceOver	[0x707d6d2c0] activating connection: mach=false listener=false peer=false name=com.apple.ax.MauiTTSSupport.MauiAUSP
default	12:53:35.005304-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Prepare using sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	12:53:35.005326-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5] [<private>(<private>)] Sending prepareUsing to managed extension; this should launch it if not already running.
default	12:53:35.004626-0500	gamepolicyd	Hit the server for a process handle 1c860a530000f001 that resolved to: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]
default	12:53:35.117618-0500	runningboardd	Setting client for [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] as ready
default	12:53:35.120573-0500	MauiAUSP	Identity resolved as xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}
default	12:53:35.123862-0500	gamepolicyd	Received state update for 61441 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-suspended-NotVisible
default	12:53:35.130954-0500	gamepolicyd	Received state update for 61441 (xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}, running-active-NotVisible
default	12:53:35.134646-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] Begin using sent as euid = 501, uid = 501, personaid = -1, type = NOPERSONA, name = <unknown>
default	12:53:35.135006-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] plugin loaded and ready for host
default	12:53:35.135514-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "com.apple.extension.session" ID:404-61431-22930 target:61441 attributes:[
	<RBSLegacyAttribute| requestedReason:ViewService reason:ViewService flags:( AllowIdleSleep PreventTaskSuspend PreventTaskThrottleDown WantsForegroundResourcePriority )>,
	<RBSAcquisitionCompletionAttribute| policy:AfterValidation>
	]>
default	12:53:35.135638-0500	runningboardd	Assertion 404-61431-22930 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]) will be created as active
default	12:53:35.136228-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] Set jetsam priority to 100 [0] flag[1]
default	12:53:35.136358-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] prevented from droping Memory Limits from 0 to -1
default	12:53:35.140460-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] invalidating startup assertion
default	12:53:35.140639-0500	runningboardd	Invalidating assertion 404-61431-22929 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:53:35.140785-0500	VoiceOver	Class EXGetExtensionContextInternalClass(void) returning EXExtensionContextImplementation
default	12:53:35.148190-0500	VoiceOver	[0x707d6e580] activating connection: mach=false listener=true peer=false name=(anonymous)
default	12:53:35.148516-0500	VoiceOver	[0x706d47c00] activating connection: mach=false listener=false peer=false name=com.apple.ax.MauiTTSSupport.MauiAUSP.apple-extension-service
default	12:53:35.148802-0500	VoiceOver	[0x707d6e580] Connection returned listener port: 0x23d0f
default	12:53:35.225924-0500	VoiceOver	[0x706d47d80] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x707d6e580.peer[61441].0x706d47d80
default	12:53:35.226555-0500	VoiceOver	[0x707d6d900] activating connection: mach=false listener=false peer=false name=com.apple.audio.AUCrashHandlerService
default	12:53:35.246121-0500	VoiceOver	   AUOOPRenderPipePool.mm:167   Host obtained render pipe 251662521
default	12:53:35.246445-0500	VoiceOver	       AUOOPWorkgroups.mm:66    AUOOPWorkgroupManager: mutating workgroups.
default	12:53:35.544498-0500	VoiceOver	[0x707d6d900] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
error	12:53:35.544544-0500	VoiceOver	        AUCrashHandler.mm:126   invalidated
default	12:53:35.728585-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] with description <RBSAssertionDescriptor| "RunningBoardAssertedAssetSets" ID:404-61441-22933 target:61441 attributes:[
	<RBSDomainAttribute| domain:"com.apple.common" name:"FinishTaskUninterruptable" sourceEnvironment:"(null)">
	]>
default	12:53:35.728720-0500	runningboardd	Assertion 404-61441-22933 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]) will be created as inactive as start-time-defining assertions exist
default	12:53:35.738655-0500	runningboardd	Invalidating assertion 404-61441-22933 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]) from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]
default	12:53:35.747416-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813e430, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:53:35.747620-0500	VoiceOver	AudioConverter -> 0x70813e430: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:53:35.747641-0500	VoiceOver	AudioConverter -> 0x70813e430: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:53:35.751801-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-22934 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:53:35.751934-0500	runningboardd	Assertion 404-61431-22934 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:53:35.752666-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:53:35.752682-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:53:35.752696-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:53:35.752799-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:53:35.752856-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:53:35.756298-0500	VoiceOver	[0x707d6de00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:53:35.763662-0500	VoiceOver	[0x707d6de00] invalidated after the last release of the connection object
default	12:53:35.781285-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:53:35.902734-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e1320, from  1 ch,  22050 Hz, Float32 (actually:  1 ch,  22050 Hz, Float32) to  1 ch,  22050 Hz, Float32 (actually:  1 ch,  22050 Hz, Float32)
default	12:53:35.902807-0500	VoiceOver	     AudioQueueObject.cpp:487   AudioQueueObject: aq@0x7074da800: New output; format  1 ch,  22050 Hz, Float32 (passthrough? no)
default	12:53:35.904088-0500	VoiceOver	           HeadTracker.mm:110   HeadTrackerSession 0x706356ee0 created for movie spatialization.
default	12:53:35.904097-0500	VoiceOver	           HeadTracker.mm:110   HeadTrackerSession 0x7063570c0 created for music spatialization.
default	12:53:35.905627-0500	VoiceOver	           AQMEIO_HAL.cpp:2218  [AddSpatialPropertiesListener] objectID=85
default	12:53:35.905704-0500	VoiceOver	           AQMEIO_HAL.cpp:2240  aqmeio@0x706a36a18: [AddSpatialPropertiesListener] Installed listener 0x7077b2480
default	12:53:36.056202-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:53:36.056263-0500	VoiceOver	CoreText note: Set a breakpoint on CTFontLogSystemFontNameRequest to debug.
default	12:53:36.120266-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:53:36.161642-0500	VoiceOver	          AQMixEngine.cpp:733   AQMEDevice (0x706ad5bd8) has neither a defaultOutStreamClient nor a defaultInStreamClient
default	12:53:36.163606-0500	VoiceOver	EnhanceDialogueProcessor.cpp:226   EnhanceDialogueProcessor() - Product does not support Enhance Dialogue
default	12:53:36.163686-0500	VoiceOver	EnhanceDialogueProcessor.cpp:226   EnhanceDialogueProcessor() - Product does not support Enhance Dialogue
default	12:53:36.163908-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708053600, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:53:36.167890-0500	VoiceOver	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	12:53:36.168730-0500	VoiceOver	[0x707d6e080] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	12:53:36.168843-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x7074da800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	12:53:36.168878-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x7074da800:
default	12:53:36.168931-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	12:53:36.168940-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	12:53:36.169006-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	12:53:36.171180-0500	VoiceOver	       LoudnessManager.mm:1257  GetHardwarePlatformKey: found acoustic ID: 37
default	12:53:36.171195-0500	VoiceOver	       LoudnessManager.mm:1387  GetHardwarePlatformKey: GetHardwarePlatformKey(): hardware platform key is Mac
default	12:53:36.171853-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	12:53:36.171878-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	12:53:36.173120-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f500f","name":"VoiceOver(61431)"}, "details":{"PID":61431,"session_type":"Primary"} }
default	12:53:36.173242-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] VoiceOver","pid":61431}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f500f, sessionType: 'prim', isRecording: false }, 
]
default	12:53:36.174109-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 61431, name = VoiceOver
default	12:53:36.174799-0500	VoiceOver	    SessionCore_Create.mm:99    Created session 0x706385740 with ID: 0x1f500f
error	12:53:36.175857-0500	VoiceOver	Reporter disconnected. { function=sendMessage, reporterID=263844135960578 }
default	12:53:36.175890-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:53:36.179567-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:53:36.184928-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:53:36.186929-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:53:36.189130-0500	VoiceOver	SpatializationManager.cpp:1418  Loaded preset file /System/Library/Audio/Tunings/AID37/AU/aid37-aumx-3dem-appl.aupreset
default	12:53:36.189924-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:53:36.190717-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:53:36.190762-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:53:36.190864-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:53:36.191520-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:53:36.192941-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f500f","name":"VoiceOver(61431)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	12:53:36.193053-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	12:53:36.193106-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:53:36.193162-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f500f, VoiceOver(61431), 'prim'', AudioCategory changed to 'MediaPlayback'
default	12:53:36.193226-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	12:53:36.193243-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 16 starting playing
default	12:53:36.193394-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:53:36.193653-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:53:36.193675-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:53:36.193759-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	12:53:36.193849-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'}
default	12:53:36.193702-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:53:36.191759-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	12:53:36.194236-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	12:53:36.194289-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:53:36.194395-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:53:36.194520-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x89380001 category Not set
default	12:53:36.194009-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	12:53:36.194080-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f500f to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":61431}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f500f, sessionType: 'prim', isRecording: false }, 
]
default	12:53:36.194905-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:53:36.194943-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:53:36.196222-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:53:36.196257-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:53:36.196114-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:53:36.196271-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 1
default	12:53:36.196281-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	12:53:36.196293-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.apple.VoiceOver
default	12:53:36.196343-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:53:36.205075-0500	VoiceOver	           AQMEIO_HAL.cpp:1922  user headtracking mode for app com.apple.VoiceOver: 1
default	12:53:36.206043-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	12:53:36.215615-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:53:36.215768-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:53:36.220715-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873749 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:53:36.221697-0500	VoiceOver	HIDAnalytics Set Value Send event com.apple.iokituser.hid.iohidpostevent
default	12:53:36.221748-0500	VoiceOver	HIDAnalytics Timer Send event com.apple.iokituser.hid.iohidpostevent
default	12:53:36.221762-0500	VoiceOver	HIDAnalytics Unregister Send event com.apple.iokituser.hid.iohidpostevent
default	12:53:36.226761-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873755 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:53:36.264851-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070ffe10, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:53:36.264911-0500	VoiceOver	AudioConverter -> 0x7070ffe10: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:53:36.264961-0500	VoiceOver	AudioConverter -> 0x7070ffe10: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:53:36.285356-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7071025b0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:53:36.285397-0500	VoiceOver	AudioConverter -> 0x7071025b0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:53:36.285412-0500	VoiceOver	AudioConverter -> 0x7071025b0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:53:36.298679-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:53:36.299750-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:53:36.300772-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:53:36.300231-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:53:36.301104-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:53:36.301249-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:53:36.301408-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:53:36.301738-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:53:36.301855-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	12:53:36.301901-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:53:36.302283-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:53:36.302337-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:53:36.321788-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 7564 ioTS st: 7564 ht: 32384.784928
default	12:53:36.519201-0500	ControlCenter	AudioController: spatial audio update: process: 61431, bundleID: com.apple.VoiceOver
error	12:53:36.803092-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:53:36.823407-0500	VoiceOver	No list of permitted front apps returned
default	12:53:38.035002-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 61449
default	12:53:38.035710-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 61449
default	12:53:39.563793-0500	VoiceOver	LSExceptions shared instance invalidated for timeout.
default	12:53:39.930605-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:53:40.326275-0500	VoiceOver	[0x707d6d400] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:53:40.326451-0500	VoiceOver	[0x707d6d400] invalidated after the last release of the connection object
default	12:53:41.783308-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 61470
default	12:53:41.783885-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 61470
default	12:53:41.907036-0500	VoiceOver	[0x707d6d400] activating connection: mach=true listener=false peer=false name=mul-xpc (Apple)_OpenStep
default	12:53:41.907403-0500	VoiceOver	[0x707d6de00] activating connection: mach=true listener=false peer=false name=com.apple.naturallanguaged
fault	12:53:42.052931-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:53:42.054960-0500	VoiceOver	No list of permitted front apps returned
default	12:53:42.156598-0500	VoiceOver	No list of permitted front apps returned
default	12:53:42.160289-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	12:53:42.167706-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:53:42.167795-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:53:42.182616-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474873755 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:53:42.183737-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873787 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:53:42.226562-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:53:42.226785-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:53:42.227111-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:53:42.227229-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:53:42.227389-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:53:42.227411-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:53:42.227441-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:53:42.227613-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:53:42.227675-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	12:53:42.227705-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:53:42.227890-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:53:42.227905-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:53:42.241738-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 138100 ioTS st: 138100 ht: 32390.704928
error	12:53:42.271101-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:53:42.786787-0500	VoiceOver	No list of permitted front apps returned
default	12:53:42.787043-0500	VoiceOver	No list of permitted front apps returned
default	12:53:42.787106-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:53:42.788152-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:53:42.788572-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:53:42.930499-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:53:42.931742-0500	VoiceOver	No list of permitted front apps returned
default	12:53:42.931943-0500	VoiceOver	No list of permitted front apps returned
default	12:53:42.933392-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:53:42.933573-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:53:42.936798-0500	VoiceOver	[0x707d6cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:53:42.936878-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:53:42.938605-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708163390, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:53:42.938688-0500	VoiceOver	AudioConverter -> 0x708163390: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:53:42.938719-0500	VoiceOver	AudioConverter -> 0x708163390: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:53:42.940198-0500	VoiceOver	No list of permitted front apps returned
default	12:53:42.945137-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:53:42.949909-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:53:42.951890-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7081634e0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:53:42.951922-0500	VoiceOver	AudioConverter -> 0x7081634e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:53:42.951936-0500	VoiceOver	AudioConverter -> 0x7081634e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:53:42.957206-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	12:53:42.967875-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:53:42.967925-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:53:42.972059-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873787 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:53:42.972419-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873788 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:53:43.027254-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:53:43.027656-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:53:43.028012-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:53:43.028012-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:53:43.028245-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:53:43.028275-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:53:43.028316-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:53:43.028511-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:53:43.028580-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	12:53:43.028610-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:53:43.028852-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:53:43.028868-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:53:43.041743-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 155740 ioTS st: 155740 ht: 32391.504928
error	12:53:43.200692-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:53:43.928792-0500	VoiceOver	No list of permitted front apps returned
fault	12:53:43.930083-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:53:43.969841-0500	VoiceOver	No list of permitted front apps returned
default	12:53:43.971348-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:53:43.972044-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:53:43.972167-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:53:44.000164-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	12:53:44.002887-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:53:44.002980-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:53:44.017231-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873788 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:53:44.017633-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474873790 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:53:44.030622-0500	VoiceOver	No list of permitted front apps returned
default	12:53:44.052417-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:53:44.052898-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:53:44.053158-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:53:44.053265-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:53:44.053467-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:53:44.053495-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:53:44.053539-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:53:44.053710-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:53:44.053776-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	12:53:44.053819-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:53:44.054037-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:53:44.054052-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	12:53:44.079602-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:53:44.125009-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:44.125041-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:53:44.126090-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
fault	12:53:44.125929-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:53:44.126111-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:53:44.126118-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:53:44.130762-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:53:44.134402-0500	runningboardd	Invalidating assertion 404-61431-22934 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:53:44.130808-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:53:44.134356-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:53:44.134418-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:53:44.134608-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:44.134651-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:53:44.134699-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:53:44.141359-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:44.141450-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:44.141602-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:44.145930-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:53:44.145982-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:53:44.145989-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:53:44.146296-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:53:44.146310-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:53:44.146332-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:53:44.146470-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:53:44.146601-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:53:44.149565-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:53:44.149683-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
error	12:53:44.149718-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	12:53:44.149771-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:53:44.149806-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:53:44.149786-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-22964 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:53:44.150085-0500	runningboardd	Assertion 404-61431-22964 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:53:44.149837-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:44.149864-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:53:44.150331-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:44.150379-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:44.153897-0500	runningboardd	Invalidating assertion 404-61431-22964 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:53:44.151659-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'}, secondSession={clientName:'sid:0x1f5010, Nexy(61449), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	12:53:44.150433-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:44.150643-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:53:44.150681-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:53:44.198096-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:53:44.198931-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:53:44.199668-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:53:44.200464-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:53:44.197782-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	12:53:44.197834-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	12:53:44.215992-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x7074da800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	12:53:44.216425-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:53:44.218056-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:53:44.218278-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:53:44.218308-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:53:44.218346-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:53:44.218555-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:53:44.218620-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:53:44.218652-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:53:44.218950-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:53:44.218985-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:53:44.319447-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'}, secondSession={clientName:'sid:0x1f5010, Nexy(61449), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	12:53:44.321436-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:53:44.321528-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:53:44.321613-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:53:44.321654-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
fault	12:53:44.765225-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:53:44.765729-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:53:44.768017-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:53:44.768703-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:53:45.145442-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474873790 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:53:45.351979-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:53:45.744906-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:53:45.765291-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:53:45.765423-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:53:45.933562-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:53:46.895580-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:46.897345-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
default	12:53:46.897394-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:53:46.897411-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:53:46.899101-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:53:46.899199-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:53:46.902631-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:53:46.902652-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:53:46.900510-0500	runningboardd	Invalidating assertion 404-61431-22968 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:53:46.902771-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:46.902792-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:53:46.902801-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:53:46.900618-0500	runningboardd	Invalidating assertion 404-337-22928 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.powerd>:337]
default	12:53:46.904385-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:53:46.906760-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:46.906796-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:46.908390-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:53:46.908412-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:53:46.908427-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:53:46.908437-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:53:46.908446-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:53:46.908694-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:46.912961-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-22971 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:53:46.913106-0500	runningboardd	Assertion 404-61431-22971 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:53:46.910810-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:53:46.910845-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:53:46.910854-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:53:46.914694-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:53:46.914879-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
error	12:53:46.914890-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	12:53:46.914944-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:53:46.914973-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:53:46.915014-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:53:46.915014-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:46.916101-0500	runningboardd	Invalidating assertion 404-61431-22971 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:53:46.915369-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:46.915388-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:46.915438-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:46.915560-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:53:46.915591-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:53:46.925523-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:53:46.925559-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:53:46.925676-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:46.927664-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:46.927937-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:53:46.927953-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:53:46.927993-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:53:46.928003-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:53:46.928013-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:53:46.928019-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:53:46.928025-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
error	12:53:46.928766-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	12:53:46.928833-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:53:46.928894-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:53:46.929419-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-22972 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:53:46.928975-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:53:46.929662-0500	runningboardd	Assertion 404-61431-22972 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:53:46.929049-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:53:46.929109-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:53:46.929155-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:53:46.929230-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:53:46.930501-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:53:46.930658-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:53:46.931070-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:53:46.931108-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:53:46.931302-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:53:46.931473-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:53:46.931544-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:46.931786-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:53:46.931879-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
error	12:53:46.932926-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	12:53:46.932940-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7081614d0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:53:46.932970-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:53:46.933005-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:53:46.933159-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:53:46.934197-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:53:46.934787-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:53:46.934861-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:53:46.934925-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:53:46.935178-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:53:46.935224-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:53:46.935497-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:53:46.935256-0500	runningboardd	Invalidating assertion 404-61431-22972 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:53:46.935580-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:53:46.935651-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:53:46.935676-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:53:46.935873-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:46.936022-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:53:46.936333-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:53:46.936636-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:53:46.937628-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-22973 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:53:46.938066-0500	runningboardd	Assertion 404-61431-22973 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:53:46.938668-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813d860, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:53:46.938760-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:53:46.938901-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:53:46.944072-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:53:46.944430-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:53:46.944447-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:53:46.944453-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:53:46.942617-0500	runningboardd	Invalidating assertion 404-61431-22973 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:53:46.944470-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x706a36a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	12:53:46.944478-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x706a36a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	12:53:46.944555-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:46.944602-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:53:47.580960-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:53:47.627276-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2505 called from <private>
default	12:53:47.627784-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x7074da800:
default	12:53:47.627860-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	12:53:47.627867-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	12:53:47.627887-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	12:53:47.627913-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	12:53:47.627934-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	12:53:47.628303-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x7074da800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	12:53:47.847585-0500	VoiceOver	aqmeio@0x706a36a18 Stop id=85
default	12:53:47.847604-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:53:47.848377-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:53:48.930551-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:53:51.623646-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 61473
default	12:53:51.935128-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:53:54.930560-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:53:56.717489-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:53:56.717991-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f500f","name":"VoiceOver(61431)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	12:53:56.718105-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 16 stopping playing
default	12:53:56.718178-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	12:53:56.718219-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:53:56.718285-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:53:56.718388-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f500f to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":61431}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f500f, sessionType: 'prim', isRecording: false }, 
]
default	12:53:56.718580-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	12:53:56.718590-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:53:56.718591-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:53:56.718758-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:53:56.718813-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:53:56.718835-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 0
default	12:53:56.721493-0500	runningboardd	Invalidating assertion 404-61431-22974 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:53:56.721594-0500	runningboardd	Invalidating assertion 404-337-22975 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.powerd>:337]
default	12:53:56.822477-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:53:56.822489-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:53:56.822499-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:53:56.822518-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:53:56.822530-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:53:56.826292-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:53:59.528939-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:59.528985-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:53:59.528995-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:53:59.530977-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
default	12:53:59.531021-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:53:59.531038-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:53:59.543514-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:53:59.543534-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:53:59.544656-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:59.544677-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:53:59.544683-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:53:59.546083-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:59.546420-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:59.546516-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:59.546694-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:59.546904-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:53:59.546997-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:53:59.549253-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:53:59.549575-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:53:59.549801-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:53:59.563286-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:53:59.563309-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:53:59.565521-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 3 3, id:2505 called from <private>
default	12:53:59.565546-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 4 4, id:2505 called from <private>
default	12:53:59.565659-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:59.571422-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:59.572063-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 4 4 id:2505 called from <private>
default	12:53:59.572076-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 3 3 id:2505 called from <private>
default	12:53:59.572199-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:53:59.576145-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:53:59.576318-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:53:59.576328-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:53:59.576356-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:53:59.576365-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:53:59.576374-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:53:59.576380-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:53:59.576389-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:53:59.576423-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:53:59.576467-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:53:59.576530-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:53:59.576565-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:53:59.576704-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:53:59.576773-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:53:59.576833-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:53:59.576922-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:53:59.576957-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:53:59.577214-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:53:59.577267-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:53:59.577454-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:53:59.577560-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	12:53:59.577585-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:53:59.577702-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:53:59.577954-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	12:53:59.578093-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:53:59.578222-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:53:59.581701-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708160f30, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:53:59.581749-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:53:59.582271-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:53:59.582283-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:53:59.582288-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:53:59.582700-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:53:59.582711-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:53:59.582942-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	12:53:59.582953-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:53:59.582962-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	12:53:59.582983-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:53:59.583024-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:53:59.583703-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708160f30, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:53:59.583753-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:53:59.583975-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:53:59.584018-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:53:59.584064-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:53:59.584114-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x706a36a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	12:53:59.584151-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x706a36a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	12:53:59.584965-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7081610e0, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:53:59.585321-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x7074da800:
default	12:53:59.585460-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	12:53:59.585500-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	12:53:59.585556-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	12:53:59.585624-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	12:53:59.587690-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x7074da800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	12:54:00.124622-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 61476
default	12:54:00.125046-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 61476
default	12:54:01.186675-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7081636f0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:54:01.186707-0500	VoiceOver	AudioConverter -> 0x7081636f0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:54:01.186723-0500	VoiceOver	AudioConverter -> 0x7081636f0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:54:01.194001-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-22988 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:54:01.194120-0500	runningboardd	Assertion 404-61431-22988 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:54:01.194761-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-22989 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:54:01.194766-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:54:01.194832-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:54:01.194880-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:54:01.194860-0500	runningboardd	Assertion 404-337-22989 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:54:01.195003-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:54:01.195044-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:54:01.191658-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:54:01.195839-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f500f","name":"VoiceOver(61431)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	12:54:01.196017-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	12:54:01.196032-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 16 starting playing
default	12:54:01.196105-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:54:01.196192-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	12:54:01.196305-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'}
default	12:54:01.196541-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	12:54:01.196357-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	12:54:01.196553-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:54:01.196465-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f500f to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":61431}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f500f, sessionType: 'prim', isRecording: false }, 
]
default	12:54:01.196949-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x89380001 category Not set
default	12:54:01.197252-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	12:54:01.198143-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:54:01.198044-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:54:01.198791-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:54:01.198810-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 1
default	12:54:01.198818-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	12:54:01.198829-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.apple.VoiceOver
default	12:54:01.198884-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:54:01.201435-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:54:01.201446-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:54:01.201457-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:54:01.201518-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:54:01.201551-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:54:01.202203-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:54:01.205280-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:54:01.213315-0500	VoiceOver	No list of permitted front apps returned
default	12:54:01.214968-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:54:01.215548-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:54:01.215637-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:54:01.222101-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:01.222213-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:54:01.264774-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:01.264960-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:54:01.265764-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7074a50e0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:54:01.265790-0500	VoiceOver	AudioConverter -> 0x7074a50e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:54:01.265803-0500	VoiceOver	AudioConverter -> 0x7074a50e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:54:01.276798-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813d5f0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:54:01.276822-0500	VoiceOver	AudioConverter -> 0x70813d5f0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:54:01.276834-0500	VoiceOver	AudioConverter -> 0x70813d5f0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:54:01.285583-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874276 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:54:01.339468-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:54:01.339970-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:01.340069-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:54:01.340198-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:01.340257-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:01.340281-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:01.340308-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:54:01.340451-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:01.340509-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:01.340555-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:01.340764-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:01.340778-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:01.369185-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 560064 ioTS st: 560064 ht: 32409.841646
error	12:54:01.585241-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:01.721698-0500	VoiceOver	No list of permitted front apps returned
fault	12:54:01.728893-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:01.823062-0500	VoiceOver	No list of permitted front apps returned
fault	12:54:01.909545-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:01.917679-0500	VoiceOver	No list of permitted front apps returned
fault	12:54:01.920739-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:01.950268-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:54:01.950406-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:54:01.986042-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874278 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:54:02.034538-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:54:02.034806-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:54:02.035118-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:02.035175-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:54:02.035386-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:02.035409-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:02.035444-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:54:02.035574-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:02.035638-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:02.035664-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:02.035872-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:02.035885-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:02.069139-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 575499 ioTS st: 575499 ht: 32410.541646
error	12:54:02.071639-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:02.173793-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:54:02.173810-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2505 called from <private>
default	12:54:02.173840-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:54:02.173949-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
fault	12:54:02.174474-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:02.173968-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:54:02.173974-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:54:02.176312-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:54:02.176453-0500	runningboardd	Invalidating assertion 404-61431-22988 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:54:02.185313-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:54:02.185332-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:54:02.185339-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:54:02.187294-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:54:02.187302-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:54:02.199347-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:54:02.199357-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:54:02.199460-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:54:02.206388-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:54:02.206559-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:54:02.206569-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:54:02.206656-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:54:02.210832-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:54:02.211030-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:54:02.211040-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:54:02.211383-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:54:02.211661-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:54:02.211782-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:54:02.211874-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:54:02.211884-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:54:02.212096-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:54:02.212306-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:54:02.212523-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:54:02.212747-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:54:02.213010-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:54:02.213231-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:54:02.213485-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:54:02.213670-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:54:02.214709-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:54:02.214920-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:54:02.599859-0500	VoiceOver	No list of permitted front apps returned
default	12:54:02.600024-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:54:02.600053-0500	VoiceOver	No list of permitted front apps returned
default	12:54:02.600439-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:54:02.600523-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:54:02.791043-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61482
default	12:54:02.792130-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61482
default	12:54:02.835280-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61483
default	12:54:02.910789-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2505 called from <private>
default	12:54:02.910810-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2505 called from <private>
fault	12:54:02.911307-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:02.912184-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:54:02.912194-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:54:02.913830-0500	runningboardd	Invalidating assertion 404-61431-23003 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:54:02.913990-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-23015 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:54:02.914058-0500	runningboardd	Assertion 404-61431-23015 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:54:02.924722-0500	VoiceOver	No list of permitted front apps returned
default	12:54:03.478771-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:54:03.519501-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2505 called from <private>
default	12:54:03.519529-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2505 called from <private>
default	12:54:03.519658-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:54:03.519659-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
fault	12:54:03.520040-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:03.521168-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:54:03.521189-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:54:03.521331-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:03.521478-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:54:03.521507-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:54:03.521541-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:54:03.521553-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:54:03.521907-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:54:03.522053-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:54:03.522166-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:54:03.522141-0500	runningboardd	Invalidating assertion 404-61431-23015 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:54:03.522335-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-23021 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:54:03.522402-0500	runningboardd	Assertion 404-61431-23021 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:54:03.522195-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:54:03.522233-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:54:03.522279-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:54:03.522325-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
error	12:54:03.530062-0500	VoiceOver	               AQMEIO.cpp:201   timed out after 0.010s (943 943); suspension count=0 (IOSuspensions: , , , , , , , , , , , , ) (maybe stale)
default	12:54:03.530317-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:54:03.530365-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:54:03.534851-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874278 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:54:03.535324-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874441 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:54:03.541348-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	12:54:04.085100-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2505 called from <private>
default	12:54:04.085138-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2505 called from <private>
default	12:54:04.087308-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:54:04.087323-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:54:04.089055-0500	runningboardd	Invalidating assertion 404-61431-23021 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:54:04.089340-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-23024 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:54:04.089472-0500	runningboardd	Assertion 404-61431-23024 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:54:04.088704-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708163e10, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:54:04.088079-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:54:04.088768-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:54:04.090148-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:54:04.090503-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:04.090579-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:04.090724-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	12:54:04.098310-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:04.640821-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:54:04.641143-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:04.641310-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:04.641364-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:04.641428-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:04.641789-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:04.641823-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	12:54:04.651000-0500	VoiceOver	1C-77-54-18-C8-A3:output: Abandoning I/O cycle because reconfig pending
error	12:54:04.660978-0500	VoiceOver	1C-77-54-18-C8-A3:output: Abandoning I/O cycle because reconfig pending
error	12:54:04.660986-0500	VoiceOver	 MEDeviceStreamClient.cpp:342   Client(0x7074da800) did not see 1 I/O cycles; suspension(s) blocking starting
default	12:54:04.661159-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:04.661123-0500	VoiceOver	aqmeio@0x706a36a18 Stop id=85
default	12:54:04.664278-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	12:54:04.664356-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	12:54:04.664416-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	12:54:04.683178-0500	VoiceOver	          AQMixEngine.cpp:1491  ->AQMixEngine_Base(0x706ad5b80)::AddRunningClient <AudioQueueObject@0x7074da800; ; [61431]; play>, retry count 1
fault	12:54:04.685173-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:04.683811-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x7074da800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	12:54:04.684413-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:54:04.686407-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:54:04.686736-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:04.686814-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:04.686974-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:54:04.687668-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:04.687908-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:04.688254-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:04.688832-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:04.688916-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:04.881899-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61498
default	12:54:04.882850-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61498
default	12:54:05.214124-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61499
default	12:54:05.262999-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61501
default	12:54:05.439486-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61502
default	12:54:05.442034-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61502
default	12:54:05.983629-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: c0000000c pid: 61494
default	12:54:05.984699-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1600000012 pid: 61494
default	12:54:06.298106-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474874441 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:54:06.299565-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:54:06.913841-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:07.214395-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7071003f0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:54:07.214420-0500	VoiceOver	AudioConverter -> 0x7071003f0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:54:07.214431-0500	VoiceOver	AudioConverter -> 0x7071003f0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:54:07.310210-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:07.310359-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:54:07.333817-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:54:07.356131-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:07.356312-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:54:07.416204-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 705
default	12:54:07.415607-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:07.415709-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
fault	12:54:07.415375-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:07.416043-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:07.416125-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:07.430978-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 693505 ioTS st: 693505 ht: 32415.893359
error	12:54:07.661655-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:08.782075-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61517
default	12:54:09.427961-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:09.428070-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:54:09.470716-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:54:09.470966-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:09.471084-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:54:09.471373-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:54:09.471415-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:54:09.472172-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:54:09.479480-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474874449 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	12:54:09.480091-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874465 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	12:54:09.490273-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:09.490376-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:54:09.511436-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:54:09.511974-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:09.512021-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:54:09.512216-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:09.512243-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	12:54:09.512223-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:09.512271-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:54:09.512444-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:09.512495-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:09.512522-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:09.512721-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:09.512736-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:09.530898-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 739810 ioTS st: 739810 ht: 32417.993359
error	12:54:09.560895-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:09.930497-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:10.971599-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:54:10.981642-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:54:10.981707-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:54:10.983342-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874465 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	12:54:11.089694-0500	VoiceOver	No list of permitted front apps returned
default	12:54:11.090187-0500	VoiceOver	No list of permitted front apps returned
default	12:54:11.093039-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:11.093224-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:54:11.108357-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:11.108567-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:54:11.121997-0500	VoiceOver	[0x707d6da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:11.122237-0500	VoiceOver	[0x707d6da40] invalidated after the last release of the connection object
default	12:54:11.126637-0500	VoiceOver	[0x707d6da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:11.126821-0500	VoiceOver	[0x707d6da40] invalidated after the last release of the connection object
default	12:54:11.129661-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874467 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	12:54:11.136611-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70816e010, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:54:11.136640-0500	VoiceOver	AudioConverter -> 0x70816e010: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:54:11.136667-0500	VoiceOver	AudioConverter -> 0x70816e010: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:54:11.170360-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:54:11.171166-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:54:11.171219-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:11.171370-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:11.171397-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:11.171438-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	12:54:11.171484-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:11.171617-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:11.171683-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:11.171716-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:11.171938-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:11.171958-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:11.181056-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:11.181231-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:54:11.190917-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 776414 ioTS st: 776414 ht: 32419.653359
default	12:54:11.217895-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:54:11.221374-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:54:11.231245-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:54:11.231281-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:54:11.232745-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874467 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	12:54:11.234385-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874468 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	12:54:11.268114-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:54:11.268474-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:54:11.268763-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:11.268881-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:54:11.269078-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:11.269102-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:11.269134-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:54:11.269285-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:11.269344-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:11.269371-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:11.269565-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:11.269581-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:11.280868-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 778399 ioTS st: 778399 ht: 32419.743359
error	12:54:11.309262-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:12.532263-0500	VoiceOver	No list of permitted front apps returned
default	12:54:12.532702-0500	VoiceOver	No list of permitted front apps returned
default	12:54:12.563199-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:12.563513-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:54:12.578351-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70816dd40, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:54:12.578392-0500	VoiceOver	AudioConverter -> 0x70816dd40: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:54:12.578416-0500	VoiceOver	AudioConverter -> 0x70816dd40: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:54:12.598077-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:54:12.603261-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x707103c00, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:54:12.603313-0500	VoiceOver	AudioConverter -> 0x707103c00: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:54:12.603328-0500	VoiceOver	AudioConverter -> 0x707103c00: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:54:12.619927-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:54:12.622031-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:54:12.622117-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:54:12.624634-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874468 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:54:12.625444-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874469 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:54:12.650638-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:54:12.651429-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:12.651660-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:54:12.651679-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:12.651917-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:12.651946-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:12.651989-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:54:12.652178-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:12.652261-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:12.652293-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:12.652520-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:12.652538-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:12.670977-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 809049 ioTS st: 809049 ht: 32421.133359
error	12:54:12.745999-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:12.930488-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
fault	12:54:14.537931-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:14.535819-0500	VoiceOver	No list of permitted front apps returned
default	12:54:14.581957-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:14.582042-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:54:14.644210-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:54:14.644690-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:54:14.644787-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:54:14.661060-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:14.661288-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:54:14.677607-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:14.677783-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:54:14.701715-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:54:14.701797-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:54:14.743647-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:54:14.744163-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:54:14.744489-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:14.744534-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:54:14.744767-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:14.744802-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:14.744849-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:54:14.745017-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:14.745090-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:14.745126-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:14.745347-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:14.745366-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:14.760906-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 855134 ioTS st: 855134 ht: 32423.223359
error	12:54:14.847106-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:15.930471-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:18.913780-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:19.402502-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474874472 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:54:19.615104-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:54:19.932744-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	12:54:19.932442-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874473 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	12:54:20.129940-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:21.935448-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:24.933325-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:27.930619-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:28.207699-0500	runningboardd	Resolved pid 61445 to [xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:61445:61445]
default	12:54:28.208126-0500	runningboardd	[xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:61445:61445] is not RunningBoard jetsam managed.
default	12:54:28.208143-0500	runningboardd	[xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:61445:61445] This process will not be managed.
default	12:54:28.210021-0500	runningboardd	Resolved pid 61444 to [xpcservice<com.apple.audio.SandboxHelper([xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441])(501)>{vt hash: 0}{definition:com.apple.audio.SandboxHelper[standard][client]}:61444:61444]
default	12:54:28.210683-0500	runningboardd	[xpcservice<com.apple.audio.SandboxHelper([xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441])(501)>{vt hash: 0}{definition:com.apple.audio.SandboxHelper[standard][client]}:61444:61444] is not RunningBoard jetsam managed.
default	12:54:28.210709-0500	runningboardd	[xpcservice<com.apple.audio.SandboxHelper([xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441])(501)>{vt hash: 0}{definition:com.apple.audio.SandboxHelper[standard][client]}:61444:61444] This process will not be managed.
default	12:54:28.215610-0500	runningboardd	Resolved pid 61440 to [xpcservice<com.apple.audio.ComponentTagHelper([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.audio.ComponentTagHelper[standard][client]}:61440:61440]
default	12:54:28.216604-0500	runningboardd	[xpcservice<com.apple.audio.ComponentTagHelper([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.audio.ComponentTagHelper[standard][client]}:61440:61440] is not RunningBoard jetsam managed.
default	12:54:28.216633-0500	runningboardd	[xpcservice<com.apple.audio.ComponentTagHelper([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.audio.ComponentTagHelper[standard][client]}:61440:61440] This process will not be managed.
default	12:54:28.285068-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:28.285237-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:54:30.485505-0500	VoiceOver	No list of permitted front apps returned
fault	12:54:30.489188-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:30.590765-0500	VoiceOver	No list of permitted front apps returned
default	12:54:30.592875-0500	VoiceOver	No list of permitted front apps returned
default	12:54:30.605784-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708164d80, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:54:30.605813-0500	VoiceOver	AudioConverter -> 0x708164d80: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:54:30.605823-0500	VoiceOver	AudioConverter -> 0x708164d80: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:54:30.610563-0500	VoiceOver	No list of permitted front apps returned
default	12:54:30.613040-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:54:30.613970-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:54:30.614059-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:54:30.639231-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:30.639372-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:54:30.675050-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:30.675164-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:54:30.676832-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708163ab0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:54:30.676855-0500	VoiceOver	AudioConverter -> 0x708163ab0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:54:30.676862-0500	VoiceOver	AudioConverter -> 0x708163ab0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:54:30.682528-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:54:30.685173-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:54:30.689387-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:54:30.691653-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:54:30.691688-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:54:30.694866-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:10  id:21474874473 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:54:30.695463-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874475 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:54:30.740149-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:54:30.740453-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:54:30.740700-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:30.740880-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:54:30.741286-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:30.741307-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:30.741336-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:54:30.741477-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:30.741530-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:30.741558-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:30.741750-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:30.741765-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:30.760868-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 1207935 ioTS st: 1207935 ht: 32439.223359
error	12:54:30.927226-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:30.930351-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:31.912101-0500	VoiceOver	No list of permitted front apps returned
fault	12:54:31.917678-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:31.939925-0500	VoiceOver	No list of permitted front apps returned
default	12:54:31.959250-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:54:31.960031-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:54:31.960154-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:54:31.977673-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:31.977832-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:54:31.991554-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:31.991743-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:54:32.009591-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:54:32.011725-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:54:32.011805-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:54:32.013742-0500	VoiceOver	No list of permitted front apps returned
default	12:54:32.029582-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874475 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:54:32.083293-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:54:32.083578-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:54:32.083838-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:32.083971-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:54:32.084161-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:32.084182-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:32.084209-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:54:32.084352-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:32.084407-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:32.084431-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:32.084654-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:32.084669-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:32.100869-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 1237483 ioTS st: 1237483 ht: 32440.563359
error	12:54:32.164705-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:33.930362-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:36.742311-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474874477 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:54:36.930381-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:36.953850-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:54:37.273607-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874488 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:54:37.283902-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	12:54:37.456547-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:39.149446-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'}, secondSession={clientName:'sid:0x1f5004, Browser Helper(4811), 'prim'', displayID:'company.thebrowser.browser.helper'} but will use session={clientName:'(null)', displayID:'(null)'}
default	12:54:39.151890-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:54:39.152061-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:54:39.323896-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:54:39.681900-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 61525
default	12:54:39.682051-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 61526
default	12:54:40.525976-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	12:54:40.525999-0500	audioaccessoryd	Updating local audio category 301 -> 201 app com.apple.VoiceOver
default	12:54:40.526103-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:54:42.040882-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:54:42.041666-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:42.930275-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 2
default	12:54:45.404041-0500	runningboardd	Periodic Run States <RBProcessState| identity:osservice<com.apple.VoiceOver(501)> role:UserInteractive gpuRole:None coalitionLevel:100 explicitJetsamBand:100 memoryLimit:Inactive(Soft) flags:60 guaranteedRunning:NO legacyFinishTaskReason:0 inheritances:<RBMutableInheritanceCollection| inheritancesByEnvironment:{
	
	}> primitiveAssertions:[
	<RBSProcessAssertionInfo| type:2 reason:20246 name:"Domain" domain:"com.apple.launchservicesd:RoleUserInteractive" expl:"uielement:61431">,
	<RBSProcessAssertionInfo| type:2 reason:0 name:"Domain" domain:"com.apple.appnap:AppDrawing" expl:"AppDrawing">,
	<RBSProcessAssertionInfo| type:2 reason:20242 name:"Domain" domain:"com.apple.appnap:AppVisible" expl:"AppVisible">,
	<RBSProcessAssertionInfo| type:2 reason:20009 name:"Domain" domain:"com.apple.CoreAudio.HAL:AudioHAL" expl:"AudioHAL">,
	<RBSProcessAssertionInfo| type:2 reason:20244 name:"Domain" domain:"com.apple.appnap:PowerAssertion" expl:"App is holding power assertion">
	] endowments:[
	<RBSProcessEndowmentInfo| namespace:com.a<…>
default	12:54:45.407110-0500	runningboardd	Periodic Run States <RBProcessState| identity:xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]} role:UserInteractiveNonFocal gpuRole:Background coalitionLevel:0 explicitJetsamBand:100 memoryLimit:Inactive(Soft) flags:140 guaranteedRunning:NO legacyFinishTaskReason:0 legacyAssertions:[
	<RBSProcessAssertionInfo| type:3 reason:13 name:"Extension" domain:"(null)" expl:"com.apple.extension.session">
	]>
default	12:54:45.612715-0500	VoiceOver	No list of permitted front apps returned
fault	12:54:45.617831-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:45.744103-0500	VoiceOver	No list of permitted front apps returned
default	12:54:45.754551-0500	VoiceOver	No list of permitted front apps returned
default	12:54:45.771497-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:54:45.771905-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:45.776846-0500	VoiceOver	No list of permitted front apps returned
default	12:54:45.779676-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:54:45.780397-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:54:45.780549-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:54:45.784220-0500	VoiceOver	[0x707d6da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:45.784420-0500	VoiceOver	[0x707d6da40] invalidated after the last release of the connection object
default	12:54:45.811714-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:45.811861-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:54:45.819964-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:54:45.824134-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:54:45.828280-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:54:45.831458-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:54:45.831502-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:54:45.837464-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:08  id:21474874488 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:54:45.837862-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874497 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:54:45.894081-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:54:45.894372-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:54:45.894618-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:45.894752-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:54:45.894926-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:45.894947-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:45.894977-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:54:45.895136-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:45.895194-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:45.895220-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:45.895401-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:45.895418-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:54:45.910878-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 1541994 ioTS st: 1541994 ht: 32454.373359
default	12:54:45.930227-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 2
error	12:54:46.134829-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	12:54:47.317948-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:47.308568-0500	VoiceOver	No list of permitted front apps returned
default	12:54:47.340704-0500	VoiceOver	No list of permitted front apps returned
default	12:54:47.366342-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:54:47.367089-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:54:47.367300-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:54:47.377429-0500	VoiceOver	[0x707d6da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:47.377630-0500	VoiceOver	[0x707d6da40] invalidated after the last release of the connection object
default	12:54:47.386631-0500	VoiceOver	[0x707d6da40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:47.386791-0500	VoiceOver	[0x707d6da40] invalidated after the last release of the connection object
default	12:54:47.402256-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:54:47.410398-0500	VoiceOver	No list of permitted front apps returned
default	12:54:47.411722-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:54:47.411796-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:54:47.438981-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874497 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:54:47.439413-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874499 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:54:47.497368-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:54:47.497677-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:47.498007-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:54:47.497988-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:54:47.498191-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:54:47.498215-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:54:47.498245-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:54:47.498375-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:54:47.498434-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:54:47.498457-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:54:47.498661-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:47.498675-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	12:54:47.568773-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:48.913650-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 2
default	12:54:50.430510-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:54:50.430644-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:54:51.930263-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:52.152133-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474874499 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:54:52.365366-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:54:52.678780-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874500 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:54:52.688740-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	12:54:52.862634-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:54:54.200464-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:54.200695-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:54:54.930286-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:55.746447-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:55.746685-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:54:56.430895-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:54:56.431461-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:54:57.913619-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:54:59.610646-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:54:59.610872-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:00.376910-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:00.377027-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:00.620048-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:55:00.620402-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:00.930248-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:01.298510-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:01.298691-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:01.970535-0500	VoiceOver	No list of permitted front apps returned
fault	12:55:01.975399-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:02.071979-0500	VoiceOver	No list of permitted front apps returned
default	12:55:02.072978-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:02.073693-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:02.073817-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
fault	12:55:02.218271-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:02.221107-0500	VoiceOver	No list of permitted front apps returned
default	12:55:02.226597-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:02.227924-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
fault	12:55:02.232273-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:02.238871-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 61532
default	12:55:02.240144-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 61532
default	12:55:02.296286-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:02.361378-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:02.402920-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:02.403327-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:02.403846-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:02.403791-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:02.404114-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:02.404146-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:02.404191-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:02.404381-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:02.404454-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:02.404496-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:02.404830-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:02.404854-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:02.420964-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 1906041 ioTS st: 1906041 ht: 32470.883359
error	12:55:02.513914-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:03.174146-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61535
default	12:55:03.178342-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61535
default	12:55:03.214946-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61536
default	12:55:03.216640-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61536
default	12:55:04.017390-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:04.829233-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61543
default	12:55:04.838231-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61543
default	12:55:05.139605-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61545
default	12:55:05.144526-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61545
default	12:55:06.441690-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:06.441756-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:06.487562-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:06.488625-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:55:06.489065-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:06.488661-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:06.488960-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:06.489002-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:06.489052-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
error	12:55:06.568725-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:06.930300-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:08.390399-0500	VoiceOver	No list of permitted front apps returned
fault	12:55:08.398143-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:08.492001-0500	VoiceOver	No list of permitted front apps returned
default	12:55:08.495064-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:08.495420-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:08.495487-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:08.516506-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:08.516618-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:55:08.568887-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:08.569000-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:55:08.580543-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70815ddd0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:08.580563-0500	VoiceOver	AudioConverter -> 0x70815ddd0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:08.580571-0500	VoiceOver	AudioConverter -> 0x70815ddd0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:08.589092-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:08.601948-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:08.611366-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:08.611417-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:08.655476-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
error	12:55:08.789366-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:09.191464-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:09.191633-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:55:09.219482-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:09.219588-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:09.219861-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:55:09.221318-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:09.221698-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:09.221754-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:09.230526-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:09.230833-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:09.235719-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874516 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	12:55:09.236217-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874517 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	12:55:09.237262-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813c870, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:09.237287-0500	VoiceOver	AudioConverter -> 0x70813c870: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:09.237297-0500	VoiceOver	AudioConverter -> 0x70813c870: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:09.267810-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:09.268194-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:09.268455-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:09.268461-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:09.268656-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:09.268677-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:09.268708-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:09.268848-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:09.268908-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:09.268940-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:09.269135-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:09.269150-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:09.280952-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2057305 ioTS st: 2057305 ht: 32477.743359
error	12:55:09.312990-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:09.914410-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:10.848833-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:10.851933-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:10.851986-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:10.853580-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874517 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:10.920546-0500	VoiceOver	No list of permitted front apps returned
default	12:55:10.920746-0500	VoiceOver	No list of permitted front apps returned
default	12:55:10.921477-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:10.921577-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:55:10.932349-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:10.932473-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:10.942222-0500	VoiceOver	[0x707d6cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:10.942353-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:55:10.945633-0500	VoiceOver	[0x707d6cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:10.945734-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:55:10.947092-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874518 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:10.973218-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813db60, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:10.973241-0500	VoiceOver	AudioConverter -> 0x70813db60: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:10.973261-0500	VoiceOver	AudioConverter -> 0x70813db60: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:10.984765-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:10.985330-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:10.985371-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:10.985574-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:10.985582-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:10.985610-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:10.985640-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:10.985796-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:10.985857-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:10.985887-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:10.986113-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:10.986124-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:10.997387-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:10.997690-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:55:11.000947-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2095232 ioTS st: 2095232 ht: 32479.463359
default	12:55:11.008164-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:11.011286-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:11.011316-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:11.012943-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874518 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:11.013231-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874519 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	12:55:11.036662-0500	VoiceOver	     AudioQueueObject.cpp:5805  buffersCreatedAndDestroyed: aq@0x7074da800: error allocating buffer
error	12:55:11.038642-0500	VoiceOver	     AudioQueueObject.cpp:5818  buffersCreatedAndDestroyed: aq@0x7074da800: invalid buffer ID
default	12:55:11.044929-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:11.045176-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:55:11.045490-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:11.045587-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:11.045759-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:11.045783-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:11.045811-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:11.045943-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:11.046003-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:11.046027-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:11.046226-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:11.046241-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:11.060919-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2096556 ioTS st: 2096556 ht: 32479.523359
error	12:55:11.087579-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:12.127509-0500	VoiceOver	No list of permitted front apps returned
default	12:55:12.127897-0500	VoiceOver	No list of permitted front apps returned
default	12:55:12.152640-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:12.153006-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:55:12.163402-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813e8e0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:12.163460-0500	VoiceOver	AudioConverter -> 0x70813e8e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:12.163492-0500	VoiceOver	AudioConverter -> 0x70813e8e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:12.192873-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:12.212707-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:12.221719-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:12.221812-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:12.223763-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874519 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:12.225001-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874522 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:12.255611-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:12.256098-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:12.256552-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:12.256537-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:12.256895-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:12.256926-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:12.256977-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:12.257157-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:12.257221-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:12.257261-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:12.257572-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:12.257586-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:12.271022-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2123237 ioTS st: 2123237 ht: 32480.733359
error	12:55:12.342858-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:12.343097-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:12.343245-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:55:12.933185-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:13.371181-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:13.371314-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
fault	12:55:13.391911-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:13.450284-0500	VoiceOver	No list of permitted front apps returned
default	12:55:13.501791-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:13.501863-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:13.519737-0500	VoiceOver	No list of permitted front apps returned
default	12:55:13.552649-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:13.553118-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:55:13.553657-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:13.553736-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:13.554037-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:13.554069-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:13.554119-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:13.554325-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:13.554414-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:13.554452-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:13.554831-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:13.554857-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	12:55:13.665807-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:15.678394-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70815c630, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:15.678422-0500	VoiceOver	AudioConverter -> 0x70815c630: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:15.678437-0500	VoiceOver	AudioConverter -> 0x70815c630: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:15.930171-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:17.654220-0500	VoiceOver	No list of permitted front apps returned
fault	12:55:17.663088-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:17.687875-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:17.691865-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:17.691950-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:17.693537-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474874523 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:17.694353-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874526 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:17.723267-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:17.723862-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:17.724176-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:17.724185-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:17.724417-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:17.724461-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:17.724514-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:17.724689-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:17.724752-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:17.724792-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:17.725018-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:17.725040-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:17.741069-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2243852 ioTS st: 2243852 ht: 32486.203359
default	12:55:17.755134-0500	VoiceOver	No list of permitted front apps returned
error	12:55:17.791471-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	12:55:17.875025-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:17.883397-0500	VoiceOver	No list of permitted front apps returned
fault	12:55:17.888046-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:17.888108-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:17.890039-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:17.890186-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:17.893340-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 61551
default	12:55:17.893740-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 61551
default	12:55:17.929462-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874527 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:17.963510-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:17.963546-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:17.963586-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:17.963748-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:17.963807-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:17.963839-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:17.964087-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:17.964101-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:17.980958-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2249144 ioTS st: 2249144 ht: 32486.443359
error	12:55:18.034956-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:18.045557-0500	VoiceOver	[0x707d6e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:18.045707-0500	VoiceOver	[0x707d6e940] invalidated after the last release of the connection object
default	12:55:18.066222-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874528 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:18.106154-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:18.106611-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:18.106919-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:18.106957-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:18.107166-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:18.107194-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:18.107239-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:18.107413-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:18.107494-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:18.107534-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:18.107798-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:18.107817-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:18.120932-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2252231 ioTS st: 2252231 ht: 32486.583359
error	12:55:18.185705-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:18.609549-0500	VoiceOver	No list of permitted front apps returned
default	12:55:18.612209-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:18.612248-0500	VoiceOver	No list of permitted front apps returned
default	12:55:18.612843-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:18.612953-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:18.635423-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:18.641974-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:18.642086-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:18.649168-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874528 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:18.650552-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874529 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:18.672786-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:18.673122-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:18.673574-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:18.673820-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:18.673851-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	12:55:18.673839-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:18.673897-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:18.674089-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:18.674170-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:18.674211-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:18.674500-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:18.674520-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:18.691092-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2264800 ioTS st: 2264800 ht: 32487.153359
error	12:55:18.723434-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:18.755445-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61554
default	12:55:18.756550-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61554
default	12:55:18.930041-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:20.354747-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61559
default	12:55:20.422585-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:55:20.513627-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61561
default	12:55:20.791495-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:20.801265-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:20.801302-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:21.002193-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61563
default	12:55:21.746650-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e1050, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:21.746680-0500	VoiceOver	AudioConverter -> 0x7070e1050: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:21.746690-0500	VoiceOver	AudioConverter -> 0x7070e1050: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:21.806663-0500	VoiceOver	[0x707d6e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:21.807018-0500	VoiceOver	[0x707d6e940] invalidated after the last release of the connection object
default	12:55:21.813731-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708167450, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:21.813802-0500	VoiceOver	AudioConverter -> 0x708167450: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:21.813812-0500	VoiceOver	AudioConverter -> 0x708167450: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:21.821306-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:21.821423-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:21.821468-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:21.831763-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874530 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:21.832083-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	12:55:21.833399-0500	VoiceOver	[0x707d6e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:21.833498-0500	VoiceOver	[0x707d6e940] invalidated after the last release of the connection object
default	12:55:21.859767-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:21.860373-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:21.860426-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:21.860606-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:21.860652-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:21.860677-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:21.860711-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:21.860896-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:21.860956-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:21.860984-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:21.861289-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:21.861305-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:21.880927-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2335140 ioTS st: 2335140 ht: 32490.343359
default	12:55:21.930152-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
error	12:55:21.979063-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:22.160317-0500	VoiceOver	[0x707d6e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:22.160475-0500	VoiceOver	[0x707d6e940] invalidated after the last release of the connection object
default	12:55:22.173679-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x707104420, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:22.173706-0500	VoiceOver	AudioConverter -> 0x707104420: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:22.173744-0500	VoiceOver	AudioConverter -> 0x707104420: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:22.176600-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:22.181613-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:22.181659-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:22.192403-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874530 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:22.193325-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874531 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:22.194550-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x707104060, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:22.194581-0500	VoiceOver	AudioConverter -> 0x707104060: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:22.194597-0500	VoiceOver	AudioConverter -> 0x707104060: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:22.232990-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:22.233599-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:22.233985-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:22.234054-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:22.234224-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:22.234257-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:22.234304-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:22.234486-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:22.234551-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:22.234587-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:22.234827-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:22.234844-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:22.250981-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2343300 ioTS st: 2343300 ht: 32490.713359
error	12:55:22.282650-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:22.605375-0500	VoiceOver	No list of permitted front apps returned
default	12:55:22.605595-0500	VoiceOver	No list of permitted front apps returned
default	12:55:22.613297-0500	VoiceOver	[0x707d6e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:22.613485-0500	VoiceOver	[0x707d6e940] invalidated after the last release of the connection object
default	12:55:22.641484-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:22.648283-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:22.651576-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:22.651638-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:22.654639-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874531 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:22.655257-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874532 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:22.694948-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:22.695425-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:22.695842-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:22.695847-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:22.696069-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:22.696099-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:22.696157-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:22.696336-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:22.696408-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:22.696448-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:22.696680-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:22.696697-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:22.710997-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2353443 ioTS st: 2353443 ht: 32491.173359
default	12:55:22.734817-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:22.742894-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:22.751373-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:22.751403-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:22.754731-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874532 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:22.755454-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874533 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:22.790292-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:22.790559-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:55:22.790812-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:22.790903-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:22.791275-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:22.791295-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:22.791317-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:22.791457-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:22.791522-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:22.791548-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:22.791743-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:22.791758-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:22.810914-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2355648 ioTS st: 2355648 ht: 32491.273359
error	12:55:22.838236-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:23.435740-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61566
default	12:55:23.437361-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61566
default	12:55:24.039448-0500	VoiceOver	[0x707d6cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:24.039716-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:55:24.063558-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:24.063920-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:24.064109-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:55:24.066030-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:24.070959-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:24.071204-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:24.071854-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:24.071924-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:24.074917-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874533 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:24.075802-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874534 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:24.093349-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x707105230, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:24.093379-0500	VoiceOver	AudioConverter -> 0x707105230: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:24.093391-0500	VoiceOver	AudioConverter -> 0x707105230: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:24.107304-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:24.107878-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:24.108019-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:24.108117-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:24.108297-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:24.108321-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:24.108354-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:24.108530-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:24.108606-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:24.108633-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:24.108863-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:24.108880-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:24.120948-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2384534 ioTS st: 2384534 ht: 32492.583359
error	12:55:24.154048-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:24.914459-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:24.922255-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:24.922292-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:24.924422-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874534 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:24.930100-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:24.938316-0500	VoiceOver	No list of permitted front apps returned
default	12:55:24.938510-0500	VoiceOver	No list of permitted front apps returned
default	12:55:24.940395-0500	VoiceOver	[0x707d6cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:24.940501-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:55:24.944672-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70816ddd0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:24.944694-0500	VoiceOver	AudioConverter -> 0x70816ddd0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:24.944703-0500	VoiceOver	AudioConverter -> 0x70816ddd0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:24.950767-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:24.959239-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874535 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:24.959333-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e2e50, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:24.959352-0500	VoiceOver	AudioConverter -> 0x7070e2e50: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:24.959381-0500	VoiceOver	AudioConverter -> 0x7070e2e50: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:24.995968-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:24.996294-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:55:24.996606-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:24.996665-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:24.996920-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:24.996942-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:24.996973-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:24.997121-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:24.997184-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:24.997211-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:24.997430-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:24.997443-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:25.003622-0500	VoiceOver	[0x707d6cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:25.003772-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:55:25.010993-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2404159 ioTS st: 2404159 ht: 32493.473359
default	12:55:25.121190-0500	VoiceOver	No list of permitted front apps returned
default	12:55:25.121377-0500	VoiceOver	No list of permitted front apps returned
default	12:55:25.122808-0500	VoiceOver	[0x707d6e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:25.122899-0500	VoiceOver	[0x707d6e940] invalidated after the last release of the connection object
default	12:55:25.128783-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708163cc0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:25.128804-0500	VoiceOver	AudioConverter -> 0x708163cc0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:25.128813-0500	VoiceOver	AudioConverter -> 0x708163cc0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:25.133610-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:25.138607-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:25.141376-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:25.141405-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:25.149770-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874535 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:25.150084-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874536 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:25.150254-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70816f570, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:25.150295-0500	VoiceOver	AudioConverter -> 0x70816f570: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:25.150302-0500	VoiceOver	AudioConverter -> 0x70816f570: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:25.195255-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:25.195540-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:55:25.195883-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:25.195907-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:25.196096-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:25.196119-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:25.196151-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:25.196290-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:25.196346-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:25.196372-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:25.196552-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:25.196564-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:25.210916-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2408570 ioTS st: 2408570 ht: 32493.673359
error	12:55:25.280958-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	12:55:26.585562-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:26.582884-0500	VoiceOver	No list of permitted front apps returned
default	12:55:26.628298-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:26.628401-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:26.684684-0500	VoiceOver	No list of permitted front apps returned
default	12:55:26.723182-0500	VoiceOver	[0x707d6e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:26.723382-0500	VoiceOver	[0x707d6e940] invalidated after the last release of the connection object
default	12:55:26.737901-0500	VoiceOver	[0x707d6e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:26.738056-0500	VoiceOver	[0x707d6e940] invalidated after the last release of the connection object
default	12:55:26.752873-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:26.761655-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:26.761746-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:26.768322-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874536 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:26.768867-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874539 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:26.801580-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:26.802191-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:26.802541-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:26.802592-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:26.802835-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:26.802872-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:26.802934-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:26.803189-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:26.803258-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:26.803303-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:26.803565-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:26.803595-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:26.821079-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2444071 ioTS st: 2444071 ht: 32495.283359
error	12:55:26.901603-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:27.930114-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:27.951509-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e2a60, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:27.951551-0500	VoiceOver	AudioConverter -> 0x7070e2a60: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:27.951566-0500	VoiceOver	AudioConverter -> 0x7070e2a60: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:27.957140-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:27.957374-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:27.958245-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:27.958368-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:27.970784-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:27.971729-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:27.971817-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:27.978920-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874539 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:27.979897-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874540 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:28.019145-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:28.019634-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:28.019882-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:28.020004-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:28.020098-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:28.020128-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:28.020172-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:28.020353-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:28.020432-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:28.020493-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:28.020737-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:28.020754-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:28.030914-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2470752 ioTS st: 2470752 ht: 32496.493359
error	12:55:28.091813-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:28.658201-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e3840, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:28.658241-0500	VoiceOver	AudioConverter -> 0x7070e3840: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:28.658256-0500	VoiceOver	AudioConverter -> 0x7070e3840: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
fault	12:55:30.887048-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:30.893119-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 61571
default	12:55:30.893686-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 61571
default	12:55:31.522516-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474874540 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:31.572242-0500	VoiceOver	No list of permitted front apps returned
default	12:55:31.572544-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:31.572576-0500	VoiceOver	No list of permitted front apps returned
default	12:55:31.573441-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:31.573344-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:31.597599-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874541 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	12:55:31.649435-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:31.719012-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61574
default	12:55:31.787039-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61576
default	12:55:32.003350-0500	VoiceOver	No list of permitted front apps returned
default	12:55:32.006460-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:32.007016-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:32.006930-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:32.021661-0500	VoiceOver	[0x707d6e940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:32.021791-0500	VoiceOver	[0x707d6e940] invalidated after the last release of the connection object
default	12:55:32.040786-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e2ca0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:32.040879-0500	VoiceOver	AudioConverter -> 0x7070e2ca0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:32.040905-0500	VoiceOver	AudioConverter -> 0x7070e2ca0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:32.041520-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:32.041636-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:55:32.071475-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e3c00, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:32.071497-0500	VoiceOver	AudioConverter -> 0x7070e3c00: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:32.071579-0500	VoiceOver	AudioConverter -> 0x7070e3c00: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:32.111870-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:32.126740-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874541 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:32.166805-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:55:32.168317-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:32.168858-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:32.168967-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:32.169085-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:32.169476-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:32.169688-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:32.169964-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:32.170515-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:32.170634-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:32.294478-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:32.301450-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:32.301495-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:32.351000-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2566009 ioTS st: 2566009 ht: 32500.813359
error	12:55:32.391657-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:32.998366-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:33.004096-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874543 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:33.034691-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:33.034733-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	12:55:33.148073-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:33.932765-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61600
default	12:55:33.939615-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61600
default	12:55:33.933445-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:34.060359-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61601
default	12:55:34.392640-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 61602
default	12:55:34.550698-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61603
default	12:55:35.326659-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:35.331896-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:35.332006-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:35.332993-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:55:35.333127-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474874544 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:36.930155-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:37.193350-0500	VoiceOver	No list of permitted front apps returned
default	12:55:37.294939-0500	VoiceOver	No list of permitted front apps returned
default	12:55:37.298145-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:37.298541-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:37.298605-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:37.306071-0500	VoiceOver	[0x707d6cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:37.306188-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:55:37.345509-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:37.345613-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:55:37.359275-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70816d020, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:37.359293-0500	VoiceOver	AudioConverter -> 0x70816d020: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:37.359302-0500	VoiceOver	AudioConverter -> 0x70816d020: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:37.366296-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:37.370579-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70816efa0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:37.370594-0500	VoiceOver	AudioConverter -> 0x70816efa0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:37.370601-0500	VoiceOver	AudioConverter -> 0x70816efa0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:37.377161-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874547 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:37.377532-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	12:55:37.411474-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:55:37.412067-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:37.412271-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:37.412292-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:37.412321-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:37.412462-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:37.412518-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:37.412542-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:37.412772-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:37.412789-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	12:55:37.412930-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:55:37.413501-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:37.428683-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 61608
error	12:55:37.641086-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:38.059155-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:38.059504-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:55:38.105542-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:38.105603-0500	VoiceOver	[0x707d6cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:38.105809-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:55:38.108302-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:38.111762-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:38.111830-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:38.114105-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:38.114392-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:38.124331-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874547 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:38.125206-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874548 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:38.125570-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708164d20, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:38.125597-0500	VoiceOver	AudioConverter -> 0x708164d20: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:38.125621-0500	VoiceOver	AudioConverter -> 0x708164d20: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:38.166208-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:38.166512-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:55:38.166779-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:38.166856-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:38.167038-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:38.167061-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:38.167089-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:38.167243-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:38.167301-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:38.167332-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:38.167531-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:38.167545-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:38.180990-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2694562 ioTS st: 2694562 ht: 32506.643359
error	12:55:38.211312-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:39.786642-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:39.791687-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:39.791774-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:39.792995-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874548 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:39.857337-0500	VoiceOver	No list of permitted front apps returned
default	12:55:39.857630-0500	VoiceOver	No list of permitted front apps returned
default	12:55:39.858395-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:39.858516-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:39.869577-0500	VoiceOver	[0x707d6e800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:39.869726-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:55:39.879271-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:39.879376-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:55:39.882586-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:39.882668-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:55:39.883754-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874549 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:39.897188-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813cb70, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:39.900321-0500	VoiceOver	AudioConverter -> 0x70813cb70: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:39.900666-0500	VoiceOver	AudioConverter -> 0x70813cb70: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:39.918154-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:55:39.918777-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:39.918739-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:39.918977-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:39.919003-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:39.919034-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	12:55:39.919028-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:39.919183-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:39.919243-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:39.919270-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:39.919461-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:39.919476-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:39.930124-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:39.931003-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2733150 ioTS st: 2733150 ht: 32508.393359
default	12:55:39.932817-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:39.933027-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:55:39.945254-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:39.951364-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:39.951397-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:39.953702-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874549 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:39.954004-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874550 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:39.986403-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:39.986710-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:55:39.986970-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:39.987059-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:39.987257-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:39.987307-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:39.987346-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:39.987495-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:39.987555-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:39.987581-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:39.987778-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:39.987792-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:40.000974-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2734694 ioTS st: 2734694 ht: 32508.463359
error	12:55:40.027429-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:41.253010-0500	VoiceOver	No list of permitted front apps returned
default	12:55:41.253340-0500	VoiceOver	No list of permitted front apps returned
default	12:55:41.272789-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:41.273057-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:55:41.282438-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7074a5350, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:41.282473-0500	VoiceOver	AudioConverter -> 0x7074a5350: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:41.282489-0500	VoiceOver	AudioConverter -> 0x7074a5350: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:41.307672-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:41.323225-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:41.331829-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:41.331945-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:41.333673-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874550 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:41.334280-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874551 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:41.361015-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:55:41.361907-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:41.362014-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:41.362143-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:41.362176-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:41.362226-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:41.362421-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
fault	12:55:41.362407-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:41.362493-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:41.362534-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:41.362786-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:41.362802-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:41.381164-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2765124 ioTS st: 2765124 ht: 32509.843359
error	12:55:41.471559-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:42.930088-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
fault	12:55:43.258867-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:43.344573-0500	VoiceOver	No list of permitted front apps returned
default	12:55:43.367338-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:43.367966-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:43.368078-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:43.390152-0500	VoiceOver	[0x707d6cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:43.390301-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:55:43.401902-0500	VoiceOver	No list of permitted front apps returned
default	12:55:43.404495-0500	VoiceOver	[0x707d6ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:43.404670-0500	VoiceOver	[0x707d6ebc0] invalidated after the last release of the connection object
default	12:55:43.404717-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813eeb0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:43.404747-0500	VoiceOver	AudioConverter -> 0x70813eeb0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:43.404758-0500	VoiceOver	AudioConverter -> 0x70813eeb0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:43.415714-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813d6e0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:43.415775-0500	VoiceOver	AudioConverter -> 0x70813d6e0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:43.415785-0500	VoiceOver	AudioConverter -> 0x70813d6e0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:43.421909-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:43.431890-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:43.432005-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:43.436669-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474874551 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:43.437853-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874552 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:43.470191-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:43.470875-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:43.471178-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:43.471278-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:43.471710-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:43.471745-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:43.471810-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:43.472054-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:43.472115-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:43.472162-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:43.472435-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:43.472455-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:43.491142-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2811650 ioTS st: 2811650 ht: 32511.953359
error	12:55:43.583411-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:44.823519-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813ecd0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:44.823559-0500	VoiceOver	AudioConverter -> 0x70813ecd0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:44.823574-0500	VoiceOver	AudioConverter -> 0x70813ecd0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:44.826139-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:44.826389-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:55:44.828210-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:44.828362-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:55:44.843614-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:44.852247-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:44.852332-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:44.862157-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874552 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:44.862730-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874553 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:44.889000-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:55:44.889697-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:44.889921-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	12:55:44.889910-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:44.889951-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:44.889997-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:44.890166-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
fault	12:55:44.890207-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:44.890233-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:44.890276-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:44.890506-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:44.890526-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:44.900991-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2842741 ioTS st: 2842741 ht: 32513.363359
error	12:55:44.917449-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:45.455492-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813d2f0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:45.455532-0500	VoiceOver	AudioConverter -> 0x70813d2f0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:45.455555-0500	VoiceOver	AudioConverter -> 0x70813d2f0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:45.930700-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:46.142273-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874553 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:46.667749-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874554 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:46.725260-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:46.725513-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:55:46.727368-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:46.727735-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:55:46.736692-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813c450, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:46.736977-0500	VoiceOver	AudioConverter -> 0x70813c450: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:46.736988-0500	VoiceOver	AudioConverter -> 0x70813c450: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:46.741725-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:46.751328-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:46.751355-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:46.755863-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874554 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:46.756508-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874555 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:46.787256-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:46.787820-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:46.787894-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:46.788089-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:46.788111-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	12:55:46.788106-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:46.788140-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:46.788286-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:46.788357-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:46.788383-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:46.788570-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:46.788583-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:46.800950-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 2884637 ioTS st: 2884637 ht: 32515.263359
error	12:55:46.814996-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:47.204849-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70813e910, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:47.204886-0500	VoiceOver	AudioConverter -> 0x70813e910: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:47.204905-0500	VoiceOver	AudioConverter -> 0x70813e910: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:47.884608-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:55:47.884695-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:55:47.884721-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:55:47.884758-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:55:48.041826-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874555 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:48.642101-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:48.651680-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:48.651802-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:48.933913-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:49.863550-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:55:50.751085-0500	VoiceOver	aqmeio@0x706a36a18 Stop id=85
default	12:55:50.751091-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:50.751555-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:51.103657-0500	VoiceOver	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	12:55:51.458914-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 61645
default	12:55:51.615659-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 61655
default	12:55:51.935954-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 1
default	12:55:52.612163-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:52.612797-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:52.612915-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:52.628607-0500	VoiceOver	No list of permitted front apps returned
default	12:55:52.729863-0500	VoiceOver	No list of permitted front apps returned
default	12:55:52.862145-0500	VoiceOver	No list of permitted front apps returned
default	12:55:52.910665-0500	VoiceOver	[0x707d6cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:52.910973-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:55:52.934333-0500	VoiceOver	[0x707d6ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:52.934462-0500	VoiceOver	[0x707d6ebc0] invalidated after the last release of the connection object
default	12:55:52.939982-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70815e340, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:52.940011-0500	VoiceOver	AudioConverter -> 0x70815e340: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:52.940026-0500	VoiceOver	AudioConverter -> 0x70815e340: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:52.950741-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70815c720, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:52.950762-0500	VoiceOver	AudioConverter -> 0x70815c720: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:52.950768-0500	VoiceOver	AudioConverter -> 0x70815c720: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:52.982624-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:55:52.983261-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:52.983484-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:52.983505-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	12:55:52.983306-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:52.983604-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:52.984091-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:52.984158-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
fault	12:55:52.983731-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:52.984246-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:52.984549-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:52.984563-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	12:55:53.097549-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	12:55:53.842931-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:53.843799-0500	VoiceOver	No list of permitted front apps returned
default	12:55:53.857981-0500	VoiceOver	No list of permitted front apps returned
default	12:55:53.959789-0500	VoiceOver	No list of permitted front apps returned
default	12:55:53.973885-0500	VoiceOver	No list of permitted front apps returned
default	12:55:53.984766-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x70815ee80, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:53.984795-0500	VoiceOver	AudioConverter -> 0x70815ee80: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:53.984806-0500	VoiceOver	AudioConverter -> 0x70815ee80: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:53.989835-0500	VoiceOver	No list of permitted front apps returned
default	12:55:53.992523-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:53.993146-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:53.993222-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:54.015664-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:54.015836-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:55:54.038003-0500	VoiceOver	No list of permitted front apps returned
default	12:55:54.038189-0500	VoiceOver	No list of permitted front apps returned
default	12:55:54.039923-0500	VoiceOver	[0x707d6ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:54.040026-0500	VoiceOver	[0x707d6ebc0] invalidated after the last release of the connection object
default	12:55:54.043184-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:54.043258-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:55:54.050729-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:54.056452-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:55:54.060781-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:54.061538-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:54.061583-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:54.068381-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874561 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:54.068828-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874580 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:54.133358-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:54.133622-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:55:54.133855-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:54.133990-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:54.134145-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:54.134165-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:54.134191-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:54.134345-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:54.134398-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:54.134423-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:54.134615-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:54.134629-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:54.150979-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 3046706 ioTS st: 3046706 ht: 32522.613359
default	12:55:54.186557-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	12:55:54.372507-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:54.930052-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 2
default	12:55:55.927867-0500	VoiceOver	No list of permitted front apps returned
fault	12:55:55.931822-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:55.956142-0500	VoiceOver	No list of permitted front apps returned
default	12:55:55.958837-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:55.959916-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:55.960041-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:55.971088-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:55.971252-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:55:56.002913-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:56.003072-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x707102940, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:56.003101-0500	VoiceOver	AudioConverter -> 0x707102940: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:56.003108-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:55:56.003114-0500	VoiceOver	AudioConverter -> 0x707102940: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:56.014977-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e3e40, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:56.015006-0500	VoiceOver	AudioConverter -> 0x7070e3e40: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:56.015016-0500	VoiceOver	AudioConverter -> 0x7070e3e40: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:56.023523-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:55:56.029239-0500	VoiceOver	No list of permitted front apps returned
default	12:55:56.031624-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:55:56.031831-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:55:56.048846-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474874580 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:55:56.049264-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874583 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:56.092828-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:55:56.093086-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:55:56.093364-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:56.093476-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:55:56.093666-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:56.093694-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:56.093724-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:55:56.093854-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:56.093910-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:56.093935-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:56.094109-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:56.094120-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:56.110913-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 3089924 ioTS st: 3089924 ht: 32524.573359
error	12:55:56.174303-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:55:57.930011-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 2
default	12:55:58.133217-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:58.134242-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:58.134069-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:58.145395-0500	VoiceOver	No list of permitted front apps returned
default	12:55:58.254009-0500	VoiceOver	No list of permitted front apps returned
default	12:55:58.294317-0500	VoiceOver	No list of permitted front apps returned
default	12:55:58.300244-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:55:58.300597-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:55:58.300668-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:55:58.305118-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:58.305239-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:55:58.322473-0500	VoiceOver	[0x707d6ebc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:55:58.322602-0500	VoiceOver	[0x707d6ebc0] invalidated after the last release of the connection object
default	12:55:58.325432-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7081669d0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:58.325464-0500	VoiceOver	AudioConverter -> 0x7081669d0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:58.325488-0500	VoiceOver	AudioConverter -> 0x7081669d0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:58.325787-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:55:58.336908-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e3c00, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:55:58.336930-0500	VoiceOver	AudioConverter -> 0x7070e3c00: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:55:58.336941-0500	VoiceOver	AudioConverter -> 0x7070e3c00: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:55:58.341727-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874591 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:55:58.342144-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	12:55:58.379153-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:55:58.379801-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:55:58.379867-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:58.380007-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:55:58.380037-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:55:58.380069-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	12:55:58.380146-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:55:58.380232-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:55:58.380322-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:55:58.380357-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:55:58.380584-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:55:58.380599-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:55:58.391038-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 3140198 ioTS st: 3140198 ht: 32526.853359
error	12:55:58.473081-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:56:00.116230-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:56:00.116929-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:56:00.117372-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:56:00.133111-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:56:00.136267-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
error	12:56:00.154740-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	12:56:00.169630-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:56:00.172076-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:56:00.170888-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:56:00.910753-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:56:00.909852-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:56:00.911015-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:56:00.933041-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 2
default	12:56:00.974879-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:56:00.974160-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:56:00.975050-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:56:03.688122-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474874591 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:56:03.897697-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:56:03.930015-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 2
default	12:56:04.206319-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474874594 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:56:04.206717-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	12:56:04.289735-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:56:06.930057-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 2
default	12:56:08.617084-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474874594 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:56:08.831402-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:56:09.217196-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:56:09.226712-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:56:09.226789-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:56:09.929960-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 2
default	12:56:11.326525-0500	VoiceOver	aqmeio@0x706a36a18 Stop id=85
default	12:56:11.326554-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:56:11.327035-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:56:12.786237-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:56:12.786864-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f500f","name":"VoiceOver(61431)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	12:56:12.787039-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 16 stopping playing
default	12:56:12.787156-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	12:56:12.787262-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:56:12.787462-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:56:12.788009-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f500f to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":61431}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f500f, sessionType: 'prim', isRecording: false }, 
]
default	12:56:12.788609-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:56:12.788186-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	12:56:12.788975-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:56:12.789120-0500	runningboardd	Invalidating assertion 404-61431-23024 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:56:12.788208-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:56:12.789089-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:56:12.789129-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 1
default	12:56:12.789333-0500	runningboardd	Invalidating assertion 404-337-22989 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.powerd>:337]
default	12:56:12.890330-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:56:12.890352-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:56:12.890367-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:56:12.890394-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:56:12.890412-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:56:12.894864-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:56:13.357877-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:13.357907-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:13.357913-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:13.360061-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
default	12:56:13.360083-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:56:13.360090-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:56:13.368098-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:13.368140-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:13.368422-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:13.368482-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:56:13.368530-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:56:13.373718-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:13.373939-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:56:13.373980-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:56:13.374063-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:13.374171-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:13.375972-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:13.376065-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:13.376266-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:13.376393-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:56:13.376509-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:56:13.379728-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:13.379894-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:13.380893-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:13.384568-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:13.385560-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:13.387259-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:56:13.387276-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:56:13.387291-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:13.387303-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:13.387311-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:13.387319-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:13.387382-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:13.387629-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:13.387823-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:13.387893-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:13.387928-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:13.387995-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:13.388783-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:56:13.388993-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:56:13.389050-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:56:13.401598-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:13.401667-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:56:13.402143-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:13.402201-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:56:13.401844-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:13.416778-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	12:56:13.416802-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:56:13.416811-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	12:56:13.416834-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:56:13.416845-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:56:13.417989-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e3540, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:56:13.418035-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:56:13.418404-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:56:13.418443-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:56:13.418545-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:56:13.418603-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x706a36a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	12:56:13.423641-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x7074da800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	12:56:17.933410-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 61666
default	12:56:17.933437-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 61665
default	12:56:18.435723-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
default	12:56:18.435770-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:56:18.435781-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:56:18.437257-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:18.437305-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:18.437314-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:18.450814-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:56:18.450882-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:56:18.450892-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:56:18.455349-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:18.455377-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:18.468596-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:56:18.468632-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:56:18.468769-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:18.471330-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:18.471801-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:56:18.471822-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:56:18.471957-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:18.475785-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:18.475821-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:18.476007-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:18.476018-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:18.476066-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:18.476073-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:18.476080-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:18.476092-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:18.476100-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:18.476186-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:18.476229-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:18.476329-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:18.476387-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:18.476578-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:18.476603-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:18.476609-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:18.476733-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:56:18.476746-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:56:18.476744-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:18.476843-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:18.476931-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:18.479902-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:18.479950-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:18.480298-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:18.480309-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:18.480328-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:18.480336-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:18.480345-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:18.480389-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:18.480639-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:56:18.480755-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:56:18.480848-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:56:18.480928-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:56:18.480995-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:56:18.483098-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e3540, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:56:18.483347-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:18.483624-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:56:18.483890-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:18.483880-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:18.484473-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:18.484946-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:18.485224-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:18.486346-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:18.486550-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:18.486588-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:18.487306-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:18.487571-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:18.491210-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:56:18.491291-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:56:18.491419-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:56:18.491478-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:56:18.491504-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:56:18.491576-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:56:18.491606-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:56:19.076040-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x7074da800:
default	12:56:19.077481-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	12:56:19.077534-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	12:56:19.077630-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	12:56:19.083497-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:56:19.077811-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	12:56:19.077991-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	12:56:19.087137-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x7074da800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	12:56:19.642059-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:56:19.788135-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:19.788168-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:19.788177-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:19.789797-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
default	12:56:19.789822-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:56:19.789829-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:56:19.800955-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:19.800997-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:19.801285-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:19.801309-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:56:19.801317-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:56:19.802834-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:56:19.802855-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:56:19.803013-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:56:19.803239-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:19.803899-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:56:19.803908-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:19.803985-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:56:19.804110-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:19.804179-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:19.804258-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:19.804336-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:19.804502-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:19.804546-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:19.804589-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:19.807235-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:19.807254-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:19.809354-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:19.815767-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:56:19.815792-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:56:19.815890-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:19.818782-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:19.819077-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:56:19.819087-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:56:19.819202-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:19.823378-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:19.823797-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:19.823808-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:19.823898-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:19.823905-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:19.823911-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:19.823916-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:19.823972-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:19.824137-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:19.824213-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:19.824291-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:19.824382-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:19.824516-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:19.826613-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:56:19.826633-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:56:19.826917-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	12:56:19.826929-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:56:19.826966-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	12:56:19.827050-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:56:19.827117-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:56:19.837009-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	12:56:25.468334-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:25.468678-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:25.468704-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:25.471190-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
default	12:56:25.471230-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:56:25.471239-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:56:25.487313-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:56:25.487361-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:56:25.487368-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:56:25.489450-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:25.489474-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:25.503941-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:56:25.503978-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:56:25.504146-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:25.508402-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:25.508686-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:56:25.508697-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:56:25.508853-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:25.514875-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:25.515355-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:25.515368-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:25.515427-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:25.515434-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:25.515441-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:25.515448-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:25.515598-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:25.515778-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:25.515964-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:25.516115-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:25.517841-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:25.518265-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:25.518476-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:25.518528-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:56:25.518640-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:56:25.518687-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:56:25.518793-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:56:25.520785-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:25.520988-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:25.521106-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:56:25.521313-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:56:25.521593-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:56:25.521687-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:25.522012-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:56:25.522284-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:25.522543-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:56:25.522790-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:25.523053-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:56:25.523238-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:25.523462-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:56:25.521425-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:25.524564-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:25.524564-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:25.524775-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:25.524962-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:25.525110-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:25.525245-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:25.525325-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:25.525403-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:25.527103-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	12:56:25.527139-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	12:56:25.527173-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	12:56:26.055217-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x7074da800:
default	12:56:26.056293-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	12:56:26.056364-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	12:56:26.056560-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	12:56:26.056791-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	12:56:26.056981-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	12:56:26.063880-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x7074da800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	12:56:26.066595-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:56:26.611745-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:56:27.159497-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:56:27.912467-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
default	12:56:27.912509-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:56:27.912517-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:56:28.080029-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:56:28.080075-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:56:28.080082-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:56:28.084883-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:28.084963-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:28.084976-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:28.095869-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:56:28.097022-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:28.097062-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:28.097230-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:28.097259-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:56:28.097266-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:56:28.103014-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:28.103955-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:56:28.104001-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:56:28.104167-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:28.104204-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:28.105329-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:28.105457-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:28.106333-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:28.106416-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:28.106532-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:28.107611-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:28.107703-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:28.107826-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:28.110055-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:28.110408-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:28.110430-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:28.132484-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:28.132519-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:28.132555-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:56:28.132740-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:28.132819-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:56:28.132930-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:28.133068-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:28.133130-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:28.133220-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:28.133302-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:56:28.133573-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:28.133934-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:28.134010-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:28.146955-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e3540, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:56:28.147030-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:56:28.147269-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:56:28.147314-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:56:28.147363-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:56:28.147413-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x706a36a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	12:56:28.147424-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x706a36a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	12:56:28.148457-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e2f10, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	12:56:28.148967-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x7074da800:
default	12:56:28.149153-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	12:56:28.149184-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	12:56:28.153258-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x7074da800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	12:56:31.037029-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:56:31.039165-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:56:31.039462-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:56:31.119534-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:56:31.124039-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875415 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:56:31.124809-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	12:56:31.124810-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-23468 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:56:31.124944-0500	runningboardd	Assertion 404-337-23468 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:56:31.125449-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:56:31.125509-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:56:31.125612-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:56:31.125683-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:56:31.125720-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:56:31.152168-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:56:31.152997-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:56:31.153394-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:56:31.153430-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:56:31.153523-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:56:31.153948-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:56:31.154306-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:56:31.154381-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
fault	12:56:31.153938-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:56:31.157121-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f500f","name":"VoiceOver(61431)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	12:56:31.155437-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:56:31.157248-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	12:56:31.157259-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 16 starting playing
default	12:56:31.157965-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
fault	12:56:31.154426-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:56:31.158134-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	12:56:31.154747-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-23469 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:56:31.158279-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f5011, Nexy(61645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	12:56:31.154824-0500	runningboardd	Assertion 404-61431-23469 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:56:31.159210-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:56:31.159029-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x89380001 category Not set
default	12:56:31.159243-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:56:31.159275-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:56:31.159336-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:56:31.159427-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:56:31.158432-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	12:56:31.158471-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f500f to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":61431}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f500f, sessionType: 'prim', isRecording: false }, 
]
default	12:56:31.158606-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	12:56:31.158615-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:56:31.160849-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:56:31.158628-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:56:31.161009-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:56:31.161036-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:56:31.161051-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 2
default	12:56:31.161058-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:56:31.165842-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
error	12:56:31.202058-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:56:31.211143-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 3864103 ioTS st: 3864103 ht: 32559.683510
default	12:56:31.369893-0500	VoiceOver	[0x707d6cb40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:56:31.370052-0500	VoiceOver	[0x707d6cb40] invalidated after the last release of the connection object
default	12:56:31.524158-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f5011, Nexy(61645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	12:56:31.524629-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f5011, Nexy(61645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	12:56:31.524916-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f5011, Nexy(61645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	12:56:31.525151-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f5011, Nexy(61645), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	12:56:31.535321-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	12:56:31.535442-0500	audioaccessoryd	Updating local audio category 501 -> 201 app com.apple.VoiceOver
default	12:56:31.535896-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:56:31.536029-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:56:31.536237-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:56:31.536344-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:56:31.536679-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:56:31.536833-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:56:31.537094-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:56:31.553030-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875415 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:56:31.763895-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:56:32.129297-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:56:32.130829-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875416 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:56:32.131293-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	12:56:32.153687-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:56:32.461673-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:56:32.461827-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:56:32.511893-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875416 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:56:32.535769-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 61670
default	12:56:32.536330-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 61670
default	12:56:32.719713-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:56:32.720130-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:56:32.722305-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:56:33.111792-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:56:33.131889-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:56:33.132185-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:56:33.143898-0500	VoiceOver	[0x707d6df40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:56:33.144160-0500	VoiceOver	[0x707d6df40] invalidated after the last release of the connection object
default	12:56:33.573071-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:56:33.573261-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	12:56:33.653657-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:33.654659-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:56:33.662226-0500	runningboardd	Invalidating assertion 404-61431-23469 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:56:33.654791-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:33.658824-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
default	12:56:33.658869-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:56:33.662393-0500	runningboardd	Invalidating assertion 404-337-23468 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.powerd>:337]
default	12:56:33.658875-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:56:33.660021-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	12:56:33.674040-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:33.674062-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:33.674228-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:33.674258-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:56:33.674268-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:56:33.679614-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:33.683557-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:56:33.683598-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:56:33.683620-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:56:33.683634-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:56:33.685158-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:56:33.685786-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:56:33.686382-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:56:33.686400-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:56:33.686409-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:56:33.686806-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:56:33.686815-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:56:33.702037-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:56:33.830801-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:56:33.902359-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 0 NumofApp 2
default	12:56:34.296865-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:56:34.298628-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-23480 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:56:34.298759-0500	runningboardd	Assertion 404-337-23480 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:56:34.300152-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:56:34.300249-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:56:34.300324-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:56:34.300466-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:56:34.300549-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:56:34.345787-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:56:34.345810-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:56:34.345828-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:56:34.346400-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:34.346417-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:34.346821-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x706be0040) Device ID: 85 (Input:No | Output:Yes): true
default	12:56:34.346846-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x706be0040)
default	12:56:34.347213-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	12:56:34.350971-0500	runningboardd	Invalidating assertion 404-61431-23478 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:56:34.347300-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	12:56:34.353226-0500	runningboardd	Invalidating assertion 404-337-23480 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.powerd>:337]
default	12:56:34.353866-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-23483 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:56:34.353979-0500	runningboardd	Assertion 404-337-23483 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:56:34.401794-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:56:34.401814-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:56:34.403019-0500	runningboardd	Invalidating assertion 404-61431-23481 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:56:34.404896-0500	runningboardd	Invalidating assertion 404-337-23483 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.powerd>:337]
default	12:56:34.404856-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e3240, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:56:34.405369-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-23485 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:56:34.404886-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	12:56:34.405540-0500	runningboardd	Assertion 404-61431-23485 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:56:34.920700-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:56:34.963037-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2505 called from <private>
default	12:56:34.963758-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	12:56:34.963798-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x706be0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	12:56:34.963819-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	12:56:34.963867-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x706a36a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	12:56:34.963907-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x706a36a18 (1C-77-54-18-C8-A3:output): Output stream format changed
default	12:56:34.964883-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e2f10, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:56:34.965177-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x7074da800:
default	12:56:34.965231-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	12:56:34.965240-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	12:56:34.965259-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	12:56:34.965293-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	12:56:34.965316-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	12:56:34.965639-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x7074da800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	12:56:34.975914-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:56:34.975991-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:56:35.213418-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:56:35.213659-0500	VoiceOver	aqmeio@0x706a36a18 Stop id=85
default	12:56:35.213885-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f500f","name":"VoiceOver(61431)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	12:56:35.214001-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 16 stopping playing
default	12:56:35.214061-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	12:56:35.214118-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:56:35.214195-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:56:35.214282-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:56:35.214334-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f500f to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":61431}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f500f, sessionType: 'prim', isRecording: false }, 
]
default	12:56:35.214411-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	12:56:35.214426-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:56:35.214473-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:56:35.214540-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:56:35.214565-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 0
default	12:56:35.218013-0500	runningboardd	Invalidating assertion 404-61431-23485 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.VoiceOver(501)>:61431]
default	12:56:35.218120-0500	runningboardd	Invalidating assertion 404-337-23486 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.powerd>:337]
default	12:56:35.322293-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:56:35.322330-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:56:35.322352-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:56:35.322392-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:56:35.322460-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:56:35.328377-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:56:51.614243-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 61676
default	12:57:02.937994-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
default	12:57:02.938060-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:57:02.938067-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:57:03.311382-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:57:03.311449-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:57:03.311466-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:57:03.312562-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:57:03.312743-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:57:03.312761-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:57:03.328157-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:57:03.328190-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:57:03.328321-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:57:03.328346-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:57:03.328468-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:57:03.334692-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:57:03.337496-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:57:03.343245-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:57:03.337779-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:57:03.337866-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:57:03.338004-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:57:08.656018-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2506)
default	12:57:08.656060-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2506 called from <private>
default	12:57:08.656070-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2506 called from <private>
default	12:57:08.656599-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:57:08.656687-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:57:08.656714-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:57:08.666528-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:57:08.666563-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:57:08.666816-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:57:08.666842-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2505 called from <private>
default	12:57:08.666850-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2505 called from <private>
default	12:57:08.669931-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:57:08.669982-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:57:08.670877-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2505 called from <private>
default	12:57:08.670924-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2505 called from <private>
default	12:57:08.671082-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:57:08.671226-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:57:08.671488-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:57:08.671606-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:57:08.673996-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:57:08.674345-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:57:08.674707-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:57:08.674869-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:57:08.674985-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:57:08.679603-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:57:08.679646-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:57:08.683065-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:57:08.684725-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:57:08.688308-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:57:08.688347-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:57:08.688361-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:57:08.688373-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:57:08.688383-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:57:08.688388-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:57:08.688394-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:57:08.688399-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:57:08.688450-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:57:08.688457-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:57:08.689578-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2506)
default	12:57:08.689619-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2506 called from <private>
default	12:57:08.689625-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2506 called from <private>
default	12:57:08.699934-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:57:08.699968-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:57:08.700122-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:57:08.701756-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:57:08.701796-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2505)
default	12:57:08.702167-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:57:08.702194-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:57:08.702280-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2505 called from <private>
default	12:57:08.702291-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2505 called from <private>
default	12:57:08.702297-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2505 called from <private>
default	12:57:08.702394-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2505 called from <private>
default	12:57:08.702575-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2505 called from <private>
default	12:57:08.702667-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2505 called from <private>
default	12:57:08.702785-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2505)
default	12:57:08.703037-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2505 called from <private>
default	12:57:08.703181-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2505 called from <private>
default	12:57:08.709623-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e3240, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:57:08.720036-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7070e2f10, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	12:57:09.391696-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x7074da800:
default	12:57:09.392138-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	12:57:09.392169-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	12:57:09.392247-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	12:57:09.392328-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	12:57:09.392415-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	12:57:09.400017-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x7074da800 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	12:57:09.401761-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	12:57:09.453742-0500	VoiceOver	No list of permitted front apps returned
default	12:57:09.554832-0500	VoiceOver	No list of permitted front apps returned
default	12:57:09.787563-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:57:09.906214-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875913 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:57:09.907072-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.powerd>:337] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:404-337-23543 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	12:57:09.907289-0500	runningboardd	Assertion 404-337-23543 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:57:09.948709-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:57:09.979100-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	12:57:09.980415-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:57:09.981677-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	12:57:09.982026-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:57:09.981770-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:57:09.981853-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	12:57:09.982744-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:57:09.987046-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:57:09.987310-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:57:09.990214-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.VoiceOver(501)>:61431] with description <RBSAssertionDescriptor| "AudioHAL" ID:404-61431-23546 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	12:57:09.990425-0500	runningboardd	Assertion 404-61431-23546 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:57:09.992120-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:57:09.992160-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:57:09.992206-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:57:09.992301-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:57:09.992332-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:57:10.029547-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:57:10.031205-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f500f","name":"VoiceOver(61431)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	12:57:10.031500-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	12:57:10.031523-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 16 starting playing
default	12:57:10.031624-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:10.031687-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	12:57:10.031730-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'}, secondSession={clientName:'sid:0x1f5004, Browser Helper(4811), 'prim'', displayID:'company.thebrowser.browser.helper'} but will use session={clientName:'(null)', displayID:'(null)'}
default	12:57:10.032089-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	12:57:10.032105-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	12:57:10.032144-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:57:10.032638-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x89380001 category Not set
default	12:57:10.031918-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	12:57:10.031938-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f500f to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":61431}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f500f, sessionType: 'prim', isRecording: false }, 
]
default	12:57:10.035526-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:57:10.035828-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:57:10.035887-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	12:57:10.035912-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 3
default	12:57:10.035953-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:57:10.068151-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:57:10.074546-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 4720819 ioTS st: 4720819 ht: 32598.536838
error	12:57:10.217219-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:57:10.315797-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 61683
default	12:57:10.315918-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 61682
default	12:57:10.525304-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708185650, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:57:10.525324-0500	VoiceOver	AudioConverter -> 0x708185650: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:57:10.525336-0500	VoiceOver	AudioConverter -> 0x708185650: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:57:10.525450-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	12:57:10.525831-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:57:10.526520-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:57:10.526690-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:57:10.545483-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:57:10.555321-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:57:10.555428-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:57:10.567296-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875913 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:57:10.568280-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875914 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:57:10.616523-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:57:10.616906-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:57:10.617273-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:57:10.617338-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:57:10.617572-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:57:10.617598-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:57:10.617640-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:57:10.617851-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:57:10.617913-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:57:10.617949-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:57:10.618215-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:57:10.618235-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:57:10.634577-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 4733167 ioTS st: 4733167 ht: 32599.096838
default	12:57:10.862756-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	12:57:10.862950-0500	audioaccessoryd	Updating local audio category 301 -> 201 app com.apple.VoiceOver
default	12:57:10.864845-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	12:57:10.992903-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f500f, VoiceOver(61431), 'prim'', displayID:'com.apple.VoiceOver'}, secondSession={clientName:'sid:0x1f5004, Browser Helper(4811), 'prim'', displayID:'company.thebrowser.browser.helper'} but will use session={clientName:'(null)', displayID:'(null)'}
default	12:57:10.995210-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:57:11.121294-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
fault	12:57:11.760056-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:57:11.763653-0500	VoiceOver	No list of permitted front apps returned
default	12:57:11.870151-0500	VoiceOver	No list of permitted front apps returned
default	12:57:11.874212-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:57:11.874754-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:57:11.874854-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:57:11.893381-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:57:11.893659-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:57:11.911716-0500	VoiceOver	[0x707d6ed00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:57:11.911875-0500	VoiceOver	[0x707d6ed00] invalidated after the last release of the connection object
default	12:57:11.913780-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708181620, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:57:11.913820-0500	VoiceOver	AudioConverter -> 0x708181620: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:57:11.913830-0500	VoiceOver	AudioConverter -> 0x708181620: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:57:11.933682-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:57:11.935272-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:57:11.935350-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:57:11.990340-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:57:11.990355-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	12:57:12.003201-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:57:12.087582-0500	VoiceOver	No list of permitted front apps returned
error	12:57:12.091135-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:57:12.091200-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708182040, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:57:12.091248-0500	VoiceOver	AudioConverter -> 0x708182040: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:57:12.091346-0500	VoiceOver	AudioConverter -> 0x708182040: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:57:12.094168-0500	VoiceOver	No list of permitted front apps returned
default	12:57:12.100266-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	12:57:12.100754-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 61431, name: VoiceOver
default	12:57:12.100838-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	12:57:12.139749-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:57:12.139900-0500	VoiceOver	[0x707d6e6c0] invalidated after the last release of the connection object
default	12:57:12.161815-0500	VoiceOver	[0x707d6c780] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	12:57:12.161979-0500	VoiceOver	[0x707d6c780] invalidated after the last release of the connection object
default	12:57:12.175334-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x708187bd0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	12:57:12.175359-0500	VoiceOver	AudioConverter -> 0x708187bd0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	12:57:12.175368-0500	VoiceOver	AudioConverter -> 0x708187bd0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	12:57:12.186717-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:57:12.195235-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:57:12.195327-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:57:12.203922-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875916 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:57:12.206496-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875919 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:57:12.243094-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:57:12.243560-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:57:12.243941-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	12:57:12.243850-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:57:12.244170-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:57:12.244204-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:57:12.244266-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:57:12.244486-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:57:12.244563-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:57:12.244837-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:57:12.245388-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:57:12.245408-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:57:12.264744-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 4769109 ioTS st: 4769109 ht: 32600.726838
error	12:57:12.365789-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:57:12.715497-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	12:57:13.123054-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:57:13.125293-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:57:13.125365-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:57:13.131251-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875919 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:57:13.131738-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875920 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:57:13.158705-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	12:57:13.159177-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	12:57:13.159492-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:57:13.159573-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:57:13.159826-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:57:13.159857-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	12:57:13.159898-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:57:13.160056-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
default	12:57:13.160109-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:57:13.160144-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:57:13.160347-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:57:13.160363-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:57:13.174583-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 4789176 ioTS st: 4789176 ht: 32601.636838
error	12:57:13.213635-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:57:13.752816-0500	VoiceOver	[0x707d6e800] activating connection: mach=false listener=false peer=false name=com.apple.ViewBridgeAuxiliary
default	12:57:13.753298-0500	VoiceOver	[0x707d6e6c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	12:57:13.753890-0500	VoiceOver	[0x707d6c780] activating connection: mach=false listener=true peer=false name=(anonymous)
default	12:57:13.753923-0500	VoiceOver	[0x707d6c780] Connection returned listener port: 0x25613
default	12:57:13.754125-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.coreservices.launchservicesd>:366] with description <RBSAssertionDescriptor| "frontmost:61431" ID:404-366-23580 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractiveFocal" sourceEnvironment:"(null)">
	]>
default	12:57:13.754255-0500	WindowServer	7e33b[DoDeferredOrdering]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x10b10b (VoiceOver) mainConnectionID: 7E33B;
} for reason: updated frontmost process
default	12:57:13.754349-0500	WindowServer	7e33b[DoDeferredOrdering]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x10b10b (VoiceOver) -> <pid: 61431>
default	12:57:13.754575-0500	WindowServer	new deferring rules for pid:396: [
    [396-90E]; <keyboardFocus; VoiceOver:0x0-0x10b10b>; () -> <pid: 61431>; reason: frontmost PSN --> outbound target,
    [396-90D]; <keyboardFocus; <frontmost>>; () -> <token: VoiceOver:0x0-0x10b10b; pid: 396>; reason: frontmost PSN,
    [396-90C]; <keyboardFocus>; () -> <token: <frontmost>; pid: 396>; reason: Deferring to <frontmost>
]
default	12:57:13.754647-0500	WindowServer	[keyboardFocus 0x76d90eb70] setRules:forPID(396): [
    [396-90E]; <keyboardFocus; VoiceOver:0x0-0x10b10b>; () -> <pid: 61431>; reason: frontmost PSN --> outbound target,
    [396-90D]; <keyboardFocus; <frontmost>>; () -> <token: VoiceOver:0x0-0x10b10b; pid: 396>; reason: frontmost PSN,
    [396-90C]; <keyboardFocus>; () -> <token: <frontmost>; pid: 396>; reason: Deferring to <frontmost>
]
default	12:57:13.754528-0500	runningboardd	Assertion 404-366-23580 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:57:13.755501-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:57:13.755515-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:57:13.755604-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Set darwin role to: UserInteractiveFocal
default	12:57:13.755645-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:57:13.755709-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:57:13.755759-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:57:13.755928-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 396>,
    <token: VoiceOver:0x0-0x10b10b; pid: 396>,
    <pid: 61431>
]
fault	12:57:13.756031-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:57:13.756946-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:61431] from originator [osservice<com.apple.coreservices.launchservicesd>:366] with description <RBSAssertionDescriptor| "notification:61431" ID:404-366-23581 target:61431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	12:57:13.757014-0500	runningboardd	Assertion 404-366-23581 (target:[osservice<com.apple.VoiceOver(501)>:61431]) will be created as active
default	12:57:13.762341-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring jetsam update because this process is not memory-managed
default	12:57:13.762360-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring suspend because this process is not lifecycle managed
default	12:57:13.762399-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring GPU update because this process is not GPU managed
default	12:57:13.762435-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Ignoring memory limit update because this process is not memory-managed
default	12:57:13.762473-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] Skipping AppNap state - not lifecycle managed
default	12:57:13.764427-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:57:13.765594-0500	intelligencecontextd	starting RequestID(61364:24 = 263556373151768) for client Spotlight: RequestParameters(timeout: 0.75 sec, requestedComponents: (commands), targetedAppBundleIdentifiers: ["com.apple.VoiceOver"], appIntentsRequest: AppIntentsRequest())
default	12:57:13.768232-0500	gamepolicyd	Received state update for 61431 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	12:57:13.858119-0500	VoiceOver	[0x707d6e800] invalidated after the last release of the connection object
default	12:57:13.871669-0500	VoiceOver	System appearance change
default	12:57:13.871833-0500	VoiceOver	Current system appearance, (HLTB: 1), (SLS: 0)
default	12:57:13.872113-0500	VoiceOver	Invalidate NSApp effectiveAppearance
default	12:57:13.872993-0500	VoiceOver	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x706c5d040
 (
    "<NSAquaAppearance: 0x706c5d220>",
    "<NSSystemAppearance: 0x706c5d180>"
)>
default	12:57:13.880346-0500	UIKitSystem	Application accessibility enabled: 0, (
	0   libAccessibility.dylib              0x00000001bc4e216c _AXSApplicationAccessibilitySetEnabled + 84
	1   libAccessibility.dylib              0x00000001bc4faa40 _AXSVoiceOverTouchSetEnabled + 368
	2   FuseBoard                           0x000000029abff42c -[FUAccessibilityServer _queue_applySettingWithKey:] + 696
	3   FuseBoard                           0x000000029ac013ec __76-[FUAccessibilityServer _handleApplicationAccessibilityChangedNotification:]_block_invoke + 708
	4   libdispatch.dylib                   0x0000000196bb0b5c _dispatch_call_block_and_release + 32
	5   libdispatch.dylib                   0x0000000196bcaad4 _dispatch_client_callout + 16
	6   libdispatch.dylib                   0x0000000196bb94e8 _dispatch_lane_serial_drain + 740
	7   libdispatch.dylib                   0x0000000196bb9ff8 _dispatch_lane_invoke + 440
	8   libdispatch.dylib                   0x0000000196bbb308 _dispatch_workloop_invoke + 1612
	9   libdispatch.dylib                   0x0000000196bc4474 _dispa
default	12:57:13.878663-0500	VoiceOver	defer invalidatation: (
    "<AXVRotorWindow: 0x70704d680, >"
)
default	12:57:13.886270-0500	VoiceOver	Current system appearance, (HLTB: 1), (SLS: 0)
default	12:57:14.047804-0500	VoiceOver	[0x707d6f200] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	12:57:14.151235-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474875920 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:57:14.168890-0500	powerd	Process VoiceOver.61431 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474875921 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	12:57:14.196980-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	12:57:14.197299-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	12:57:14.197323-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	12:57:14.196880-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:57:14.197423-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x7074da800 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	12:57:14.197823-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 1
fault	12:57:14.197444-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	12:57:14.197907-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	12:57:14.197940-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	12:57:14.198256-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	12:57:14.198271-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x706a36a18, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	12:57:14.214540-0500	VoiceOver	AQSTL aq(0x7074da800) start time resolved to: 4812109 ioTS st: 4812109 ht: 32602.676838
error	12:57:14.226824-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	12:57:14.831805-0500	intelligencecontextd	starting RequestID(61364:25 = 263556373151769) for client Spotlight: RequestParameters(timeout: 0.75 sec, requestedComponents: (commands), targetedAppBundleIdentifiers: ["com.apple.VoiceOver"], appIntentsRequest: AppIntentsRequest())
default	12:57:15.245804-0500	powerd	Process VoiceOver.61431 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474875921 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	12:57:15.250281-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	12:57:15.273343-0500	WindowServer	Connection removed: IOHIDEventSystemConnection uuid:336206AB-338D-4D00-B12B-8E90A3232605 pid:61431 process:VoiceOver type:Rate Controlled entitlements:0xa caller:ScreenReader: -[SCREventFactory completeInitialization] + 1196 attributes:(null) state:0x1 events:0 mask:0x0 dropped:0 dropStatus:0 droppedMask:0x0 lastDroppedTime:NONE
default	12:57:15.272969-0500	VoiceOver	Released connection: 336206AB-338D-4D00-B12B-8E90A3232605
{
    UUID = "336206AB-338D-4D00-B12B-8E90A3232605";
    caller = "ScreenReader: -[SCREventFactory completeInitialization] + 1196";
    dispatchQueue = 0;
    eventCount = 0;
    eventMask = 0;
    port = 125955;
    resetCount = 0;
    runloop = 0;
    services =     (
        4294969136
    );
    virtualServices =     (
    );
}
default	12:57:15.273307-0500	VoiceOver	OSErr AERemoveEventHandler(AEEventClass, AEEventID, AEEventHandlerUPP, Boolean)(aevt,quit handler=0x68450002757cb1c8 isSys=YES) err=0/noErr
default	12:57:15.845365-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	12:57:15.855320-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	12:57:15.855448-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x7074da800; ; [61431]; play>; running count now 0
default	12:57:16.781151-0500	VoiceOver	[0x707d6ed00] activating connection: mach=true listener=false peer=false name=com.apple.powerlog.plxpclogger.xpc
default	12:57:16.781193-0500	VoiceOver	Entering exit handler.
default	12:57:16.781203-0500	VoiceOver	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	12:57:16.781254-0500	VoiceOver	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	12:57:16.781260-0500	VoiceOver	[0x707050640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	12:57:16.781275-0500	VoiceOver	Exiting exit handler.
default	12:57:16.781384-0500	VoiceOver	XPC connection invalidated (daemon unloaded/disabled)
default	12:57:16.784616-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x10b10b (VoiceOver) connectionID: 7E33B pid: 61431 in session 0x101
default	12:57:16.784646-0500	WindowServer	<BSCompoundAssertion:0x76cc11580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x10b10b (VoiceOver) acq:0x76fcac3e0 count:1
default	12:57:16.788999-0500	WindowManager	Connection invalidated | (61431) VoiceOver
default	12:57:16.790142-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f500f","name":"VoiceOver(61431)"}, "details":null }
default	12:57:16.790174-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f500f from AudioApp, recording state unchanged (app: {"name":"[implicit] VoiceOver","pid":61431})
default	12:57:16.790184-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] VoiceOver","pid":61431})
default	12:57:16.790482-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 16 stopping playing
default	12:57:16.790534-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	12:57:16.790584-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	12:57:16.790693-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 16, PID = 61431, Name = sid:0x1f500f, VoiceOver(61431), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	12:57:16.791194-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:57:16.791263-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:57:16.791292-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:57:16.791316-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 1
default	12:57:16.790815-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:57:16.791060-0500	audiomxd	UpdateAudioState CID 0x89380001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	12:57:16.790729-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x10b10b removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10b10b (VoiceOver)"
)}
default	12:57:16.793993-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xeff7 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10b10b (VoiceOver)"
)}
default	12:57:16.797471-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: updated frontmost process - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x10b10b (VoiceOver)"
)}
default	12:57:16.800054-0500	runningboardd	XPC connection invalidated: [osservice<com.apple.VoiceOver(501)>:61431]
default	12:57:16.800550-0500	runningboardd	Invalidating assertion 404-366-23580 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.coreservices.launchservicesd>:366]
default	12:57:16.801122-0500	runningboardd	XPC connection invalidated: [osservice<com.apple.VoiceOver(501)>:61431]
default	12:57:16.801657-0500	runningboardd	Invalidating assertion 404-366-23581 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.coreservices.launchservicesd>:366]
default	12:57:16.803702-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
error	12:57:16.807996-0500	runningboardd	RBSStateCapture remove item called for untracked item <RBConnectionClient| 61431 name:osservice<com.apple.VoiceOver(501)> entitlements:<RBEntitlements| [
			com.apple.assertiond.app-state-monitor,
			com.apple.private.security.container-required
			]> inheritanceManager:<RBClientInheritanceManager|  inheritances:[
	<RBSInheritance| environment:(none) name:com.apple.launchservices.userfacing origID:404-366-22917 0>,
	<RBSInheritance| environment:(none) name:com.apple.launchservices.userfacing origID:404-366-23580 0>,
	<RBSInheritance| environment:(none) name:com.apple.launchservices.userfacing origID:404-366-23580 0>
	]>>
default	12:57:16.808072-0500	runningboardd	Invalidating assertion 404-337-23543 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.powerd>:337]
default	12:57:16.808393-0500	runningboardd	Invalidating assertion 404-396-22922 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.WindowServer(88)>:396]
default	12:57:16.812006-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.apple.VoiceOver with asn: LSASN:{hi=0x0;lo=0x10b10b} for bundle path: /System/Library/CoreServices/VoiceOver.app with URL: file:///System/Library/CoreServices/VoiceOver.app/
default	12:57:16.812047-0500	loginwindow	-[Application setState:] | enter: <Application: 0xaa0802620: VoiceOver> state 3
default	12:57:16.812078-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:VoiceOver, _appTrackingState = 2
default	12:57:16.813834-0500	loginwindow	-[Application setState:] | enter: <Application: 0xaa0802620: VoiceOver> state 4
default	12:57:16.813848-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:VoiceOver, _appTrackingState = 2
default	12:57:16.815804-0500	runningboardd	Invalidating assertion 404-366-22917 (target:[osservice<com.apple.VoiceOver(501)>:61431]) from originator [osservice<com.apple.coreservices.launchservicesd>:366]
default	12:57:16.833442-0500	runningboardd	[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441] termination reported by launchd (2, 15, 15)
default	12:57:16.833432-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:61431] termination reported by launchd (0, 0, 0)
default	12:57:16.833493-0500	runningboardd	Removing process: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]
default	12:57:16.833587-0500	runningboardd	Removing process: [osservice<com.apple.VoiceOver(501)>:61431]
default	12:57:16.833714-0500	runningboardd	Removing assertions for terminated process: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]
default	12:57:16.833755-0500	runningboardd	Removed last relative-start-date-defining assertion for process xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}
default	12:57:16.833786-0500	runningboardd	removeJobWithInstance called for identity without existing job [osservice<com.apple.VoiceOver(501)>:61431]
default	12:57:16.834029-0500	runningboardd	Removing assertions for terminated process: [osservice<com.apple.VoiceOver(501)>:61431]
default	12:57:16.852969-0500	runningboardd	XPC connection invalidated: [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:61431])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:61441]
