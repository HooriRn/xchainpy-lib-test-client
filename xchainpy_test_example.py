from xchainpy.xchainpy_crypto import crypto
from xchainpy.xchainpy_binance import clients
import asyncio
import json

class example_xchainpy:
    """
        example_xchainpy
        run the main
    """

    def readMnemonicfromFile(self, mnemonic_file):
        with open(mnemonic_file) as mnemonic:
            return mnemonic.readline()

    async def importKeystore(self, password, file):
        with open(file) as json_file:
            keystore = json.load(json_file)
            res = await crypto.decrypt_from_keystore(keystore, password)
            return res

    async def importMnemonic(self, keyPhrase_file):
        mnemonic_str = self.readMnemonicfromFile(keyPhrase_file)
        return mnemonic_str

    async def getWallet(self, phrase):
        return clients.Client(phrase, network="testnet")


    async def getUrlOfBNB(self):
        return self.client.get_client_url()

    async def getAddressBNBChain(self):
        return self.client.get_address()

    async def getBalancesOfAllAssets(self):
        return await self.client.get_balance()

    async def getFees(self):
        return await self.client.get_fees()

    async def transferToItself(self, amount):
        balance_assets = await self.client.get_balance()
        address = self.client.get_address()
        # maybe choosing the asset should be better
        runeAsset = balance_assets[1]['asset']
        # the only thing that gets back is the hash
        hash = await self.client.transfer(runeAsset, amount, address)
        return hash

    async def transferAsset(self, address, asset, amount):
        balance_assets = await self.client.get_balance()
        # maybe choosing the asset should be better
        for balance_asset in balance_assets:
            if asset == balance_asset.asset:
                trans_asset = balance_asset.asset
                break
        # the only thing that gets back is the hash
        hash = await self.client.transfer(trans_asset, amount, address)
        return hash

    async def main(self):
        # before begin fill these variables
        walletPassword = "your wallet password goes here"
        phraseMode = 1

        try:
            # testing phrase wallet and mnemonic examples
            if phraseMode:
                phrase = await self.importMnemonic('./example-mnemonic.txt')
            else:
                phrase = await self.importKeystore(walletPassword, "./wallet.txt")
            print(phrase)

            # accessing the wallet
            self.client = await self.getWallet(phrase)

            # getting the url of BNB this method might be a helper method so it should be used later
            url = await self.getUrlOfBNB()
            print(url)

            # getting the address of BNB chain asset it could be better for clients if they backup asset wise
            walletAddress = await self.getAddressBNBChain()
            print(walletAddress)

            # getting balances of all assets from BNB chain
            assets = await self.getBalancesOfAllAssets()

            # printing all assets and theirs amount
            for asset in assets:
                print(asset.asset)
                print(asset.amount)

            # getting current fee in three order from BNB chain also there is more fee getters
            fees = await self.getFees()
            print(fees)

            # doing a self transfer
            hash = await self.transferToItself(0.5)
            print(hash)

            #doing a simple transfer for RUNE (BNB.RUNE-67C)
            hash = await self.transferAsset('your address', 'BNB.RUNE-67C', 0.5)
            print(hash)

        except Exception as e:
            print("Exception is catched:", e)
            return

        print("\npassed without any exceptions \n")
        return

if __name__ == '__main__':
    exp = example_xchainpy()
    asyncio.run(exp.main()) # using asyncio application style

    # some connection errors will occur that's might be because there is no purge client yet in the code


    """
        for python 3.6 or lower run this one
        ------------>
        exp = example_xchainpy()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(exp.main())
        loop.close()
    """



