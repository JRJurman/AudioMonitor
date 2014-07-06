#SingleInstance, Force
MeterLength = 30
tCounter := 0
tDelay := 0

; Feel free to change the values below
tAudio := 0.10    ; Volume which triggers program (lowest = 0.00, highest = 1.00)
tLimit := 120     ; Number of periods where audio is over tAudio to trigger program (set as tCounter below)
tDLimit := 40     ; Periods of delay before we reset tCounter to 0
pDelay := 5       ; Number of seconds that programs are muted and screen is blacked out
pPunish := 5      ; Number of seconds that are added to pDelay for everytime we have to black out
fSize := 80       ; Size of Font on Blackout



audioMeter := VA_GetAudioMeter("Microphone")

VA_IAudioMeterInformation_GetMeteringChannelCount(audioMeter, channelCount)

VA_GetDevicePeriod("capture", devicePeriod)

Loop
{
    VA_IAudioMeterInformation_GetPeakValue(audioMeter, peakValue)    
    
    VarSetCapacity(peakValues, channelCount*4)
    VA_IAudioMeterInformation_GetChannelsPeakValues(audioMeter, channelCount, &peakValues)
    Loop %channelCount%
        meter := NumGet(peakValues, A_Index*4-4, "float")

    if ( meter > tAudio ) {
      ; We hit the volume limit
      tCounter := tCounter + 1
      tDelay := 0
    }
    else {
      ; The audio was below the volume limit
      tDelay := tDelay + 1
    }
    if ( tCounter > tLimit ) {
      ; The audio was above the volume limit too long

      ; The box below is useful for debugging, it has been commented out to remove verbosity
      ;MsgBox, %meter% | %tCounter% | %tDelay%

      VA_SetMasterMute(true, "playback")
      RunWait python AVMuter.py %pDelay% %fSize%
      VA_SetMasterMute(false, "playback")

      tCounter := 0
      pDelay := pDelay + pPunish
    }
    if ( tDelay > tDLimit ) {
      ; The audio was under the volume limit long enough to reset tCounter
      tCounter := 0
    }
    Sleep, %devicePeriod%
}
