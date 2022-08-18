# Elastomeric Foam Impact Mitigating Materials Database

**2022-08-04** This repository is under construction, check back soon

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

## Access Data by Composition

Add instructions and links here...

## Access Data by Data Type

Add instructions and links here...


## Example Notebooks

Add instructions and links to notebooks here that show how to use the data


# How to Cite this Work
```
Landauer, Alexander K, Orion L Kafka, Newell H Moser, and Aaron M Forster. 
“A Materials Dataset for Elastomeric Foam Impact Mitigating Materials.” 
Materials Data Facility, 2022. https://doi.org/10.18126/6H74-LEB4.
```

# Project Support

Add NIST team support.


*Data infrastructure:* This work was performed under financial assistance award 70NANB14H012 from U.S. Department of Commerce, National Institute of Standards and Technology as part of the Center for Hierarchical Material Design (CHiMaD). This work was performed under the following financial assistance award 70NANB19H005 from U.S. Department of Commerce, National Institute of Standards and Technology as part of the Center for Hierarchical Materials Design (CHiMaD). 

