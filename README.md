# Anti-dengue-drug-predict
This repository contains the application module of our research paper "Machine Learning Based Prediction of Biological Activity of  Dengue Virus Type 2 NS3 Protein". In order to test the application of our proposed model, you can use the ".ipynb" file.

# The prerequisites of using the app:
1. Basic knowledge of python
2. Install python in your computer or use Google Colab
3. Download the file "finalized_model_ET_150.pkl" file to your disk/drive.

# Steps of using the python notebook
1. Open the notebook in your computer or Google Colab. ( I have used Google Colab to create this notebook.)
2. Run the cells as they are.
3.  For the 3rd cell, follow the dataset preparation method as described in the notebook (also mentioned right before the corresonding cell) and replace the URL of the dataset with yours.
4. In the 5th cell, replace the URL of the DATA_PATH variable with the location where you placed the 'finalized_model_ET_150.pkl'


# The steps of dataset preparation method:

1. Prepare a dataset with the SMILES ID(s) of the small molecule(s) you want to test along with their ID or Name.
2. Convert the dataset from step 1 into SDF format
3. Utilize the PaDEL descriptor in ChemDES (http://www.scbdd.com/padel_desc/index/) to extract the 1D and 2D molecular descriptors of the small molecules(s). The server accepts SDF formatted input.
4.   Upload the dataset containing the ID/Name and the corresponding molecular descriptors (extracted in step 3) in your drive or you can upload it in this notebook directly.
5. Replace the drive link below with the URL to the location of your dataset.


# This github repository has the file "finalized_model_ET_150.pkl" uploaded to it. It must be downloaded to your disk/drive. 
1.   Download the "finalized_model_ET_150.pkl" file to your disk/drive.
2.   Replace the URL in the DATA_PATH variable with the location where you placed the 'finalized_model_ET_150.pkl'

# Test Dataset:
A test dataset is added named "Sample_Test_Dataset_FDA_approved_drugs.csv". You can use it to test our model.
