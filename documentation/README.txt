-------------------
GENERAL INFORMATION
-------------------


1. Title of Dataset: A Materials Dataset for Elastomeric Foam Impact Mitigating Materials


2. File formats: .txt, .xls(x), .tri, .tprc, .py, .m, .csv, .mat, .tif, .pdf, .vtk, .stl, .zip


3. Author Information


  Principal Investigator Contact Information
        Name: Aaron Forster
           Institution: National Institute of Standards and Technology
           Address: 100 Bureau Drive, Stop 8102, Gaithersburg, MD 20899 
           Email: aaron.forster@nist.gov


  Co-investigator Contact Information
        Name: Alexander Landauer
           Institution: National Institute of Standards and Technology
           Address: 100 Bureau Drive, Stop 8102, Gaithersburg, MD 20899 
           Email: alexander.landauer@nist.gov


  Alternate Contact Information
           Name: Alexander Landauer
           Email: alexander_landauer@alumni.brown.edu


4. Dates of data collection: Nov. 2020 to Feb. 2022


5. Location of data collection: 
      National Institute of Standards and Technology
      Materials Measurement Science Division, Material Measurement Laboratory
      100 Bureau Drive, Bldgs. 220 and 202, Gaithersburg, MD 20899
           
      and
  
      National Institute of Standards and Technology
      Applied Chemicals and Materials Division, Material Measurement Laboratory
      325 Broadway, , Boulder CO 80305


6. Information about any NON-NIST funding sources that supported the collection of the data: 
      VN600 dataset was collected in part while A.L., O.K., and N.M. were NRC-funded post-docs


--------------------------
SHARING/ACCESS INFORMATION
-------------------------- 


7.	This dataset is provided according NIST statements for Copyright, Fair Use, and Licensing found at: 
              https://www.nist.gov/director/copyright-fair-use-and-licensing-statements-srd-data-and-software 
        and in the license.txt file.


8. Links to publications that cite or use the data:
        N/A (to be added)


9. Links to other publicly accessible locations of the data:
       https://doi.org/10.18434/mds2-2606 OR https://datapub.nist.gov/od/id/mds2-2606
Add MDF link here


10. Recommended citation for the data:
       Landauer AK, Kafka OL, Moser NH, Forster AM, (2022), "A Materials Database for Elastomeric 
       Foam Impact Mitigating Materials". National Institute of Standards and Technology, https://doi.org/10.18434/mds2-2606

       and/or

       Landauer AK, Kafka OL, Moser NH, Foster I, Blaiszik B, Forster AM. "A Materials Data 
       Framework and Dataset for Elastomeric Foam Impact Mitigating Materials". (In prep) 




---------------------
DATA & FILE OVERVIEW
---------------------

11. File structure: data are stored in directories for each experiment type, and subdirectories for each 
    material. Each directory has a text file describing naming conventions, data types and other notes.

   A. Filename: DMA_data       
      Short description: data folder for dynamic mechanical analysis raw data, results, uncertainty 
	                     statements, and analysis tools
        
   B. Filename: intermediate_rate_data
      Short description: data folder for intermediate rate (servo-hydraulic UTS based) raw data including 
                         digital image correlation (DIC) images, results, uncertainty statements, and analysis tools
        
   C. Filename: quasistatic_rate_data
      Short description: data folder for quasistatic rate (electro-mechanical UTS based) raw data including 
                         digital image correlation (DIC), results, uncertainty statements, and analysis tools

   D. Filename: microCT_data
      Short description: data folder for micro-computed tomography data including raw projection images, volume 
                         images, binarized images, uncertainty statements, other results, and analysis tools


12. Additional related data collected that was not included in the current data package:
      Certain method development and validation data are not included in the final data package included here. 
      
      DMA data does not include, for example, method design and validation experiments such as relaxation time and 
      amplitude sweep experiments. Post-hoc analyses for shift factors are not included, although analysis tools are.

      UTS data does not include, for example, baseline isotropy, repeatability, size dependence, or out-of-plane 
      motion material validations, or uncertainty quantification, speckle pattern optimization, trigger timing, and 
      lubrication testing set-up experiments. Post-hoc analyses to select DIC parameters are not included,
      although analysis tools are.

      MicroCT data does not include, for example, thermal equilibration and beam setting selection experiments or 
      post-hoc settings analyses for filter parameters and binarization. As with other data type, the analysis tools 
      to perform filter selection and binarization are included.

      The above data is available upon reasonable request.

13. Dataset versions (major.minor.edit):
     v1.0.0 - Initial release
	


--------------------------
METHODOLOGICAL INFORMATION
--------------------------


14. Description of methods used for collection/generation of data: 
    See: Landauer AK, Kafka OL, Moser NH, Forster AM. "A Materials Data Framework and Dataset for Elastomeric 
         Foam Impact Mitigating Materials". (In prep) 

15. Methods for processing the data:
   MicroCT: Maire E, Withers PJ. "Quantitative X-ray tomography". International Mat. Rev. 59, 1–43 (2014).

   DIC: qDIC code: https://github.com/FranckLab/qDIC 
        Landauer AK, Patel M, Henann DL. et al. "A q-Factor-Based Digital Image Correlation Algorithm (qDIC) 
        for Resolving Finite Deformations with Degenerate Speckle Patterns". Exp. Mech. (2018). 
        https://doi.org/10.1007/s11340-018-0377-4)
    
   TTS: Williams ML, Landel RF, Ferry JD. "The Temperature Dependence of Relaxation Mechanisms in Amorphous 
        Polymers and Other Glass-forming Liquids". J. Am. Chem. Soc. 77, 3701–3707 (1955).

16. Specific instruments and software information:
      MicroCT: Zeiss Versa 500 with "Scout-and-Scan Reconstructor" v. 14 and Deben CT500 in situ load frame
      Quasistatic UTS: Instron 5582 with MTS ReNew upgrade package (Instron static +/-10 kN load cell) and 
                       MTS TestSuite TW Elite v. 4.1.6.819
                       FLIR Blackfly S (8.9 megapixel, grayscale 8 bit CMOS) with SpinView and TitanTL 0.377X 22.5 mm lens
      Intermediate UTS: MTS Landmark 370.10 (+/- 20 kN force transducer) with MTS TestSuite Multipurpose v. 4.1.5.736
                        Elite FlexTest
                        Photron SA5 (1 megapixel, grayscale 8 bit) with PFV v3 and Sigma DG Macro HSM 105 mm lens
      DMA: TA Instruments RSA G2 with Trios version 5.1.1

17. Standards and calibration information, if appropriate:
      Instruments were calibrated according to respective schedules and manufacturer specifications.

18. Environmental/experimental conditions:
      MicroCT were at ambient conditions in the x-ray hutch (ca. 28 degrees C). UTS experiments were conducted at room temperature. 
      For the quasistatic this was in the range [22.8, 24.3] degrees C. For the intermediate this was in the range [17.3, 24.8] degrees C.

19. People involved with sample collection, processing, analysis and/or submission:
      Alexander Landauer: Sample collection and preparation, quasi-static testing and analysis, intermediate testing 
                          and analysis, DMA testing and analysis, and dataset preparation and documentation for 
                          all experiments.
      Orion Kafka: MicroCT sample preparation, testing, analysis, and dataset preparation/documentation.
      Newell Moser: MicroCT sample preparation, testing, analysis, and dataset preparation/documentation.
      Aaron Forster: Sample collection and preparation; DMA testing, analysis, and dataset preparation/documentation.



-----------------------------------------
DATA-SPECIFIC INFORMATION
-----------------------------------------

Additional documentation and supporting uncertainty quantification for each dataset and analysis code is 
included in respective subdirectories.

-----------------------------------------
DISCLAIMER
-----------------------------------------

Certain commercial equipment, instruments, or materials are identified in this dataset in order to 
specify the experimental procedure adequately.  Such identification is not intended to imply 
recommendation or endorsement by NIST, nor is it intended to imply that the materials or equipment 
identified are necessarily the best available for the purpose.

This readme.txt file was prepared by Alexander Landauer on Feb 8, 2022.