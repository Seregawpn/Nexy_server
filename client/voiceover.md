default	11:51:50.416016-0500	VoiceOver	No list of permitted front apps returned
default	11:51:50.416174-0500	VoiceOver	No list of permitted front apps returned
default	11:51:50.448431-0500	VoiceOver	[0x984116080] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:51:50.448574-0500	VoiceOver	[0x984116080] invalidated after the last release of the connection object
default	11:51:50.449949-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dc1080, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:51:50.450548-0500	VoiceOver	AudioConverter -> 0x983dc1080: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:51:50.450561-0500	VoiceOver	AudioConverter -> 0x983dc1080: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:51:50.462805-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dc0d80, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:51:50.462857-0500	VoiceOver	AudioConverter -> 0x983dc0d80: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:51:50.462969-0500	VoiceOver	AudioConverter -> 0x983dc0d80: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:51:50.464997-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:51:50.474033-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:51:50.474376-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:51:50.475941-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474876683 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:50.476465-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876684 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:51:50.508275-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:51:50.508881-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:51:50.509149-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:50.509412-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:51:50.509645-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:51:50.509671-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:51:50.509706-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:51:50.509906-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:51:50.509970-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	11:51:50.510004-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:51:50.510519-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:51:50.510534-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:51:50.526779-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 152118 ioTS st: 152118 ht: 23628.875428
error	11:51:50.553549-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:51:51.017216-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:51:51.198210-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:51:51.200225-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:51:51.201375-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:51:51.749689-0500	VoiceOver	[0x984116080] activating connection: mach=true listener=false peer=false name=mul-xpc (Apple)_OpenStep
default	11:51:51.749995-0500	VoiceOver	[0x984115e00] activating connection: mach=true listener=false peer=false name=com.apple.naturallanguaged
default	11:51:52.309079-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876684 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:52.313731-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876685 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	11:51:52.363893-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:51:52.459462-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:51:52.459974-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:51:52.460063-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:51:52.493674-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:51:52.501673-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:51:52.501830-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:51:52.505124-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876685 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:52.505646-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876686 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:51:52.505439-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:51:52.508222-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	11:51:52.524745-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:51:52.525465-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:51:52.525528-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:52.525672-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:51:52.525700-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:51:52.525742-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	11:51:52.525799-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:52.525901-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:51:52.525955-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	11:51:52.525994-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:51:52.526210-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:51:52.526226-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:51:52.542799-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 196571 ioTS st: 196571 ht: 23630.891428
error	11:51:52.543479-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:51:52.895519-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876686 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:53.108580-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:51:53.138629-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:51:53.139277-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:51:53.139415-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:51:53.176171-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876687 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:51:53.176516-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	11:51:53.199775-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:51:53.357139-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:51:53.357971-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:51:53.358144-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:51:53.386459-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:51:53.396918-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:51:53.396998-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:51:53.398379-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876687 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:53.399776-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876688 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:51:53.419500-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:51:53.420047-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:51:53.420391-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:53.420506-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:51:53.420795-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:51:53.420835-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:51:53.420896-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:51:53.421313-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:51:53.421394-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	11:51:53.421441-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:51:53.421741-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:51:53.421761-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:51:53.438766-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 216328 ioTS st: 216328 ht: 23631.787428
error	11:51:53.442082-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:51:53.618513-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:51:53.619185-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:51:53.619304-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:51:53.633533-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:51:53.641953-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:51:53.642034-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:51:53.643680-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876688 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:53.644221-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876689 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:51:53.662785-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:51:53.663502-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:51:53.663763-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:53.663872-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:51:53.664072-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:51:53.664098-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:51:53.664144-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:51:53.664314-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:51:53.664376-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	11:51:53.664421-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:51:53.664657-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:51:53.664674-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:51:53.684153-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 221738 ioTS st: 221738 ht: 23632.032761
error	11:51:53.686661-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:51:53.748584-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:51:53.749182-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:51:53.749283-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:51:53.803976-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:51:53.812688-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:51:53.812789-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:51:53.813983-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876689 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:53.814831-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876690 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:51:53.834300-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:51:53.834561-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:51:53.834810-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:53.834969-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:51:53.835135-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:51:53.835161-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:51:53.835190-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:51:53.835310-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:51:53.835359-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	11:51:53.835387-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:51:53.835567-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:51:53.835582-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:51:53.854690-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 225502 ioTS st: 225502 ht: 23632.203428
error	11:51:53.859617-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:51:54.025737-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:51:54.570900-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876690 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:54.783229-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:51:55.098978-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876691 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:51:55.107626-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	11:51:55.340133-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:51:55.997972-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:51:55.999291-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:51:55.999351-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:51:56.026448-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876691 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:56.026808-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876692 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:51:56.083396-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:51:56.083934-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:56.084054-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:51:56.084184-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:56.084242-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:51:56.084266-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:51:56.084292-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:51:56.084431-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:51:56.084486-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	11:51:56.084513-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:51:56.084717-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:51:56.084733-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:51:56.105298-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 275130 ioTS st: 275130 ht: 23634.454095
error	11:51:56.130903-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:51:56.289114-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:51:56.289732-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:51:56.289829-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:51:56.351161-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:51:56.362082-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:51:56.362144-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:51:56.365597-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876692 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:56.365916-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876693 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:51:56.392699-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:51:56.392981-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:51:56.393210-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:56.393340-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:51:56.393842-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:51:56.393871-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:51:56.393901-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:51:56.394051-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:51:56.394110-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	11:51:56.394139-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:51:56.394332-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:51:56.394346-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:51:56.414683-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 281951 ioTS st: 281951 ht: 23634.763428
error	11:51:56.425256-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:51:57.023667-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:51:57.567689-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876693 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:57.778238-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
fault	11:51:57.959273-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:57.952581-0500	VoiceOver	No list of permitted front apps returned
default	11:51:58.054222-0500	VoiceOver	No list of permitted front apps returned
default	11:51:58.054378-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:51:58.054771-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:51:58.054855-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:51:58.100630-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:51:58.100754-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:51:58.102432-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984dafab0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:51:58.102454-0500	VoiceOver	AudioConverter -> 0x984dafab0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:51:58.102464-0500	VoiceOver	AudioConverter -> 0x984dafab0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:51:58.117734-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876694 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:51:58.118566-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	11:51:58.234708-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:51:58.525463-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:51:58.526110-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:51:58.526206-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:51:58.570415-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:51:58.570729-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:51:59.597378-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:51:59.604531-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:51:59.604588-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:51:59.609894-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876694 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:51:59.610594-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876695 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:51:59.644309-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:51:59.645149-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:51:59.645145-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:59.645368-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:51:59.645395-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:51:59.645437-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	11:51:59.645498-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:51:59.645606-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:51:59.645699-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	11:51:59.645739-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:51:59.645977-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:51:59.645993-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:51:59.657404-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 353452 ioTS st: 353452 ht: 23638.006095
error	11:51:59.707580-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:00.024147-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:01.754192-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 24899
fault	11:52:02.570168-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:02.581536-0500	VoiceOver	No list of permitted front apps returned
default	11:52:02.682370-0500	VoiceOver	No list of permitted front apps returned
default	11:52:02.684082-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:02.684657-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:02.684746-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:02.696799-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:02.696969-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:02.706497-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:02.706707-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:52:02.731307-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:52:02.740827-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:02.740885-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:02.742443-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474876695 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:02.742939-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876696 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:02.781694-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:52:02.782602-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:02.783726-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:02.784092-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:02.784198-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:02.784477-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:02.784940-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
fault	11:52:02.784003-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:02.785059-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:02.785455-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:02.785476-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	11:52:02.786186-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:02.804023-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 422836 ioTS st: 422836 ht: 23641.152761
error	11:52:02.902007-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:03.024148-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:04.722177-0500	VoiceOver	No list of permitted front apps returned
default	11:52:04.854681-0500	VoiceOver	No list of permitted front apps returned
default	11:52:05.004734-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:05.005585-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:05.005764-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:05.084112-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:05.084414-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:52:05.122361-0500	VoiceOver	No list of permitted front apps returned
default	11:52:05.122769-0500	VoiceOver	No list of permitted front apps returned
default	11:52:05.134629-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:05.146065-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:05.171190-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:05.171602-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:05.196129-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:52:05.205106-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:05.205236-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:05.221450-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474876696 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:05.223223-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876704 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:05.281718-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:52:05.283341-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:05.283679-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:05.283749-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:05.283871-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:05.284121-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:05.284296-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	11:52:05.284436-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:05.284955-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:05.285057-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	11:52:05.480567-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:06.024152-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:07.289716-0500	VoiceOver	No list of permitted front apps returned
default	11:52:07.289900-0500	VoiceOver	No list of permitted front apps returned
default	11:52:07.304256-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:07.304416-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:52:07.331002-0500	VoiceOver	No list of permitted front apps returned
default	11:52:07.432306-0500	VoiceOver	No list of permitted front apps returned
default	11:52:07.433828-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:07.434313-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:07.434396-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:07.439750-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:07.439923-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:07.450572-0500	VoiceOver	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	11:52:07.453083-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:08.452584-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 24908
default	11:52:08.453027-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 24908
default	11:52:09.024105-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:10.751584-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474876704 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:10.753082-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:52:10.768656-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876719 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:10.779741-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	11:52:10.890630-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:11.632728-0500	VoiceOver	No list of permitted front apps returned
fault	11:52:11.635689-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:11.734214-0500	VoiceOver	No list of permitted front apps returned
default	11:52:11.746722-0500	VoiceOver	No list of permitted front apps returned
default	11:52:11.763734-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984db0f90, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:11.763751-0500	VoiceOver	AudioConverter -> 0x984db0f90: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:11.763761-0500	VoiceOver	AudioConverter -> 0x984db0f90: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:11.767004-0500	VoiceOver	No list of permitted front apps returned
default	11:52:11.768795-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:11.769206-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:11.769267-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:11.788918-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:11.789024-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:52:11.823518-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:11.823630-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:11.830593-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984d4e100, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:11.830616-0500	VoiceOver	AudioConverter -> 0x984d4e100: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:11.830624-0500	VoiceOver	AudioConverter -> 0x984d4e100: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:11.836673-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:52:11.840306-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:52:11.846016-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:52:11.849785-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:11.849818-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:11.856384-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876719 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:11.856758-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876737 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:11.896198-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:11.896538-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:11.896828-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:52:11.896868-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:11.897018-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:11.897042-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:11.897074-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:11.897228-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:11.897284-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	11:52:11.897319-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:11.897526-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:11.897541-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:11.913388-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 623697 ioTS st: 623697 ht: 23650.262095
default	11:52:12.024499-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
error	11:52:12.026065-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:13.342995-0500	VoiceOver	No list of permitted front apps returned
fault	11:52:13.347202-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:13.372894-0500	VoiceOver	No list of permitted front apps returned
default	11:52:13.410029-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:13.410604-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:13.410674-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:13.444709-0500	VoiceOver	No list of permitted front apps returned
default	11:52:13.445554-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:13.445768-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:52:13.457324-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:13.457474-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:13.459492-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984db2e20, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:13.459517-0500	VoiceOver	AudioConverter -> 0x984db2e20: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:13.459537-0500	VoiceOver	AudioConverter -> 0x984db2e20: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:13.476007-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 512
default	11:52:13.481874-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:13.481935-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:13.494528-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474876737 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:13.495034-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474876739 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:13.544245-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:13.544847-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:13.545211-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:52:13.545312-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:13.545856-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:13.545897-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:13.545952-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:13.546206-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:13.546284-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 512
default	11:52:13.546436-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:13.546799-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:13.546825-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:13.566915-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 660154 ioTS st: 660154 ht: 23651.915428
default	11:52:13.613949-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:13.616035-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(805)
default	11:52:13.616261-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:805 called from <private>
default	11:52:13.616297-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:805 called from <private>
default	11:52:13.624748-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:52:13.625268-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:52:13.666766-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984d4fae0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:52:13.666897-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:52:13.667015-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:52:13.667809-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:13.668538-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x100c06d80) Device ID: 85 (Input:No | Output:Yes): true
default	11:52:13.668596-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x100c06d80)
default	11:52:13.697362-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984d4fde0, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	11:52:13.705925-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x984838000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	11:52:13.706357-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:52:13.696824-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:52:13.707451-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:13.707767-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:13.707791-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:13.707848-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:13.708069-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:13.783246-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:52:13.783415-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:52:13.783947-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
error	11:52:13.824898-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	11:52:14.286659-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:14.287106-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:14.288141-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:14.288682-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:15.023538-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:15.368628-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:15.367831-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:15.370413-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:15.458460-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:15.459414-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:15.459109-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:16.415369-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:16.416821-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(805)
default	11:52:16.416855-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:805 called from <private>
fault	11:52:16.416596-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:16.416865-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:805 called from <private>
default	11:52:16.417467-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:52:16.422097-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:52:16.422185-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:52:16.423571-0500	runningboardd	Invalidating assertion 394-24873-16568 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.VoiceOver(501)>:24873]
default	11:52:16.431541-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:16.431576-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:16.431974-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:16.432002-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:52:16.432008-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:52:16.432121-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(805)
default	11:52:16.432142-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:805 called from <private>
default	11:52:16.432502-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:805 called from <private>
default	11:52:16.434324-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:16.434427-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:16.434494-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:16.435148-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:52:16.435184-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:52:16.435261-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:16.435296-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:16.435316-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:52:16.436686-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:52:16.436774-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
error	11:52:16.436806-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	11:52:16.436837-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:16.436885-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:16.436897-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:16.436913-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:16.436321-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.VoiceOver(501)>:24873] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-24873-16588 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:52:16.436597-0500	runningboardd	Assertion 394-24873-16588 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:52:16.437268-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:16.437319-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:16.437331-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:16.437442-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:16.437493-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:16.437874-0500	runningboardd	Invalidating assertion 394-24873-16588 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.VoiceOver(501)>:24873]
default	11:52:16.451419-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:16.451453-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:16.451590-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:16.458939-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:16.459297-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:16.459311-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:16.459403-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:16.459413-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:16.459420-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:16.459428-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:16.459577-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:16.459826-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:16.460006-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:16.460118-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:16.460191-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:16.460268-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:16.460356-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:16.460655-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:16.465691-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:16.465744-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
error	11:52:16.467272-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	11:52:16.467283-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:804 called from <private>
default	11:52:16.468231-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:16.468496-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:52:16.468673-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:16.468862-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:52:16.469564-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:52:16.467772-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.VoiceOver(501)>:24873] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-24873-16589 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:52:16.469540-0500	runningboardd	Assertion 394-24873-16589 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:52:16.471554-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x100c06d80) Device ID: 85 (Input:No | Output:Yes): true
default	11:52:16.472007-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x100c06d80)
default	11:52:16.473834-0500	runningboardd	Invalidating assertion 394-24873-16589 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.VoiceOver(501)>:24873]
default	11:52:16.474111-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.VoiceOver(501)>:24873] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-24873-16590 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:52:16.474224-0500	runningboardd	Assertion 394-24873-16590 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:52:16.473226-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:52:16.473243-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:52:16.473279-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:52:16.473360-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:52:16.473427-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
error	11:52:16.684364-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	11:52:17.128765-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	11:52:17.171452-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:804 called from <private>
default	11:52:17.172096-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984d4fae0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:52:17.172132-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:52:17.172239-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:52:17.172589-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:17.172756-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:52:17.172772-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:52:17.172781-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:52:17.172899-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x100c06d80) Device ID: 85 (Input:No | Output:Yes): true
default	11:52:17.172910-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x100c06d80)
default	11:52:17.173010-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:52:17.173023-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:52:17.173032-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:52:17.173047-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:52:17.173057-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:52:17.173454-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984d4fae0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:52:17.173475-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:52:17.173557-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:52:17.173887-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:17.174032-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:52:17.174052-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:52:17.174060-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:52:17.174089-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x984591818 (1C-77-54-18-C8-A3:output): Output stream format changed
default	11:52:17.174101-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x984591818 (1C-77-54-18-C8-A3:output): Output stream format changed
default	11:52:17.174808-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984d4fde0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:52:17.175400-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:17.175692-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:17.176069-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:17.176361-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:17.176594-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:17.176873-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:17.176913-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:17.177313-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x984838000:
default	11:52:17.177372-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	11:52:17.177381-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	11:52:17.177397-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	11:52:17.177437-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	11:52:17.177467-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	11:52:17.177767-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:17.177804-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:17.177943-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x984838000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	11:52:17.178332-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:17.178642-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:17.178960-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:17.179296-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:17.179567-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:17.179603-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:17.179653-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:17.179828-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:17.179904-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:17.179951-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:17.180243-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:17.180269-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:17.986771-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
fault	11:52:19.301120-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:19.302592-0500	VoiceOver	No list of permitted front apps returned
default	11:52:19.372498-0500	VoiceOver	No list of permitted front apps returned
default	11:52:19.382641-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984d4ff30, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:19.382662-0500	VoiceOver	AudioConverter -> 0x984d4ff30: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:19.382673-0500	VoiceOver	AudioConverter -> 0x984d4ff30: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:19.387732-0500	VoiceOver	No list of permitted front apps returned
default	11:52:19.390500-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:19.390935-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:19.391016-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:19.406824-0500	VoiceOver	No list of permitted front apps returned
default	11:52:19.410757-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:19.410914-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:19.432982-0500	VoiceOver	No list of permitted front apps returned
default	11:52:19.433137-0500	VoiceOver	No list of permitted front apps returned
default	11:52:19.434613-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:19.434706-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:52:19.437674-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:19.437743-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:52:19.445226-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:52:19.448453-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:52:19.452438-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:19.462476-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:19.462512-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:19.464652-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474876739 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:19.465257-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877085 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:19.518043-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:19.518363-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:19.518687-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:52:19.518683-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:19.518898-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:19.518920-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:19.518949-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:19.519124-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:19.519182-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:19.519213-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:19.519414-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:19.519429-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:19.531682-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 791667 ioTS st: 791667 ht: 23657.879730
error	11:52:19.693720-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:20.785657-0500	VoiceOver	No list of permitted front apps returned
fault	11:52:20.788794-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:20.795530-0500	VoiceOver	No list of permitted front apps returned
default	11:52:20.831341-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:20.831809-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:20.832015-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:20.837470-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:20.837599-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:20.847249-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:20.847444-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:52:20.848723-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984d4e790, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:20.848767-0500	VoiceOver	AudioConverter -> 0x984d4e790: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:20.848789-0500	VoiceOver	AudioConverter -> 0x984d4e790: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:20.862448-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:20.872071-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:20.872133-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:20.935820-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:20.936093-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:20.936386-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:20.936491-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:20.936686-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:20.936707-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:20.936734-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:20.936862-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:20.936920-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:20.936944-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:20.937139-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:20.937151-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:20.951669-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 822978 ioTS st: 822978 ht: 23659.299730
default	11:52:21.023964-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
error	11:52:21.027968-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:24.024044-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:25.941948-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:25.942224-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:52:26.269571-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:26.269881-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:52:27.024570-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:27.241249-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:27.241456-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:52:27.893399-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:07  id:21474877086 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:28.099675-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:52:28.413206-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877087 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:28.413530-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	11:52:28.632237-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:29.999506-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
fault	11:52:29.001039-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:29.005265-0500	runningboardd	Invalidating assertion 394-24873-16590 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.VoiceOver(501)>:24873]
default	11:52:29.002513-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:52:29.002604-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:52:29.002954-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(805)
default	11:52:29.002995-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:805 called from <private>
default	11:52:29.003012-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:805 called from <private>
default	11:52:29.007219-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:29.007318-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:29.007545-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:29.007587-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:52:29.007662-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:52:29.012801-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:29.015769-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea011, Nexy(24908), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:52:29.013147-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:29.013394-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:29.018831-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.VoiceOver(501)>:24873] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-24873-16599 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:52:29.019035-0500	runningboardd	Assertion 394-24873-16599 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:52:29.016410-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:52:29.016462-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:52:29.016506-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:29.016549-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:29.016580-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:52:29.020335-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:52:29.020060-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(805)
default	11:52:29.020539-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:52:29.021059-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:805 called from <private>
default	11:52:29.021477-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:29.021557-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:805 called from <private>
error	11:52:29.021312-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	11:52:29.021944-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:29.021989-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:29.022023-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:29.022454-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:29.022654-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:29.022665-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:29.022665-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:29.022797-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:29.028505-0500	runningboardd	Invalidating assertion 394-24873-16599 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.VoiceOver(501)>:24873]
default	11:52:29.038758-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:29.038789-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:29.038943-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:29.042561-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:29.042803-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:29.042812-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:29.042887-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:29.042901-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:29.042978-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:29.043011-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:29.043082-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:52:29.043287-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x100c06d80) Device ID: 85 (Input:No | Output:Yes): true
default	11:52:29.043312-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x100c06d80)
default	11:52:29.043534-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	11:52:29.043627-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:52:29.043720-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
error	11:52:29.043848-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	11:52:29.043967-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:52:29.043987-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:804 called from <private>
default	11:52:29.044003-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:52:29.044009-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:52:29.044049-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:52:29.044087-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:29.044112-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:29.044145-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:29.044261-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:29.046520-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983e04720, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	11:52:29.046668-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:52:29.046840-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:52:29.047411-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:29.047657-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:52:29.047878-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:52:29.053642-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:29.077508-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:29.077961-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:52:29.078238-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:52:29.077817-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:52:29.077843-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:52:29.077855-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:52:29.077881-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x984591818 (1C-77-54-18-C8-A3:output): Output stream format changed
default	11:52:29.077891-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x984591818 (1C-77-54-18-C8-A3:output): Output stream format changed
default	11:52:29.085223-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:29.085506-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:29.085541-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:29.085591-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:29.085803-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:29.086056-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:29.086107-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:29.349664-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea011, Nexy(24908), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:52:29.350511-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:52:29.350632-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:52:29.350663-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:52:29.352070-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:52:29.565726-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 24917
default	11:52:29.566175-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 24917
fault	11:52:29.644821-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:29.645333-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:29.646478-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:29.647207-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:30.024396-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:30.629005-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983e04630, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:30.629035-0500	VoiceOver	AudioConverter -> 0x983e04630: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:30.629050-0500	VoiceOver	AudioConverter -> 0x983e04630: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:30.650202-0500	VoiceOver	No list of permitted front apps returned
default	11:52:30.652048-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:30.652726-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:30.652834-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:30.656770-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:30.657002-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:30.701065-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:30.701262-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:52:30.701715-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984dac450, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:30.701738-0500	VoiceOver	AudioConverter -> 0x984dac450: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:30.701750-0500	VoiceOver	AudioConverter -> 0x984dac450: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:30.714729-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983e1f480, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:30.714744-0500	VoiceOver	AudioConverter -> 0x983e1f480: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:30.714751-0500	VoiceOver	AudioConverter -> 0x983e1f480: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:30.719234-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:30.735969-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:30.736011-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:30.756242-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474877087 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:30.756604-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877263 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:30.833048-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:30.833316-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:30.833571-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:30.833689-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:30.833880-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:30.833900-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:30.833926-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:30.834031-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:30.834089-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:30.834115-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:30.834314-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:30.834331-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:31.126665-0500	VoiceOver	No list of permitted front apps returned
default	11:52:31.135987-0500	VoiceOver	No list of permitted front apps returned
default	11:52:31.136056-0500	VoiceOver	Application set focus not permitted for (null)
default	11:52:31.151243-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:31.151835-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:31.151904-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:31.169909-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:31.170088-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:52:31.227179-0500	VoiceOver	No list of permitted front apps returned
default	11:52:31.268102-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:31.268378-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:31.268683-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:31.268726-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:31.268913-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:31.268935-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:31.268969-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:31.269085-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:31.269138-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:31.269167-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:31.269382-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:31.269397-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:31.773824-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:31.775270-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(805)
default	11:52:31.775309-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:805 called from <private>
default	11:52:31.775316-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:805 called from <private>
default	11:52:31.777045-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:52:31.777127-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
fault	11:52:31.774708-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:31.780798-0500	runningboardd	Invalidating assertion 394-24873-16603 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.VoiceOver(501)>:24873]
default	11:52:31.787621-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(805)
default	11:52:31.787671-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:805 called from <private>
default	11:52:31.787683-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:805 called from <private>
default	11:52:31.788794-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:52:31.795669-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:31.795696-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:31.806613-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:52:31.806649-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:52:31.806790-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:31.808310-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:31.808521-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:52:31.808531-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:52:31.808667-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:31.811491-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:31.811952-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:31.811971-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:31.813936-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:52:31.814021-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:52:31.814088-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:52:31.814146-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:52:31.814193-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:52:31.814212-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:31.814254-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:52:31.814346-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:52:31.814371-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:52:31.814404-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:52:31.814573-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:52:31.814699-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:52:31.814795-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:52:31.821497-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:31.821554-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:52:31.821628-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:52:31.821795-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:52:31.821810-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:52:31.821819-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:52:31.821829-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:52:31.821933-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:52:31.822387-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x100c06d80) Device ID: 85 (Input:No | Output:Yes): true
default	11:52:31.822448-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x100c06d80)
error	11:52:31.822851-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	11:52:31.822896-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:804 called from <private>
default	11:52:31.822926-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:52:31.822984-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:52:31.823790-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:52:31.823807-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:52:31.823964-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:52:31.824073-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:52:31.833982-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.VoiceOver(501)>:24873] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-24873-16626 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:52:31.834062-0500	runningboardd	Assertion 394-24873-16626 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:52:32.018289-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 24923
default	11:52:32.023377-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 24923
default	11:52:32.094019-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 24924
default	11:52:32.564827-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	11:52:32.611745-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:804 called from <private>
default	11:52:32.611772-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:804 called from <private>
default	11:52:32.611917-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
fault	11:52:32.612483-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:32.613668-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:52:32.613681-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:52:32.613867-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:32.613940-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:32.614003-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:52:32.614031-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:52:32.614056-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:52:32.614286-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x100c06d80) Device ID: 85 (Input:No | Output:Yes): true
default	11:52:32.614598-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x100c06d80)
default	11:52:32.614820-0500	runningboardd	Invalidating assertion 394-24873-16626 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.VoiceOver(501)>:24873]
default	11:52:32.615027-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.VoiceOver(501)>:24873] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-24873-16642 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:52:32.615132-0500	runningboardd	Assertion 394-24873-16642 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:52:32.614706-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:52:32.614732-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:52:32.614758-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:52:32.614794-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:52:32.614823-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
error	11:52:32.616980-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
error	11:52:32.624114-0500	VoiceOver	               AQMEIO.cpp:201   timed out after 0.010s (4100 4100); suspension count=0 (IOSuspensions: , , , , , , , , , , , , ) (maybe stale)
default	11:52:32.624377-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:32.624418-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:32.634902-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877265 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:32.635710-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877440 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:32.950635-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:33.198471-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:804 called from <private>
default	11:52:33.198954-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:52:33.199009-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983e04720, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:52:33.199028-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:52:33.199115-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:52:33.199445-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:33.199594-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
fault	11:52:33.199383-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:33.199645-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:52:33.199675-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:52:33.199718-0500	VoiceOver	           AQMEIO_HAL.cpp:3593  0x984591818 (1C-77-54-18-C8-A3:output): lock contended, setting stream format change pending
default	11:52:33.199918-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:33.200148-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:33.200192-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:33.200265-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:33.202393-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	11:52:33.202414-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	11:52:33.222227-0500	VoiceOver	          AQMixEngine.cpp:1491  ->AQMixEngine_Base(0x985e23c00)::AddRunningClient <AudioQueueObject@0x984838000; ; [24873]; play>, retry count 1
default	11:52:33.222407-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x984838000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	11:52:33.222729-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:52:33.238727-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 1093907 ioTS st: 1093907 ht: 23671.586779
default	11:52:35.349149-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:35.349220-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:36.029272-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:36.223571-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:36.223731-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:52:36.247229-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:36.247533-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:52:36.256021-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:52:36.285582-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	11:52:36.285142-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877443 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:36.331068-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:36.332638-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:36.332319-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:36.332597-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:36.332634-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	11:52:36.332984-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:36.332753-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:36.333090-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:36.333161-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:36.333209-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:36.333509-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:36.333528-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:36.337208-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:36.337363-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:52:36.554126-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 2c00000025 pid: 24944
default	11:52:36.555509-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 360000002d pid: 24944
default	11:52:37.812764-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:37.812956-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:52:38.878079-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:52:38.880646-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:38.889189-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:38.889233-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:38.896899-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474877443 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:52:38.897351-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877464 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:52:38.907000-0500	VoiceOver	No list of permitted front apps returned
default	11:52:38.907207-0500	VoiceOver	No list of permitted front apps returned
default	11:52:38.924850-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:38.924956-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:52:38.927767-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:52:38.928410-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:52:38.928487-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:38.928606-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:38.928628-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:38.928658-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	11:52:38.928755-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:38.928836-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:38.928906-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:38.928934-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:38.929138-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:38.929151-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:38.938899-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:38.949033-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:38.949069-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:38.949882-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877464 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:52:38.953365-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:38.953466-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:52:38.963562-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:38.963716-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:52:38.964739-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:52:38.967385-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:38.967466-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:38.969058-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877465 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:52:38.970350-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	11:52:38.979135-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dc9650, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:38.979154-0500	VoiceOver	AudioConverter -> 0x983dc9650: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:38.979962-0500	VoiceOver	AudioConverter -> 0x983dc9650: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:39.001307-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:39.001708-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:39.002036-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:52:39.002080-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:39.002271-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:39.002298-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:39.002336-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:39.002512-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:39.002573-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:39.002609-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:39.002892-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:39.002908-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:39.018841-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 1221357 ioTS st: 1221357 ht: 23677.366779
default	11:52:39.019606-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:39.020277-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:39.023947-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:39.040046-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:39.051877-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877465 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:52:39.052299-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877466 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:52:39.086656-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:39.087172-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:39.087641-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:52:39.087685-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:39.087937-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:39.087975-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:39.088030-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:39.088238-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:39.088319-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:39.088361-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:39.088648-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:39.088670-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:39.098892-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 1223122 ioTS st: 1223122 ht: 23677.446779
error	11:52:39.125777-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:39.957359-0500	VoiceOver	No list of permitted front apps returned
default	11:52:39.957632-0500	VoiceOver	No list of permitted front apps returned
default	11:52:39.989188-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:39.989394-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:40.000391-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dc8960, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:40.000420-0500	VoiceOver	AudioConverter -> 0x983dc8960: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:40.000433-0500	VoiceOver	AudioConverter -> 0x983dc8960: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:40.019690-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:52:40.025583-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984d4a640, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:40.025614-0500	VoiceOver	AudioConverter -> 0x984d4a640: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:40.025626-0500	VoiceOver	AudioConverter -> 0x984d4a640: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:40.034152-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:40.039674-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:40.039752-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:40.041970-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877466 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:52:40.042840-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877467 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:52:40.066293-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:40.066792-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:40.067152-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:52:40.067238-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:40.067377-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:40.067404-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:40.067462-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:40.067636-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:40.067698-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:40.067734-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:40.067974-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:40.067991-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:40.078733-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 1244731 ioTS st: 1244731 ht: 23678.426779
error	11:52:40.140631-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:40.146766-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:40.146878-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:41.504188-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:41.504297-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
fault	11:52:41.536400-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:41.540713-0500	VoiceOver	No list of permitted front apps returned
default	11:52:41.649074-0500	VoiceOver	No list of permitted front apps returned
default	11:52:41.696001-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:41.695789-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:41.723423-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:41.723692-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:52:41.750370-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:41.750587-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:52:41.753799-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dc9350, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:41.753953-0500	VoiceOver	AudioConverter -> 0x983dc9350: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:41.753997-0500	VoiceOver	AudioConverter -> 0x983dc9350: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:41.773031-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:41.779745-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:41.779808-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:41.790791-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877467 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:41.792140-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877470 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:41.834414-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:41.835134-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:41.835575-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:41.835644-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:41.835952-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:41.835982-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:41.836102-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:41.836406-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:41.836479-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:41.836519-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:41.836849-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:41.836864-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:42.023902-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:45.024000-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:48.023943-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:48.579752-0500	VoiceOver	No list of permitted front apps returned
default	11:52:48.650738-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:06  id:21474877470 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:48.652188-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:52:48.653645-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dcb660, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:48.653755-0500	VoiceOver	AudioConverter -> 0x983dcb660: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:48.653842-0500	VoiceOver	AudioConverter -> 0x983dcb660: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:48.655035-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:52:48.658922-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:52:48.680126-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877471 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:48.697261-0500	VoiceOver	No list of permitted front apps returned
default	11:52:48.697519-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:48.697762-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	11:52:48.698889-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:48.699085-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:48.745625-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:48.745929-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
error	11:52:48.782634-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:48.786840-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:48.789160-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:48.789191-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:48.831973-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:52:48.832627-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:52:48.832628-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:48.832837-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	11:52:48.832844-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:48.832859-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:48.832906-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:48.833069-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:48.833122-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:48.833153-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:48.833353-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:48.833367-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	11:52:48.890244-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:49.015018-0500	VoiceOver	No list of permitted front apps returned
default	11:52:49.030652-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:49.030853-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:52:49.032449-0500	VoiceOver	No list of permitted front apps returned
default	11:52:49.032641-0500	VoiceOver	No list of permitted front apps returned
default	11:52:49.033539-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:52:49.034081-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:52:49.034167-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:52:49.038295-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:49.038378-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:52:49.048485-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:49.048711-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:52:49.050307-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984dac570, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:49.050331-0500	VoiceOver	AudioConverter -> 0x984dac570: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:49.050340-0500	VoiceOver	AudioConverter -> 0x984dac570: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:49.060904-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:49.069324-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:49.069375-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:49.075354-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877472 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:49.075792-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877473 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:49.112008-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:49.112418-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:49.112646-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:52:49.112751-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:49.112886-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:49.112919-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:49.112957-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:49.113138-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:49.113198-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:49.113231-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:49.113446-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:49.113461-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:49.116549-0500	VoiceOver	No list of permitted front apps returned
default	11:52:49.128740-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 1444284 ioTS st: 1444284 ht: 23687.476779
error	11:52:49.212449-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:49.885437-0500	VoiceOver	No list of permitted front apps returned
default	11:52:49.885656-0500	VoiceOver	No list of permitted front apps returned
default	11:52:49.904175-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:49.904334-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:49.931591-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984d4cc00, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:52:49.931612-0500	VoiceOver	AudioConverter -> 0x984d4cc00: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:52:49.931622-0500	VoiceOver	AudioConverter -> 0x984d4cc00: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:52:49.951890-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:52:49.959124-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:52:49.959157-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:52:49.968013-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877473 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:49.968302-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877474 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:49.999406-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877474 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:52:50.999797-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877475 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:52:50.051372-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:52:50.051635-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:52:50.051902-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:50.052071-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:52:50.052246-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:52:50.052273-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:52:50.052304-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:52:50.052449-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:52:50.052509-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:52:50.052537-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:52:50.052721-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:52:50.052735-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:52:50.068698-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 1465012 ioTS st: 1465012 ht: 23688.416779
error	11:52:50.299952-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:52:51.024550-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:51.867352-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:51.867495-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:52:52.587464-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:52.587690-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
default	11:52:53.589158-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:53.589364-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
default	11:52:54.026843-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:55.344682-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:55.345004-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
default	11:52:56.603826-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:56.604077-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
default	11:52:57.023869-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:52:57.603697-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:57.603954-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
default	11:52:58.608439-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:58.608688-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
default	11:52:59.288898-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:59.289172-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
default	11:52:59.718265-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:52:59.718375-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
fault	11:52:59.950922-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:52:59.952585-0500	VoiceOver	No list of permitted front apps returned
default	11:53:00.022206-0500	VoiceOver	No list of permitted front apps returned
default	11:53:00.023801-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:00.034485-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984db2070, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:00.034503-0500	VoiceOver	AudioConverter -> 0x984db2070: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:00.034513-0500	VoiceOver	AudioConverter -> 0x984db2070: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:00.042751-0500	VoiceOver	No list of permitted front apps returned
default	11:53:00.045994-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:53:00.046399-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:53:00.046471-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:53:00.057902-0500	VoiceOver	No list of permitted front apps returned
default	11:53:00.061122-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:00.061242-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
default	11:53:00.087611-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:00.087708-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:00.089330-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d1ec40, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:00.089354-0500	VoiceOver	AudioConverter -> 0x983d1ec40: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:00.089361-0500	VoiceOver	AudioConverter -> 0x983d1ec40: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:00.095153-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:00.097801-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:00.101742-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:00.109422-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:00.109452-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:00.121675-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:10  id:21474877475 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:00.122308-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877477 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:53:00.175369-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:00.175641-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:00.175863-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:00.176028-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:00.176208-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:00.176229-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:00.176258-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:00.176395-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:00.176460-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:00.176486-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:00.176693-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:00.176709-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:00.188709-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 1688158 ioTS st: 1688158 ht: 23698.536779
error	11:53:00.306679-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
fault	11:53:01.267182-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:01.269283-0500	VoiceOver	No list of permitted front apps returned
default	11:53:01.278338-0500	VoiceOver	No list of permitted front apps returned
default	11:53:01.301718-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:53:01.302088-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:53:01.302228-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:53:01.323662-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:01.323780-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
default	11:53:01.369884-0500	VoiceOver	No list of permitted front apps returned
default	11:53:01.375734-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:01.375845-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:01.377224-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x98416a880, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:01.377240-0500	VoiceOver	AudioConverter -> 0x98416a880: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:01.377254-0500	VoiceOver	AudioConverter -> 0x98416a880: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:01.402947-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:01.408417-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:01.408499-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:01.409158-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:01.409210-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:01.426223-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877477 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:01.426696-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877478 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:53:01.479072-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:01.479391-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:01.479669-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:01.479684-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:01.479877-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:01.479897-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:01.479923-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:01.480062-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:01.480122-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:01.480150-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:01.480346-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:01.480362-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	11:53:01.650856-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:01.783335-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 24980
default	11:53:02.418426-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:02.418664-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:03.023875-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:03.218898-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:03.219120-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:04.418620-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:04.418988-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:05.419219-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:05.419465-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:06.000372-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:06.568861-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:06.569107-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:06.973474-0500	VoiceOver	[0x9848603c0] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	11:53:07.583987-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:07.584237-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:08.595899-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:08.596153-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:09.023814-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:09.603636-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:09.603904-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:10.605210-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:10.605456-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:11.610707-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:11.610959-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:12.026812-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:12.582787-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:12.583015-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:13.467701-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:13.467927-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:14.613280-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:14.613507-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:15.023798-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
fault	11:53:15.065275-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:15.067960-0500	VoiceOver	No list of permitted front apps returned
default	11:53:15.142925-0500	VoiceOver	No list of permitted front apps returned
default	11:53:15.154519-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dc9860, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:15.154541-0500	VoiceOver	AudioConverter -> 0x983dc9860: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:15.154553-0500	VoiceOver	AudioConverter -> 0x983dc9860: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:15.169538-0500	VoiceOver	No list of permitted front apps returned
default	11:53:15.169979-0500	VoiceOver	No list of permitted front apps returned
default	11:53:15.173041-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:53:15.173476-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:53:15.173542-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:53:15.181622-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:15.181768-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:15.212614-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:15.212729-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
default	11:53:15.220127-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:15.223905-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:15.227705-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:15.229868-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:15.229901-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:15.231097-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:13  id:21474877478 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:15.231651-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877480 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:53:15.281088-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:15.281326-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:15.281569-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:15.281727-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:15.281887-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:15.281909-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:15.281938-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:15.282078-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:15.282134-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:15.282162-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:15.282345-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:15.282358-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:15.298734-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2021335 ioTS st: 2021335 ht: 23713.646779
error	11:53:15.476061-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:16.316530-0500	VoiceOver	No list of permitted front apps returned
fault	11:53:16.317863-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:16.327835-0500	VoiceOver	No list of permitted front apps returned
default	11:53:16.370183-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:53:16.370537-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:53:16.370595-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:53:16.399502-0500	VoiceOver	[0x9841157c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:16.399605-0500	VoiceOver	[0x9841157c0] invalidated after the last release of the connection object
default	11:53:16.417731-0500	VoiceOver	No list of permitted front apps returned
default	11:53:16.451133-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:16.451247-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:16.452565-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984d4ef70, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:16.452586-0500	VoiceOver	AudioConverter -> 0x984d4ef70: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:16.452596-0500	VoiceOver	AudioConverter -> 0x984d4ef70: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:16.475860-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:16.479516-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:16.479614-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:16.498150-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877480 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:16.499281-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877481 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:53:16.558567-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:16.558873-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:16.559156-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:16.559297-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:16.559474-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:16.559495-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:16.559529-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:16.559652-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:16.559705-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:16.559731-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:16.559900-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:16.559914-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:16.578758-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2049559 ioTS st: 2049559 ht: 23714.926779
error	11:53:16.723139-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:17.593945-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:17.594182-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:18.023766-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:18.600917-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:18.601152-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:19.604358-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:19.604506-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:20.598856-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:20.599123-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:21.023751-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:21.606739-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:21.606950-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:22.058350-0500	VoiceOver	[0x984115e00] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	11:53:22.160170-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:22.160413-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:23.619246-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:23.619491-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:24.023729-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:24.619019-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:24.619280-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:25.592350-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:25.592617-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:26.596965-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:26.597280-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:27.023720-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:27.595185-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:27.595396-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:28.606883-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:28.607197-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:28.608804-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:53:28.609513-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:29.369951-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:12  id:21474877481 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:29.370549-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:29.371830-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:53:29.372477-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:29.375137-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:29.390871-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877486 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	11:53:29.449413-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:29.592678-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:29.592890-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
default	11:53:30.023643-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:30.127866-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dd09c0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:30.127897-0500	VoiceOver	AudioConverter -> 0x983dd09c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:30.127904-0500	VoiceOver	AudioConverter -> 0x983dd09c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:30.226222-0500	VoiceOver	[0x984116940] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:30.226408-0500	VoiceOver	[0x984116940] invalidated after the last release of the connection object
fault	11:53:31.162203-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:31.164159-0500	VoiceOver	No list of permitted front apps returned
default	11:53:31.268718-0500	VoiceOver	No list of permitted front apps returned
fault	11:53:31.357471-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:31.368381-0500	VoiceOver	No list of permitted front apps returned
default	11:53:31.369820-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:53:31.371990-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
fault	11:53:31.372585-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:31.380598-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 24991
default	11:53:31.380795-0500	VoiceOver	Aquired asertion <BKSProcessAssertion: 0x984e88230> for running extension with pid 24885
default	11:53:31.381097-0500	VoiceOver	[u 14844CB3-B750-5F5A-987A-D4BBC31613B5:m (null)] [<private>(<private>)] plugin reference count incremented to 2, and ready for host.
default	11:53:31.389230-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:31.469958-0500	VoiceOver	No list of permitted front apps returned
default	11:53:31.507750-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:53:31.523606-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:31.523740-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:53:31.580630-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:31.580775-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:31.582245-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dd2a60, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:31.582281-0500	VoiceOver	AudioConverter -> 0x983dd2a60: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:31.582290-0500	VoiceOver	AudioConverter -> 0x983dd2a60: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:31.624339-0500	runningboardd	Acquiring assertion targeting [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:24873])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:24885] from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:24873])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:24885] with description <RBSAssertionDescriptor| "RunningBoardAssertedAssetSets" ID:394-24885-16929 target:24885 attributes:[
	<RBSDomainAttribute| domain:"com.apple.common" name:"FinishTaskUninterruptable" sourceEnvironment:"(null)">
	]>
default	11:53:31.624417-0500	runningboardd	Assertion 394-24885-16929 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:24873])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:24885]) will be created as inactive as start-time-defining assertions exist
default	11:53:31.629074-0500	runningboardd	Invalidating assertion 394-24885-16929 (target:[xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:24873])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:24885]) from originator [xpcservice<com.apple.ax.MauiTTSSupport.MauiAUSP([osservice<com.apple.VoiceOver(501)>:24873])(501)>{vt hash: 0}{definition:com.apple.ax.MauiTTSSupport.MauiAUSP[extension][client]}:24885]
default	11:53:31.657444-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474877486 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:31.657763-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877487 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:53:31.680794-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:31.681097-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:31.681355-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:31.681442-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:31.681655-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:31.681677-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:31.681708-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:31.681865-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:31.681957-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:31.681982-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:31.682218-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:31.682234-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:31.698745-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2382956 ioTS st: 2382956 ht: 23730.046779
default	11:53:31.728254-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:31.729181-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:31.739224-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:31.739260-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:31.740681-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877487 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:31.741472-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877488 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:53:31.777009-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:31.777364-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:31.777647-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:53:31.777838-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:31.777909-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:31.777937-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:31.777966-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:31.778132-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:31.778192-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:31.778218-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:31.778423-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:31.778439-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:31.788759-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2384941 ioTS st: 2384941 ht: 23730.136779
error	11:53:31.956281-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:32.121006-0500	VoiceOver	No list of permitted front apps returned
default	11:53:32.121370-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:53:32.121390-0500	VoiceOver	No list of permitted front apps returned
default	11:53:32.122050-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:53:32.122165-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:53:32.139079-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:32.149611-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:32.149753-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:32.168884-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877488 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:32.169219-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877489 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:53:32.224088-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:32.224373-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:32.224611-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:32.224641-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:32.224822-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:32.224844-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:32.224874-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:32.225013-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:32.225069-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:32.225095-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:32.225325-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:32.225337-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	11:53:32.261605-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:32.275171-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 24995
default	11:53:32.277929-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 24995
default	11:53:32.399492-0500	VoiceOver	No list of permitted front apps returned
default	11:53:33.739607-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877489 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:33.840681-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 25003
default	11:53:33.841628-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25003
default	11:53:33.969835-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25004
default	11:53:34.204881-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 25005
default	11:53:34.204984-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 25006
default	11:53:34.215733-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25005
default	11:53:34.215797-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25006
default	11:53:34.565918-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 25007
default	11:53:34.591169-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25007
default	11:53:35.406413-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:35.406578-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:53:35.432243-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:35.443928-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:35.444109-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:35.454463-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877498 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:35.454803-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	11:53:35.490458-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
error	11:53:35.648355-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:35.792725-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25008
default	11:53:35.960987-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:35.961143-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:36.023619-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:36.362904-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983e1d470, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:36.362922-0500	VoiceOver	AudioConverter -> 0x983e1d470: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:36.362938-0500	VoiceOver	AudioConverter -> 0x983e1d470: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:36.366827-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:36.369849-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:36.369921-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:36.378154-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877498 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:36.378946-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877499 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:36.379919-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984dac360, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:36.379940-0500	VoiceOver	AudioConverter -> 0x984dac360: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:36.379946-0500	VoiceOver	AudioConverter -> 0x984dac360: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:36.397094-0500	VoiceOver	[0x984116580] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:36.397284-0500	VoiceOver	[0x984116580] invalidated after the last release of the connection object
default	11:53:36.406054-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:36.406416-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:36.406709-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:53:36.406749-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:36.406923-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:36.406944-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:36.406981-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:36.407128-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:36.407188-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:36.407217-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:36.407433-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:36.407448-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:36.418778-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2487034 ioTS st: 2487034 ht: 23734.766779
default	11:53:36.436347-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:36.436511-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:53:36.437480-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:36.441211-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:36.441309-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:36.462191-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:36.469280-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:36.479331-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:36.479372-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:36.482443-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877499 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:36.482960-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877500 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:36.521553-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:36.521925-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:36.522236-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:36.522258-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:36.522480-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:36.522505-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:36.522541-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:36.522687-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:36.522747-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:36.522778-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:36.522977-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:36.522993-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	11:53:36.566845-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:36.597119-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:36.597259-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:53:37.567128-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:37.569190-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:37.569240-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:37.571135-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877500 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:37.629869-0500	VoiceOver	No list of permitted front apps returned
default	11:53:37.630049-0500	VoiceOver	No list of permitted front apps returned
default	11:53:37.630825-0500	VoiceOver	[0x984114c80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:37.630954-0500	VoiceOver	[0x984114c80] invalidated after the last release of the connection object
default	11:53:37.641513-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:37.641633-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:53:37.651734-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:37.651882-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:53:37.652689-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983e1ffc0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:37.652712-0500	VoiceOver	AudioConverter -> 0x983e1ffc0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:37.652719-0500	VoiceOver	AudioConverter -> 0x983e1ffc0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:37.654982-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:37.655085-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:53:37.656341-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:37.656424-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:53:37.656482-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877502 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:37.679516-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d04b70, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:37.679553-0500	VoiceOver	AudioConverter -> 0x983d04b70: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:37.679565-0500	VoiceOver	AudioConverter -> 0x983d04b70: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:37.690984-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:37.691333-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:37.691659-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:53:37.691668-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:37.691885-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:37.691909-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:37.691942-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:37.692101-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:37.692156-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:37.692184-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:37.692393-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:37.692405-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:37.708782-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2515479 ioTS st: 2515479 ht: 23736.056779
default	11:53:37.712389-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:37.712604-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:53:37.724890-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:37.729154-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:37.729187-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:37.732072-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877502 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:37.732435-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877503 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:37.763187-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:37.763504-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:37.763773-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:37.763856-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:37.764049-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:37.764072-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:37.764102-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:37.764242-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:37.764302-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:37.764333-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:37.764522-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:37.764538-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:37.778826-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2517023 ioTS st: 2517023 ht: 23736.126779
error	11:53:37.803055-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:38.702712-0500	VoiceOver	No list of permitted front apps returned
default	11:53:38.703028-0500	VoiceOver	No list of permitted front apps returned
default	11:53:38.723491-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:38.723710-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:53:38.731146-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d12a30, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:38.731170-0500	VoiceOver	AudioConverter -> 0x983d12a30: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:38.731187-0500	VoiceOver	AudioConverter -> 0x983d12a30: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:38.748989-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:38.755743-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d195f0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:38.755775-0500	VoiceOver	AudioConverter -> 0x983d195f0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:38.755789-0500	VoiceOver	AudioConverter -> 0x983d195f0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:38.763169-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:38.769402-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:38.769471-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:38.771631-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877503 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:38.772104-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877504 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:38.797430-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:38.797966-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:38.798362-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:38.798366-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:38.798602-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:38.798629-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:38.798683-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:38.798862-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:38.798932-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:38.798969-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:38.799278-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:38.799293-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:38.818535-0500	VoiceOver	[0x984114c80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:38.818803-0500	VoiceOver	[0x984114c80] invalidated after the last release of the connection object
default	11:53:38.818918-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2539956 ioTS st: 2539956 ht: 23737.166779
error	11:53:38.890743-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:38.913366-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:38.913593-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:53:39.023670-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:39.421386-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:39.421528-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
fault	11:53:39.424226-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:39.433222-0500	VoiceOver	No list of permitted front apps returned
default	11:53:39.530842-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:53:39.530905-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:53:39.540396-0500	VoiceOver	No list of permitted front apps returned
default	11:53:39.549443-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:39.549565-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:53:39.601082-0500	VoiceOver	[0x984114c80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:39.601196-0500	VoiceOver	[0x984114c80] invalidated after the last release of the connection object
default	11:53:39.602453-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984db1a70, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:39.602473-0500	VoiceOver	AudioConverter -> 0x984db1a70: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:39.602483-0500	VoiceOver	AudioConverter -> 0x984db1a70: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:39.604520-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:39.604626-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:53:39.614569-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dc0540, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:39.614588-0500	VoiceOver	AudioConverter -> 0x983dc0540: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:39.614598-0500	VoiceOver	AudioConverter -> 0x983dc0540: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:39.626271-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:39.629117-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:39.629158-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:39.633510-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877504 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:39.634010-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877505 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:39.683453-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:39.683783-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:39.684094-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:39.684171-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:39.684372-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:39.684396-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:39.684427-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:39.684561-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:39.684618-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:39.684648-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:39.684840-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:39.684856-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:39.698767-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2559361 ioTS st: 2559361 ht: 23738.046779
error	11:53:39.877728-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:40.609981-0500	VoiceOver	[0x984114c80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:40.610223-0500	VoiceOver	[0x984114c80] invalidated after the last release of the connection object
default	11:53:41.610604-0500	VoiceOver	[0x984114c80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:41.610881-0500	VoiceOver	[0x984114c80] invalidated after the last release of the connection object
default	11:53:42.026669-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:42.600780-0500	VoiceOver	[0x984114c80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:42.601001-0500	VoiceOver	[0x984114c80] invalidated after the last release of the connection object
default	11:53:43.181005-0500	VoiceOver	[0x984114c80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:43.181260-0500	VoiceOver	[0x984114c80] invalidated after the last release of the connection object
default	11:53:44.375787-0500	VoiceOver	[0x984114c80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:44.376003-0500	VoiceOver	[0x984114c80] invalidated after the last release of the connection object
default	11:53:45.027229-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:45.196113-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984db0ba0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:45.196139-0500	VoiceOver	AudioConverter -> 0x984db0ba0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:45.196156-0500	VoiceOver	AudioConverter -> 0x984db0ba0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:45.438015-0500	VoiceOver	[0x984114c80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:45.438337-0500	VoiceOver	[0x984114c80] invalidated after the last release of the connection object
fault	11:53:46.132210-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:46.129746-0500	VoiceOver	No list of permitted front apps returned
default	11:53:46.231698-0500	VoiceOver	No list of permitted front apps returned
default	11:53:46.232284-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:53:46.232661-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:53:46.232718-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
fault	11:53:46.337712-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:46.344321-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:46.345604-0500	VoiceOver	No list of permitted front apps returned
default	11:53:46.351528-0500	VoiceOver	[0x984114c80] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:46.351727-0500	VoiceOver	[0x984114c80] invalidated after the last release of the connection object
default	11:53:46.360256-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:46.360493-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:53:46.362386-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 25015
default	11:53:46.365685-0500	VoiceOver	Application set focus not permitted for (null)
default	11:53:46.366563-0500	VoiceOver	No list of permitted front apps returned
default	11:53:46.367063-0500	VoiceOver	No list of permitted front apps returned
default	11:53:46.374530-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:46.374741-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:53:46.375358-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:53:46.375473-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:53:46.447788-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:46.448098-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:46.448468-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:53:46.448482-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:46.448661-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:46.448683-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:46.448712-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:46.448992-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:46.449054-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:46.449081-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:46.449278-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:46.449294-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:46.505930-0500	VoiceOver	[0x984114c80] invalidated after the last release of the connection object
default	11:53:46.516642-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
error	11:53:46.516702-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:46.516823-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:53:46.549381-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:46.549434-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:46.607645-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:46.608036-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:46.608374-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:46.608419-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:46.608680-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:46.608709-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:46.608756-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:46.609170-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:46.609236-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:46.609268-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:46.609513-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:46.609530-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:46.628802-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2712168 ioTS st: 2712168 ht: 23744.976779
error	11:53:46.829025-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:47.173742-0500	VoiceOver	No list of permitted front apps returned
default	11:53:47.182506-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:53:47.182645-0500	VoiceOver	No list of permitted front apps returned
default	11:53:47.183299-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:53:47.183429-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:53:47.194731-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:47.199353-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:47.199395-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:47.224925-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877508 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:47.225408-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877509 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:53:47.302354-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25018
error	11:53:47.325119-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:48.023643-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:49.046524-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 25023
default	11:53:49.046262-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:53:49.047863-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25023
default	11:53:49.389553-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:49.399533-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:49.399615-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:49.612277-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25027
default	11:53:49.700350-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:49.766825-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877512 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:53:49.822045-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:53:49.822819-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:49.823157-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:49.823220-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:49.823318-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:49.823607-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:49.823721-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:49.823764-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:49.824032-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:49.824115-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
fault	11:53:49.825423-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
error	11:53:49.901170-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:49.977471-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	11:53:50.780994-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dc21c0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:50.781035-0500	VoiceOver	AudioConverter -> 0x983dc21c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:50.781050-0500	VoiceOver	AudioConverter -> 0x983dc21c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:50.835629-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:50.835860-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:53:50.843007-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d17750, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:50.843041-0500	VoiceOver	AudioConverter -> 0x983d17750: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:50.843059-0500	VoiceOver	AudioConverter -> 0x983d17750: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:50.850948-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:50.851150-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:53:50.853535-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:50.864809-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:50.865150-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:50.865271-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:53:50.869188-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:50.869237-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:50.870874-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877512 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:50.871824-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877514 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:50.900048-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:50.900362-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:50.900671-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:50.900695-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:50.900944-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:50.900970-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:50.901004-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:50.901509-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:50.901582-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:50.901611-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:50.901825-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:50.901842-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:50.918803-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2806765 ioTS st: 2806765 ht: 23749.266779
default	11:53:51.023569-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
error	11:53:51.046215-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:51.114303-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:51.114506-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:51.193382-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:51.193526-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:51.206772-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983e04cc0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:51.206821-0500	VoiceOver	AudioConverter -> 0x983e04cc0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:51.206830-0500	VoiceOver	AudioConverter -> 0x983e04cc0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:51.209623-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:51.219552-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:51.219604-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:51.229387-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877514 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:51.230062-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983e07ed0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:51.230086-0500	VoiceOver	AudioConverter -> 0x983e07ed0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:51.230127-0500	VoiceOver	AudioConverter -> 0x983e07ed0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:51.230454-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877515 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:51.268021-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:51.268341-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:51.268604-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:51.268642-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:51.269078-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:51.269102-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:51.269135-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:51.269272-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:51.269323-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:51.269347-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:51.269536-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:51.269551-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:51.288767-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2814924 ioTS st: 2814924 ht: 23749.636779
error	11:53:51.311269-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:52.129482-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:52.130260-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:53.100023-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877515 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:53.132278-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:53.132555-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:53.217422-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:53:53.617559-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877516 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:53.625185-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	11:53:53.732822-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:53.928083-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 25028
default	11:53:53.931432-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25028
default	11:53:54.023533-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:53:54.514184-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:54.514456-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:53:54.557451-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:54.557564-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:54.557746-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:53:54.559640-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:54.559720-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:54.560384-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:53:54.566566-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:54.566831-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:53:54.573148-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877516 [System: PrevIdle DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:54.573693-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877517 [System: PrevIdle PrevDisp DeclUser IntPrevDisp NetAcc kDisp]
default	11:53:54.574841-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dd09c0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:54.574872-0500	VoiceOver	AudioConverter -> 0x983dd09c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:54.574884-0500	VoiceOver	AudioConverter -> 0x983dd09c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:54.598087-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:54.598270-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:53:54.616341-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:53:54.617049-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:53:54.617120-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:54.617245-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:54.617273-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:54.617319-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	11:53:54.617384-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:54.617466-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:54.617528-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:54.617566-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:54.617769-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:54.617786-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:54.628937-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2888572 ioTS st: 2888572 ht: 23752.976779
error	11:53:54.657649-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:55.486118-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:55.489270-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:55.489317-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:55.491465-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877517 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:55.555354-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:55.555506-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:53:55.561381-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dd2910, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:55.561403-0500	VoiceOver	AudioConverter -> 0x983dd2910: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:55.561414-0500	VoiceOver	AudioConverter -> 0x983dd2910: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:55.568341-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877518 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:53:55.590939-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:55.591100-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:53:55.601584-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:55.601934-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:55.602235-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:55.602317-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:55.602509-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:55.602534-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:55.602569-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:55.602715-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:55.602775-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:55.602812-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:55.603007-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:55.603025-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:55.618802-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2910402 ioTS st: 2910402 ht: 23753.966779
error	11:53:55.657620-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:56.625183-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:56.625480-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:53:57.026566-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
fault	11:53:57.279186-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:57.284801-0500	VoiceOver	No list of permitted front apps returned
default	11:53:57.331778-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:57.331881-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:53:57.406805-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:53:57.407200-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:53:57.407268-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:53:57.443428-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:57.443573-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:53:57.512336-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:57.512486-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:53:57.526849-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dc2e80, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:53:57.526873-0500	VoiceOver	AudioConverter -> 0x983dc2e80: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:53:57.526885-0500	VoiceOver	AudioConverter -> 0x983dc2e80: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:53:57.538047-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:53:57.539206-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:53:57.539266-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:53:57.540956-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877518 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:53:57.541351-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877519 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:53:57.593357-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:53:57.593660-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:53:57.593936-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:53:57.594033-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:53:57.594225-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:53:57.594249-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:53:57.594281-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:53:57.594433-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:53:57.594491-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:53:57.594523-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:53:57.594743-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:53:57.594758-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:53:57.608731-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 2954282 ioTS st: 2954282 ht: 23755.956779
error	11:53:57.782970-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:53:58.613481-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:58.613718-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:53:59.595850-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:53:59.596091-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:54:00.023613-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
fault	11:54:00.394701-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:00.398338-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 25034
default	11:54:00.398883-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 25034
default	11:54:00.680634-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 25037
default	11:54:00.683247-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25037
default	11:54:01.222367-0500	VoiceOver	No list of permitted front apps returned
default	11:54:01.222523-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:01.222541-0500	VoiceOver	No list of permitted front apps returned
default	11:54:01.222891-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:01.222959-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:01.237652-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:01.239206-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:01.239253-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:01.258718-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:03  id:21474877519 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:01.259728-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877520 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
fault	11:54:01.292092-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:54:01.292360-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:01.292382-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:54:01.292602-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:54:01.292623-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:01.292655-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:54:01.292792-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:54:01.292856-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:01.292884-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:01.293104-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:01.293122-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:01.357352-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 25039
default	11:54:02.454040-0500	runningboardd	Resolved pid 24992 to [xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:24873])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:24992:24992]
default	11:54:02.454957-0500	runningboardd	[xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:24873])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:24992:24992] is not RunningBoard jetsam managed.
default	11:54:02.454983-0500	runningboardd	[xpcservice<com.apple.audio.AUCrashHandlerService([osservice<com.apple.VoiceOver(501)>:24873])(501)>{vt hash: 0}{definition:com.apple.audio.AUCrashHandlerService[standard][client]}:24992:24992] This process will not be managed.
default	11:54:02.809401-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877520 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:03.054059-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25044
default	11:54:03.461219-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25047
default	11:54:04.757955-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984db2340, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:54:04.757992-0500	VoiceOver	AudioConverter -> 0x984db2340: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:54:04.758006-0500	VoiceOver	AudioConverter -> 0x984db2340: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:54:04.804753-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:04.804889-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:04.811120-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dd0210, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:54:04.811146-0500	VoiceOver	AudioConverter -> 0x983dd0210: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:54:04.811161-0500	VoiceOver	AudioConverter -> 0x983dd0210: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:54:04.818353-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:04.818490-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:54:04.821973-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:54:04.831134-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:04.831351-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:54:04.834454-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877522 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:04.835025-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	11:54:04.861102-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:54:04.861824-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:54:04.861965-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:04.862015-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:54:04.862044-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:04.862087-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:54:04.862245-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
fault	11:54:04.862262-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:04.862303-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:04.862344-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:04.862597-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:04.862615-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:04.878850-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 3114587 ioTS st: 3114587 ht: 23763.226779
default	11:54:04.889452-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 25049
default	11:54:04.889898-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 25049
error	11:54:05.054442-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:05.152604-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:05.152748-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:05.170860-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983e1d4d0, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:54:05.170883-0500	VoiceOver	AudioConverter -> 0x983e1d4d0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:54:05.170892-0500	VoiceOver	AudioConverter -> 0x983e1d4d0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:54:05.173573-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:05.179757-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:05.179800-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:05.188307-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877522 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:05.188730-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983e1f240, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:54:05.188750-0500	VoiceOver	AudioConverter -> 0x983e1f240: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:54:05.188781-0500	VoiceOver	AudioConverter -> 0x983e1f240: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:54:05.189330-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877523 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:05.232520-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:54:05.232877-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:54:05.233149-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:05.233231-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:54:05.233422-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:54:05.233453-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:05.233490-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:54:05.233640-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:54:05.233691-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:05.233722-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:05.233920-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:05.233936-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:05.248891-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 3122746 ioTS st: 3122746 ht: 23763.596779
error	11:54:05.278038-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:05.591757-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:05.591968-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:05.884035-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 25050
default	11:54:05.885612-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25050
default	11:54:06.026505-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:54:06.483474-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:06.483730-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:54:06.524539-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:06.524713-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:06.524913-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:06.526480-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:54:06.529910-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:06.530004-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:06.532385-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877523 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:06.533273-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:06.533570-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877524 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:06.534336-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:54:06.535433-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983dc1d70, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:54:06.535470-0500	VoiceOver	AudioConverter -> 0x983dc1d70: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:54:06.535480-0500	VoiceOver	AudioConverter -> 0x983dc1d70: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:54:06.556245-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:54:06.556859-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:54:06.556999-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:06.557060-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:54:06.557086-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:06.557125-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	11:54:06.557307-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:06.557291-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:54:06.557362-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:06.557394-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:06.557624-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:06.557641-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:06.568835-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 3151852 ioTS st: 3151852 ht: 23764.916779
error	11:54:06.599057-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:06.606600-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:06.606739-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:54:07.602899-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:07.609146-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:07.609200-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:07.611021-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877524 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:07.664967-0500	VoiceOver	No list of permitted front apps returned
default	11:54:07.665188-0500	VoiceOver	No list of permitted front apps returned
default	11:54:07.666045-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:07.666166-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:07.677387-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:07.677516-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:54:07.689393-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:07.689552-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:54:07.693202-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:07.693326-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:07.694334-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:07.694432-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:07.695422-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877525 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:07.702255-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x984db0ea0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:54:07.702275-0500	VoiceOver	AudioConverter -> 0x984db0ea0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:54:07.702287-0500	VoiceOver	AudioConverter -> 0x984db0ea0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:54:07.733213-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:54:07.733572-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:07.733819-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:54:07.733916-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:07.734040-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:54:07.734070-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:07.734105-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:54:07.734261-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:54:07.734321-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:07.734355-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:07.734577-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:07.734601-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:07.744424-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:07.744630-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:07.748856-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 3177871 ioTS st: 3177871 ht: 23766.096779
default	11:54:07.781203-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:07.789423-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:07.799750-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:07.799803-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:07.801697-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877525 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:07.802087-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877526 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:07.837012-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:54:07.837446-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:54:07.837742-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:07.837821-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:54:07.838027-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:54:07.838057-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:07.838098-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:54:07.838273-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:54:07.838335-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:07.838371-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:07.838589-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:07.838604-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:07.848783-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 3180077 ioTS st: 3180077 ht: 23766.196779
error	11:54:07.869924-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:08.620452-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:08.620768-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:09.024055-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:54:09.418330-0500	VoiceOver	No list of permitted front apps returned
default	11:54:09.418745-0500	VoiceOver	No list of permitted front apps returned
default	11:54:09.446060-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:09.446329-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:09.454010-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d09cb0, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:54:09.454041-0500	VoiceOver	AudioConverter -> 0x983d09cb0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:54:09.454060-0500	VoiceOver	AudioConverter -> 0x983d09cb0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:54:09.474704-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:54:09.493645-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:09.499952-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:09.500102-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:09.501543-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877526 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:09.503026-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877527 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:09.536220-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:54:09.537034-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:09.537056-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:54:09.537278-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:54:09.537312-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:09.537358-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	11:54:09.537442-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:09.537543-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:54:09.537611-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:09.537647-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:09.537872-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:09.537889-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:09.548772-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 3217563 ioTS st: 3217563 ht: 23767.896779
default	11:54:09.572866-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:09.573084-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
error	11:54:09.601233-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:10.109637-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:10.110347-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:10.110471-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:10.591427-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:10.591654-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:11.128540-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:11.129286-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:11.129410-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:11.254218-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:11.254371-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:11.264483-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:11.264652-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:11.274625-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:11.274842-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:11.285681-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:11.285913-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:11.295828-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:11.295947-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:11.306787-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:11.306915-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:11.790364-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:11.790597-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:11.797746-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d0f540, from  1 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:54:11.797799-0500	VoiceOver	AudioConverter -> 0x983d0f540: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:54:11.797817-0500	VoiceOver	AudioConverter -> 0x983d0f540: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:54:11.800785-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:11.800997-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:11.802366-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:11.810023-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:11.810106-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:11.814105-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474877527 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:11.815222-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877528 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:11.816463-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d0daa0, from  2 ch,  22050 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:54:11.816508-0500	VoiceOver	AudioConverter -> 0x983d0daa0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:54:11.816526-0500	VoiceOver	AudioConverter -> 0x983d0daa0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:54:11.849889-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:54:11.850493-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:11.850595-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:54:11.850728-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:11.850886-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:54:11.850908-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:11.850938-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:54:11.851080-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:54:11.851133-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:11.851162-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:11.851347-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:11.851361-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:11.868807-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 3268719 ioTS st: 3268719 ht: 23770.216779
error	11:54:11.898046-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:12.023567-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:54:12.610950-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:12.611186-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:13.624819-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:13.625036-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
fault	11:54:13.945483-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:13.958055-0500	VoiceOver	No list of permitted front apps returned
default	11:54:13.979335-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:13.979717-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:54:14.089843-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:14.090226-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:14.090297-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:14.129540-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474877528 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:14.131975-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:14.132239-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:14.205621-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:14.205789-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:14.207681-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:54:14.219388-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d0c390, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:54:14.219413-0500	VoiceOver	AudioConverter -> 0x983d0c390: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:54:14.219427-0500	VoiceOver	AudioConverter -> 0x983d0c390: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:54:14.241615-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877529 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:14.242113-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	11:54:14.516772-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:14.671149-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:14.671818-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:14.671931-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:14.706011-0500	VoiceOver	No list of permitted front apps returned
default	11:54:14.810152-0500	VoiceOver	No list of permitted front apps returned
default	11:54:14.818550-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:14.819109-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:14.819160-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:14.841692-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877529 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:14.867929-0500	VoiceOver	No list of permitted front apps returned
default	11:54:14.887022-0500	VoiceOver	No list of permitted front apps returned
default	11:54:14.889364-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:14.889738-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:14.889796-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:14.914819-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:14.914928-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:14.927496-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:14.927629-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:14.942276-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877530 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:14.988334-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:54:14.988663-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:14.988985-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:54:14.988998-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:14.989192-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:54:14.989216-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:14.989245-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:54:14.989403-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:54:14.989458-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:14.989486-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:14.989713-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:14.989728-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:15.008801-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 3337957 ioTS st: 3337957 ht: 23773.356779
default	11:54:15.025723-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
error	11:54:15.124891-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:16.215720-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:16.215970-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:16.715815-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:16.716104-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:17.615374-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:17.615603-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:18.023045-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:54:18.598705-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:18.598964-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:19.611799-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:19.612067-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:20.300225-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474877530 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:20.387170-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:54:20.387259-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:54:20.387329-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:54:20.387428-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:54:20.511487-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:54:20.591510-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:20.591723-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:20.817578-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877542 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:20.818001-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
error	11:54:20.892164-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:21.023477-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:54:21.140868-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:21.141113-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:22.157584-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:22.157921-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:23.165842-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:23.166143-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:24.023401-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:54:24.157943-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:24.160017-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:25.240609-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:04  id:21474877542 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:25.381762-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:25.381889-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:25.448980-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:54:25.839867-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:25.849773-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:25.849953-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:26.608078-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:26.608351-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:26.644077-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:54:26.655102-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877565 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:26.655453-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	11:54:26.679460-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:54:26.680179-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:54:26.680201-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:26.680475-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
fault	11:54:26.680497-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:26.680506-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:26.680561-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:54:26.680780-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:54:26.680844-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:26.680877-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:26.681117-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:26.681133-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:26.698756-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 3595722 ioTS st: 3595722 ht: 23785.046779
error	11:54:26.826534-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:27.023453-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:54:27.592520-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:27.592777-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:27.652915-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:54:27.662746-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:27.669907-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:27.670017-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:27.688601-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474877565 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:27.689469-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877568 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:27.740793-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:54:27.741147-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
fault	11:54:27.741518-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:27.741651-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:54:27.741838-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:54:27.741864-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:27.741899-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:54:27.742088-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:54:27.742157-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:27.742192-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:27.742440-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:27.742456-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:27.758766-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 3619096 ioTS st: 3619096 ht: 23786.106779
error	11:54:27.933974-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:28.607563-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:28.607806-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:29.598886-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:29.599185-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:30.023431-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:54:30.610510-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:30.610675-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:31.611130-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:31.611378-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:32.596987-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:32.597569-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:33.023446-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 1
default	11:54:33.615607-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:33.615866-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:34.618172-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:34.618527-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:35.279953-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:54:35.280016-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:54:35.280062-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:54:35.280462-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:54:35.280500-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:54:35.590905-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:35.591140-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:36.023406-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:54:36.226154-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:36.226397-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:37.232913-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:37.233151-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:38.224184-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:38.224462-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:54:38.453149-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:54:38.456537-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:54:38.468707-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:38.469086-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:38.469141-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:38.475390-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:10  id:21474877568 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:38.476478-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877571 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:54:38.537058-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:54:38.537844-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:54:38.538014-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:38.538048-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:54:38.538077-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:54:38.538120-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	11:54:38.538244-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:54:38.538336-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:54:38.538399-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:54:38.538445-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:38.538660-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:38.538676-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:54:38.548929-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 3857016 ioTS st: 3857016 ht: 23796.896779
error	11:54:38.576450-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:38.978252-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 25094
default	11:54:38.978357-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 25095
default	11:54:39.023540-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:54:39.207406-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:39.207571-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
error	11:54:40.576340-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:40.606625-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:40.606740-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:41.240694-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:41.240987-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:42.023381-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:54:42.615504-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:42.615819-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:43.607786-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:43.608084-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:44.615520-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:44.615880-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:44.991260-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:44.996522-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:44.993486-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:45.025881-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:54:45.066734-0500	coreaudiod	Sending message. { reporterID=107730664685570, category=IO, type=error, message=["scheduler_latency": Optional(22541), "safety_violation": Optional(1), "HAL_client_IO_duration": Optional(125291), "io_buffer_size": Optional(512), "io_cycle_budget": Optional(11354166), "output_device_source_list": Optional(Unknown), "start_time": Optional(571280250783), "safety_violation_sample_gap": Optional(33), "wg_external_wakeups": Optional(1), "cause": Optional(SafetyViolationOccurred), "other_page_faults": Optional(0), "other_active_clients": Optional([ { HostApplicationDisplayID_other_client: com.apple.VoiceOver, sample_rate_other_client: 48000.000000, io_buffer_size_other_client: 480 } ]), "cause_set": Optional(8), "lateness": Optional(2), "sample_rate": Optional(48000), "wg_system_time_mach": Optional(3289), "reporting_latency": Optional(47508291), "io_cycle": Optional(912), "input_device_transport_list": Optional(), "is_recovering": Optional(0), "io_cycle_usage": Optional(1), "input_device_uid_list": Optional(), "safety_violation_time_gap": Optional(0.0006<…> }
default	11:54:45.119827-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:45.119184-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:45.120707-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:45.231125-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:45.230295-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:45.232619-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:45.302706-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:45.302050-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:45.303342-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:45.433465-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:45.432548-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:45.435115-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:45.530148-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:54:45.529423-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:54:45.530481-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:54:45.582449-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:45.582700-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:46.274187-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:46.274450-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:47.600509-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:47.600759-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:54:48.022897-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
error	11:54:48.465735-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:54:48.615427-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:48.615648-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:49.615267-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:49.615549-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:50.593688-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:50.593905-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:51.023323-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:54:51.595570-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:51.595876-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:51.598849-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:54:51.599351-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:54:52.599098-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:52.599417-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:52.944200-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:14  id:21474877571 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:54:53.149051-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:54:53.539278-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:54:53.549038-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:54:53.549160-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:54:53.593803-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:53.594048-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:54.023376-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:54:54.615740-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:54.616039-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:55.615497-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:55.615756-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:55.648791-0500	VoiceOver	aqmeio@0x984591818 Stop id=85
default	11:54:55.648806-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:54:55.649580-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea010","name":"VoiceOver(24873)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:54:55.649815-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 17 stopping playing
default	11:54:55.649925-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:54:55.650019-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:54:55.650253-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:54:55.651196-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:54:55.651225-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:54:55.651943-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	11:54:55.652034-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	11:54:55.652034-0500	runningboardd	Invalidating assertion 394-24873-16642 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.VoiceOver(501)>:24873]
default	11:54:55.650964-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea010 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":24873}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea010, sessionType: 'prim', isRecording: false }, 
]
default	11:54:55.652074-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 1
default	11:54:55.652204-0500	runningboardd	Invalidating assertion 394-328-16315 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.powerd>:328]
default	11:54:55.651503-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	11:54:55.757508-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring jetsam update because this process is not memory-managed
default	11:54:55.757524-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring suspend because this process is not lifecycle managed
default	11:54:55.757539-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring GPU update because this process is not GPU managed
default	11:54:55.757580-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring memory limit update because this process is not memory-managed
default	11:54:55.757635-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Skipping AppNap state - not lifecycle managed
default	11:54:55.761440-0500	gamepolicyd	Received state update for 24873 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	11:54:56.612916-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:56.613306-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:57.613600-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:57.613908-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:58.611704-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:58.611995-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:54:59.607508-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:54:59.607841-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:00.598683-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:00.598905-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:01.615778-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:01.616365-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:02.598622-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:02.598866-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:03.613317-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:03.613589-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:04.600318-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:04.600611-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:05.603212-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:05.603501-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:05.688513-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 25101
default	11:55:05.688891-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 25101
default	11:55:06.598649-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:06.598928-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:07.602370-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:07.602701-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:08.590744-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:08.590964-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:09.608045-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:09.608319-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:10.077306-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:55:10.080461-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.VoiceOver(501)>:24873] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-24873-17264 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:55:10.080619-0500	runningboardd	Assertion 394-24873-17264 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:55:10.081136-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-17265 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:55:10.081147-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring jetsam update because this process is not memory-managed
default	11:55:10.081162-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring suspend because this process is not lifecycle managed
default	11:55:10.081190-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring GPU update because this process is not GPU managed
default	11:55:10.081212-0500	runningboardd	Assertion 394-328-17265 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:55:10.081267-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring memory limit update because this process is not memory-managed
default	11:55:10.081298-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Skipping AppNap state - not lifecycle managed
default	11:55:10.083904-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:55:10.084872-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring jetsam update because this process is not memory-managed
default	11:55:10.084886-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring suspend because this process is not lifecycle managed
default	11:55:10.084897-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring GPU update because this process is not GPU managed
default	11:55:10.084958-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring memory limit update because this process is not memory-managed
default	11:55:10.084974-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Skipping AppNap state - not lifecycle managed
default	11:55:10.085921-0500	gamepolicyd	Received state update for 24873 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	11:55:10.088268-0500	gamepolicyd	Received state update for 24873 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	11:55:10.095568-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877576 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:55:10.107361-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea010","name":"VoiceOver(24873)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	11:55:10.107649-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	11:55:10.107666-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 17 starting playing
default	11:55:10.107939-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:55:10.108129-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	11:55:10.108170-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:10.106436-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:55:10.108335-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	11:55:10.108342-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:55:10.108242-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea010 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":24873}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea010, sessionType: 'prim', isRecording: false }, 
]
default	11:55:10.108288-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	11:55:10.109054-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x19BF0001 category Not set
default	11:55:10.108521-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	11:55:10.111675-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	11:55:10.111900-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	11:55:10.111932-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	11:55:10.111948-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 2
default	11:55:10.111957-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:55:10.112005-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:55:10.121654-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:55:10.122179-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:55:10.122277-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:55:10.122394-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:55:10.122522-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:55:10.122544-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:55:10.122569-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:55:10.122740-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:55:10.122805-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:55:10.122860-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:55:10.123053-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:55:10.123066-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:55:10.136765-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 4553531 ioTS st: 4553531 ht: 23828.484779
error	11:55:10.157876-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:55:10.606924-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:10.607156-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:55:11.590714-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:11.590960-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:55:12.023241-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
error	11:55:12.110167-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:55:12.615602-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:12.615902-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:55:13.606951-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:13.607218-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:55:14.590420-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:14.590549-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:55:15.023236-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:55:15.600925-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:15.601216-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:55:16.114156-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:55:16.117873-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:55:16.127099-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:55:16.137737-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:55:16.137845-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:55:16.139261-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:06  id:21474877576 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:55:16.140247-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474877578 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:55:16.179019-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:55:16.179727-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:55:16.179755-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:55:16.179955-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:55:16.179982-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	11:55:16.179985-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:55:16.180020-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:55:16.180208-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:55:16.180268-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:55:16.180301-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:55:16.180493-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:55:16.180506-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:55:16.196820-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 4687155 ioTS st: 4687155 ht: 23834.544779
error	11:55:16.219580-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:55:16.590126-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:16.590351-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:17.600219-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:17.600544-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:18.022747-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
error	11:55:18.130505-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:55:18.603071-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:18.603343-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
error	11:55:19.389941-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:55:19.599204-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:19.599509-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:20.590240-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:20.590485-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:21.023204-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:55:21.607311-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:21.607633-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:22.607296-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:22.607645-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:23.598500-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:23.598732-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:23.868428-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:07  id:21474877578 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:55:24.023252-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:55:24.082231-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:55:24.265248-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:24.265501-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:24.467859-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:55:24.477653-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:55:24.477786-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:55:24.849138-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:24.849523-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:55:24.851021-0500	runningboardd	Invalidating assertion 394-24873-17264 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.VoiceOver(501)>:24873]
default	11:55:24.849642-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:55:24.851149-0500	runningboardd	Invalidating assertion 394-328-17265 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.powerd>:328]
default	11:55:24.853050-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:55:24.857345-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(805)
default	11:55:24.857372-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:805 called from <private>
default	11:55:24.857383-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:805 called from <private>
error	11:55:24.855791-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	11:55:24.877758-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(805)
default	11:55:24.877790-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:805 called from <private>
default	11:55:24.877799-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:805 called from <private>
default	11:55:24.880894-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:55:24.880911-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:55:24.892616-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:55:24.892633-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:55:24.892760-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:24.921624-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:55:24.921663-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:55:24.921703-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:55:24.921756-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x984591818 (1C-77-54-18-C8-A3:output): Output stream format changed
default	11:55:24.921797-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x984591818 (1C-77-54-18-C8-A3:output): Output stream format changed
default	11:55:24.957374-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:24.957596-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:24.957770-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:25.607604-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:25.607886-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:26.570719-0500	VoiceOver	aqmeio@0x984591818 Stop id=85
default	11:55:26.570728-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:55:26.571034-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:55:26.574913-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:26.575052-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:26.575263-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:26.576394-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:55:26.576689-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:55:26.576734-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:55:26.576858-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:55:26.576992-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:55:26.612128-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:26.612368-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:27.297216-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:27.297339-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:27.297492-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:27.297612-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:27.299338-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
error	11:55:27.299366-0500	audioaccessoryd	Updating local audio category 501 -> 201 app com.apple.VoiceOver
error	11:55:27.299441-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	11:55:27.299550-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:55:27.299581-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:55:27.299624-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:55:27.299671-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:55:27.299710-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:55:27.299734-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:55:27.299794-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:55:27.592797-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:27.593012-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:28.605212-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:28.605494-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:29.424959-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:29.426134-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(805)
default	11:55:29.426168-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:805 called from <private>
default	11:55:29.426177-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:805 called from <private>
default	11:55:29.429197-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:55:29.429297-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:55:29.430335-0500	runningboardd	Invalidating assertion 394-24873-17309 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.VoiceOver(501)>:24873]
default	11:55:29.432502-0500	VoiceOver	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:55:29.430408-0500	runningboardd	Invalidating assertion 394-328-17311 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.powerd>:328]
default	11:55:29.443658-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(805)
default	11:55:29.443701-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:805 called from <private>
default	11:55:29.443708-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:805 called from <private>
default	11:55:29.450206-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:55:29.450229-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:55:29.465312-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:55:29.465342-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:55:29.465435-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:29.475131-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:29.475756-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:55:29.475775-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:55:29.475980-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:29.477478-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:29.477534-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:29.477778-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:29.477818-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:55:29.477864-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:29.478127-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:55:29.478358-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:29.478580-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:55:29.479146-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:55:29.479362-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:55:29.479523-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:29.479623-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:55:29.479932-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:55:29.480074-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:55:29.480272-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:55:29.480453-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:55:29.480659-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:55:29.480822-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:55:29.480978-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:55:29.481074-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:55:29.481182-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:29.481197-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:55:29.481278-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:29.481415-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:55:29.481668-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:29.482002-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:55:29.482331-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:29.482563-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:55:29.482806-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:55:29.482901-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:55:29.482959-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:55:29.483015-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:55:29.483086-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:55:29.483135-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:55:29.483602-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:55:29.483937-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:55:29.484215-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:55:29.484519-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x100c06d80) Device ID: 85 (Input:No | Output:Yes): true
default	11:55:29.484565-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x100c06d80)
default	11:55:29.485898-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.VoiceOver(501)>:24873] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-24873-17332 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:55:29.484838-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:55:29.486011-0500	runningboardd	Assertion 394-24873-17332 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:55:29.532615-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring jetsam update because this process is not memory-managed
default	11:55:29.532627-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring suspend because this process is not lifecycle managed
default	11:55:29.532636-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring GPU update because this process is not GPU managed
default	11:55:29.532669-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring memory limit update because this process is not memory-managed
default	11:55:29.532680-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Skipping AppNap state - not lifecycle managed
default	11:55:29.535896-0500	gamepolicyd	Received state update for 24873 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	11:55:29.598510-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:29.598730-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
error	11:55:29.962966-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.apple.VoiceOver",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	11:55:29.982924-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:55:30.430294-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-17337 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:55:30.430392-0500	runningboardd	Assertion 394-328-17337 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:55:30.431066-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring jetsam update because this process is not memory-managed
default	11:55:30.431113-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring suspend because this process is not lifecycle managed
default	11:55:30.431174-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring GPU update because this process is not GPU managed
default	11:55:30.431279-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring memory limit update because this process is not memory-managed
default	11:55:30.431339-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Skipping AppNap state - not lifecycle managed
default	11:55:30.440831-0500	gamepolicyd	Received state update for 24873 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	11:55:30.441734-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	11:55:30.481106-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:804 called from <private>
default	11:55:30.481755-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d09200, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:55:30.481817-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:55:30.481940-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:55:30.482259-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:55:30.482419-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:55:30.482433-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:55:30.482439-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:55:30.482547-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x100c06d80) Device ID: 85 (Input:No | Output:Yes): true
default	11:55:30.482561-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x100c06d80)
default	11:55:30.482654-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:55:30.482666-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:55:30.482675-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:55:30.482688-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:55:30.482698-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:55:30.483099-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d09200, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:55:30.483117-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:55:30.483181-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:55:30.483444-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:55:30.483546-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:55:30.483561-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:55:30.483567-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:55:30.483587-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x984591818 (1C-77-54-18-C8-A3:output): Output stream format changed
default	11:55:30.483596-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x984591818 (1C-77-54-18-C8-A3:output): Output stream format changed
default	11:55:30.484292-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d08c60, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:55:30.484523-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x984838000:
default	11:55:30.484574-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	11:55:30.484580-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	11:55:30.484596-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	11:55:30.484622-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	11:55:30.484642-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	11:55:30.484932-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x984838000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	11:55:30.493304-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:55:30.493380-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:55:30.603779-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:30.603987-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:31.281315-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:55:31.281876-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea010","name":"VoiceOver(24873)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:55:31.282044-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 17 stopping playing
default	11:55:31.282140-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:55:31.282222-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:55:31.282342-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:55:31.282471-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	11:55:31.282567-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea010 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":24873}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea010, sessionType: 'prim', isRecording: false }, 
]
default	11:55:31.282699-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:55:31.282735-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:55:31.282748-0500	audioaccessoryd	Audio state update Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	11:55:31.282843-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.apple.VoiceOver" : 201,
}
default	11:55:31.282885-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.apple.VoiceOver 201 count 0
default	11:55:31.287245-0500	runningboardd	Invalidating assertion 394-24873-17332 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.VoiceOver(501)>:24873]
default	11:55:31.287390-0500	runningboardd	Invalidating assertion 394-328-17337 (target:[osservice<com.apple.VoiceOver(501)>:24873]) from originator [osservice<com.apple.powerd>:328]
default	11:55:31.390284-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring jetsam update because this process is not memory-managed
default	11:55:31.390295-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring suspend because this process is not lifecycle managed
default	11:55:31.390305-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring GPU update because this process is not GPU managed
default	11:55:31.390331-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring memory limit update because this process is not memory-managed
default	11:55:31.390361-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Skipping AppNap state - not lifecycle managed
default	11:55:31.393021-0500	gamepolicyd	Received state update for 24873 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	11:55:31.590614-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:31.590822-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:32.194065-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	11:55:32.610310-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:32.610553-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:33.334964-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:33.335283-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:34.340657-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:34.341002-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:35.332210-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:35.332513-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:36.348834-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:36.349126-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:37.344598-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:37.344965-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:38.340617-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:38.340843-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:39.598778-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:39.599073-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:40.373909-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:40.374231-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:40.835005-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:40.835028-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:55:40.835036-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:55:40.836122-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(805)
default	11:55:40.836148-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:805 called from <private>
default	11:55:40.836154-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:805 called from <private>
default	11:55:40.847512-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:55:40.847531-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:55:40.847661-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:40.847738-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:55:40.847805-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:55:40.850637-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:40.850794-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:55:40.850918-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:55:40.852092-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:55:40.852107-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:55:40.852994-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:55:40.853018-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:55:40.853182-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:40.853306-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:55:40.853395-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:55:40.856036-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:40.859669-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:40.859683-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:55:40.859694-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:55:40.859704-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:55:40.859714-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:55:40.859833-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:55:40.859900-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:804 called from <private>
default	11:55:40.860071-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:40.860202-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:55:40.860372-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:55:40.862838-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(805)
default	11:55:40.862867-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:805 called from <private>
default	11:55:40.862875-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:805 called from <private>
default	11:55:40.864356-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:40.864439-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:40.871997-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:55:40.886455-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	11:55:40.886518-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	11:55:41.593436-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:41.593816-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:42.615303-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:42.615586-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:43.601021-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:43.601284-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:44.615108-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:44.615323-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:45.599764-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:45.600022-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:46.600492-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:46.600779-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:47.592891-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:47.593254-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:47.914433-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(805)
default	11:55:47.914486-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:805 called from <private>
default	11:55:47.914495-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:805 called from <private>
default	11:55:47.915040-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:47.915070-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:55:47.915080-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:55:47.927993-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:55:47.928030-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:55:47.928772-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:47.928833-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:55:47.928842-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:55:47.931644-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:47.932024-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(805)
default	11:55:47.932075-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:805 called from <private>
default	11:55:47.932378-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:47.932718-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:805 called from <private>
default	11:55:47.933172-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:55:47.933428-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:55:47.933600-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:55:47.933830-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:55:47.935524-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:47.937496-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:804 called from <private>
default	11:55:47.937519-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:804 called from <private>
default	11:55:47.939363-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:47.947643-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:804 called from <private>
default	11:55:47.947674-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:804 called from <private>
default	11:55:47.947774-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:47.950167-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:47.950409-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:804 called from <private>
default	11:55:47.950419-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:804 called from <private>
default	11:55:47.950556-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(804)
default	11:55:47.954910-0500	VoiceOver	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(804)
default	11:55:47.955328-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:804 called from <private>
default	11:55:47.955341-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:804 called from <private>
default	11:55:47.955444-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:55:47.955454-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:804 called from <private>
default	11:55:47.955466-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:55:47.955472-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:55:47.955713-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:55:47.955791-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:804 called from <private>
default	11:55:47.955851-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:55:47.955934-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:55:47.956046-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:55:47.956119-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:804 called from <private>
default	11:55:47.956203-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:804 called from <private>
default	11:55:47.956264-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:804 called from <private>
default	11:55:47.956314-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:804 called from <private>
default	11:55:47.956372-0500	VoiceOver	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:804 called from <private>
default	11:55:47.956744-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x100c06d80) Device ID: 85 (Input:No | Output:Yes): true
default	11:55:47.956758-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x100c06d80)
default	11:55:47.957268-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:55:47.957283-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:55:47.957290-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:55:47.957339-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:55:47.957351-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:55:47.958010-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d09200, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:55:47.958041-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:55:47.958589-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:55:47.958611-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:55:47.958621-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:55:47.959290-0500	VoiceOver	                AUHAL.cpp:3418  IsDeviceUsable: (0x100c06d80) Device ID: 85 (Input:No | Output:Yes): true
default	11:55:47.959306-0500	VoiceOver	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x100c06d80)
default	11:55:47.959553-0500	VoiceOver	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:55:47.959563-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:55:47.959570-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:55:47.959593-0500	VoiceOver	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:55:47.959631-0500	VoiceOver	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:55:47.961353-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d09200, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:55:47.961405-0500	VoiceOver	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:55:47.963267-0500	VoiceOver	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:55:47.963318-0500	VoiceOver	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x100c06d80) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:55:47.963360-0500	VoiceOver	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:55:47.963602-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x984591818 (1C-77-54-18-C8-A3:output): Output stream format changed
default	11:55:47.963785-0500	VoiceOver	           AQMEIO_HAL.cpp:3624  0x984591818 (1C-77-54-18-C8-A3:output): Output stream format changed
default	11:55:47.966109-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d08c60, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:55:47.967001-0500	VoiceOver	     AudioQueueObject.cpp:10012 SetLoudnessFromLM: -> aq@0x984838000:
default	11:55:47.967243-0500	VoiceOver	     AudioQueueObject.cpp:10122 SetLoudnessFromLM: is CoreAudioServices/LoudnessManager enabled? yes
default	11:55:47.967324-0500	VoiceOver	     AudioQueueObject.cpp:10125 SetLoudnessFromLM: is CoreAudioServices/LoudnessManagerV2 enabled? yes
default	11:55:47.967499-0500	VoiceOver	     AudioQueueObject.cpp:10128 SetLoudnessFromLM: is CoreAudioServices/lm-disable-hardware-check on? no
default	11:55:47.967629-0500	VoiceOver	     AudioQueueObject.cpp:10131 SetLoudnessFromLM: is hardware supported? no
default	11:55:47.967721-0500	VoiceOver	     AudioQueueObject.cpp:10141 SetLoudnessFromLM: hardware not supported, Loudness Manager disabled
default	11:55:47.969888-0500	VoiceOver	     AudioQueueObject.cpp:3249  CheckSpatialization: aq@0x984838000 CheckSpatialization mAutomaticSpatialization=1, mSpatializationEnabled=0 mContentRequiresAUSpatialMixer=0 mHasMetadata=0 mIsOffline=0 STSLabel valid:0 is stereo: 0
default	11:55:48.607161-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:48.607430-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:49.314223-0500	bluetoothd	Dynamic Latency Trigger fKeyboardOn =0, fVoiceOverOn=0, fGameModeOn=0, fGarageBandOn=0, fSpatialVideoOn=0, fSpatialMusicOn=0, fScreenOn =1, fExpanseOn =0, fAudioInputAggregateOn=0, fConsoleGameModeOn=0
default	11:55:49.601479-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:49.601699-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:50.201488-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:55:50.204260-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.VoiceOver(501)>:24873] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-24873-17355 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:55:50.204375-0500	runningboardd	Assertion 394-24873-17355 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:55:50.204847-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring jetsam update because this process is not memory-managed
default	11:55:50.204834-0500	runningboardd	Acquiring assertion targeting [osservice<com.apple.VoiceOver(501)>:24873] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-17356 target:24873 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:55:50.204922-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring suspend because this process is not lifecycle managed
default	11:55:50.204962-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring GPU update because this process is not GPU managed
default	11:55:50.204986-0500	runningboardd	Assertion 394-328-17356 (target:[osservice<com.apple.VoiceOver(501)>:24873]) will be created as active
default	11:55:50.205017-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring memory limit update because this process is not memory-managed
default	11:55:50.205058-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Skipping AppNap state - not lifecycle managed
default	11:55:50.208699-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring jetsam update because this process is not memory-managed
default	11:55:50.208741-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring suspend because this process is not lifecycle managed
default	11:55:50.208767-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring GPU update because this process is not GPU managed
default	11:55:50.208820-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Ignoring memory limit update because this process is not memory-managed
default	11:55:50.208853-0500	runningboardd	[osservice<com.apple.VoiceOver(501)>:24873] Skipping AppNap state - not lifecycle managed
default	11:55:50.209795-0500	gamepolicyd	Received state update for 24873 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	11:55:50.212759-0500	gamepolicyd	Received state update for 24873 (osservice<com.apple.VoiceOver(501)>, running-NotVisible
default	11:55:50.213347-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:55:50.214354-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ea010","name":"VoiceOver(24873)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	11:55:50.214570-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	11:55:50.214592-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.apple.VoiceOver with category/mode MediaPlayback/Default and coreSessionID = 17 starting playing
default	11:55:50.214673-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:55:50.214729-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 17, PID = 24873, Name = sid:0x1ea010, VoiceOver(24873), 'prim', BundleID = com.apple.VoiceOver, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	11:55:50.214764-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ea012, Nexy(25083), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1ea010, VoiceOver(24873), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:55:50.214807-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.apple.VoiceOver, isDoingIO = YES, score = 201, deviceID = <private>
default	11:55:50.214847-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ea010 to isSessionRecording: 0
	app: {"name":"[implicit] VoiceOver","pid":24873}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ea010, sessionType: 'prim', isRecording: false }, 
]
default	11:55:50.214958-0500	VoiceOver	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	11:55:50.214989-0500	VoiceOver	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:55:50.215146-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.apple.VoiceOver CID 0x19BF0001 category Not set
default	11:55:50.215409-0500	audiomxd	UpdateAudioState CID 0x19BF0001 audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	11:55:50.215301-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 0.425000, [0, 0], 0.000000)
default	11:55:50.215513-0500	audioaccessoryd	Audio state update Start apps {
    "com.apple.VoiceOver" : 201,
}
default	11:55:50.215545-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.apple.VoiceOver" : 201,
}
default	11:55:50.215563-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.apple.VoiceOver NULL -> 201 count 2
default	11:55:50.215573-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:55:50.215655-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:55:50.216130-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474878280 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:55:50.243918-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:55:50.244754-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:55:50.245019-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:55:50.245059-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
fault	11:55:50.245069-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:55:50.245146-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:55:50.245635-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:55:50.245728-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:55:50.245791-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
fault	11:55:50.245868-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:55:50.246057-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:55:50.246077-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:55:50.260091-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 5438250 ioTS st: 5438250 ht: 23868.608048
error	11:55:50.431731-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:55:50.590061-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:50.590310-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:55:51.023088-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:55:51.593033-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:51.593265-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:55:52.135612-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 25109
default	11:55:52.136039-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 25109
default	11:55:52.156310-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:52.156428-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:55:52.617429-0500	VoiceOver	CoreText note: Client requested name "<private>", it will get TimesNewRomanPSMT rather than the intended font. All system UI font access should be through proper APIs such as CTFontCreateUIFontForLanguage() or +[NSFont systemFontOfSize:].
default	11:55:52.626055-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:55:52.631180-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:55:52.631264-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:55:52.647329-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:02  id:21474878280 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:55:52.648216-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474878286 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:55:52.719750-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:55:52.720639-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:55:52.720840-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:55:52.720861-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:55:52.720901-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:55:52.721120-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
fault	11:55:52.720963-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:55:52.721175-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:55:52.721256-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:55:52.721537-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
fault	11:55:52.721585-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:55:52.721551-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	11:55:52.971941-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:55:53.032679-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000007 pid: 25119
default	11:55:53.033073-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 25119
fault	11:55:53.322835-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:55:53.323241-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 25122
default	11:55:53.323263-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 25121
default	11:55:53.629690-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:53.629923-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:55:53.636112-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:53.636514-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:55:54.026031-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:55:54.061876-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:54.062000-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:55:54.294576-0500	VoiceOver	No list of permitted front apps returned
default	11:55:54.294758-0500	VoiceOver	SACScreenSaverIsRunning:290: enter
default	11:55:54.294795-0500	VoiceOver	No list of permitted front apps returned
default	11:55:54.295216-0500	loginwindow	-[SessionAgentCom SACScreenSaverIsRunning:] | Enter,   sent by pid: 24873, name: VoiceOver
default	11:55:54.295291-0500	VoiceOver	SACScreenSaverIsRunning:301: SACScreenSaverIsRunning: exit: isRunning = 0
default	11:55:54.344940-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: e0000000f pid: 25123
default	11:55:54.348956-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1800000019 pid: 25123
default	11:55:54.355938-0500	VoiceOver	[0x984116800] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:54.359205-0500	VoiceOver	[0x984116800] invalidated after the last release of the connection object
default	11:55:54.446398-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 25125
default	11:55:54.498939-0500	VoiceOver	No list of permitted front apps returned
default	11:55:54.499119-0500	VoiceOver	No list of permitted front apps returned
default	11:55:54.525213-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:54.525335-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:54.527753-0500	VoiceOver	[0x9841166c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:54.527864-0500	VoiceOver	[0x9841166c0] invalidated after the last release of the connection object
default	11:55:54.529546-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983c05980, from  2 ch,  44100 Hz, lpcm (0x0000000E) 16-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:55:54.529567-0500	VoiceOver	AudioConverter -> 0x983c05980: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:55:54.529616-0500	VoiceOver	AudioConverter -> 0x983c05980: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:55:54.538969-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 25127
default	11:55:54.539494-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 25126
default	11:55:54.546778-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:55:54.550597-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:55:54.550661-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:55:54.578672-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474878286 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:55:54.579416-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474878287 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:55:54.607680-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474878287 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:55:54.608361-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474878288 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:55:54.609656-0500	VoiceOver	[0x984115f40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:54.609813-0500	VoiceOver	[0x984115f40] invalidated after the last release of the connection object
default	11:55:54.663131-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
fault	11:55:54.663822-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:55:54.663857-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
default	11:55:54.664083-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:55:54.664110-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:55:54.664148-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
fault	11:55:54.664257-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:55:54.664321-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:55:54.664412-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
default	11:55:54.664448-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:55:54.664705-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:55:54.664730-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
error	11:55:54.691498-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:55:55.055433-0500	VoiceOver	No list of permitted front apps returned
default	11:55:55.607319-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:55.607630-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:55:55.831670-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474878288 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:55:56.346313-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474878289 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	11:55:56.578017-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:55:56.617621-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:56.617741-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:55:57.023025-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:55:57.624358-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:57.624696-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:55:58.624310-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:58.624583-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:55:59.618541-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:55:59.618757-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:56:00.023055-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:56:00.622759-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:56:00.622988-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:56:01.611572-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:56:01.611773-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:56:01.744103-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 25132
default	11:56:02.212409-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:56:02.220618-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:56:02.220705-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:56:02.230695-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 300000002 pid: 25133
default	11:56:02.240170-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:05  id:21474878289 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:56:02.247020-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474878292 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
default	11:56:02.325644-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=3, err=0
default	11:56:02.326316-0500	VoiceOver	           AQMEIO_HAL.cpp:1555  User-selected BT device category is 0
fault	11:56:02.326401-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:56:02.326507-0500	VoiceOver	           AQMEIO_HAL.cpp:1914  user spatial mode for app com.apple.VoiceOver: 1
default	11:56:02.326529-0500	VoiceOver	SpatializationManager.cpp:184   Spatial info for binding = Default-Output: {
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
default	11:56:02.326561-0500	VoiceOver	     AudioQueueObject.cpp:5762  ApplyParameters: aq@0x984838000 volume 1.000 1.000 1.000 1.000 1.000 1.000, 1.000
default	11:56:02.326716-0500	VoiceOver	 MEDeviceStreamClient.cpp:245   AQME Default-Output: client starting: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 1
default	11:56:02.326780-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize starting IO deviceID=85, frame size is 480
fault	11:56:02.326869-0500	runningboardd	Two equal instances have unequal identities. <type=daemon identifier=com.apple.VoiceOver AUID=501> and <type=daemon identifier=com.apple.VoiceOver AUID=202>
default	11:56:02.326805-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:56:02.327040-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 2]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:56:02.327053-0500	VoiceOver	           AQMEIO_HAL.cpp:2818  aqmeio@0x984591818, device 85 (1C-77-54-18-C8-A3:output), AudioDeviceStart (err 0)
default	11:56:02.340082-0500	VoiceOver	AQSTL aq(0x984838000) start time resolved to: 5704616 ioTS st: 5704616 ht: 23880.688048
error	11:56:02.373310-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:56:02.609767-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:56:02.609929-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:56:03.022995-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:56:03.494846-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:56:03.494951-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:56:03.495953-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:56:03.496042-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:56:03.645246-0500	VoiceOver	[0x984115a40] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:56:03.645495-0500	VoiceOver	[0x984115a40] invalidated after the last release of the connection object
default	11:56:03.856744-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000007 pid: 25139
default	11:56:03.857436-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 25139
default	11:56:04.037412-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:56:04.037950-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:56:04.106431-0500	VoiceOver	       AudioConverter.cpp:1067  Created a new in process converter -> 0x983d0d410, from  2 ch,  44100 Hz, lpcm (0x0000000E) 24-bit big-endian signed integer to  2 ch,  44100 Hz, Float32, deinterleaved
default	11:56:04.106471-0500	VoiceOver	AudioConverter -> 0x983d0d410: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:56:04.106481-0500	VoiceOver	AudioConverter -> 0x983d0d410: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	11:56:04.141098-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474878294 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:56:04.640924-0500	VoiceOver	[0x984116bc0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:56:04.641041-0500	VoiceOver	[0x984116bc0] invalidated after the last release of the connection object
default	11:56:04.660020-0500	powerd	Process VoiceOver.24873 Created PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:00  id:21474878327 [System: PrevIdle PrevDisp DeclUser IntPrevDisp kDisp]
error	11:56:04.754600-0500	VoiceOver	         AVAudioBuffer.mm:281   mBuffers[0].mDataByteSize (0) should be non-zero
default	11:56:05.615683-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:56:05.615890-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:56:06.022975-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 3
default	11:56:06.313224-0500	VoiceOver	           AQMEIO_HAL.cpp:2849  FetchAndLogFrameSize GetCurrentIOBufferFrameSize deviceID=85, frame size is 480
default	11:56:06.321403-0500	VoiceOver	       MEMixerChannel.cpp:3281  mFormatID='lpcm', mNumChannels=1, mBestAvailableContentType=0, mContentspatializable=0, mSpatializationStatus=0, err=0
default	11:56:06.321501-0500	VoiceOver	 MEDeviceStreamClient.cpp:468   AQME Default-Output: client stopping: <AudioQueueObject@0x984838000; ; [24873]; play>; running count now 0
default	11:56:06.328181-0500	powerd	Process VoiceOver.24873 Released PreventUserIdleDisplaySleep "VoiceOver.isSpeaking" age:00:00:01  id:21474878327 [System: PrevIdle DeclUser IntPrevDisp kDisp]
default	11:56:06.536873-0500	VoiceOver	AudioHardware-mac-imp.cpp:3422   AudioDeviceDuck(85, 1.000000, [0, 0], 1.700000)
default	11:56:06.620606-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:56:06.620836-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:56:06.689100-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 900000008 pid: 25141
default	11:56:06.689524-0500	distnoted	register name: com.apple.universalaccess.VoiceOverSettingsDidChange object: kCFNotificationAnyObject token: 1300000015 pid: 25141
default	11:56:06.814476-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.apple.VoiceOver 201
default	11:56:06.814527-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.apple.VoiceOver
default	11:56:06.835144-0500	VoiceOver	[0x984116d00] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.AXVisualSupportAgent
default	11:56:06.835259-0500	VoiceOver	[0x984116d00] invalidated after the last release of the connection object
default	11:56:08.420205-0500	VoiceOver	aqmeio@0x984591818 Stop id=85
default	11:56:08.420197-0500	VoiceOver	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:56:08.420646-0500	VoiceOver	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:56:09.022969-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:56:12.023005-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.apple.VoiceOver, Score 201, Remote 100 NumofApp 2
default	11:56:13.500669-0500	VoiceOver	No list of permitted front apps returned

