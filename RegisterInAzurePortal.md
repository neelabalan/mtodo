## Register in Azure portal

To obtain the client id to get access to microsoft todo account go to [azure portal](portal.azure.com) and register an application by following the steps

1. Select the *Azure active directory* icon 


![aad](https://github.com/neelabalan/mtodo/blob/main/assets/azure-ad.png)


2. Click on *App Registrations* in the left tab


![app-register](https://github.com/neelabalan/mtodo/blob/main/assets/app-registration-tab.png)


3. Click register new app and then give `todo` as name and select `Accounts in any organizational directory and personal microsoft accounts`


![option-select](https://github.com/neelabalan/mtodo/blob/main/assets/options-register.png)


4. Once the app the is registered, In the left tab select the *Authentication* option. Turn the Allow public code flow to *Yes*


![device-code](https://github.com/neelabalan/mtodo/blob/main/assets/device-code-flow.png)


5. In the same windows select the *Add Platform* in *Platform Configuration* section and then select *Configure Desktop+Devices*. Select the option as show in the below image


![desktop-device](https://github.com/neelabalan/mtodo/blob/main/assets/desktop-devices.png)


6. Once done select the *Overview* in the left tab and you should be able to find *Application (client) ID*. Copy that value and write that to `config.toml`
