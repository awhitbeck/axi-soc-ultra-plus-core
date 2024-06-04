# https://github.com/Xilinx/embeddedsw/blob/xilinx_v2023.2/XilinxProcessorIPLib/drivers/rfdc/src/L133-L495
XRFDC_CLK_EN_OFFSET = 0x000 
XRFDC_ADC_DEBUG_RST_OFFSET = 0x004
XRFDC_ADC_FABRIC_RATE_OFFSET = 0x008
XRFDC_ADC_FABRIC_RATE_OBS_OFFSET = 0x050

def XRFDC_ADC_FABRIC_RATE_TDD_OFFSET(X):    
    if (X == 0):
        return XRFDC_ADC_FABRIC_RATE_OFFSET
    else:
        return XRFDC_ADC_FABRIC_RATE_OBS_OFFSET

XRFDC_DAC_FABRIC_RATE_OFFSET = 0x008 
XRFDC_ADC_FABRIC_OFFSET = 0x00C 
XRFDC_ADC_FABRIC_OBS_OFFSET = 0x054 

def XRFDC_ADC_FABRIC_TDD_OFFSET(X):    
    if (X == 0):
        return XRFDC_ADC_FABRIC_OFFSET
    else:
        return XRFDC_ADC_FABRIC_OBS_OFFSET

XRFDC_ADC_FABRIC_ISR_OFFSET = 0x010 
XRFDC_DAC_FIFO_START_OFFSET = 0x010 
XRFDC_DAC_FABRIC_ISR_OFFSET = 0x014 
XRFDC_ADC_FABRIC_IMR_OFFSET = 0x014 
XRFDC_DAC_FABRIC_IMR_OFFSET = 0x018 
XRFDC_ADC_FABRIC_DBG_OFFSET = 0x018 
XRFDC_ADC_FABRIC_DBG_OBS_OFFSET = 0x058 

def XRFDC_ADC_FABRIC_DBG_TDD_OFFSET(X):    
    if (X == 0):
        return XRFDC_ADC_FABRIC_DBG_OFFSET
    else:
        return XRFDC_ADC_FABRIC_DBG_OBS_OFFSET

XRFDC_ADC_UPDATE_DYN_OFFSET = 0x01C 
XRFDC_DAC_UPDATE_DYN_OFFSET = 0x020 
XRFDC_ADC_FIFO_LTNC_CRL_OFFSET = 0x020 
XRFDC_ADC_FIFO_LTNC_CRL_OBS_OFFSET = 0x064 

def XRFDC_ADC_FIFO_LTNC_CRL_TDD_OFFSET(X):    
    if (X == 0):
        return XRFDC_ADC_FIFO_LTNC_CRL_OFFSET
    else:
        return XRFDC_ADC_FIFO_LTNC_CRL_OBS_OFFSET

XRFDC_ADC_DEC_ISR_OFFSET = 0x030 
XRFDC_DAC_DATAPATH_OFFSET = 0x034 
XRFDC_ADC_DEC_IMR_OFFSET = 0x034 
XRFDC_DATPATH_ISR_OFFSET = 0x038 
XRFDC_DATPATH_IMR_OFFSET = 0x03C 
XRFDC_ADC_DECI_CONFIG_OFFSET = 0x040 
XRFDC_ADC_DECI_CONFIG_OBS_OFFSET = 0x048 

def XRFDC_ADC_DECI_CONFIG_TDD_OFFSET(X):    
    if (X == 0):
        return XRFDC_ADC_DECI_CONFIG_OFFSET
    else:
        return XRFDC_ADC_DECI_CONFIG_OBS_OFFSET

XRFDC_DAC_INTERP_CTRL_OFFSET = 0x040 
XRFDC_ADC_DECI_MODE_OFFSET = 0x044 
XRFDC_ADC_DECI_MODE_OBS_OFFSET = 0x04C 

def XRFDC_ADC_DECI_MODE_TDD_OFFSET(X):    
    if (X == 0):
        return XRFDC_ADC_DECI_MODE_OFFSET
    else:
        return XRFDC_ADC_DECI_MODE_OBS_OFFSET

XRFDC_DAC_ITERP_DATA_OFFSET = 0x044 
XRFDC_ADC_FABRIC_ISR_OBS_OFFSET = 0x05C 
XRFDC_ADC_FABRIC_IMR_OBS_OFFSET = 0x060 
XRFDC_DAC_TDD_MODE0_OFFSET = 0x060 
XRFDC_ADC_TDD_MODE0_OFFSET = 0x068 

def XRFDC_TDD_MODE0_OFFSET(X):    
    if (X == 0):
        return XRFDC_ADC_TDD_MODE0_OFFSET
    else:
        return XRFDC_DAC_TDD_MODE0_OFFSET

XRFDC_ADC_MXR_CFG0_OFFSET = 0x080 
XRFDC_ADC_MXR_CFG1_OFFSET = 0x084 
XRFDC_MXR_MODE_OFFSET = 0x088 
XRFDC_NCO_UPDT_OFFSET = 0x08C 
XRFDC_NCO_RST_OFFSET = 0x090 
XRFDC_ADC_NCO_FQWD_UPP_OFFSET = 0x094 
XRFDC_ADC_NCO_FQWD_MID_OFFSET = 0x098 
XRFDC_ADC_NCO_FQWD_LOW_OFFSET = 0x09C 
XRFDC_NCO_PHASE_UPP_OFFSET = 0x0A0 
XRFDC_NCO_PHASE_LOW_OFFSET = 0x0A4 
XRFDC_ADC_NCO_PHASE_MOD_OFFSET = 0x0A8 
XRFDC_QMC_UPDT_OFFSET = 0x0C8 
XRFDC_QMC_CFG_OFFSET = 0x0CC 
XRFDC_QMC_OFF_OFFSET = 0x0D0 
XRFDC_QMC_GAIN_OFFSET = 0x0D4 
XRFDC_QMC_PHASE_OFFSET = 0x0D8 
XRFDC_ADC_CRSE_DLY_UPDT_OFFSET = 0x0DC 
XRFDC_DAC_CRSE_DLY_UPDT_OFFSET = 0x0E0 
XRFDC_ADC_CRSE_DLY_CFG_OFFSET = 0x0E0 
XRFDC_DAC_CRSE_DLY_CFG_OFFSET = 0x0DC 
XRFDC_ADC_DAT_SCAL_CFG_OFFSET = 0x0E4 
XRFDC_ADC_SWITCH_MATRX_OFFSET = 0x0E8 
XRFDC_ADC_TRSHD0_CFG_OFFSET = 0x0EC 
XRFDC_ADC_TRSHD0_AVG_UP_OFFSET = 0x0F0 
XRFDC_ADC_TRSHD0_AVG_LO_OFFSET = 0x0F4 
XRFDC_ADC_TRSHD0_UNDER_OFFSET = 0x0F8 
XRFDC_ADC_TRSHD0_OVER_OFFSET = 0x0FC 
XRFDC_ADC_TRSHD1_CFG_OFFSET = 0x100 
XRFDC_ADC_TRSHD1_AVG_UP_OFFSET = 0x104 
XRFDC_ADC_TRSHD1_AVG_LO_OFFSET = 0x108 
XRFDC_ADC_TRSHD1_UNDER_OFFSET = 0x10C 
XRFDC_ADC_TRSHD1_OVER_OFFSET = 0x110 
XRFDC_ADC_FEND_DAT_CRL_OFFSET = 0x140 
XRFDC_ADC_TI_DCB_CRL0_OFFSET = 0x144 
XRFDC_ADC_TI_DCB_CRL1_OFFSET = 0x148 
XRFDC_ADC_TI_DCB_CRL2_OFFSET = 0x14C 
XRFDC_ADC_TI_DCB_CRL3_OFFSET = 0x150 
XRFDC_ADC_TI_TISK_CRL0_OFFSET = 0x154 
XRFDC_DAC_MC_CFG0_OFFSET = 0x1C4 
XRFDC_ADC_TI_TISK_CRL1_OFFSET = 0x158 
XRFDC_ADC_TI_TISK_CRL2_OFFSET = 0x15C 
XRFDC_ADC_TI_TISK_CRL3_OFFSET = 0x160 
XRFDC_ADC_TI_TISK_CRL4_OFFSET = 0x164 
XRFDC_ADC_TI_TISK_CRL5_OFFSET = 0x168 
XRFDC_ADC_TI_TISK_DAC0_OFFSET = 0x168 
XRFDC_ADC_TI_TISK_DAC1_OFFSET = 0x16C 
XRFDC_ADC_TI_TISK_DAC2_OFFSET = 0x170 
XRFDC_ADC_TI_TISK_DAC3_OFFSET = 0x174 
XRFDC_ADC_TI_TISK_DACP0_OFFSET = 0x178 
XRFDC_ADC_TI_TISK_DACP1_OFFSET = 0x17C 
XRFDC_ADC_TI_TISK_DACP2_OFFSET = 0x180 
XRFDC_ADC_TI_TISK_DACP3_OFFSET = 0x184 
XRFDC_DATA_SCALER_OFFSET = 0x190 
XRFDC_DAC_VOP_CTRL_OFFSET = 0x198 
XRFDC_ADC0_SUBDRP_ADDR_OFFSET = 0x198 
XRFDC_ADC0_SUBDRP_DAT_OFFSET = 0x19C 
XRFDC_ADC1_SUBDRP_ADDR_OFFSET = 0x1A0 
XRFDC_ADC1_SUBDRP_DAT_OFFSET = 0x1A4 
XRFDC_ADC2_SUBDRP_ADDR_OFFSET = 0x1A8 
XRFDC_ADC2_SUBDRP_DAT_OFFSET = 0x1AC 
XRFDC_ADC3_SUBDRP_ADDR_OFFSET = 0x1B0 
XRFDC_ADC3_SUBDRP_DAT_OFFSET = 0x1B4 
XRFDC_ADC_RX_MC_PWRDWN_OFFSET = 0x1C0 
XRFDC_ADC_DAC_MC_CFG0_OFFSET = 0x1C4 
XRFDC_ADC_DAC_MC_CFG1_OFFSET = 0x1C8 
XRFDC_ADC_DAC_MC_CFG2_OFFSET = 0x1CC 
XRFDC_DAC_MC_CFG3_OFFSET = 0x1D0 
XRFDC_ADC_RXPR_MC_CFG0_OFFSET = 0x1D0 
XRFDC_ADC_RXPR_MC_CFG1_OFFSET = 0x1D4 
XRFDC_ADC_TI_DCBSTS0_BG_OFFSET = 0x200 
XRFDC_ADC_TI_DCBSTS0_FG_OFFSET = 0x204 
XRFDC_ADC_TI_DCBSTS1_BG_OFFSET = 0x208 
XRFDC_ADC_TI_DCBSTS1_FG_OFFSET = 0x20C 
XRFDC_ADC_TI_DCBSTS2_BG_OFFSET = 0x210 
XRFDC_ADC_TI_DCBSTS2_FG_OFFSET = 0x214 
XRFDC_ADC_TI_DCBSTS3_BG_OFFSET = 0x218 
XRFDC_ADC_TI_DCBSTS3_FG_OFFSET = 0x21C 
XRFDC_ADC_TI_DCBSTS4_MB_OFFSET = 0x220 
XRFDC_ADC_TI_DCBSTS4_LB_OFFSET = 0x224 
XRFDC_ADC_TI_DCBSTS5_MB_OFFSET = 0x228 
XRFDC_ADC_TI_DCBSTS5_LB_OFFSET = 0x22C 
XRFDC_ADC_TI_DCBSTS6_MB_OFFSET = 0x230 
XRFDC_ADC_TI_DCBSTS6_LB_OFFSET = 0x234 
XRFDC_ADC_TI_DCBSTS7_MB_OFFSET = 0x238 
XRFDC_ADC_TI_DCBSTS7_LB_OFFSET = 0x23C 
XRFDC_DSA_UPDT_OFFSET = 0x254 
XRFDC_ADC_FIFO_LTNCY_LB_OFFSET = 0x280 
XRFDC_ADC_FIFO_LTNCY_MB_OFFSET = 0x284 
XRFDC_DAC_DECODER_CTRL_OFFSET = 0x180 
XRFDC_DAC_DECODER_CLK_OFFSET = 0x184 
XRFDC_MB_CONFIG_OFFSET = 0x308 
XRFDC_ADC_SIG_DETECT_CTRL_OFFSET = 0x114 
XRFDC_ADC_SIG_DETECT_THRESHOLD0_LEVEL_OFFSET = 0x118 
XRFDC_ADC_SIG_DETECT_THRESHOLD0_CNT_OFF_OFFSET = 0x11C 
XRFDC_ADC_SIG_DETECT_THRESHOLD0_CNT_ON_OFFSET = 0x120 
XRFDC_ADC_SIG_DETECT_MAGN_OFFSET = 0x130 
XRFDC_HSCOM_CLK_DSTR_OFFSET = 0x088 
XRFDC_HSCOM_CLK_DSTR_MASK = 0xC788 
XRFDC_HSCOM_CLK_DSTR_MASK_ALT = 0x1870 
XRFDC_HSCOM_PWR_OFFSET = 0x094 
XRFDC_HSCOM_CLK_DIV_OFFSET = 0xB0 
XRFDC_HSCOM_PWR_STATE_OFFSET = 0xB4 
XRFDC_HSCOM_UPDT_DYN_OFFSET = 0x0B8 
XRFDC_HSCOM_EFUSE_2_OFFSET = 0x144
XRFDC_DAC_INVSINC_OFFSET = 0x0C0 
XRFDC_DAC_MB_CFG_OFFSET = 0x0C4 
XRFDC_MTS_SRDIST = 0x1CA0
XRFDC_MTS_SRCAP_T1 = (0x24 << 2)
XRFDC_MTS_SRCAP_PLL = (0x0C << 2)
XRFDC_MTS_SRCAP_DIG = (0x2C << 2)
XRFDC_MTS_SRDTC_T1 = (0x27 << 2)
XRFDC_MTS_SRDTC_PLL = (0x26 << 2)
XRFDC_MTS_SRFLAG = (0x49 << 2)
XRFDC_MTS_CLKSTAT = (0x24 << 2)
XRFDC_MTS_SRCOUNT_CTRL = 0x004C
XRFDC_MTS_SRCOUNT_VAL = 0x0050
XRFDC_MTS_SRFREQ_VAL = 0x0054
XRFDC_MTS_FIFO_CTRL_ADC = 0x0010
XRFDC_MTS_FIFO_CTRL_DAC = 0x0014
XRFDC_MTS_DELAY_CTRL = 0x0028
XRFDC_MTS_ADC_MARKER = 0x0018
XRFDC_MTS_ADC_MARKER_CNT = 0x0010
XRFDC_MTS_DAC_MARKER_CTRL = 0x0048
XRFDC_MTS_DAC_MARKER_CNT = (0x92 << 2)
XRFDC_MTS_DAC_MARKER_LOC = (0x93 << 2)
XRFDC_MTS_DAC_FIFO_MARKER_CTRL = (0x94 << 2)
XRFDC_MTS_DAC_FABRIC_OFFSET = 0x0C
XRFDC_RESET_OFFSET = 0x00 
XRFDC_RESTART_OFFSET = 0x04 
XRFDC_RESTART_STATE_OFFSET = 0x08 
XRFDC_CURRENT_STATE_OFFSET = 0x0C 
XRFDC_CLOCK_DETECT_OFFSET = 0x80 
XRFDC_STATUS_OFFSET = 0x228 
XRFDC_CAL_DIV_BYP_OFFSET = 0x100 
XRFDC_COMMON_INTR_STS = 0x100 
XRFDC_COMMON_INTR_ENABLE = 0x104 
XRFDC_INTR_STS = 0x200 
XRFDC_INTR_ENABLE = 0x204 

def XRFDC_CONV_INTR_STS(X):
    return (0x208 + (X * 0x08))
def XRFDC_CONV_INTR_EN(X):
    return (0x20C + (X * 0x08))
def XRFDC_CONV_CAL_STGS(X):
    return (0x234 + (X * 0x04))
def XRFDC_CONV_DSA_STGS(X):
    return (0x244 + (X * 0x04))
def XRFDC_CAL_GCB_COEFF0_FAB(X):
    return (0x280 + (X * 0x10))
def XRFDC_CAL_GCB_COEFF1_FAB(X):
    return (0x284 + (X * 0x10))
def XRFDC_CAL_GCB_COEFF2_FAB(X):
    return (0x288 + (X * 0x10))
def XRFDC_CAL_GCB_COEFF3_FAB(X):
    return (0x28C + (X * 0x10))
def XRFDC_TDD_CTRL_SLICE_OFFSET(X):
    return (0x260 + (X * 0x04))

XRFDC_PLL_FREQ = 0x300 
XRFDC_PLL_FS = 0x304 
XRFDC_CAL_TMR_MULT_OFFSET = 0x30C
XRFDC_CAL_DLY_OFFSET = 0x310 
XRFDC_CPL_TYPE_OFFSET = 0x314 
XRFDC_FIFO_ENABLE = 0x230 
XRFDC_PLL_SDM_CFG0 = 0x00 
XRFDC_PLL_SDM_SEED0 = 0x18 
XRFDC_PLL_SDM_SEED1 = 0x1C 
XRFDC_PLL_VREG = 0x44 
XRFDC_PLL_VCO0 = 0x54 
XRFDC_PLL_VCO1 = 0x58 
XRFDC_PLL_CRS1 = 0x28 
XRFDC_PLL_CRS2 = 0x2C 
XRFDC_PLL_DIVIDER0 = 0x30 
XRFDC_PLL_DIVIDER1 = 0x34 
XRFDC_PLL_SPARE0 = 0x38 
XRFDC_PLL_SPARE1 = 0x3C 
XRFDC_PLL_REFDIV = 0x40 
XRFDC_PLL_VREG = 0x44 
XRFDC_PLL_CHARGEPUMP = 0x48 
XRFDC_PLL_LPF0 = 0x4C 
XRFDC_PLL_LPF1 = 0x50 
XRFDC_PLL_FPDIV = 0x5C 
XRFDC_CLK_NETWORK_CTRL0 = 0x8C 
XRFDC_CLK_NETWORK_CTRL1 = 0x90 
XRFDC_HSCOM_NETWORK_CTRL1_MASK = 0x02F 
XRFDC_PLL_REFDIV_MASK = 0x0E0 
XRFDC_PLL_DIVIDER0_ALT_MASK = 0xC00 
XRFDC_PLL_DIVIDER0_BYPPLL_MASK = 0x800 
XRFDC_PLL_DIVIDER0_BYPDIV_MASK = 0x400 
XRFDC_CAL_OCB1_OFFSET_COEFF0 = 0x200 
XRFDC_CAL_OCB1_OFFSET_COEFF1 = 0x208 
XRFDC_CAL_OCB1_OFFSET_COEFF2 = 0x210 
XRFDC_CAL_OCB1_OFFSET_COEFF3 = 0x218 
XRFDC_CAL_OCB2_OFFSET_COEFF0 = 0x204 
XRFDC_CAL_OCB2_OFFSET_COEFF1 = 0x20C 
XRFDC_CAL_OCB2_OFFSET_COEFF2 = 0x214 
XRFDC_CAL_OCB2_OFFSET_COEFF3 = 0x21C 
XRFDC_CAL_GCB_OFFSET_COEFF0 = 0x220 
XRFDC_CAL_GCB_OFFSET_COEFF1 = 0x224 
XRFDC_CAL_GCB_OFFSET_COEFF2 = 0x228 
XRFDC_CAL_GCB_OFFSET_COEFF3 = 0x22C 
XRFDC_CAL_GCB_OFFSET_COEFF0_ALT = 0x220 
XRFDC_CAL_GCB_OFFSET_COEFF1_ALT = 0x228 
XRFDC_CAL_GCB_OFFSET_COEFF2_ALT = 0x230 
XRFDC_CAL_GCB_OFFSET_COEFF3_ALT = 0x238 
XRFDC_CAL_TSCB_OFFSET_COEFF0 = 0x170 
XRFDC_CAL_TSCB_OFFSET_COEFF1 = 0x174 
XRFDC_CAL_TSCB_OFFSET_COEFF2 = 0x178 
XRFDC_CAL_TSCB_OFFSET_COEFF3 = 0x17C 
XRFDC_CAL_TSCB_OFFSET_COEFF4 = 0x180 
XRFDC_CAL_TSCB_OFFSET_COEFF5 = 0x184 
XRFDC_CAL_TSCB_OFFSET_COEFF6 = 0x188 
XRFDC_CAL_TSCB_OFFSET_COEFF7 = 0x18C 
XRFDC_CAL_TSCB_OFFSET_COEFF0_ALT = 0x168 
XRFDC_CAL_TSCB_OFFSET_COEFF1_ALT = 0x16C 
XRFDC_CAL_TSCB_OFFSET_COEFF2_ALT = 0x170 
XRFDC_CAL_TSCB_OFFSET_COEFF3_ALT = 0x174 
XRFDC_CAL_TSCB_OFFSET_COEFF4_ALT = 0x178 
XRFDC_CAL_TSCB_OFFSET_COEFF5_ALT = 0x17C 
XRFDC_CAL_TSCB_OFFSET_COEFF6_ALT = 0x180 
XRFDC_CAL_TSCB_OFFSET_COEFF7_ALT = 0x184 
XRFDC_HSCOM_FIFO_START_OFFSET = 0x0C0 
XRFDC_HSCOM_FIFO_START_OBS_OFFSET = 0x0BC 

def XRFDC_HSCOM_FIFO_START_TDD_OFFSET(X):    
    if (X == 0):
        return XRFDC_HSCOM_FIFO_START_OFFSET
    else:
        return XRFDC_HSCOM_FIFO_START_OBS_OFFSET

XRFDC_TILES_ENABLED_OFFSET = 0x00A0 
XRFDC_ADC_PATHS_ENABLED_OFFSET = 0x00A4 
XRFDC_DAC_PATHS_ENABLED_OFFSET = 0x00A8 
XRFDC_PATH_ENABLED_TILE_SHIFT = 4 
XRFDC_CURRENT_STATE_MASK = 0x0000000F 
XRFDC_CAL_MODES_MASK = 0x0003 
XRFDC_CAL_OCB_MASK = 0xFFFF 
XRFDC_CAL_GCB_MASK = 0x0FFF 
XRFDC_CAL_GCB_FAB_MASK = 0xFFF0 
XRFDC_CAL_TSCB_MASK = 0x01FF 
XRFDC_CAL_GCB_FLSH_MASK = 0x1000 
XRFDC_CAL_GCB_ACEN_MASK = 0x0800 
XRFDC_CAL_GCB_ENFL_MASK = 0x1800 
XRFDC_CAL_OCB_EN_MASK = 0x0001 
XRFDC_CAL_GCB_EN_MASK = 0x2000 
XRFDC_CAL_TSCB_EN_MASK = 0x8000 
XRFDC_CAL_OCB_EN_SHIFT = 0 
XRFDC_CAL_GCB_EN_SHIFT = 13 
XRFDC_CAL_TSCB_EN_SHIFT = 15 
XRFDC_CAL_GCB_FLSH_SHIFT = 12 
XRFDC_CAL_GCB_ACEN_SHIFT = 11 
XRFDC_CAL_TSCB_TUNE_MASK = 0x0FF0 
XRFDC_CAL_SLICE_SHIFT = 16 
XRFDC_CAL_FREEZE_CAL_MASK = 0x1 
XRFDC_CAL_FREEZE_STS_MASK = 0x2 
XRFDC_CAL_FREEZE_PIN_MASK = 0x4 
XRFDC_CAL_FREEZE_CAL_SHIFT = 0 
XRFDC_CAL_FREEZE_STS_SHIFT = 1 
XRFDC_CAL_FREEZE_PIN_SHIFT = 2 

# https://github.com/Xilinx/embeddedsw/blob/xilinx_v2023.2/XilinxProcessorIPLib/drivers/rfdc/src/xrfdc_hw.h#L497-L997
XRFDC_FIFO_EN_MASK = 0x00000001 
XRFDC_FIFO_EN_OBS_MASK = 0x00000002 
XRFDC_FIFO_EN_OBS_SHIFT = 1 
XRFDC_RESTART_MASK = 0x00000001 
XRFDC_CLK_EN_CAL_MASK = 0x00000001 
XRFDC_CLK_EN_DIG_MASK = 0x00000002 
XRFDC_CLK_EN_DP_MASK = 0x00000004 
XRFDC_CLK_EN_FAB_MASK = 0x00000008 
XRFDC_DAT_CLK_EN_MASK = 0x0000000F 
XRFDC_CLK_EN_LM_MASK = 0x00000010 
XRFDC_DBG_RST_CAL_MASK = 0x00000001 
XRFDC_DBG_RST_DP_MASK = 0x00000002 
XRFDC_DBG_RST_FAB_MASK = 0x00000004 
XRFDC_DBG_RST_DIG_MASK = 0x00000008 
XRFDC_DBG_RST_DRP_CAL_MASK = 0x00000010 
XRFDC_DBG_RST_LM_MASK = 0x00000020 
XRFDC_ADC_FAB_RATE_WR_MASK = 0x0000000F 
XRFDC_DAC_FAB_RATE_WR_MASK = 0x0000001F 
XRFDC_ADC_FAB_RATE_RD_MASK = 0x00000F00 
XRFDC_DAC_FAB_RATE_RD_MASK = 0x00001F00 
XRFDC_FAB_RATE_RD_SHIFT = 8 
XRFDC_FAB_RD_PTR_OFFST_MASK = 0x0000003F 
XRFDC_FAB_ISR_USRDAT_OVR_MASK = 0x00000001 
XRFDC_FAB_ISR_USRDAT_UND_MASK = 0x00000002 
XRFDC_FAB_ISR_USRDAT_MASK = 0x00000003 
XRFDC_FAB_ISR_MARGIND_OVR_MASK = 0x00000004 
XRFDC_FAB_ISR_MARGIND_UND_MASK = 0x00000008 
XRFDC_FAB_IMR_USRDAT_OVR_MASK = 0x00000001 
XRFDC_FAB_IMR_USRDAT_UND_MASK = 0x00000002 
XRFDC_FAB_IMR_USRDAT_MASK = 0x00000003 
XRFDC_FAB_IMR_MARGIND_OVR_MASK = 0x00000004 
XRFDC_FAB_IMR_MARGIND_UND_MASK = 0x00000008 
XRFDC_UPDT_EVNT_MASK = 0x0000000F 
XRFDC_UPDT_EVNT_SLICE_MASK = 0x00000001 
XRFDC_UPDT_EVNT_NCO_MASK = 0x00000002 
XRFDC_UPDT_EVNT_QMC_MASK = 0x00000004 
XRFDC_ADC_UPDT_CRSE_DLY_MASK = 0x00000008 
XRFDC_DAC_UPDT_CRSE_DLY_MASK = 0x00000020 
XRFDC_FIFO_LTNCY_PRD_MASK = 0x00000007 
XRFDC_FIFO_LTNCY_RESTRT_MASK = 0x00000008 
XRFDC_FIFO_LTNCY_DIS_MASK = 0x000000010 
XRFDC_DEC_ISR_SUBADC_MASK = 0x000000FF 
XRFDC_DEC_ISR_SUBADC0_UND_MASK = 0x00000001 
XRFDC_DEC_ISR_SUBADC0_OVR_MASK = 0x00000002 
XRFDC_DEC_ISR_SUBADC1_UND_MASK = 0x00000004 
XRFDC_DEC_ISR_SUBADC1_OVR_MASK = 0x00000008 
XRFDC_DEC_ISR_SUBADC2_UND_MASK = 0x00000010 
XRFDC_DEC_ISR_SUBADC2_OVR_MASK = 0x00000020 
XRFDC_DEC_ISR_SUBADC3_UND_MASK = 0x00000040 
XRFDC_DEC_ISR_SUBADC3_OVR_MASK = 0x00000080 
XRFDC_DEC_IMR_SUBADC0_UND_MASK = 0x00000001 
XRFDC_DEC_IMR_SUBADC0_OVR_MASK = 0x00000002 
XRFDC_DEC_IMR_SUBADC1_UND_MASK = 0x00000004 
XRFDC_DEC_IMR_SUBADC1_OVR_MASK = 0x00000008 
XRFDC_DEC_IMR_SUBADC2_UND_MASK = 0x00000010 
XRFDC_DEC_IMR_SUBADC2_OVR_MASK = 0x00000020 
XRFDC_DEC_IMR_SUBADC3_UND_MASK = 0x00000040 
XRFDC_DEC_IMR_SUBADC3_OVR_MASK = 0x00000080 
XRFDC_DEC_IMR_MASK = 0x000000FF
XRFDC_DATAPATH_MODE_MASK = 0x00000003 
XRFDC_DATAPATH_IMR_MASK = 0x00000004 
XRFDC_DATAPATH_LATENCY_MASK = 0x00000008 
XRFDC_DATAPATH_IMR_SHIFT = 2 
XRFDC_ADC_DAT_PATH_ISR_MASK = 0x000000FF 
XRFDC_DAC_DAT_PATH_ISR_MASK = 0x0000FFFF 
XRFDC_DAT_ISR_DECI_IPATH_MASK = 0x00000007 
XRFDC_DAT_ISR_INTR_QPATH_MASK = 0x00000038 
XRFDC_DAT_ISR_QMC_GAIN_MASK = 0x00000040 
XRFDC_DAT_ISR_QMC_OFFST_MASK = 0x00000080 
XRFDC_DAC_DAT_ISR_INVSINC_MASK = 0x00000100 
XRFDC_DAT_IMR_DECI_IPATH_MASK = 0x00000007 
XRFDC_DAT_IMR_INTR_QPATH_MASK = 0x00000038 
XRFDC_DAT_IMR_QMC_GAIN_MASK = 0x00000040 
XRFDC_DAT_IMR_QMC_OFFST_MASK = 0x00000080 
XRFDC_DAC_DAT_IMR_INV_SINC_MASK = 0x00000100 
XRFDC_DAC_DAT_IMR_MXR_HLF_I_MASK = 0x00000200 
XRFDC_DAC_DAT_IMR_MXR_HLF_Q_MASK = 0x00000400 
XRFDC_DAC_DAT_IMR_DP_SCALE_MASK = 0x00000800 
XRFDC_DAC_DAT_IMR_INTR_IPATH3_MASK = 0x00001000 
XRFDC_DAC_DAT_IMR_INTR_QPATH3_MASK = 0x00002000 
XRFDC_DAC_DAT_IMR_IMR_OV_MASK = 0x00004000
XRFDC_DAC_DAT_IMR_INV_SINC_EVEN_NYQ_MASK = 0x00008000
XRFDC_ADC_DAT_IMR_MASK = 0x000000FF
XRFDC_DAC_DAT_IMR_MASK = 0x0000FFFF
XRFDC_FIFO_USRD_OF_MASK = 0x00000001 
XRFDC_FIFO_USRD_UF_MASK = 0x00000002 
XRFDC_FIFO_MRGN_OF_MASK = 0x00000004 
XRFDC_FIFO_MRGN_UF_MASK = 0x00000008 
XRFDC_FIFO_ACTL_OF_MASK = 0x00000010 
XRFDC_FIFO_ACTL_UF_MASK = 0x00000020 
XRFDC_DAC_FIFO_IMR_SUPP_MASK = 0x00000030 
XRFDC_DAC_FIFO_IMR_MASK = 0x0000003F 
XRFDC_DEC_CFG_MASK = 0x00000003 
XRFDC_DEC_CFG_CHA_MASK = 0x00000000 
XRFDC_DEC_CFG_CHB_MASK = 0x00000001 
XRFDC_DEC_CFG_IQ_MASK = 0x00000002 
XRFDC_DEC_CFG_4GSPS_MASK = 0x00000003 
XRFDC_DEC_MOD_MASK = 0x00000007 
XRFDC_DEC_MOD_MASK_EXT = 0x0000003F 
XRFDC_MIX_CFG0_MASK = 0x00000FFF 
XRFDC_MIX_I_DAT_WRD0_MASK = 0x00000007 
XRFDC_MIX_I_DAT_WRD1_MASK = 0x00000038 
XRFDC_MIX_I_DAT_WRD2_MASK = 0x000001C0 
XRFDC_MIX_I_DAT_WRD3_MASK = 0x00000E00 
XRFDC_MIX_CFG1_MASK = 0x00000FFF 
XRFDC_MIX_Q_DAT_WRD0_MASK = 0x00000007 
XRFDC_MIX_Q_DAT_WRD1_MASK = 0x00000038 
XRFDC_MIX_Q_DAT_WRD2_MASK = 0x000001C0 
XRFDC_MIX_Q_DAT_WRD3_MASK = 0x00000E00 
XRFDC_EN_I_IQ_MASK = 0x00000003 
XRFDC_EN_Q_IQ_MASK = 0x0000000C 
XRFDC_FINE_MIX_SCALE_MASK = 0x00000010 
XRFDC_SEL_I_IQ_MASK = 0x00000F00 
XRFDC_SEL_Q_IQ_MASK = 0x0000F000 
XRFDC_I_IQ_COS_MINSIN = 0x00000C00 
XRFDC_Q_IQ_SIN_COS = 0x00001000 
XRFDC_MIXER_MODE_C2C_MASK = 0x0000000F 
XRFDC_MIXER_MODE_R2C_MASK = 0x00000005 
XRFDC_MIXER_MODE_C2R_MASK = 0x00000003 
XRFDC_MIXER_MODE_OFF_MASK = 0x00000000 
XRFDC_NCO_UPDT_MODE_MASK = 0x00000007 
XRFDC_NCO_UPDT_MODE_GRP = 0x00000000 
XRFDC_NCO_UPDT_MODE_SLICE = 0x00000001 
XRFDC_NCO_UPDT_MODE_TILE = 0x00000002 
XRFDC_NCO_UPDT_MODE_SYSREF = 0x00000003 
XRFDC_NCO_UPDT_MODE_MARKER = 0x00000004 
XRFDC_NCO_UPDT_MODE_FABRIC = 0x00000005 
XRFDC_NCO_UPDT_DLY_MASK = 0x00001FF8 
XRFDC_NCO_UPDT_RST_DLY_MASK = 0x0000D000 
XRFDC_NCO_PHASE_RST_MASK = 0x00000001 
XRFDC_DAC_INTERP_DATA_MASK = 0x00000001 
XRFDC_NCO_FQWD_UPP_MASK = 0x0000FFFF 
XRFDC_NCO_FQWD_UPP_SHIFT = 32 
XRFDC_NCO_FQWD_MID_MASK = 0x0000FFFF 
XRFDC_NCO_FQWD_MID_SHIFT = 16 
XRFDC_NCO_FQWD_LOW_MASK = 0x0000FFFF 
XRFDC_NCO_FQWD_MASK = 0x0000FFFFFFFFFFFF 
XRFDC_NCO_PHASE_UPP_MASK = 0x00000003 
XRFDC_NCO_PHASE_UPP_SHIFT = 16 
XRFDC_NCO_PHASE_LOW_MASK = 0x0000FFFF
XRFDC_NCO_PHASE_MASK = 0x0003FFFF 
XRFDC_NCO_PHASE_MOD_MASK = 0x00000003 
XRFDC_NCO_PHASE_MOD_4PHASE = 0x00000003 
XRFDC_NCO_PHASE_MOD_EVEN = 0x00000001 
XRFDC_NCO_PHASE_MODE_ODD = 0x00000002 
XRFDC_QMC_UPDT_MODE_MASK = 0x00000007 
XRFDC_QMC_UPDT_MODE_GRP = 0x00000000 
XRFDC_QMC_UPDT_MODE_SLICE = 0x00000001 
XRFDC_QMC_UPDT_MODE_TILE = 0x00000002 
XRFDC_QMC_UPDT_MODE_SYSREF = 0x00000003 
XRFDC_QMC_UPDT_MODE_MARKER = 0x00000004 
XRFDC_QMC_UPDT_MODE_FABRIC = 0x00000005 
XRFDC_QMC_UPDT_DLY_MASK = 0x00001FF8 
XRFDC_QMC_CFG_EN_GAIN_MASK = 0x00000001 
XRFDC_QMC_CFG_EN_PHASE_MASK = 0x00000002 
XRFDC_QMC_CFG_PHASE_SHIFT = 1 
XRFDC_QMC_OFFST_CRCTN_MASK = 0x00000FFF 
XRFDC_QMC_OFFST_CRCTN_SIGN_MASK = 0x00000800 
XRFDC_QMC_GAIN_CRCTN_MASK = 0x00003FFF 
XRFDC_QMC_PHASE_CRCTN_MASK = 0x00000FFF 
XRFDC_QMC_PHASE_CRCTN_SIGN_MASK = 0x00000800 

# https://github.com/Xilinx/embeddedsw/blob/xilinx_v2023.2/XilinxProcessorIPLib/drivers/rfdc/src/xrfdc_hw.h#L999-L1529
XRFDC_CRSEDLY_UPDT_MODE_MASK = 0x00000007
XRFDC_CRSEDLY_UPDT_MODE_GRP = 0x00000000 
XRFDC_CRSEDLY_UPDT_MODE_SLICE = 0x00000001 
XRFDC_CRSEDLY_UPDT_MODE_TILE = 0x00000002 
XRFDC_CRSEDLY_UPDT_MODE_SYSREF = 0x00000003 
XRFDC_CRSEDLY_UPDT_MODE_MARKER = 0x00000004 
XRFDC_CRSEDLY_UPDT_MODE_FABRIC = 0x00000005 
XRFDC_CRSEDLY_UPDT_DLY_MASK = 0x00001FF8 
XRFDC_CRSE_DLY_CFG_MASK = 0x00000007 
XRFDC_CRSE_DLY_CFG_MASK_EXT = 0x0000003F 
XRFDC_DAT_SCALE_CFG_MASK = 0x00000001 
XRFDC_DAT_SCALE_CFG_MASK = 0x00000001 
XRFDC_SWITCH_MTRX_MASK = 0x0000003F 
XRFDC_SEL_CB_TO_MIX1_MASK = 0x00000003 
XRFDC_SEL_CB_TO_MIX0_MASK = 0x0000000C 
XRFDC_SEL_CB_TO_QMC_MASK = 0x00000010 
XRFDC_SEL_CB_TO_DECI_MASK = 0x00000020 
XRFDC_SEL_CB_TO_MIX0_SHIFT = 2
XRFDC_TRSHD0_EN_MOD_MASK = 0x00000003 
XRFDC_TRSHD0_CLR_MOD_MASK = 0x00000004 
XRFDC_TRSHD0_STIKY_CLR_MASK = 0x00000008 
XRFDC_TRSHD0_AVG_UPP_MASK = 0x0000FFFF 
XRFDC_TRSHD0_AVG_UPP_SHIFT = 16 
XRFDC_TRSHD0_AVG_LOW_MASK = 0x0000FFFF 
XRFDC_TRSHD0_UNDER_MASK = 0x00003FFF 
XRFDC_TRSHD0_OVER_MASK = 0x00003FFF
XRFDC_TRSHD1_EN_MOD_MASK = 0x00000003 
XRFDC_TRSHD1_CLR_MOD_MASK = 0x00000004 
XRFDC_TRSHD1_STIKY_CLR_MASK = 0x00000008 
XRFDC_TRSHD1_AVG_UPP_MASK = 0x0000FFFF 
XRFDC_TRSHD1_AVG_UPP_SHIFT = 16 
XRFDC_TRSHD1_AVG_LOW_MASK = 0x0000FFFF 
XRFDC_TRSHD1_UNDER_MASK = 0x00003FFF 
XRFDC_TRSHD1_OVER_MASK = 0x00003FFF 
XRFDC_TDD_CTRL_MASK = 0x0000001F 
XRFDC_TDD_CTRL_MODE01_MASK = 0x00000003 
XRFDC_TDD_CTRL_MODE0_MASK = 0x00000001 
XRFDC_TDD_CTRL_MODE1_MASK = 0x00000002
XRFDC_TDD_CTRL_OBS_EN_MASK = 0x00000008 
XRFDC_TDD_CTRL_RTP_MASK = 0x00000004 
XRFDC_TDD_CTRL_RTP_OBS_MASK = 0x00000010 
XRFDC_TDD_CTRL_MODE1_SHIFT = 1 
XRFDC_TDD_CTRL_OBS_EN_SHIFT = 3 
XRFDC_TDD_CTRL_RTP_SHIFT = 2 
XRFDC_TDD_CTRL_RTP_OBS_SHIFT = 4 
XRFDC_FEND_DAT_CTRL_MASK = 0x000000FF 
XRFDC_TI_DCB_CTRL0_MASK = 0x0000FFFF 
XRFDC_TI_DCB_MODE_MASK = 0x00007800 
XRFDC_TI_DCB_CTRL1_MASK = 0x00001FFF 
XRFDC_TI_DCB_CTRL2_MASK = 0x00001FFF 
XRFDC_TI_TISK_EN_MASK = 0x00000001 
XRFDC_TI_TISK_MODE_MASK = 0x00000002
XRFDC_TI_TISK_ZONE_MASK = 0x00000004 
XRFDC_TI_TISK_CHOP_EN_MASK = 0x00000008 
XRFDC_TI_TISK_MU_CM_MASK = 0x000000F0 
XRFDC_TI_TISK_MU_DF_MASK = 0x00000F00 
XRFDC_TI_TISK_DBG_CTRL_MASK = 0x0000F000 
XRFDC_TI_TISK_DBG_UPDT_RT_MASK = 0x00001000 
XRFDC_TI_TISK_DITH_DLY_MASK = 0x0000E000 
XRFDC_TISK_ZONE_SHIFT = 2 
XRFDC_MC_CFG0_MIX_MODE_MASK = 0x00000002 
XRFDC_MC_CFG0_MIX_MODE_SHIFT = 1
XRFDC_TISK_EN_MASK = 0x00000001 
XRFDC_TISK_MODE_MASK = 0x00000002 
XRFDC_TISK_ZONE_MASK = 0x00000004 
XRFDC_TISK_CHOP_EN_MASK = 0x00000008 
XRFDC_TISK_MU_CM_MASK = 0x000000F0 
XRFDC_TISK_MU_DF_MASK = 0x00000F00 
XRFDC_TISK_DBG_CTRL_MASK = 0x0000F000 
XRFDC_TISK_DBG_UPDT_RT_MASK = 0x00001000 
XRFDC_TISK_DITH_DLY_MASK = 0x0000E000 
XRFDC_TISK_DZ_MIN_VAL_MASK = 0x000000FF 
XRFDC_TISK_DZ_MAX_VAL_MASK = 0x0000FF00 
XRFDC_TISK_MU0_MASK = 0x0000000F 
XRFDC_TISK_BYPASS0_MASK = 0x00000080 
XRFDC_TISK_MU1_MASK = 0x00000F00 
XRFDC_TISK_BYPASS1_MASK = 0x00008000 
XRFDC_TISK_SETTLE_MASK = 0x000000FF 
XRFDC_TISK_CAL_PRI_MASK = 0x00000001 
XRFDC_TISK_DITH_INV_MASK = 0x00000FF0 
XRFDC_TISK_DAC0_CODE_MASK = 0x000000FF 
XRFDC_TISK_DAC0_OVRID_EN_MASK = 0x00008000 
XRFDC_TISK_DAC1_CODE_MASK = 0x000000FF 
XRFDC_TISK_DAC1_OVRID_EN_MASK = 0x00008000 
XRFDC_TISK_DAC2_CODE_MASK = 0x000000FF 
XRFDC_TISK_DAC2_OVRID_EN_MASK = 0x00008000 
XRFDC_TISK_DAC3_CODE_MASK = 0x000000FF 
XRFDC_TISK_DAC3_OVRID_EN_MASK = 0x00008000 
XRFDC_TISK_DACP0_CODE_MASK = 0x000000FF 
XRFDC_TISK_DACP0_OVRID_EN_MASK = 0x00008000 
XRFDC_TISK_DACP1_CODE_MASK = 0x000000FF 
XRFDC_TISK_DACP1_OVRID_EN_MASK = 0x00008000 
XRFDC_TISK_DACP2_CODE_MASK = 0x000000FF 
XRFDC_TISK_DACP2_OVRID_EN_MASK = 0x00008000 
XRFDC_TISK_DACP3_CODE_MASK = 0x000000FF 
XRFDC_TISK_DACP3_OVRID_EN_MASK = 0x00008000 
XRFDC_SUBDRP_ADC0_ADDR_MASK = 0x000000FF 
XRFDC_SUBDRP_ADC0_DAT_MASK = 0x0000FFFF 
XRFDC_SUBDRP_ADC1_ADDR_MASK = 0x000000FF 
XRFDC_SUBDRP_ADC1_DAT_MASK = 0x0000FFFF 
XRFDC_SUBDRP_ADC2_ADDR_MASK = 0x000000FF 
XRFDC_SUBDRP_ADC2_DAT_MASK = 0x0000FFFF 
XRFDC_SUBDRP_ADC3_ADDR_MASK = 0x000000FF 
XRFDC_SUBDRP_ADC3_DAT_MASK = 0x0000FFFF 

# https://github.com/Xilinx/embeddedsw/blob/xilinx_v2023.2/XilinxProcessorIPLib/drivers/rfdc/src/xrfdc_hw.h#L1531-L2054
XRFDC_RX_MC_PWRDWN_MASK = 0x0000FFFF
XRFDC_RX_MC_CFG0_MASK = 0x0000FFFF
XRFDC_RX_MC_CFG0_CM_MASK = 0x00000040
XRFDC_RX_MC_CFG0_IM3_DITH_MASK = 0x00000020
XRFDC_RX_MC_CFG0_IM3_DITH_SHIFT = 5
XRFDC_RX_MC_CFG1_MASK = 0x0000FFFF
XRFDC_RX_MC_CFG2_MASK = 0x0000FFFF 
XRFDC_RX_PR_MC_CFG0_MASK = 0x0000FFFF 
XRFDC_RX_PR_MC_CFG0_PSNK_MASK = 0x00002000 
XRFDC_RX_PR_MC_CFG0_IDIV_MASK = 0x00000010
XRFDC_RX_PR_MC_CFG1_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS0_BG_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS0_FG_MASK = 0x0000FFFF
XRFDC_TI_DCB_STS1_BG_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS1_FG_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS2_BG_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS2_FG_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS3_BG_MASK = 0x0000FFFF
XRFDC_TI_DCB_STS3_FG_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS4_MSB_MASK = 0x0000FFFF
XRFDC_TI_DCB_STS4_LSB_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS5_MSB_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS5_LSB_MASK = 0x0000FFFF
XRFDC_TI_DCB_STS6_MSB_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS6_LSB_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS7_MSB_MASK = 0x0000FFFF 
XRFDC_TI_DCB_STS7_LSB_MASK = 0x0000FFFF
XRFDC_REFCLK_DIV_MASK = 0x1F
XRFDC_REFCLK_DIV_1_MASK = 0x10
XRFDC_REFCLK_DIV_2_MASK = 0x0 
XRFDC_REFCLK_DIV_3_MASK = 0x1 
XRFDC_REFCLK_DIV_4_MASK = 0x2 
XRFDC_FIFO_LTNCY_RES_MASK = 0x00000FFF 
XRFDC_FIFO_LTNCY_KEY_MASK = 0x00004000 
XRFDC_FIFO_LTNCY_DONE_MASK = 0x00008000
XRFDC_DEC_CTRL_MODE_MASK = 0x00000007
XRFDC_HSCOM_PWR_STATE_MASK = 0x0000FFFF
XRFDC_INTERP_MODE_MASK = 0x00000077 
XRFDC_INTERP_MODE_I_MASK = 0x00000007 
XRFDC_INTERP_MODE_Q_SHIFT = 4 
XRFDC_INTERP_MODE_MASK_EXT = 0x00003F3F 
XRFDC_INTERP_MODE_I_MASK_EXT = 0x0000003F 
XRFDC_INTERP_MODE_Q_SHIFT_EXT = 8 
XRFDC_DAC_TILES_ENABLED_SHIFT = 4 
XRFDC_DIGITAL_PATH_ENABLED_SHIFT = 16
XRFDC_TILE_RESET_MASK = 0x00000001
XRFDC_PWR_UP_STAT_MASK = 0x00000004 
XRFDC_PWR_UP_STAT_SHIFT = 2 
XRFDC_PLL_LOCKED_MASK = 0x00000008 
XRFDC_PLL_LOCKED_SHIFT = 3 
XRFDC_PWR_STATE_MASK = 0x0000FFFF
XRFDC_RSR_START_SHIFT = 8
XRFDC_CLOCK_DETECT_MASK = 0x0000FFFF
XRFDC_CLOCK_DETECT_SRC_MASK = 0x00005555
XRFDC_CLOCK_DETECT_DST_SHIFT = 1
XRFDC_EN_INTR_DAC_TILE0_MASK = 0x00000001
XRFDC_EN_INTR_DAC_TILE1_MASK = 0x00000002
XRFDC_EN_INTR_DAC_TILE2_MASK = 0x00000004
XRFDC_EN_INTR_DAC_TILE3_MASK = 0x00000008
XRFDC_EN_INTR_ADC_TILE0_MASK = 0x00000010
XRFDC_EN_INTR_ADC_TILE1_MASK = 0x00000020
XRFDC_EN_INTR_ADC_TILE2_MASK = 0x00000040
XRFDC_EN_INTR_ADC_TILE3_MASK = 0x00000080
XRFDC_EN_INTR_SLICE_MASK = 0x0000000F
XRFDC_EN_INTR_SLICE0_MASK = 0x00000001 
XRFDC_EN_INTR_SLICE1_MASK = 0x00000002 
XRFDC_EN_INTR_SLICE2_MASK = 0x00000004 
XRFDC_EN_INTR_SLICE3_MASK = 0x00000008 
XRFDC_INTR_COMMON_MASK = 0x00000010 
XRFDC_INTR_OVR_RANGE_MASK = 0x00000008 
XRFDC_INTR_OVR_VOLTAGE_MASK = 0x00000004 
XRFDC_INTR_FIFO_OVR_MASK = 0x00008000 
XRFDC_INTR_DAT_OVR_MASK = 0x00004000
XRFDC_INTR_CMODE_OVR_MASK = 0x00040000
XRFDC_INTR_CMODE_UNDR_MASK = 0x00080000
XRFDC_EN_MB_MASK = 0x00000008
XRFDC_EN_MB_SHIFT = 3
XRFDC_DAC_MB_SEL_MASK = 0x0003
XRFDC_ALT_BOND_MASK = 0x0200
XRFDC_ALT_BOND_SHIFT = 9
XRFDC_ALT_BOND_CLKDP_MASK = 0x4
XRFDC_ALT_BOND_CLKDP_SHIFT = 2
XRFDC_MB_CONFIG_MASK = 0x00000007
XRFDC_EN_INVSINC_MASK = 0x00000001
XRFDC_MODE_INVSINC_MASK = 0x00000003
XRFDC_HSCOM_FIFO_START_OBS_EN_MASK = 0x00000200
XRFDC_HSCOM_FIFO_START_OBS_EN_SHIFT = 9
XRFDC_ADC_SIG_DETECT_MASK = 0xFF
XRFDC_ADC_SIG_DETECT_THRESH_MASK = 0xFFFF
XRFDC_ADC_SIG_DETECT_THRESH_CNT_MASK = 0xFFFF
XRFDC_ADC_SIG_DETECT_INTG_MASK = 0x01
XRFDC_ADC_SIG_DETECT_FLUSH_MASK = 0x02
XRFDC_ADC_SIG_DETECT_TCONST_MASK = 0x1C
XRFDC_ADC_SIG_DETECT_MODE_MASK = 0x60
XRFDC_ADC_SIG_DETECT_HYST_MASK = 0x80
XRFDC_ADC_SIG_DETECT_INTG_SHIFT = 0
XRFDC_ADC_SIG_DETECT_FLUSH_SHIFT = 1
XRFDC_ADC_SIG_DETECT_TCONST_SHIFT = 2
XRFDC_ADC_SIG_DETECT_MODE_WRITE_SHIFT = 5
XRFDC_ADC_SIG_DETECT_MODE_READ_SHIFT = 6
XRFDC_ADC_SIG_DETECT_HYST_SHIFT = 7
XRFDC_FAB_CLK_DIV_MASK = 0x0000000F
XRFDC_FAB_CLK_DIV_CAL_MASK = 0x000000F0
XRFDC_FAB_CLK_DIV_SYNC_PULSE_MASK = 0x00000400
XRFDC_MB_CFG_MASK = 0x000001FF
XRFDC_MB_EN_4X_MASK = 0x00000100
XRFDC_MTS_SRCAP_PLL_M = 0x0100
XRFDC_MTS_SRCAP_DIG_M = 0x0100
XRFDC_MTS_SRCAP_EN_TRX_M = 0x0400
XRFDC_MTS_SRCAP_INIT_M = 0x8200
XRFDC_MTS_SRCLR_T1_M = 0x2000
XRFDC_MTS_SRCLR_PLL_M = 0x0200
XRFDC_MTS_PLLEN_M = 0x0001
XRFDC_MTS_SRCOUNT_M = 0x00FF
XRFDC_MTS_DELAY_VAL_M = 0x041F
XRFDC_MTS_AMARK_CNT_M = 0x00FF
XRFDC_MTS_AMARK_LOC_M = 0x0F0000
XRFDC_MTS_AMARK_DONE_M = 0x100000

# https://github.com/Xilinx/embeddedsw/blob/xilinx_v2023.2/XilinxProcessorIPLib/drivers/rfdc/src/xrfdc_hw.h#L2056-L2134
XRFDC_PLL_DIVIDER0_MASK = 0x0CFF
XRFDC_PLL_DIVIDER0_MODE_MASK = 0x00C0
XRFDC_PLL_DIVIDER0_BYP_OPDIV_MASK = 0x0400
XRFDC_PLL_DIVIDER0_BYP_PLL_MASK = 0x0800
XRFDC_PLL_DIVIDER0_VALUE_MASK = 0x003F
XRFDC_PLL_DIVIDER0_SHIFT = 6
XRFDC_CLK_NETWORK_CTRL1_USE_PLL_MASK = 0x1
XRFDC_CLK_NETWORK_CTRL1_USE_RX_MASK = 0x2
XRFDC_CLK_NETWORK_CTRL1_REGS_MASK = 0x3
XRFDC_CLK_NETWORK_CTRL1_EN_SYNC_MASK = 0x1000
XRFDC_PLL_CRS1_VCO_SEL_MASK = 0x00008001
XRFDC_PLL_VCO_SEL_AUTO_MASK = 0x00008000
XRFDC_DIGI_ANALOG_SHIFT4 = 4
XRFDC_DIGI_ANALOG_SHIFT8 = 8
XRFDC_DIGI_ANALOG_SHIFT12 = 12
XRFDC_DAC_FIFO_DELAY_MASK = 0x000000FFF
XRFDC_ADC_FIFO_DELAY_MASK = 0x0000001C0
XRFDC_ADC_FIFO_DELAY_SHIFT = 6
XRFDC_DATA_SCALER_MASK = 0x00000001
XRFDC_CAL_DIV_BYP_MASK = 0x00000004

# https://github.com/Xilinx/embeddedsw/blob/xilinx_v2023.2/XilinxProcessorIPLib/drivers/rfdc/src/xrfdc_hw.h#L2138-L2207
XRFDC_IXR_FIFOUSRDAT_MASK = 0x0000000F
XRFDC_DAC_IXR_FIFOUSRDAT_SUPP_MASK = 0x30000000
XRFDC_DAC_IXR_FIFOUSRDAT_MASK = 0x3000000F
XRFDC_IXR_FIFOUSRDAT_OBS_MASK = 0x0000F000
XRFDC_IXR_FIFOUSRDAT_OF_MASK = 0x00000001
XRFDC_IXR_FIFOUSRDAT_UF_MASK = 0x00000002
XRFDC_IXR_FIFOMRGNIND_OF_MASK = 0x00000004
XRFDC_IXR_FIFOMRGNIND_UF_MASK = 0x00000008
XRFDC_DAC_IXR_FIFOACTIND_OF_MASK = 0x20000000
XRFDC_DAC_IXR_FIFOACTIND_UF_MASK = 0x10000000
XRFDC_ADC_IXR_DATAPATH_MASK = 0x00000FF0
XRFDC_ADC_IXR_DMON_STG_MASK = 0x000003F0
XRFDC_DAC_IXR_DATAPATH_MASK = 0x000FFFF0
XRFDC_DAC_IXR_INTP_STG_MASK = 0x000003F0
XRFDC_DAC_IXR_INTP_I_STG0_MASK = 0x00000010
XRFDC_DAC_IXR_INTP_I_STG1_MASK = 0x00000020
XRFDC_DAC_IXR_INTP_I_STG2_MASK = 0x00000040
XRFDC_DAC_IXR_INTP_Q_STG0_MASK = 0x00000080
XRFDC_DAC_IXR_INTP_Q_STG1_MASK = 0x00000100
XRFDC_DAC_IXR_INTP_Q_STG2_MASK = 0x00000200
XRFDC_ADC_IXR_DMON_I_STG0_MASK = 0x00000010
XRFDC_ADC_IXR_DMON_I_STG1_MASK = 0x00000020
XRFDC_ADC_IXR_DMON_I_STG2_MASK = 0x00000040
XRFDC_ADC_IXR_DMON_Q_STG0_MASK = 0x00000080
XRFDC_ADC_IXR_DMON_Q_STG1_MASK = 0x00000100
XRFDC_ADC_IXR_DMON_Q_STG2_MASK = 0x00000200
XRFDC_IXR_QMC_GAIN_PHASE_MASK = 0x00000400
XRFDC_IXR_QMC_OFFST_MASK = 0x00000800
XRFDC_DAC_IXR_INVSNC_OF_MASK = 0x00001000
XRFDC_DAC_IXR_MXR_HLF_I_MASK = 0x00002000
XRFDC_DAC_IXR_MXR_HLF_Q_MASK = 0x00004000
XRFDC_DAC_IXR_DP_SCALE_MASK = 0x00008000
XRFDC_DAC_IXR_INTP_I_STG3_MASK = 0x00010000
XRFDC_DAC_IXR_INTP_Q_STG3_MASK = 0x00020000
XRFDC_DAC_IXR_IMR_OV_MASK = 0x00040000
XRFDC_DAC_IXR_INV_SINC_EVEN_NYQ_MASK = 0x00080000
XRFDC_SUBADC_IXR_DCDR_MASK = 0x00FF0000
XRFDC_SUBADC0_IXR_DCDR_OF_MASK = 0x00010000
XRFDC_SUBADC0_IXR_DCDR_UF_MASK = 0x00020000
XRFDC_SUBADC1_IXR_DCDR_OF_MASK = 0x00040000
XRFDC_SUBADC1_IXR_DCDR_UF_MASK = 0x00080000
XRFDC_SUBADC2_IXR_DCDR_OF_MASK = 0x00100000
XRFDC_SUBADC2_IXR_DCDR_UF_MASK = 0x00200000
XRFDC_SUBADC3_IXR_DCDR_OF_MASK = 0x00400000
XRFDC_SUBADC3_IXR_DCDR_UF_MASK = 0x00800000
XRFDC_ADC_OVR_VOLTAGE_MASK = 0x04000000
XRFDC_COMMON_MASK = 0x01000000
XRFDC_ADC_OVR_RANGE_MASK = 0x08000000
XRFDC_ADC_CMODE_OVR_MASK = 0x10000000
XRFDC_ADC_CMODE_UNDR_MASK = 0x20000000
XRFDC_ADC_DAT_OVR_MASK = 0x40000000
XRFDC_DAT_OVR_MASK = 0x40000000
XRFDC_ADC_FIFO_OVR_MASK = 0x80000000
XRFDC_FIFO_OVR_MASK = 0x80000000
XRFDC_DAC_MC_CFG2_OPCSCAS_MASK = 0x0000F8F8
XRFDC_DAC_MC_CFG2_BLDGAIN_MASK = 0x0000FFC0
XRFDC_DAC_MC_CFG3_CSGAIN_MASK = 0x0000FFC0
XRFDC_DAC_MC_CFG2_OPCSCAS_20MA = 0x00004858
XRFDC_DAC_MC_CFG3_CSGAIN_20MA = 0x000087C0
XRFDC_DAC_MC_CFG2_OPCSCAS_32MA = 0x0000A0D8
XRFDC_DAC_MC_CFG3_CSGAIN_32MA = 0x0000FFC0
XRFDC_DAC_MC_CFG2_GEN1_COMP_MASK = 0x0020
XRFDC_DAC_MC_CFG3_OPT_LUT_MASK = 0x03F0
XRFDC_DAC_MC_CFG3_OPT_MASK = 0x001F
XRFDC_DAC_MC_CFG3_UPDATE_MASK = 0x0020
XRFDC_DAC_MC_CFG0_CAS_BLDR_MASK = 0xE000
XRFDC_DAC_MC_CFG2_CAS_BIAS_MASK = 0x001F
XRFDC_ADC_DSA_RTS_PIN_MASK = 0x0020
XRFDC_ADC_DSA_CODE_MASK = 0x001F
XRFDC_ADC_DSA_UPDT_MASK = 0x0001

# https://github.com/Xilinx/embeddedsw/blob/xilinx_v2023.2/XilinxProcessorIPLib/drivers/rfdc/src/L2209-L2222
XRFDC_DAC_MC_CFG2_BLDGAIN_SHIFT = 6
XRFDC_DAC_MC_CFG3_CSGAIN_SHIFT = 6
XRFDC_DAC_MC_CFG3_OPT_LUT_SHIFT = 4
XRFDC_ADC_OVR_VOL_RANGE_SHIFT = 24
XRFDC_ADC_DAT_FIFO_OVR_SHIFT = 16
XRFDC_DAT_FIFO_OVR_SHIFT = 16
XRFDC_ADC_SUBADC_DCDR_SHIFT = 16
XRFDC_IXR_FIFOUSRDAT_OBS_SHIFT = 12
XRFDC_DAC_IXR_FIFOUSRDAT_SUPP_SHIFT = 24
XRFDC_DATA_PATH_SHIFT = 4
XRFDC_ADC_CMODE_SHIFT = 10
XRFDC_COMMON_SHIFT = 20
XRFDC_DAC_MC_CFG2_GEN1_COMP_SHIFT = 5
XRFDC_ADC_DSA_RTS_PIN_SHIFT = 5

# https://github.com/Xilinx/embeddedsw/blob/xilinx_v2023.2/XilinxProcessorIPLib/drivers/rfdc/src/xrfdc_hw.h#L2224-L2231
def XRFDC_DAC_TILE_DRP_ADDR(X): 
    return  (0x6000 + (X * 0x4000))
def XRFDC_DAC_TILE_CTRL_STATS_ADDR(X): 
    return  (0x4000 + (X * 0x4000))
def XRFDC_ADC_TILE_DRP_ADDR(X): 
    return  (0x16000 + (X * 0x4000))
def XRFDC_ADC_TILE_CTRL_STATS_ADDR(X): 
    return  (0x14000 + (X * 0x4000))
XRFDC_CTRL_STATS_OFFSET = 0x0
XRFDC_HSCOM_ADDR = 0x1C00
def XRFDC_BLOCK_ADDR_OFFSET(X):
    return (X * 0x400)
XRFDC_TILE_DRP_OFFSET = 0x2000
    
# https://github.com/Xilinx/embeddedsw/blob/xilinx_v2023.2/XilinxProcessorIPLib/drivers/rfdc/src/xrfdc_hw.h#L2233-L2396
def XRFdc_ReadReg(InstancePtr, BaseAddress, RegOffset):
    return InstancePtr.RegSpace.get(index=(BaseAddress+RegOffset)//4)

def XRFdc_WriteReg(InstancePtr, BaseAddress, RegOffset, RegisterValue):
    InstancePtr.RegSpace.set(value=RegisterValue,index=(BaseAddress+RegOffset)//4)

def XRFdc_ReadReg16(InstancePtr, BaseAddress, RegOffset):
    return InstancePtr.RegSpace.get(index=(BaseAddress+RegOffset)//4)&0xFFFF

def XRFdc_WriteReg16(InstancePtr, BaseAddress, RegOffset, RegisterValue):
	InstancePtr.RegSpace.set(value=RegisterValue,index=(BaseAddress+RegOffset)//4)
