#-----------------------------------------------------------------------------
# This file is part of the 'axi-soc-ultra-plus-core'. It is subject to
# the license terms in the LICENSE.txt file found in the top-level directory
# of this distribution and at:
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
# No part of the 'axi-soc-ultra-plus-core', including this file, may be
# copied, modified, propagated, or distributed except according to the terms
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------

import pyrogue as pr
import axi_soc_ultra_plus_core.rfdc as rfdc
import time

class RfDataConverter(pr.Device):
    def __init__(
            self,
            gen3      = True, # True if using RFSoC GEN3 Hardware
            enAdcTile = [True,True,True,True],
            enDacTile = [True,True,True,True],
            **kwargs):
        super().__init__(**kwargs)

        ##############################
        # Variables
        ##############################
        self.add(pr.RemoteVariable(
            name         = 'ipVersionMajor',
            description  = 'IP version major',
            offset       =  0x0000,
            bitSize      =  8,
            bitOffset    =  24,
            mode         = 'RO',
            overlapEn    = True,
        ))

        self.add(pr.RemoteVariable(
            name         = 'ipVersionMinor',
            description  = 'IP version minor',
            offset       =  0x0000,
            bitSize      =  8,
            bitOffset    =  16,
            mode         = 'RO',
            overlapEn    = True,
        ))

        self.add(pr.RemoteVariable(
            name         = 'ipVersionRevision',
            description  = 'IP version revision',
            offset       =  0x0000,
            bitSize      =  8,
            bitOffset    =  8,
            mode         = 'RO',
            overlapEn    = True,
        ))

        self.add(pr.RemoteVariable(
            name         = 'Reset',
            description  = 'Reset all tiles, autoclear',
            offset       =  0x0004,
            bitSize      =  1,
            bitOffset    =  0,
            mode         = 'WO',
            overlapEn    = True,
        ))

        self.add(pr.RemoteVariable(
            name         = 'InterruptStatus',
            description  = 'Interrupt status register',
            offset       =  0x0100,
            bitSize      =  8,
            bitOffset    =  0,
            mode         = 'RO',
            hidden       = True,
            overlapEn    = True,
        ))

        self.add(pr.RemoteVariable(
            name         = 'axiTimeoutInterrupt',
            description  = 'Interrupt status register',
            offset       =  0x0100,
            bitSize      =  1,
            bitOffset    =  31,
            mode         = 'RO',
            hidden       = True,
            overlapEn    = True,
        ))

        self.add(pr.RemoteVariable(
            name         = 'InterruptEnable',
            description  = 'Interrupt enable register',
            offset       =  0x0104,
            bitSize      =  8,
            bitOffset    =  0,
            mode         = 'RW',
            hidden       = True,
            overlapEn    = True,
        ))

        self.add(pr.RemoteVariable(
            name         = 'axiTimeoutInterruptEnable',
            description  = 'Interrupt status register',
            offset       =  0x0104,
            bitSize      =  1,
            bitOffset    =  31,
            mode         = 'RW',
            hidden       = True,
            overlapEn    = True,
        ))

        for i in range(4):
            if enDacTile[i]:
                self.add(rfdc.RfTile(
                    name    = f'dacTile[{i}]',
                    isAdc   = False,
                    gen3    = gen3,
                    offset  = 0x04000 + 0x4000*i,
                    expand  = False,
                ))

        for i in range(4):
            if enAdcTile[i]:
                self.add(rfdc.RfTile(
                    name    = f'adcTile[{i}]',
                    isAdc   = True,
                    gen3    = gen3,
                    offset  = 0x14000 + 0x4000*i,
                    expand  = False,
                ))

        for i in range(2):
            self.add(pr.RemoteVariable(
                name         = f'MtsFifoCtrl[{i}]',
                description  = 'index[0] is MtsFifoCtrlADC, index[1] is MtsFifoCtrlDAC',
                offset       =  0x0010+4*i,
                bitSize      =  2,
                bitOffset    =  0,
                mode         = 'RW',
                hidden       = True,
                overlapEn    = True,
            ))

        self.add(pr.RemoteVariable(
            name         = 'MtsSysRefEnable',
            offset       =  0x6000+0x1C00+(0x24<<2), # XRFDC_DAC_TILE_DRP_ADDR(0) + XRFDC_HSCOM_ADDR offsets + XRFDC_MTS_SRCAP_T1
            bitSize      =  1,
            bitOffset    =  10, #  XRFDC_MTS_SRCAP_EN_TRX_M=0x0400
            mode         = 'RW',
            hidden       = True,
            overlapEn    = True,
        ))


        self.add(pr.RemoteVariable(
            name         = "RegSpace",
            description  = "",
            offset       = 0,
            bitSize      = 32 * 0x10000,
            bitOffset    = 0,
            numValues    = 0x10000,
            valueBits    = 32,
            valueStride  = 32,
            bulkOpEn     = False,
            overlapEn    = True,
            verify       = False,
            hidden       = True,
            base         = pr.UInt,
            mode         = "RW",
            groups       = ['NoState', 'NoConfig', 'NoStream'], # No YAML save/load
        ))

    def MultiTileSync(self):
        # ADC MTS Settings
        ADC_Sync_Config = XRFdc_MultiConverter_Sync_Config()
        
        # DAC MTS Settings
        DAC_Sync_Config = XRFdc_MultiConverter_Sync_Config()
        
        # Run MTS for the ADC & DAC


    def MtsAdcSync(self):
        # Disable the FIFOs
        self.MtsFifoCtrl[0].set(0x2)
        # Enable SysRef Rx
        self.MtsSysRefEnable.set(1)
        # Disable the FIFOs
        self.MtsFifoCtrl[0].set(0x3)

    def MtsDacSync(self):
        # Disable the FIFOs
        self.MtsFifoCtrl[1].set(0x2)
        # Enable SysRef Rx
        self.MtsSysRefEnable.set(1)
        # Disable the FIFOs
        self.MtsFifoCtrl[1].set(0x3)

    def Init(self, dynamicNco=False):

        # Useful pointers
        rfTile = self.find(typ=rfdc.RfTile)

        # Reset the RF Data Converter
        for tile in rfTile:
            tile.RestartStateStart.set(0)
            tile.RestartStateEnd.set(15)
            tile.RestartSM.set(0x1)
        self.Reset.set(0x1)
        time.sleep(0.2)
        for tile in rfTile:
            tile.RestartSM.set(0x1)
            while tile.RestartStateEnd.get() != 15:
                time.sleep(0.1)
        self.Reset.set(0x1)
        time.sleep(0.2)

        # Check for dynamic NCO
        if dynamicNco:
            # Change the RestartStateStart for dynamic NCO changes
            for tile in rfTile:
                tile.RestartStateStart.setDisp('Clock_Configuration[0]')
