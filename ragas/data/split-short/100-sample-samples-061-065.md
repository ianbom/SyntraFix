# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 61

- conversation_id: 14
- user_chat_id: 800
- bot_chat_id: 801

### user_input

Bagaimana machine learning digunakan dalam software testing?

### retrieved_context

1. Some studies, e.g., [8], [10]- [12], have already analyzed the application of ML in SE in the past. Durelli et al. [8] conducts a systematic mapping study on the application of ML for software testing. The study highlights the use of ML techniques in various software testing activities such as testcase generation and oracle construction. Results of the study show that a vast majority of articles employ supervised learning, such as ANN and DT, to solve testing-related problems. Moreover, the key advantages and disadvantages of using ML for software testing are discussed. Mainly, the advantage of ML techniques is their scalability and efficient application to large-scale and complex software systems. The disadvantage, on the other hand, is the unavailability of data that fits well with the learning process. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

2. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Although there are many successful studies about the automated generation of test cases, determining whether a program has passed a given test remains largely manual. Langdon et al. [16] proposed the use of search-based learning from existing open-source test suites to automatically generate partially correct test oracles. They argued that mutation testing, n-version computing, and machine learning could be combined to allow automated output checking to catch up with progress on automated input generation.

AI software testing differs from AI-based software testing in diverse views such as test objectives, test focuses, test scope, test coverage as well as test techniques and tools. For example, AI-based testing primarily aims to increase efficiency for a test process, reduce testing costs by reduce human operations, and increase bug detection effectiveness and speed. AI testing aims to provide on-demand testing services for AI software to support software validation and quality engineering process. AI-based testing majorly focuses on test selection, automatic test execution, bug detection and prediction based large-scale testing history data and AI techniques. In addition, AI testing needs innovative continuous, timeliness, and currency testing techniques. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

4. Most of the articles we found were focusing on applying ML to various software quality assurance and analytic tasks. The applications include: fault/bug/defect prediction category, which revolves around the prediction of faults, bugs, or defects using ML techniques [34]- [39]. Test case/ data/oracle generation surrounds ML techniques that help in generating test data, test oracles, or entire test suites. Braga et al. [40] proposed an ML technique to automate the process of test oracle generation. Test case selection/ prioritization/ classification deals with the class that particularly focuses on test case prioritization or classification techniques using ML. Rosenfeld et al. [41] employed an ML technique in order to select generic test cases for android applications. The technique is aimed at reducing the manual testing efforts by classifying the activities and automatically selecting the activity-specific test cases. Vulnerability/ anomaly/malware discovery/analysis mostly concerns the security aspect of the software, e.g., Huang et al. [42] employed the term frequency-inverse document frequency (TF-IDF) technique and deep neural network to automatically classify software vulnerabilities. Software analysis, technique assessment, and software process assessment come under assessment and analysis of software. In this regard, Fu et al. [43] proposed a regression-based ML technique in order to estimate software energy consumption by analyzing software performance features. The verification and validation category specifically addresses prediction and verification of software reliability through ML, e.g., Tamura et al. [44] proposed a DL-based technique to select the most suitable software reliability model for the development project. Testing effort estimation refers to the amount of testing effort required in order to test a software system using ML techniques, e.g., Silva et al. [6] evaluated various ML tools in order to estimate the execution times for running functional test cases. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

5. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

6. In the requirements stage, writing requirements specifications is highly deemed to be a human-centric task. Prior work by Pandita et al. [50] and Jahan et al. [51] have inferred the most probable specifications and identified its unexpected behaviors from various artifacts by employing ML techniques, respectively. Ferrari et al. [52] identified ambiguous requirements among different domains using ML. In the architecture and design stage, predicting design patterns is an important reverse engineering activity to improve software integrity. However, it often suffers from false positives and negatives [53]. As the number of patterns is increasing rapidly due to their variations, the process of recognizing these patterns can be effectively learned using ML [53]. In the implementation stage, detecting code smells in a large codebase can be extremely difficult for a human as opposed to a machine, thus ML techniques can greatly reduce this effort of detecting code smells or technical debt [30], [31]. In quality assurance, there is a need to ensure that the system remains error-free or to be able to timely identify the cause of failure. ML techniques employed in literature for this purpose proved to be promising in detecting software faults [34]- [36]. Test generation is also considered to be a task that requires human intelligence. Zhang et al. [54] have employed ML to automatically generate test data in order to improve return on investment. In software maintenance, Malgonde et al. [55] have shown ML techniques perform significantly better at predicting the effort as compared to the team estimates (human-centric). (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

7. We found several studies on ML assisting the software implementation stage. Among many applications, code clone/ localization/refactoring/ labeling aims at finding code duplication, specific location of code in software, refactoring of code, or labeling of code with the help of ML, e.g., Alahmadi et al. [29] employed CNN in order to predict the code blocks in video tutorials. Code/bad smell detection focuses on applying ML in order to detect code and bad smells in software source code and design models, respectively. Code smells are indications of poor software code quality leading to the rise of technical debt. It generally includes god classes, spaghetti code, etc., whereas bad smells in design models have similar characteristics such as lazy classes and middle man. Pecorelli et al. [30] investigated data balancing techniques and addressed unbalanced dataset issues when employing ML for code smell detection. Maneerat et al. [31] proposed an approach to predict bad smells from design models such as class diagrams. Code inspection/analysis represents the class in which an ML technique is employed for the purpose of code reviews. For instance, Lal et al. [32] proposed an ML approach to automate code reviews for the pushed code. The code/program similarity category refers to the identification of specific piece(s) of code, which are similar between two or more software projects. Additionally, Kim et al. [33] proposed an ML technique in order to reduce the number of program similarity comparisons aimed at distinguishing between original and pirated/cracked software. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 6)

8. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

### response

Menurut beberapa studi, seperti yang disebutkan di [8], [10]-[12], machine learning telah digunakan dalam aktivitas software testing, seperti:

* Tes kasus generasi
* Konstruksi oracle
* Pilihan tes kasus
* Deteksi bug
* Prediksi kesalahan

Hasil studi menunjukkan bahwa sebagian besar artikel menggunakan pembelajaran terawat (supervised learning) untuk mengatasi masalah software testing, seperti ANN dan DT. Selain itu, kelebihan dan kekurangan penggunaan machine learning dalam software testing juga dibahas.

Dalam salah satu studi, Langdon et al. [16] melaporkan bahwa machine learning dapat digunakan untuk secara otomatis menghasilkan tes kasus yang sebagian tepat dengan menggunakan pembelajaran dari test suite sumber terbuka.

### reference


Some studies, e.g., [8], [10]- [12], have already analyzed the application of ML in SE in the past. Durelli et al. [8] conducts a systematic mapping study on the application of ML for software testing.

Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases.

Although there are many successful studies about the automated generation of test cases, determining whether a program has passed a given test remains largely manual. Langdon et al. [16] proposed the use of search-based learning from existing open-source test suites to automatically generate partially correct test oracles.

Most of the articles we found were focusing on applying ML to various software quality assurance and analytic tasks. The applications include: fault/bug/defect prediction category, which revolves around the prediction of faults, bugs, or defects using ML techniques [34]- [39].

The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations.

In the requirements stage, writing requirements specifications is highly deemed to be a human-centric task. Prior work by Pandita et al. [50] and Jahan et al. [51] have inferred the most probable specifications and identified its unexpected behaviors from various artifacts by employing ML techniques, respectively.

We found several studies on ML assisting the software implementation stage. Among many applications, code clone/ localization/refactoring/ labeling aims at finding code duplication, specific location of code in software, refactoring of code, or labeling of code with the help of ML, e.g., Alahmadi et al. [29] employed CNN in order to predict the code blocks in video tutorials.

The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6].

---

## Sample 62

- conversation_id: 14
- user_chat_id: 804
- bot_chat_id: 805

### user_input

Apa itu systematic literature review?

### retrieved_context

1. A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49]. According to Kitchenham [49], [50], an SLR has three main phases: planning, conducting and reviewing the review, as shown in Table 1. Researchers have used the SLR process in several domains [2], [51]- [55].

The authors of this work completed all three phases of the SLR. Inter-rate reliability analyses were undertaken during the initial and final selection phases of the SLR to reduce inter-person bias. The findings of the inter-rater reliability review are discussed in Section 3.2. We followed all of the processes in the three phases of the SLR, as stated in Table 1.

TABLE 1. SLR phases. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

2. FIGURE 1. Steps of the systematic literature review process.

Gambar ini merupakan sebuah diagram alur proses sistematis tinjauan literatur, dengan menggunakan jenis visual yang disebut flowchart. Elemen yang tampak dalam gambar tersebut adalah serangkaian simbol dan garis yang membentuk alur proses. Terdapat beberapa elemen kunci yang dapat dilihat, yaitu:

* Simbol "1." pada bagian atas gambar yang menunjukkan tahap awal dari sistematis tinjauan literatur.
* Garis horizontal yang menghubungkan simbol "1." dengan simbol berikutnya, menunjukkan bahwa tahap tersebut adalah langkah awal dalam proses sistematis tinjauan literatur.
* Simbol lainnya seperti lingkaran dan persegi panjang yang menggambarkan tahapan-tahapan selanjutnya dalam proses tersebut.

Meskipun tidak terdapat angka atau label penting secara eksplisit, namun dapat disimpulkan bahwa gambar ini menunjukkan bahwa sistematis tinjauan literatur dilakukan melalui beberapa tahap yang jelas dan sistematik. Maka dari itu, makna singkat yang dapat ditarik adalah bahwa proses sistematis tinjauan literatur merupakan suatu proses yang terstruktur dengan baik untuk mencari dan menganalisis informasi yang relevan. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

3. FIGURE 1. Steps of the systematic literature review process.

Gambar tersebut menampilkan langkah-langkah proses tinjauan literatur sistematis dalam format diagram alir. Diagram ini terdiri atas beberapa langkah yang disajikan secara linear, dengan koneksi antar langkah menggunakan garis berwarna biru.

Pertama-tama, gambar menunjukkan langkah persiapan (Preparation), yang mencakup identifikasi topik penelitian dan perumusan pertanyaan penelitian. Langkah ini diikuti oleh langkah pencarian literatur, yaitu proses pengumpulan dan seleksi artikel yang relevan dengan topik penelitian.

Selanjutnya, gambar menampilkan langkah analisis data, dimana hasil dari literatur yang dipilih akan dianalisis untuk mengidentifikasi temuan-temuan penting. Langkah ini diakhiri dengan konfirmasi keabsahan dan kualitas hasil penelitian, yang merupakan langkah yang sangat penting dalam proses tinjauan literatur sistematis.

Terdapat beberapa elemen yang tampak pada gambar ini, seperti simbol-simbol yang merepresentasikan masing-masing langkah, serta garis-garis yang menghubungkan antar langkah. Namun, tidak terdapat angka atau label penting yang menonjol dalam diagram ini.

Makna singkat dari gambar ini adalah sebagai peta proses tinjauan literatur sistematis, memberikan panduan langkah demi langkah untuk mengembangkan penelitian dan memastikan kualitas hasilnya. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

4. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

5. The SLR was conducted to extract critical success factors, barriers, and implementation practices from the literature. Rockart [38] defined SLR as a method of systematically collecting, analyzing, and reporting data from the literature of a specific research area and questions of interest [38].

The SLR technique was used to search for the most relevant literature by applying explicit inclusion and exclusion criteria for primary studies [38].

We followed the guidelines provided by Rockart [38] to conduct our SLR study. The approach consists of three main phases: planning, conducting, and reporting the review. A thorough discussion of the SLR study conducted for this research project can be found in our previously published articles [25], [63], [64]. (SPIIMM: Toward a Model for Software Process Improvement Implementation and Management in Global Software Development, page 3)

6. In this systematic literature review (SLR), we focused on examining the most reputable and reliable databases available to researchers, as previously mentioned. It is important to note that we allocated publications to specific databases based on the chronological order of the searches conducted, even though some papers might be present across multiple databases. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 5)

7. This systematic review follows a structured approach aligned with prior systematic reviews on LLM-based agents in software engineering [1], [13]. The methodology ensures comprehensive coverage of relevant literature while maintaining rigor and transparency throughout the review process. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 3)

8. Table 1. Researchers have used the SLR process in several domain sebagai dasar penelitian ini membagikan beberapa metode dan langkah dalam melakukan Systematic Literature Review (SLR). Secara singkat, SLR adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan.

Dalam fase perencanaan, para peneliti harus menentukan topik atau pertanyaan penelitian, serta mengidentifikasi sumber-sumber informasi yang relevan. Mereka juga harus menetapkan kriteria inklusi dan eksklusi untuk memilih artikel-artikel yang akan diintervensi.

Fase pelaksanaan melibatkan proses mencari dan menganalisis artikel-artikel yang telah dipilih berdasarkan kriteria sebelumnya. Para peneliti harus mengidentifikasi informasi yang relevan, mengumpulkan data, serta melakukan analisis untuk mendapatkan hasil yang diinginkan.

Fase tinjauan adalah tahap akhir dalam proses SLR. Pada fase ini, para peneliti akan meninjau dan menganalisis hasil-hasil dari fase sebelumnya. Mereka juga harus memastikan bahwa hasil penelitian mereka tidak memiliki bias atau kesalahan.

Dalam beberapa domain yang telah diidentifikasi oleh peneliti, metode SLR digunakan untuk mengurangi ketidakakuratan dan kesalahan dalam penelitian. Penulis juga menggunakan teknik inter-rater reliability analisis untuk memastikan bahwa hasil-hasil dari fase tinjauan tidak memiliki bias.

Dalam beberapa kasus, metode SLR digunakan dalam beberapa domain, seperti informasi keamanan (security), pengembangan perangkat lunak (software development) dan sebagainya. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

### response

Systematic Literature Review (SLR) adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan. SLR digunakan untuk mengumpulkan, menganalisis, dan melaporkan data dari literatur yang relevan dengan topik penelitian tertentu.

Dalam fase perencanaan, para peneliti harus menentukan topik atau pertanyaan penelitian serta mengidentifikasi sumber-sumber informasi yang relevan. Mereka juga harus menetapkan kriteria inklusi dan eksklusi untuk memilih artikel-artikel yang akan diintervensi.

Fase pelaksanaan melibatkan proses mencari dan menganalisis artikel-artikel yang telah dipilih berdasarkan kriteria sebelumnya. Para peneliti harus mengidentifikasi informasi yang relevan, mengumpulkan data, serta melakukan analisis untuk mendapatkan hasil yang diinginkan.

Fase tinjauan adalah tahap akhir dalam proses SLR. Pada fase ini, para peneliti akan meninjau dan menganalisis hasil-hasil dari fase sebelumnya. Mereka juga harus memastikan bahwa hasil penelitian mereka tidak memiliki bias atau kesalahan.

SLR digunakan dalam beberapa domain, seperti informasi keamanan (security), pengembangan perangkat lunak (software development) dan sebagainya.

### reference


A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49].

Steps of the systematic literature review process. Gambar ini merupakan sebuah diagram alur proses sistematis tinjauan literatur, dengan menggunakan jenis visual yang disebut flowchart.

Steps of the systematic literature review process. Gambar tersebut menampilkan langkah-langkah proses tinjauan literatur sistematis dalam format diagram alir.

To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject.

The SLR was conducted to extract critical success factors, barriers, and implementation practices from the literature. Rockart [38] defined SLR as a method of systematically collecting, analyzing, and reporting data from the literature of a specific research area and questions of interest [38].

In this systematic literature review (SLR), we focused on examining the most reputable and reliable databases available to researchers, as previously mentioned. It is important to note that we allocated publications to specific databases based on the chronological order of the searches conducted, even though some papers might be present across multiple databases.

This systematic review follows a structured approach aligned with prior systematic reviews on LLM-based agents in software engineering [1], [13]. The methodology ensures comprehensive coverage of relevant literature while maintaining rigor and transparency throughout the review process.

Researchers have used the SLR process in several domain sebagai dasar penelitian ini membagikan beberapa metode dan langkah dalam melakukan Systematic Literature Review (SLR). Secara singkat, SLR adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan.

---

## Sample 63

- conversation_id: 14
- user_chat_id: 806
- bot_chat_id: 807

### user_input

Mengapa systematic literature review penting?

### retrieved_context

1. FIGURE 1. Steps of the systematic literature review process.

Gambar ini merupakan sebuah diagram alur proses sistematis tinjauan literatur, dengan menggunakan jenis visual yang disebut flowchart. Elemen yang tampak dalam gambar tersebut adalah serangkaian simbol dan garis yang membentuk alur proses. Terdapat beberapa elemen kunci yang dapat dilihat, yaitu:

* Simbol "1." pada bagian atas gambar yang menunjukkan tahap awal dari sistematis tinjauan literatur.
* Garis horizontal yang menghubungkan simbol "1." dengan simbol berikutnya, menunjukkan bahwa tahap tersebut adalah langkah awal dalam proses sistematis tinjauan literatur.
* Simbol lainnya seperti lingkaran dan persegi panjang yang menggambarkan tahapan-tahapan selanjutnya dalam proses tersebut.

Meskipun tidak terdapat angka atau label penting secara eksplisit, namun dapat disimpulkan bahwa gambar ini menunjukkan bahwa sistematis tinjauan literatur dilakukan melalui beberapa tahap yang jelas dan sistematik. Maka dari itu, makna singkat yang dapat ditarik adalah bahwa proses sistematis tinjauan literatur merupakan suatu proses yang terstruktur dengan baik untuk mencari dan menganalisis informasi yang relevan. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

2. A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49]. According to Kitchenham [49], [50], an SLR has three main phases: planning, conducting and reviewing the review, as shown in Table 1. Researchers have used the SLR process in several domains [2], [51]- [55].

The authors of this work completed all three phases of the SLR. Inter-rate reliability analyses were undertaken during the initial and final selection phases of the SLR to reduce inter-person bias. The findings of the inter-rater reliability review are discussed in Section 3.2. We followed all of the processes in the three phases of the SLR, as stated in Table 1.

TABLE 1. SLR phases. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

3. Table 1. Researchers have used the SLR process in several domain sebagai dasar penelitian ini membagikan beberapa metode dan langkah dalam melakukan Systematic Literature Review (SLR). Secara singkat, SLR adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan.

Dalam fase perencanaan, para peneliti harus menentukan topik atau pertanyaan penelitian, serta mengidentifikasi sumber-sumber informasi yang relevan. Mereka juga harus menetapkan kriteria inklusi dan eksklusi untuk memilih artikel-artikel yang akan diintervensi.

Fase pelaksanaan melibatkan proses mencari dan menganalisis artikel-artikel yang telah dipilih berdasarkan kriteria sebelumnya. Para peneliti harus mengidentifikasi informasi yang relevan, mengumpulkan data, serta melakukan analisis untuk mendapatkan hasil yang diinginkan.

Fase tinjauan adalah tahap akhir dalam proses SLR. Pada fase ini, para peneliti akan meninjau dan menganalisis hasil-hasil dari fase sebelumnya. Mereka juga harus memastikan bahwa hasil penelitian mereka tidak memiliki bias atau kesalahan.

Dalam beberapa domain yang telah diidentifikasi oleh peneliti, metode SLR digunakan untuk mengurangi ketidakakuratan dan kesalahan dalam penelitian. Penulis juga menggunakan teknik inter-rater reliability analisis untuk memastikan bahwa hasil-hasil dari fase tinjauan tidak memiliki bias.

Dalam beberapa kasus, metode SLR digunakan dalam beberapa domain, seperti informasi keamanan (security), pengembangan perangkat lunak (software development) dan sebagainya. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

4. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

5. Systematic mapping or scoping studies are conducted to provide an overview of a research domain through classification. These studies mainly explore the existing literature to investigate the coverage of multiple topics, the frequency of publications, the research trends, and the publication venues where relevant studies have been published [14]. The systematic mapping in the current study mainly follows the guidelines suggested by Petersen et al. [15]. According to the guidelines for systematic mapping studies in SE [15], the essential process steps of the current systematic mapping study were defining the research questions, searching for relevant papers, screening the papers, keywording the abstracts, extracting the data, and mapping, as shown in Fig. 1. Each process step has an outcome and the outcome of the complete process is the systematic map, which is explained as follows [15]: Definition of Research Questions (Research Scope) -The primary goal of a systematic mapping study is to provide an overview of a research area and identify the quantity and type of research and results available within this area. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 1)

6. FIGURE 1. Steps of the systematic literature review process.

Gambar tersebut menampilkan langkah-langkah proses tinjauan literatur sistematis dalam format diagram alir. Diagram ini terdiri atas beberapa langkah yang disajikan secara linear, dengan koneksi antar langkah menggunakan garis berwarna biru.

Pertama-tama, gambar menunjukkan langkah persiapan (Preparation), yang mencakup identifikasi topik penelitian dan perumusan pertanyaan penelitian. Langkah ini diikuti oleh langkah pencarian literatur, yaitu proses pengumpulan dan seleksi artikel yang relevan dengan topik penelitian.

Selanjutnya, gambar menampilkan langkah analisis data, dimana hasil dari literatur yang dipilih akan dianalisis untuk mengidentifikasi temuan-temuan penting. Langkah ini diakhiri dengan konfirmasi keabsahan dan kualitas hasil penelitian, yang merupakan langkah yang sangat penting dalam proses tinjauan literatur sistematis.

Terdapat beberapa elemen yang tampak pada gambar ini, seperti simbol-simbol yang merepresentasikan masing-masing langkah, serta garis-garis yang menghubungkan antar langkah. Namun, tidak terdapat angka atau label penting yang menonjol dalam diagram ini.

Makna singkat dari gambar ini adalah sebagai peta proses tinjauan literatur sistematis, memberikan panduan langkah demi langkah untuk mengembangkan penelitian dan memastikan kualitas hasilnya. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

7. The initial step in conducting a literature review is to identify a set of individual research questions. These questions guide the development of this work and inform the readers about the main focus of the study. To formulate the most appropriate research questions, we referred to the ''Goal Question Metric'' model developed by Caldiera et al. [16]. With this model, it is necessary to predetermine the analysis's objectives, target objects and issues, as well as the analytical vantage points. According to the model, we specified the purpose, target objectives, issues, and viewpoints of the analysis as follows: (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 3)

8. The assessment of methods and quality of research is vital to this study in demonstrating the extent of rigor and relevance of the selected articles in this study. Although the high relevance observed demonstrates how much evidence produced in the study has been adduced to working with the software companies themselves, this demonstrates how the study can influence the industry practice. On the other hand, rigor is reported as inadequate, and this is an area that requires substantial attention. This is similar to the findings of similar mapping studies of Klotins et al. [40] and Paternoster et al. [7]. This means that the description of context and study design in most of the studies has remained a challenge and, therefore a threat to generalizability and knowledge transfer. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 17)

### response

Systematic literature review (SLR) penting karena:

* SLR dapat memberikan gambaran yang komprehensif tentang kualitas software berbasis AI, seperti dalam [Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review].
* SLR dapat membantu mengidentifikasi celah dan kesempatan dalam pengembangan software berbasis AI, seperti dalam [Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities].
* SLR dapat memberikan panduan langkah demi langkah untuk mengembangkan penelitian dan memastikan kualitas hasilnya, seperti yang ditunjukkan pada gambar FIGURE 1 dalam [Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities].
* SLR dapat membantu meningkatkan ketepatan dan akurasi penelitian dengan menggunakan metode yang sistematis dan berdasarkan bukti, seperti yang disebutkan dalam [Systematic Literature Review on Security Risks and its Practices in Secure Software Development].
* SLR dapat membantu mengidentifikasi dan memahami tren penelitian dalam bidang software engineering, seperti yang ditunjukkan pada gambar FIGURE 1 dalam [Systematic Mapping: Artificial Intelligence Techniques in Software Engineering].

### reference


Steps of the systematic literature review process. Gambar ini merupakan sebuah diagram alur proses sistematis tinjauan literatur, dengan menggunakan jenis visual yang disebut flowchart.

A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49].

Researchers have used the SLR process in several domain sebagai dasar penelitian ini membagikan beberapa metode dan langkah dalam melakukan Systematic Literature Review (SLR). Secara singkat, SLR adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan.

To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject.

Systematic mapping or scoping studies are conducted to provide an overview of a research domain through classification. These studies mainly explore the existing literature to investigate the coverage of multiple topics, the frequency of publications, the research trends, and the publication venues where relevant studies have been published [14].

Steps of the systematic literature review process. Gambar tersebut menampilkan langkah-langkah proses tinjauan literatur sistematis dalam format diagram alir.

The initial step in conducting a literature review is to identify a set of individual research questions. These questions guide the development of this work and inform the readers about the main focus of the study.

The assessment of methods and quality of research is vital to this study in demonstrating the extent of rigor and relevance of the selected articles in this study. Although the high relevance observed demonstrates how much evidence produced in the study has been adduced to working with the software companies themselves, this demonstrates how the study can influence the industry practice.

---

## Sample 64

- conversation_id: 14
- user_chat_id: 808
- bot_chat_id: 809

### user_input

Apa tujuan systematic literature review?

### retrieved_context

1. A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49]. According to Kitchenham [49], [50], an SLR has three main phases: planning, conducting and reviewing the review, as shown in Table 1. Researchers have used the SLR process in several domains [2], [51]- [55].

The authors of this work completed all three phases of the SLR. Inter-rate reliability analyses were undertaken during the initial and final selection phases of the SLR to reduce inter-person bias. The findings of the inter-rater reliability review are discussed in Section 3.2. We followed all of the processes in the three phases of the SLR, as stated in Table 1.

TABLE 1. SLR phases. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

2. Systematic mapping or scoping studies are conducted to provide an overview of a research domain through classification. These studies mainly explore the existing literature to investigate the coverage of multiple topics, the frequency of publications, the research trends, and the publication venues where relevant studies have been published [14]. The systematic mapping in the current study mainly follows the guidelines suggested by Petersen et al. [15]. According to the guidelines for systematic mapping studies in SE [15], the essential process steps of the current systematic mapping study were defining the research questions, searching for relevant papers, screening the papers, keywording the abstracts, extracting the data, and mapping, as shown in Fig. 1. Each process step has an outcome and the outcome of the complete process is the systematic map, which is explained as follows [15]: Definition of Research Questions (Research Scope) -The primary goal of a systematic mapping study is to provide an overview of a research area and identify the quantity and type of research and results available within this area. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 1)

3. The SLR was conducted to extract critical success factors, barriers, and implementation practices from the literature. Rockart [38] defined SLR as a method of systematically collecting, analyzing, and reporting data from the literature of a specific research area and questions of interest [38].

The SLR technique was used to search for the most relevant literature by applying explicit inclusion and exclusion criteria for primary studies [38].

We followed the guidelines provided by Rockart [38] to conduct our SLR study. The approach consists of three main phases: planning, conducting, and reporting the review. A thorough discussion of the SLR study conducted for this research project can be found in our previously published articles [25], [63], [64]. (SPIIMM: Toward a Model for Software Process Improvement Implementation and Management in Global Software Development, page 3)

4. FIGURE 1. Steps of the systematic literature review process.

Gambar tersebut menampilkan langkah-langkah proses tinjauan literatur sistematis dalam format diagram alir. Diagram ini terdiri atas beberapa langkah yang disajikan secara linear, dengan koneksi antar langkah menggunakan garis berwarna biru.

Pertama-tama, gambar menunjukkan langkah persiapan (Preparation), yang mencakup identifikasi topik penelitian dan perumusan pertanyaan penelitian. Langkah ini diikuti oleh langkah pencarian literatur, yaitu proses pengumpulan dan seleksi artikel yang relevan dengan topik penelitian.

Selanjutnya, gambar menampilkan langkah analisis data, dimana hasil dari literatur yang dipilih akan dianalisis untuk mengidentifikasi temuan-temuan penting. Langkah ini diakhiri dengan konfirmasi keabsahan dan kualitas hasil penelitian, yang merupakan langkah yang sangat penting dalam proses tinjauan literatur sistematis.

Terdapat beberapa elemen yang tampak pada gambar ini, seperti simbol-simbol yang merepresentasikan masing-masing langkah, serta garis-garis yang menghubungkan antar langkah. Namun, tidak terdapat angka atau label penting yang menonjol dalam diagram ini.

Makna singkat dari gambar ini adalah sebagai peta proses tinjauan literatur sistematis, memberikan panduan langkah demi langkah untuk mengembangkan penelitian dan memastikan kualitas hasilnya. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

5. By implementing a structured and objective quality assessment process, this systematic literature review aims

TABLE 2. Questions -quality assessment.

to provide a comprehensive and reliable synthesis of the most relevant and high-quality publications in the field. This approach ensures that the findings and conclusions drawn from the reviewed literature are robust and trustworthy, thereby contributing to the overall validity of the research. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 4)

6. FIGURE 1. Steps of the systematic literature review process.

Gambar ini merupakan sebuah diagram alur proses sistematis tinjauan literatur, dengan menggunakan jenis visual yang disebut flowchart. Elemen yang tampak dalam gambar tersebut adalah serangkaian simbol dan garis yang membentuk alur proses. Terdapat beberapa elemen kunci yang dapat dilihat, yaitu:

* Simbol "1." pada bagian atas gambar yang menunjukkan tahap awal dari sistematis tinjauan literatur.
* Garis horizontal yang menghubungkan simbol "1." dengan simbol berikutnya, menunjukkan bahwa tahap tersebut adalah langkah awal dalam proses sistematis tinjauan literatur.
* Simbol lainnya seperti lingkaran dan persegi panjang yang menggambarkan tahapan-tahapan selanjutnya dalam proses tersebut.

Meskipun tidak terdapat angka atau label penting secara eksplisit, namun dapat disimpulkan bahwa gambar ini menunjukkan bahwa sistematis tinjauan literatur dilakukan melalui beberapa tahap yang jelas dan sistematik. Maka dari itu, makna singkat yang dapat ditarik adalah bahwa proses sistematis tinjauan literatur merupakan suatu proses yang terstruktur dengan baik untuk mencari dan menganalisis informasi yang relevan. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

7. The initial step in conducting a literature review is to identify a set of individual research questions. These questions guide the development of this work and inform the readers about the main focus of the study. To formulate the most appropriate research questions, we referred to the ''Goal Question Metric'' model developed by Caldiera et al. [16]. With this model, it is necessary to predetermine the analysis's objectives, target objects and issues, as well as the analytical vantage points. According to the model, we specified the purpose, target objectives, issues, and viewpoints of the analysis as follows: (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 3)

8. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

### response

Menurut Kitchenham [49], [50], SLR bertujuan untuk mengidentifikasi, menerjemahkan, dan membicarakan bukti-bukti yang relevan dengan pertanyaan penelitian. Selain itu, menurut Rockart [38], SLR digunakan untuk menyusun data, menganalisis, dan melaporkan data dari literatur tertentu dan pertanyaan penelitian.

### reference


A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49].

Systematic mapping or scoping studies are conducted to provide an overview of a research domain through classification. These studies mainly explore the existing literature to investigate the coverage of multiple topics, the frequency of publications, the research trends, and the publication venues where relevant studies have been published [14].

The SLR was conducted to extract critical success factors, barriers, and implementation practices from the literature. Rockart [38] defined SLR as a method of systematically collecting, analyzing, and reporting data from the literature of a specific research area and questions of interest [38].

Steps of the systematic literature review process. Gambar tersebut menampilkan langkah-langkah proses tinjauan literatur sistematis dalam format diagram alir.

By implementing a structured and objective quality assessment process, this systematic literature review aims TABLE 2. Questions -quality assessment. to provide a comprehensive and reliable synthesis of the most relevant and high-quality publications in the field.

Steps of the systematic literature review process. Gambar ini merupakan sebuah diagram alur proses sistematis tinjauan literatur, dengan menggunakan jenis visual yang disebut flowchart.

The initial step in conducting a literature review is to identify a set of individual research questions. These questions guide the development of this work and inform the readers about the main focus of the study.

To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject.

---

## Sample 65

- conversation_id: 14
- user_chat_id: 810
- bot_chat_id: 811

### user_input

Bagaimana systematic literature review dilakukan?

### retrieved_context

1. A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49]. According to Kitchenham [49], [50], an SLR has three main phases: planning, conducting and reviewing the review, as shown in Table 1. Researchers have used the SLR process in several domains [2], [51]- [55].

The authors of this work completed all three phases of the SLR. Inter-rate reliability analyses were undertaken during the initial and final selection phases of the SLR to reduce inter-person bias. The findings of the inter-rater reliability review are discussed in Section 3.2. We followed all of the processes in the three phases of the SLR, as stated in Table 1.

TABLE 1. SLR phases. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

2. FIGURE 1. Steps of the systematic literature review process.

Gambar tersebut menampilkan langkah-langkah proses tinjauan literatur sistematis dalam format diagram alir. Diagram ini terdiri atas beberapa langkah yang disajikan secara linear, dengan koneksi antar langkah menggunakan garis berwarna biru.

Pertama-tama, gambar menunjukkan langkah persiapan (Preparation), yang mencakup identifikasi topik penelitian dan perumusan pertanyaan penelitian. Langkah ini diikuti oleh langkah pencarian literatur, yaitu proses pengumpulan dan seleksi artikel yang relevan dengan topik penelitian.

Selanjutnya, gambar menampilkan langkah analisis data, dimana hasil dari literatur yang dipilih akan dianalisis untuk mengidentifikasi temuan-temuan penting. Langkah ini diakhiri dengan konfirmasi keabsahan dan kualitas hasil penelitian, yang merupakan langkah yang sangat penting dalam proses tinjauan literatur sistematis.

Terdapat beberapa elemen yang tampak pada gambar ini, seperti simbol-simbol yang merepresentasikan masing-masing langkah, serta garis-garis yang menghubungkan antar langkah. Namun, tidak terdapat angka atau label penting yang menonjol dalam diagram ini.

Makna singkat dari gambar ini adalah sebagai peta proses tinjauan literatur sistematis, memberikan panduan langkah demi langkah untuk mengembangkan penelitian dan memastikan kualitas hasilnya. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

3. The SLR was conducted to extract critical success factors, barriers, and implementation practices from the literature. Rockart [38] defined SLR as a method of systematically collecting, analyzing, and reporting data from the literature of a specific research area and questions of interest [38].

The SLR technique was used to search for the most relevant literature by applying explicit inclusion and exclusion criteria for primary studies [38].

We followed the guidelines provided by Rockart [38] to conduct our SLR study. The approach consists of three main phases: planning, conducting, and reporting the review. A thorough discussion of the SLR study conducted for this research project can be found in our previously published articles [25], [63], [64]. (SPIIMM: Toward a Model for Software Process Improvement Implementation and Management in Global Software Development, page 3)

4. FIGURE 1. Steps of the systematic literature review process.

Gambar ini merupakan sebuah diagram alur proses sistematis tinjauan literatur, dengan menggunakan jenis visual yang disebut flowchart. Elemen yang tampak dalam gambar tersebut adalah serangkaian simbol dan garis yang membentuk alur proses. Terdapat beberapa elemen kunci yang dapat dilihat, yaitu:

* Simbol "1." pada bagian atas gambar yang menunjukkan tahap awal dari sistematis tinjauan literatur.
* Garis horizontal yang menghubungkan simbol "1." dengan simbol berikutnya, menunjukkan bahwa tahap tersebut adalah langkah awal dalam proses sistematis tinjauan literatur.
* Simbol lainnya seperti lingkaran dan persegi panjang yang menggambarkan tahapan-tahapan selanjutnya dalam proses tersebut.

Meskipun tidak terdapat angka atau label penting secara eksplisit, namun dapat disimpulkan bahwa gambar ini menunjukkan bahwa sistematis tinjauan literatur dilakukan melalui beberapa tahap yang jelas dan sistematik. Maka dari itu, makna singkat yang dapat ditarik adalah bahwa proses sistematis tinjauan literatur merupakan suatu proses yang terstruktur dengan baik untuk mencari dan menganalisis informasi yang relevan. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

5. The initial step in conducting a literature review is to identify a set of individual research questions. These questions guide the development of this work and inform the readers about the main focus of the study. To formulate the most appropriate research questions, we referred to the ''Goal Question Metric'' model developed by Caldiera et al. [16]. With this model, it is necessary to predetermine the analysis's objectives, target objects and issues, as well as the analytical vantage points. According to the model, we specified the purpose, target objectives, issues, and viewpoints of the analysis as follows: (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 3)

6. Table 1. Researchers have used the SLR process in several domain sebagai dasar penelitian ini membagikan beberapa metode dan langkah dalam melakukan Systematic Literature Review (SLR). Secara singkat, SLR adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan.

Dalam fase perencanaan, para peneliti harus menentukan topik atau pertanyaan penelitian, serta mengidentifikasi sumber-sumber informasi yang relevan. Mereka juga harus menetapkan kriteria inklusi dan eksklusi untuk memilih artikel-artikel yang akan diintervensi.

Fase pelaksanaan melibatkan proses mencari dan menganalisis artikel-artikel yang telah dipilih berdasarkan kriteria sebelumnya. Para peneliti harus mengidentifikasi informasi yang relevan, mengumpulkan data, serta melakukan analisis untuk mendapatkan hasil yang diinginkan.

Fase tinjauan adalah tahap akhir dalam proses SLR. Pada fase ini, para peneliti akan meninjau dan menganalisis hasil-hasil dari fase sebelumnya. Mereka juga harus memastikan bahwa hasil penelitian mereka tidak memiliki bias atau kesalahan.

Dalam beberapa domain yang telah diidentifikasi oleh peneliti, metode SLR digunakan untuk mengurangi ketidakakuratan dan kesalahan dalam penelitian. Penulis juga menggunakan teknik inter-rater reliability analisis untuk memastikan bahwa hasil-hasil dari fase tinjauan tidak memiliki bias.

Dalam beberapa kasus, metode SLR digunakan dalam beberapa domain, seperti informasi keamanan (security), pengembangan perangkat lunak (software development) dan sebagainya. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

7. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

8. This systematic review follows a structured approach aligned with prior systematic reviews on LLM-based agents in software engineering [1], [13]. The methodology ensures comprehensive coverage of relevant literature while maintaining rigor and transparency throughout the review process. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 3)

### response

Terdapat beberapa langkah dalam melakukan Systematic Literature Review (SLR), yaitu:

* Perencanaan: menentukan topik atau pertanyaan penelitian, serta mengidentifikasi sumber-sumber informasi yang relevan.
* Pelaksanaan: mencari dan menganalisis artikel-artikel yang telah dipilih berdasarkan kriteria sebelumnya, serta melakukan analisis untuk mendapatkan hasil yang diinginkan.
* Tinjauan: meninjau dan menganalisis hasil-hasil dari fase sebelumnya, serta memastikan bahwa hasil penelitian tidak memiliki bias atau kesalahan.

### reference


A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49].

Steps of the systematic literature review process. Gambar tersebut menampilkan langkah-langkah proses tinjauan literatur sistematis dalam format diagram alir.

The SLR was conducted to extract critical success factors, barriers, and implementation practices from the literature. Rockart [38] defined SLR as a method of systematically collecting, analyzing, and reporting data from the literature of a specific research area and questions of interest [38].

Steps of the systematic literature review process. Gambar ini merupakan sebuah diagram alur proses sistematis tinjauan literatur, dengan menggunakan jenis visual yang disebut flowchart.

The initial step in conducting a literature review is to identify a set of individual research questions. These questions guide the development of this work and inform the readers about the main focus of the study.

Researchers have used the SLR process in several domain sebagai dasar penelitian ini membagikan beberapa metode dan langkah dalam melakukan Systematic Literature Review (SLR). Secara singkat, SLR adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan.

To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject.

This systematic review follows a structured approach aligned with prior systematic reviews on LLM-based agents in software engineering [1], [13]. The methodology ensures comprehensive coverage of relevant literature while maintaining rigor and transparency throughout the review process.
