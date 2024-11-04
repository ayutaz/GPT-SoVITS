import requests

def tts_get():
    # GETリクエストのパラメータを設定
    params = {
        'text': 'こんにちは',
        'text_lang': 'ja',
        'ref_audio_path': 'ref_audio.wav',
        'prompt_text': 'また、東寺のように、五大明王と呼ばれる、主要な明王の中央に配されることも多い。',
        'prompt_lang': 'ja',
        'media_type': 'wav',
        'streaming_mode': 'false'
    }

    # GETリクエストを送信
    response = requests.get('http://127.0.0.1:9880/tts', params=params)

    # レスポンスの処理
    if response.status_code == 200:
        # 音声データをファイルに保存
        with open('output_get.wav', 'wb') as f:
            f.write(response.content)
        print('音声ファイルをoutput_get.wavに保存しました。')
    else:
        print(f"エラー {response.status_code}: {response.text}")

if __name__ == '__main__':
    tts_get()