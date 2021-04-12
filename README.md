# Wake On Keyword System

## TODO:

- Create a dataset of my voice repeating the keyword
- Augment the voice dataset as it is heavily imbalanced using SpecAugment
- Push data to Google Drive or to AWS S3(if Drive is unstable)
- Convert the audio files to Mel-Frequency Cepstrum Coeffiencients
- Train a LSTM or Transformer model for binary classification on the wake words
- Run inference on local machine to confirm model's predictions

## Future improvements

- Add in a dataset with room noise to the negative class
- Try out other augmentation methods

## Preprocessing Explanation

1. Convert the Waveform to the Time Domain
   ![Waveform](https://github.com/yudhiesh/Wake-On-Call-Voice-Bot/blob/master/Audio/waveform.png)

2. Convert the Waveform which is in the Time Domain to the Frequency Domain
   using Fast Fourier Transform. This outputs complex values for each sample so
   you take the absolute value of the results as the magnitude. The frequency is
   the range of values in linear space starting from 0Hz to the sampling
   rate(i.e. 22050Hz) with even spaces across the length of the magnitude.
   ![Power Spectrum](https://github.com/yudhiesh/Wake-On-Call-Voice-Bot/blob/master/Audio/powerspectrum.png)

3. If you noticed in the Power Spectrum image, the image is symmetric(property of
   the results from a Fast Fourier Transformation) so we only need to take half of
   the entire Power Spectrum(half of the magnitude and half of the frequency).
   ![Half of the Power Spectrum](https://github.com/yudhiesh/Wake-On-Call-Voice-Bot/blob/master/Audio/half_powerspectrum.png)

4. There is an important feature about sound that is it is composed of
   sinusoidal waves in different frequencies. To correctly represent human
   speech we will have to break the recording up into small windows and compute
   the frequencies used in each of the windows similar to how convolution works.
   This can be accomplished using the Short-time Fourier Transform. The values
   are passed through a log function as the loudness of sound is not linear but
   log-like instead.
   ![Log Spectrogram](https://github.com/yudhiesh/Wake-On-Call-Voice-Bot/blob/master/Audio/spectrogram.png)

5. Mel-frequency Cepstrum Coeffiencients are then computed on the original
   signal with the number of coefficients set to 13(values in the range of 12 to
   40 are suitable).
   ![MFCC](https://github.com/yudhiesh/Wake-On-Call-Voice-Bot/blob/master/Audio/mfcc.png)
