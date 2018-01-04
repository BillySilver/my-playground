安裝 Nvidia 驅動以及 CUDA / cuDNN 在 Linux 上
=============================================

這篇是寫給第一次在 Linux 系統上安裝 Nvidia 顯示卡，且要讓 TensorFlow 在它上面執行的人看的。

執行這些流程時，我只安裝一張顯示卡。不過之後插上第二張不用再做其他設定，就能被識別了。

1. [環境](#環境)
2. [Nvidia 驅動](#nvidia-驅動)
    1. [移除舊版 Nvidia 驅動（選用）](#移除舊版-nvidia-驅動選用)
    2. [安裝所需的 Nvidia 驅動](#安裝所需的-nvidia-驅動)
    3. [參考](#參考)
3. [CUDA 與 cuDNN](#cuda-與-cudnn)
    1. [安裝 CUDA](#安裝-cuda)
    2. [安裝 cuDNN](#安裝-cudnn)
    3. [設置臨時環境變數](#設置臨時環境變數)
    4. [參考](#參考-1)



環境
----

* Ubuntu 16.04 LTS 64-bit
* Nvidia 驅動版本：387
* CUDA 版本：8.0
* cuDNN 版本：6.0

CUDA 與 cuDNN 版本皆為了對應 TensorFlow 1.3 或 1.4。

Nvidia 驅動版本 387 為目前（Jan. 4, 2018）最新版。



Nvidia 驅動
-----------

### 移除舊版 Nvidia 驅動（選用）

如果曾安裝過 Nvidia 驅動，要先移除的話，可以使用下列命令；否則，跳過這一步。

> sudo apt-get autoremove --purge nvidia*

徹底移除 Nvidia 驅動並清除相關遺留檔案後，重新開機。


### 安裝所需的 Nvidia 驅動

因為 Ubuntu 使用的 X-Window GUI 會在開機後用 GPU 執行，先不要透過登入後開啟 terminal 安裝。

啟動作業系統後，在登入畫面按下 `Ctrl + Alt + [F1-F6]` 開啟 `tty`。在這個 terminal 打帳號密碼登入。

* 如果需要回到 GUI 介面，按下 `Ctrl + Alt + F7`。

再來，新增 graphics-drivers 這個 PPA（Personal Package Archives），更新一下套件管理工具。

> sudo add-apt-repository ppa:graphics-drivers  
> sudo apt-get update

之後就能透過 `apt-get` 安裝 Nvidia 驅動了。

> sudo apt-get install nvidia-***387***

***387*** 是目前（Jan. 4, 2018）最新的版本，可以根據需求換成所需版本編號。

下載完一堆相依套件後，會直接在 terminal 出現安裝 UI。選項依個人需求選擇（我也忘了有什麼選項）。

如果看到跟 `nvidia-xconfig` 有關的選項，應該和 X-Window 在 GPU 中執行有關。

安裝完後，可以重新啟動系統。如果解析度不再很低，那應該是安裝成功了。

想額外確認的話，可以在登入後，再用下列命令檢查是否安裝成功：

> lsmod | grep nvidia

有安裝成功的話，應該會有幾行輸出結果。否則請砍掉 Nvidia 驅動再重來。

完全不想遇到驅動被更新而出問題的話，可以用下列命令鎖住當前版本而不更新。（非必要）

> sudo apt-mark hold nvidia-***387***


### 參考

* [[How To] Install Latest NVIDIA Drivers In Linux](http://www.linuxandubuntu.com/home/how-to-install-latest-nvidia-drivers-in-linux)



CUDA 與 cuDNN
-------------

### 安裝 CUDA

如果你的環境跟我不同，可能會需要自己選擇適合的安裝檔。點擊 [這裡](https://developer.nvidia.com/cuda-80-ga2-download-archive) 選擇適合你的環境的 CUDA 8.0。

選擇完後，複製頁面上 Base Installer 旁 Download 按鈕的連結，並設在 `CUDA_DL_LINK` 即可。

這邊採用的選擇是 **Linux > x86_64 > Ubuntu > 16.04 > deb (network)**。

* `sudo` 可能會要求你輸入密碼。先執行一下 `sudo echo ""` 讓之後的操作暫時不需要再輸入密碼。
* `apt-get` 命令是 Debian/Ubuntu 使用的套件管理工具。其他系統可能會要改用 `yum`、`zypper` 等。
* `dpkg` 命令是 Debian/Ubuntu 使用的套件安裝程式。其他系統可能會要改用 `rpm`。

> CUDA_DL_LINK="***https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb***"  
> CUDA_REPO_PKG=$(echo $CUDA_DL_LINK | grep -E "[^/]+$" -o)  
> wget $CUDA_DL_LINK  
> sudo ***dpkg*** -i $CUDA_REPO_PKG  
> sudo ***apt-get*** update  
> sudo ***apt-get*** -y install cuda-***8.0***  
> \# Delete remaining files.  
> rm $CUDA_REPO_PKG

如果在上面的安裝命令中不是用 `cuda-8.0` 而是 `cuda` 的話，會安裝最新版的 CUDA，但你使用的 TensorFlow 版本不一定支援。


### 安裝 cuDNN

安裝完 CUDA 後，就可以安裝 cuDNN 了。應該是不分 Linux 發行版。

> CUDNN_TAR_FILE="cudnn-8.0-linux-x64-v6.0.tgz"  
> wget http://developer.download.nvidia.com/compute/redist/cudnn/v6.0/$CUDNN_TAR_FILE  
> tar -xzvf $CUDNN_TAR_FILE  
> sudo cp -P cuda/include/cudnn.h /usr/local/cuda-8.0/include/  
> sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-8.0/lib64/  
> sudo chmod a+r /usr/local/cuda-8.0/lib64/libcudnn*  
> \# Delete remaining files.  
> rm $CUDNN_TAR_FILE  
> rm -rf cuda


### 設置臨時環境變數

我不太確定這個步驟是要在 `pip3 install tensorflow-gpu` 之前還之後，甚至是有沒有關聯。

有遇過每次開 terminal 都得要設置這些環境變數，才能在 `python3` 成功 `import tensorflow`。（不然會說找不到 CUDA 或是 cuDNN 之類的錯誤）

一般而言，之後都不用再設這些環境變數。

> export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}  
> export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}


### 參考
* [Install CUDA Toolkit v8.0 and cuDNN v6.0 on Ubuntu 16.04](https://gist.github.com/mjdietzx/0ff77af5ae60622ce6ed8c4d9b419f45)
