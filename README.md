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

    before installing libraries setup secp256k1 C library with
    ```bash
        $ sudo apt-get install libssl-dev build-essential automake pkg-config libtool libffi-dev libgmp-dev libyaml-cpp-dev
        $ sudo apt install libsecp256k1-dev
    ```
   
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
