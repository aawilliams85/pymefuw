import os
import unittest

from pymefuw import MEFirmware

# Turn off sort so that tests run in line order
unittest.TestLoader.sortTestMethodsUsing = None

# Expected folder structure
# <Project Path>\tests\firmware\Helper\FUWhelper6xX.dll
# <Project Path>\tests\firmware\FUC\PVP6\<Version>\upgrade\SC.IMG

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
FIRMWARE_FOLDER_PATH = os.path.join(BASE_PATH, 'firmware')

class fuw_tests(unittest.TestCase):
    def setUp(self):
        self.ip_address = '192.168.40.123'
        #self.ip_address = '192.168.40.104,4,192.168.1.20'
        #self.ip_address = '192.168.1.20'
        pass

    def test_pvp6_v11(self):
        print('')
        self.fuw_helper_path = os.path.join(FIRMWARE_FOLDER_PATH, 'Helper', 'v15', 'FUWhelper6xX.dll')
        self.fuw_image_path = os.path.join(FIRMWARE_FOLDER_PATH, 'FUC', 'PVP6', 'ME_PVP6xX_11.00-20190915', 'upgrade', 'SC.IMG')
        print(self.fuw_helper_path)
        print(self.fuw_image_path)
        fuw = MEFirmware(self.ip_address)
        resp = fuw.upgrade(self.fuw_helper_path, self.fuw_image_path)
        for s in resp.device.log: print(s)
        print('')
        
    def test_pvp6_v12(self):
        print('')
        self.fuw_helper_path = os.path.join(FIRMWARE_FOLDER_PATH, 'Helper', 'v15', 'FUWhelper6xX.dll')
        self.fuw_image_path = os.path.join(FIRMWARE_FOLDER_PATH, 'FUC', 'PVP6', 'ME_PVP6xX_12.00-20200922', 'upgrade', 'SC.IMG')
        print(self.fuw_helper_path)
        print(self.fuw_image_path)
        fuw = MEFirmware(self.ip_address)
        resp = fuw.upgrade(self.fuw_helper_path, self.fuw_image_path)
        for s in resp.device.log: print(s)
        print('')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()