class AudioService {
  constructor() {
    this.currentAudio = null;
    this.isPlaying = false;
  }

  async play(audioUrl, onEnd, onError) {
    try {
      this.stop();
      this.currentAudio = new Audio(audioUrl);
      this.currentAudio.volume = 1.0;

      this.currentAudio.onended = () => {
        this.isPlaying = false;
        if (onEnd) onEnd();
      };

      this.currentAudio.onerror = (error) => {
        this.isPlaying = false;
        if (onError) onError(error);
      };

      await this.currentAudio.play();
      this.isPlaying = true;
    } catch (error) {
      this.isPlaying = false;
      if (onError) onError(error);
      throw error;
    }
  }

  stop() {
    if (this.currentAudio) {
      this.currentAudio.pause();
      this.currentAudio.currentTime = 0;
      this.currentAudio = null;
      this.isPlaying = false;
    }
  }

  getIsPlaying() {
    return this.isPlaying;
  }
}

export default new AudioService();
