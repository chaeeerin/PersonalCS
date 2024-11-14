{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OJakj2Fch7pR",
        "outputId": "ef2e404d-a42b-458f-a1de-27ad46bcbad5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'mixedillWB'...\n",
            "remote: Enumerating objects: 152, done.\u001b[K\n",
            "remote: Counting objects: 100% (9/9), done.\u001b[K\n",
            "remote: Compressing objects: 100% (8/8), done.\u001b[K\n",
            "remote: Total 152 (delta 3), reused 1 (delta 0), pack-reused 143 (from 1)\u001b[K\n",
            "Receiving objects: 100% (152/152), 72.10 MiB | 11.91 MiB/s, done.\n",
            "Resolving deltas: 100% (39/39), done.\n",
            "Updating files: 100% (53/53), done.\n"
          ]
        }
      ],
      "source": [
        "!git clone https://github.com/mahmoudnafifi/mixedillWB.git"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q3tSnqbLK2mF",
        "outputId": "213478f8-a220-4a2d-dfff-e0e10be9e38a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pwd"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vf4j5AK4dYOU",
        "outputId": "4114d15f-e1d1-450a-b62f-bb03487b3463"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/mixedillWB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd mixedillWB"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OsB4vAR2TLhR",
        "outputId": "1d49c2e9-eb5a-430a-e5ec-4ee8472c5ee0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/mixedillWB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "# dataset 폴더 경로\n",
        "base_dir = \"/content/drive/MyDrive/dataset_origin\"\n",
        "output_dir = \"/content/drive/MyDrive/dataset\"\n",
        "\n",
        "# 모든 하위 폴더 탐색\n",
        "for root, dirs, files in os.walk(base_dir):\n",
        "    # 이미지 파일이 있는 폴더만 대상으로 처리\n",
        "    if files:\n",
        "        os.makedirs(output_dir, exist_ok=True)\n",
        "\n",
        "        # test.py를 각 하위 폴더에 대해 실행\n",
        "        !python test.py --wb-settings D S T \\\n",
        "            --model-name WB_model_p_128_D_S_T \\\n",
        "            --testing-dir \"{root}\" \\\n",
        "            --outdir \"{output_dir}\" \\\n",
        "            --target-size 256\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TTrMvrooXkec",
        "outputId": "f4dbee46-0ac7-4c78-dc3e-d5b2fabdf7cf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/mixedillWB/src/ops.py:43: SyntaxWarning: \"is\" with a literal. Did you mean \"==\"?\n",
            "  if aug_op is 1:\n",
            "/content/mixedillWB/src/ops.py:52: SyntaxWarning: \"is\" with a literal. Did you mean \"==\"?\n",
            "  elif aug_op is 2:\n",
            "/content/mixedillWB/src/ops.py:61: SyntaxWarning: \"is\" with a literal. Did you mean \"==\"?\n",
            "  elif aug_op is 3:\n",
            "/content/mixedillWB/src/imresize.py:105: SyntaxWarning: \"is\" with a literal. Did you mean \"==\"?\n",
            "  if method is 'bicubic':\n",
            "/content/mixedillWB/src/imresize.py:107: SyntaxWarning: \"is\" with a literal. Did you mean \"==\"?\n",
            "  elif method is 'bilinear':\n",
            "INFO: Testing Mixed-Ill WB correction\n",
            "INFO: Using device cuda\n",
            "/content/mixedillWB/test.py:213: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.\n",
            "  net.load_state_dict(torch.load(model_path, map_location=device))\n",
            "INFO: Model loaded from models/WB_model_p_128_D_S_T.pth\n",
            "INFO: Loading images information from /content/drive/MyDrive/fall_05...\n",
            "INFO: Loading images information from /content/drive/MyDrive/fall_05...\n",
            "/content/mixedillWB/src/dataset.py:50: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.\n",
            "  self.deepWB_T.load_state_dict(torch.load('DeepWB/models/net_t.pth'))\n",
            "/content/mixedillWB/src/dataset.py:52: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.\n",
            "  self.deepWB_S.load_state_dict(torch.load('DeepWB/models/net_s.pth'))\n",
            "INFO: Creating dataset with 200 examples\n",
            "INFO: Starting testing:\n",
            "        Model Name:            WB_model_p_128_D_S_T\n",
            "        Batch size:            1\n",
            "        Output dir:            /content/drive/MyDrive/dataset_modified/fall\n",
            "        WB settings:           ['D', 'S', 'T']\n",
            "        Save weights:          True\n",
            "        Device:                cuda\n",
            "  \n",
            "INFO: End of testing\n"
          ]
        }
      ]
    }
  ]
}