<h1 align="center">XChainPY-lib Test for Client</h1>

![GitHub](https://img.shields.io/github/license/HooriRn/xchainpy-lib-test-client)

XChainPY is a library with a common interface for multiple blockchains, built for simple and fast integration for wallets and more.

This is a test for client side of XChainPY library.

## Usage
Initially this project is based upon `python3.8`

1. Clone the repo
    
   ```bash
       $ git clone https://github.com/HooriRn/xchainpy-lib-test-client
   ```

2. Install the dependencies

    XChainPy python library requirements :
    * bip_utils
    * pytest
    * mnemonic
    * python_binance_chain
    * secp256k1
    * pywallet
    * binance_chain

    ### before installing libraries setup secp256k1 C library with
    
    #### Linux
    ```bash
        $ sudo apt-get install libssl-dev build-essential automake pkg-config libtool libffi-dev libgmp-dev libyaml-cpp-dev
        $ sudo apt install libsecp256k1-dev
    ```
    
    #### Macintoch
    - need to have brew installed
    ```bash
        $ sudo brew install automake pkg-config libtool libffi gmp
    ```
    
    If you are running older version of macOS install dependencies with this parameter `--build-from-source`
    
    for more installation info, please see [this link](https://github.com/ludbb/secp256k1-py)
    
    #### !! There is no native support for this library in Windows yet, so you might use WSL for this installation
    
    
    Then get into the repo folder and run this
   
   ```bash
       $ pip install -r requirements.txt 
   ```

3. Run xchainpy test

    ```bash
       $ python xchainpy_test_example.py
   ```

## Other Things
⏲ coming soon...

## License
[MIT licensed](LICENSE)
