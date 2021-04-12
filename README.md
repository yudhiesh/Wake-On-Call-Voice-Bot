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
