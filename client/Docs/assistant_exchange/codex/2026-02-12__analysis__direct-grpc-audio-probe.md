# Analysis: Direct gRPC audio probe (server payload quality)

## Goal
Проверить прямым запросом, что реально приходит от сервера в `audio_chunk` (формат + амплитуда), чтобы исключить гипотезу о некорректных данных.

## Probe
- Request: `GrpcClient.stream_audio(...)`
- Hardware ID: `E03D2455-8EF1-5270-AA03-13B5771C7CB2`
- Session: `66fa89d0-977b-4562-a301-1596f4e54d5e`

## Raw result
- `TOTAL=99`, `AUDIO=97`, `TEXT=1`
- `sample_rate=[48000]`, `channels=[1]`, `dtype=['int16']`
- `PEAK_MAX=21107`, `RMS_MAX=7536.35`
- First chunks:
  - `(1, 2240 bytes, peak=0, rms=0.0)`
  - `(2, 4096 bytes, peak=0, rms=0.0)`
  - `(3, 512 bytes, peak=0, rms=0.0)`
  - `(4, 2304 bytes, peak=0, rms=0.0)`
  - `(5, 4096 bytes, peak=3, rms=0.68)`
  - `(6, 4096 bytes, peak=10, rms=1.30)`
  - `(7, 4096 bytes, peak=4535, rms=1759.59)`
  - `(8, 4096 bytes, peak=13830, rms=5459.96)`
  - `(9, 4096 bytes, peak=21107, rms=7257.90)`

## Conclusion
- Данные с сервера корректные по формату (`int16/48k/mono`) и имеют высокую амплитуду в полезной части потока.
- Root-cause не в "битом формате" ответа сервера.
- В потоке есть стартовые silent/near-silent чанки, значит проблема вероятнее в клиентской обработке/рендере после ingress (не в payload contract).
