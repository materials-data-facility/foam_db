# Elastomeric Foam Impact Mitigating Materials Database

The database includes data for structure-properties relationships and mechanical modeling of elastic impact protection foams from a variety of imaging (micro-computed tomography, digital image correlation) and force-sensing instruments (dynamic mechanical analysis, universal test system) under a wide range of experimental conditions and modes. The data repository includes directories for: dynamic mechanical analysis raw data, results, and analysis tools; intermediate rate (servo-hydraulic UTS based) raw data including 2D digital image correlation (DIC) images, results, and analysis tools; quasi-static rate (electro-mechanical UTS based) raw data including 2D digital image correlation (DIC), results, and analysis tools; and, micro-computed tomography data including raw volume images, filtered images, binarized images, other results, and analysis tools. For more information see the readme and data documentation in each respective directory. A complete manuscript describing data collection, analysis, and database documentation is to be published.

[Access the Full Dataset](https://doi.org/10.18126/6h74-leb4)

## Data Structure
```
.
└── Elastomeric Foam Database/
    ├── README.txt
    ├── license.txt
    ├── foam_data_entity_relationship_diagram.pdf
    ├── DMA_data/
    │   ├── data_framework_DMA.txt
    │   ├── supporting_analyses/
    │   │   └── [analysis files]
    │   └── VN01/
    |       |── VN01_DMA_data_notes.txt
    │       |── VN01_001_D06_003_R01/
    |       |   |── VN01_001_D06_003_R01_Procedures/
    |       |   |   └── [procedure files]
    |       |   |── VN01_001_D06_003_R01_TTS/
    |       |   |   |── [VN01_001_D06_003_sweep_60C_to_n35C_full_data.xls]
    |       |   |   └── [VN01_TTS_D06_003_R01.xlsx]
    |       |   └── [raw data files] 
    |       |── VN01_001_D06_004_R01/
    |       |   |── VN01_001_D06_004_R01_Procedures/
    |       |   |   └── [procedure files]
    |       |   |── VN01_001_D06_004_R01_TTS/
    |       |   |   |── [VN01_001_D06_004_sweep_60C_to_n35C_full_data.xls]
    |       |   |   └── [VN01_TTS_D06_004_R01.xlsx]
    |       |   └── [raw data files]
    |       └── VN01_001_D06_preliminary_experiments/
    |           |── VN01_001_D06_preliminary_procedures/
    |           |   └── [procedure files]
    |           └── [raw data files]
    ├── intermediate_rate_data
    │   ├── data_framework_intermediate.txt
    │   ├── Foam_intermediate_rate_Table_of_Contents.txt
    │   ├── supporting_analyses/
    │   │   └── [analysis files]
    │   └── VN01/
    |       |── VN01_notes_intermediate.txt
    │       └── VN01_001_003_[R0p01,R0p10,R01p0,R10p0]_[00,01,02]/
    |           |── VN01_001_003_[R0p01,R0p10,R01p0,R10p0]_[00,01,02]_images/
    |           |   └── [image files]
    |           |── VN01_001_003_[R0p01,R0p10,R01p0,R10p0]_[00,01,02]_dic.mat
    |           |── VN01_001_003_[R0p01,R0p10,R01p0,R10p0]_[00,01,02]_load.csv
    |           |── VN01_001_003_[R0p01,R0p10,R01p0,R10p0]_[00,01,02]_load.xml
    |           └── VN01_001_003_[R0p01,R0p10,R01p0,R10p0]_[00,01,02]_length_scale.tif
    ├── microCT_data
    │   ├── data_framework_microCT.txt
    │   ├── Foam_microCT_Table_of_Contents.txt
    │   ├── supporting_analyses/
    │   │   └── python_imaging_library/
    |   |       |── dependencies/
    |   |       |   └── [analysis scripts]
    |   |       |── segmentation_scripts/
    |   |       |   └── [analysis scripts] 
    |   |       └── visualization_3D_script/
    |   |           └── [analysis scripts]
    │   └── VN01/
    |       |── VN01_notes_microCT.txt
    │       |── VN01_16X2_S004_BASE/
    |       |   |── VN01_16X2_S004_BASE_notes.txt
    |       |   |── VN01_16X2_S004_BASE_BIN0/
    |       |   |   └── [binarized images]
    |       |   |── VN01_16X2_S004_BASE_IMG0/
    |       |   |   └── [greyscale images]
    |       |   └── VN01_16X2_S004_BASE_RAW0/
    |       |       └── [raw projection data]
    |       |── VN01_[8X02,4X02]_S003_BASE/
    |       |   |── VN01_[8X02,4X02]_S003_BASE_notes.txt
    |       |   |── VN01_[8X02,4X02]_S003_BASE_BIN0/
    |       |   |   └── [binarized images]
    |       |   |── VN01_[8X02,4X02]_S003_BASE_IMG0/
    |       |   |   └── [greyscale images]
    |       |   └── VN01_[8X02,4X02]_S003_BASE_RAW0/
    |       |       └── [raw projection data]
    |       |── VN01_4X02_S001_COMP/
    |       |   |── VN01_4X02_S001_COMP_notes.txt
    |       |   |── VN01_4X02_S001_COMP_BIN[0-6]/
    |       |   |   └── [binarized images]
    |       |   |── VN01_4X02_S001_COMP_IMG[0-6]/
    |       |   |   └── [greyscale images]
    |       |   └── VN01_4X02_S001_COMP_RAW[0-6]/
    |       |       └── [raw projection data]
    |       └── VN01_20X2_S002_COMP/
    |           |── VN01_20X2_S002_COMP_notes.txt
    |           |── VN01_20X2_S002_COMP_BIN[0-6]/
    |           |   └── [binarized images]
    |           |── VN01_20X2_S002_COMP_IMG[0-6]/
    |           |   └── [greyscale images]
    |           └── VN01_20X2_S002_COMP_RAW[0-6]/
    |               └── [raw projection data]
    └── quasistatic_rate_data
        ├── data_framework_quasistatic.txt
        ├── foam_quasistatic_Table_of_Contents.txt
        ├── supporting_analyses/
        │   └── [analysis files]
        └── VN01/
            |── VN01_notes_quasistatic.txt
            └── VN01_001_003_QS06_[00,01,02]/
                |── VN01_001_003_QS06_[00,01,02]_images/
                |   └── [image files]
                |── VN01_001_003_QS06_[00,01,02]_dic.mat
                |── VN01_001_003_QS06_[00,01,02]_load.csv
                └── VN01_001_003_QS06_[00,01,02]_length_scale.bmp
 ```


## DATA SOURCE MODALITIES (top level folders)

### DMA_data 
data from dynamic mechanical analysis from small-amplitude oscillatory strain experiments and time-temperature superposition (TTS)

### intermediate_rate_data 
data from a series of load-frame experiments at effective strains rates from 0.001 1/s to 10.0 1/s with high-speed imaging-base digital image correlation

### microCT_data 
Micro-x-ray computed tomograph volume images (greyscale and binarized) at assorted magnifications and/or with in-situ compression

### quasistatic_rate_data
data from quasistatic (no rate-dependent effects active) load-frame experiments with high-resolution digital image correlation 

## Access Data by Composition

Currently there is one composition in this dataset VN01 foam.

DMA [VN01](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=%2Fmdf_open%2Ffoam_db_v1.1%2FDMA_data%2FVN01%2F)

Quasi-Static [VN01](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=%2Fmdf_open%2Ffoam_db_v1.1%2Fquasistatic_rate_data%2FVN01%2F)

Intermediate Rate Compression [VN01](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=%2Fmdf_open%2Ffoam_db_v1.1%2Fintermediate_rate_data%2FVN01%2F)

microCT [VN01](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=%2Fmdf_open%2Ffoam_db_v1.1%2FmicroCT_data%2FVN01%2F)

### VN01 
vinyl-nitrile close-cell foam from Dertex Corp "Impax VN600". Probably a  nitrilebutadiene/polyvinyl-chloride blend, manufacture quoted specifications are as follows:
```
        ____________________________________________________________________________
       | DESCRIPTION             TEST METHOD       VN600           UNITS            |
       |----------------------------------------------------------------------------|
       | HARDNESS (DUROMETER)    ASTM D2240          (55 - 75)     SHORE 00         |
       |                         (TEMP. 21±0.5 °C)	                            |
       | DENSITY                 ASTM D297	     (0.09 - 0.12) g/cm³            |
       | TENSILE STRENGTH        ASTM D412            13           kg/cm²           | 
       | TEAR STRENGTH           ASTM D624	      6.5          kg/cm            |
       | ELONGATION              ASTM D412            150 (min.)   % elongation     |
       | LINEAR SHRINKAGE        70 °C x 24 HR (10mm) 2.5          % shrinkage      |
       | COMPRESSION DEFLECTION  ASTM D1056           58.6 (min.)  25 % MPa         |
       |                         (TEMP. 21± 0.5°c)    8.4 (min.)   25 % PSI         |
       | RESILENCE               DIN 53512            13           % rebound        |
       |____________________________________________________________________________|

 ```

## Access Data by Experiment Type

[DMA Data](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=%2Fmdf_open%2Ffoam_db_v1.1%2FDMA_data%2F)

[Quasi-static Compression](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=%2Fmdf_open%2Ffoam_db_v1.1%2Fquasistatic_rate_data%2F)

[Intermediate Rate Compression](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=%2Fmdf_open%2Ffoam_db_v1.1%2Fintermediate_rate_data%2F)

[microCT Data](https://app.globus.org/file-manager?origin_id=82f1b5c6-6e9b-11e5-ba47-22000b92c6ec&origin_path=%2Fmdf_open%2Ffoam_db_v1.1%2FmicroCT_data%2F)


## SUPPORTING ANALYSIS METHODS (subfolders with a given test modality, see readme files):

### DMA analysis            
input datasheet (.xls). Python conversion sheet to convert input data format to TTS format. Example template for TTS (.xls)

### Intermediate rate analysis
Matlab-base digital image correlation package set up to run on servo-hydraulic data and high-speed camera data

### Micro CT analysis     
Python library to read in, process, and write out volume images from .tif stacks. This includes tools to pre-process (denoising filters, cropping, etc.) binarize and compute relative density and to write out volumes as .stl files. 

### Intermediate rate analysis
Matlab-base digital image correlation package set up to run on electromechanical data and high-resolution camera data

## Example Notebooks

### Stress Strain Curve Example
[Example Notebook](https://github.com/materials-data-facility/foam_db/blob/main/examples/stress-strain.ipynb)

<img src="https://raw.githubusercontent.com/materials-data-facility/foam_db/main/examples/imgs/stress-strain.png" width="200">

**2022-08-18** This example notebooks are under construction, check back soon

# How to Cite this Work
```
Landauer, Alexander K, Orion L Kafka, Newell H Moser, and Aaron M Forster. 
“A Materials Dataset for Elastomeric Foam Impact Mitigating Materials.” 
Materials Data Facility, 2022. https://doi.org/10.18126/6H74-LEB4.
```

# Changelog
**2022-08-04** Repository created

**2022-08-18** Added links and instructions for how to access data, more thorough description of data artifacts, NIST disclaimer.


# Project Support

Data was collected in part while A.L., O.K. and N.M. held NRC Research Associateship awards at the National Institute of Standards and Technology. 

*Data infrastructure:* This work was performed under financial assistance award 70NANB14H012 from U.S. Department of Commerce, National Institute of Standards and Technology as part of the Center for Hierarchical Material Design (CHiMaD). This work was performed under the following financial assistance award 70NANB19H005 from U.S. Department of Commerce, National Institute of Standards and Technology as part of the Center for Hierarchical Materials Design (CHiMaD). 

<img src="https://www.materialsdatafacility.org/images/MDF-logo@2x.png" height="80">




----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
## DISCLAIMER
----------------------------------------------------------------------------------------------

Certain commercial equipment, instruments, or materials are identified in this dataset in order to 
specify the experimental procedure adequately.  Such identification is not intended to imply 
recommendation or endorsement by NIST, nor is it intended to imply that the materials or equipment 
identified are necessarily the best available for the purpose.
