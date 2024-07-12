# DE-Kaggle-Airflow-Azure

# Goal
This project is based on video tutorial by [**Darshil Parmar**](https://www.youtube.com/watch?v=q8q3OFFfY6c&list=PLBJe2dFI4sgvQTNNkI3ETYJgNPR4CBpFd&index=4).


The goal of this project is to perform Basic ETL Data Pipeline on Kaggle data using various tools and technologies, including Azure Storage, Python, Virtual Machnine, Airflow Data Pipeline Tool.


<hr/>

# What Did I Learned?
* Whole project of Tutorial was based on [AWS](https://github.com/darshilparmar/twitter-airflow-data-engineering-project/tree/main), Here, I implemented whole project on [Azure].
* Hands On Experinece with [Python], [Azure], [Azure Storage Account], [VM], [Airflow].
* End-to-End Pipeline with [Airflow].
* Challenges Overcame
  *   VM Setup & Dependencies Download Error
  *   Kaggle API directly download on local directory. I want to download directly on Azure Blob Storage. Here, I came to know about **tempfile** library which downloads on temperory location and then can upload.
  *   During Installing Airflow in Ubuntu VM, Airflow shows some error so need to create virtual-environment(venv) and then install in that venv.

<hr/>

## Tools Used
[<img align="left" alt="Python" width="33px" src="https://i.imgur.com/gixjL0a.png" />][Python]
[<img align="left" alt="Jupyter" width="75px" src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Kaggle_logo.png" />][Kaggle]
[<img align="left" alt="vscode" width="33px" src="https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/visual-studio-code-icon.png" />][VSCode]
<br/>
<br/>
[<img align="left" alt="a" width="55px" src="https://www.business-central-app.it/wp-content/uploads/2021/12/logo-azure.png"/>][Azure]
[<img align="left" alt="VM" width="33px" src="https://static-00.iconduck.com/assets.00/azure-vms-color-icon-2048x1891-chkcdc9i.png"/>][VM]
[<img align="left" alt="Azure Storage Account" width="33px" src="https://i0.wp.com/mattruma.com/wp-content/uploads/2020/02/Icon-storage-86-Storage-Accounts-1.png?fit=400%2C400&ssl=1"/>][Azure Storage Account]
<br/>
<br/>
[<img align="left" alt="Azure Storage Account" width="125px" src="https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png"/>][Airflow]
<br/>
<br/>
<hr/>


## Data Architecture
![Architecture](https://github.com/manthan-ladva/DE-Kaggle-Airflow-Azure/blob/main/diagrams/kaggle_airflow.png)


[Python]:https://www.python.org/
[PowerBI]:https://powerbi.microsoft.com/en-us/
[R]:https://www.r-project.org/
[VSCode]:https://code.visualstudio.com/
[Jupyter]:https://jupyter.org/
[Mage-AI]:https://www.mage.ai/
[Azure Storage Account]:https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction/
[VM]:https://azure.microsoft.com/en-in/products/virtual-machines/
[Azure SQL]:https://azure.microsoft.com/en-in/products/azure-sql/database/
[Azure]:https://portal.azure.com/
[Kaggle]:https://www.kaggle.com/
[Airflow]:https://airflow.apache.org/
