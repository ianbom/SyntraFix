# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 16

- conversation_id: 13
- user_chat_id: 511
- bot_chat_id: 512

### user_input

Bagaimana software metrics digunakan untuk menilai software quality?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

4. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

5. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

6. The set of features are consisting of single or multiple metrics derived through artifacts of software, it is believed that these are useful to predict labels of class. All of the metrics are grouped into the product, project, and process metrics. It is observed that metrics of the product are mostly utilized in the research arena [31]. The further level of product metrics includes method, class, and file levels where overall 60% method-level metrics are utilized followed by 24% classlevel metrics [15]. Metrics of the product also consist of, volume, design, code, and complexity metrics. The performance of SFP heavily depends on these metrics. Researchers have assessed the utilization rate of metrics in [32] where highly use product metrics in software fault prediction are Halstead [1], McCabe [3], LoC in structural programming, and in object-oriented paradigm C&K metrics suite [33]. The subject metrics are become the approved standard metrics in software fault prediction. PROMISE and D'Ambros [34] are frequently used datasets repositories having these metrics. Both the repositories encompass datasets of about fifty-two percent of the research paper published after 2005 [9]. Since these datasets are publicly available therefore it is frequently used. The other reason is the non-availability of bug's data of industrial software. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 4)

7. Object-oriented metrics are used to predict the quality of object-oriented software. The attributes that determine software quality include maintainability, fault tolerance, understandability, fault density, standardized rework rate, reusability, etc. Several studies were carried out, including the empirical verification of the object-oriented metrics in open source software for the prediction of faults using CBO, LOC, LCOM, NOC and DIT [10], reuse analysis of objectoriented systems using metrics of inheritance, coupling and cohesion [92], heuristic review of CK metrics [93], reusable metrics for object-oriented design [94] and empirical analysis of CK metrics for object-oriented design complexity [95]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 5)

8. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

### response

Software metrics digunakan untuk menilai kualitas software dengan beberapa cara, antara lain:

* Menilai kompleksitas dan kualitas kode program
* Memprediksi kemungkinan adanya kerusakan (fault) dalam sistem
* Menganalisis perilaku atau fungsi sistem
* Mengukur efisiensi dan keamanan sistem

Dalam beberapa sumber, disebutkan bahwa software metrics dapat digunakan untuk menilai kualitas software melalui:

* Internal metrics: mengukur kualitas kode program
* Eksternal metrics: mengukur perilaku atau fungsi sistem
* Structural complexity measures: mengukur kompleksitas arsitektur sistem
* Quality metrics: mengukur keandalan sistem
* Productivity metrics: mengukur dampak alat bantu GAI terhadap kecepatan, kualitas, dan efisiensi pengembangan sistem.

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1) Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

---

## Sample 17

- conversation_id: 13
- user_chat_id: 513
- bot_chat_id: 514

### user_input

Mengapa software quality perlu dijaga selama software maintenance?

### retrieved_context

1. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

2. According to a 2013 study by the University of Cambridge [17], [18], the global cost of finding and removing bugs from software has risen to $312 billion annually, and it makes up half of the development time of the average project. Furthermore, constant change makes matters worse. Changes are the main causes of software bugs and major issues faced by the software industry. Studies conducted by Javed et al. [1] indicated that there is a significant relationship between change requests and overall bugs. Based on Mozilla quality assurance process [19], the focus of the quality assurance is correcting bugs. Therefore, based on these studies, our Quality Assurance Subsystem is modeled and depicted in Figure 7. (Change-Oriented Open Source Software Process Simulation, page 1)

3. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

4. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

5. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

6. Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment. New threats are tracked during this phase. The software can never be 100 percent secure, and new threats emerge regularly phase [14]. As a result, efforts must be made to secure the software. The maintenance team should keep track of new threats that the system encounters to address them promptly and prevent security breaches [83], [116]. Table 15 presents prescriptive actions to increase security during the maintenance phase of SDLC [14], [65], [105], [114], [117], [118]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

7. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

8. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

### response

Jawaban:
Software quality perlu dijaga selama software maintenance karena hal ini dapat mempengaruhi kinerja, keamanan, dan keandalan sistem. Dengan menjaga software quality, masalah yang tidak terduga dapat dicegah dan biaya yang diperlukan untuk mengatasi masalah tersebut dapat diminimalkan.

Rujukan:
- [Source: How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success]
- [Source: Change-Oriented Open Source Software Process Simulation]
- [Source: Systematic Mapping: Artificial Intelligence Techniques in Software Engineering]

### reference


A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2) In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3) Therefore, based on these studies, our Quality Assurance Subsystem is modeled and depicted in Figure 7. (Change-Oriented Open Source Software Process Simulation, page 1)

---

## Sample 18

- conversation_id: 13
- user_chat_id: 515
- bot_chat_id: 516

### user_input

Bagaimana Agile software development dapat membantu meningkatkan software quality?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

3. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

4. Currently, in many software development companies, teams are using various specific tools (such as Jira, GitLab and SonarQube) in order to support the development process and the quality of the code and products. This is usually done in a regular retrospective meeting that involves all the team. As far as the code quality is concerned, those tools provide sufficient information for the Scrum Team. However, there is still a gap and the need for more solutions reflecting team effectiveness and process quality. It can be stated that, at present, process improvement activities are mainly based on developers' perceptions and little support is given to make process wise data-driven decisions. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

5. TABLE 1. Examples of actions to improve software quality for the adalah tabel yang menyajikan contoh tindakan untuk meningkatkan kualitas perangkat lunak dengan menggunakan alat analitik perangkat lunak. Tabel ini terdiri dari 38 baris dan memiliki 8 kolom.

Tabel tersebut menjelaskan beberapa indikator strategis yang digunakan untuk mengevaluasi kinerja perangkat lunak, seperti "Blocking" yang merupakan indikator strategis untuk mengidentifikasi potensi masalah dalam proses pengembangan. Dalam tabel ini juga dapat dilihat bahwa ada empat faktor utama yang digunakan untuk menilai kualitas perangkat lunak: Code Smells, Design Issues, Performance, dan Security.

Salah satu contoh kasus yang disajikan dalam tabel adalah "Blocking" files problem yang dialami oleh perusahaan NeverLate. Dalam kasus ini, analis perangkat lunak dapat menggunakan alat analitik untuk mengidentifikasi klas-klas file yang memiliki kualitas rendah dan membutuhkan perbaikan.

Analisis dari tabel menunjukkan bahwa perusahaan yang menggunakan Q-Rapids dapat meningkatkan kualitas perangkat lunak mereka dengan menggunakan data historis dan visualisasi data. Dengan demikian, mereka dapat mengidentifikasi masalah-masalah yang signifikan dan mengambil tindakan untuk memperbaiki kinerja perangkat lunak.

Dalam kesimpulan, tabel ini menunjukkan bahwa penggunaan alat analitik perangkat lunak dapat membantu meningkatkan kualitas perangkat lunak dengan cara yang lebih objektif dan data-driven. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 6)

6. Currently, in many software development companies and software houses, teams are already using some common tools (such as Jira, GitLab, and SonarQube) to manage the development process and the quality of their code and products. Such tools are now embedded into developers' way of working, and into the processes used in companies. Therefore, when introducing the Q-Rapids tool, it has to be clear when it is going to be used to assess and improve software quality, e.g., before checking the status of the project in GitLab or Jira or afterwards. It needs to be clarified when exactly in the agile (or any other) process this new tool should be used. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 15)

7. Currently, in many software development companies and software houses, teams are already using some common tools (such as Jira, GitLab, and SonarQube) to manage the development process and the quality of their code and products. Such tools are now embedded into developers' way of working, and into the processes used in companies. Therefore, when introducing the Q-Rapids tool, it has to be clear when it is going to be used to assess and improve software quality, e.g., before checking the status of the project in GitLab or Jira or afterwards. It needs to be clarified when exactly in the agile (or any other) process this new tool should be used. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 15)

8. Two well-accepted strategies that software companies can implement to preserve their competitive advantage, reducing their time to market, are Agile Software Development (ASD) and Reuse-Driven Software Engineering (RDSE) [1]. While ASD achieves this by having short validation cycles, incremental delivery and minimizing activities not directly related to executable code, RDSE reduces the effort necessary to pro-The associate editor coordinating the review of this manuscript and approving it for publication was Adnan Abid. duce artifacts by reusing existent knowledge (i.e., artifacts) such as source code, requirements, and test cases. (Enabling the Reuse of Software Development Assets Through a Taxonomy for User Stories, page 1)

### response

Agile software development dapat membantu meningkatkan software quality dengan cara berikut:

• Menggunakan short feedback cycles untuk mendapatkan umpan balik yang cepat dan efektif
• Melakukan perubahan secara terus-menerus dan iteratif untuk memastikan bahwa sistem yang dikembangkan sesuai dengan kebutuhan pelanggan
• Meningkatkan kerja sama antara tim pengembangan dan pelanggan melalui komunikasi yang lebih baik
• Menggunakan alat analitik perangkat lunak untuk mengidentifikasi masalah-masalah yang signifikan dan mengambil tindakan untuk memperbaiki kinerja perangkat lunak.

Referensi:
[Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study]
[Measuring and Improving Agile Processes in a Small-Size Software Development Company]

### reference


Dalam kesimpulan, tabel ini menunjukkan bahwa penggunaan alat analitik perangkat lunak dapat membantu meningkatkan kualitas perangkat lunak dengan cara yang lebih objektif dan data-driven. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 6) Dengan demikian, mereka dapat mengidentifikasi masalah-masalah yang signifikan dan mengambil tindakan untuk memperbaiki kinerja perangkat lunak. Examples of actions to improve software quality for the adalah tabel yang menyajikan contoh tindakan untuk meningkatkan kualitas perangkat lunak dengan menggunakan alat analitik perangkat lunak.

---

## Sample 19

- conversation_id: 13
- user_chat_id: 517
- bot_chat_id: 518

### user_input

Bagaimana machine learning dapat digunakan untuk memprediksi software quality?

### retrieved_context

1. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. The prediction of refactoring refers to identifying the locations (i.e., classes, methods) in the software system that need to be refactored. Machine learning (ML) techniques have been used to detect code smells and predict refactoring. Ratzinger et al. [39] conducted an empirical study on two open-source software projects to identify where refactoring can be applied. They used classification algorithms (J482, LMT, Rip, and NNge) to predict where in the code should be refactored based on the project development history obtained from the Concurrent Versions System (CVS). Al Dallal [40] carried out an empirical study to predict the opportunities of using the Move Method refactoring technique in the classes. Logistic regression models were applied to create the prediction models on seven open-source projects of different sizes (one large-scale project and the others were medium and small projects). (Revisiting Scenarios of Using Refactoring Techniques to Improve Software Systems Quality, page 1)

4. Software fault prediction process typically involves two phases which are denoted as training phase and the second is prediction phase where in the first phase, a model for prediction is constructed, which utilizes method or class level metrics of software with fault information associated with every single module of the software. Later, the same model is used to predict faulty classes in a new version of the software. SFP is effective to enhance the quality of software along with reducing the cost of testing. Also, it assists testing teams to limit testing on faulty classes only. Fault prediction in software possibly lays down yardstick for knowing, which areas may require attention. Many software fault prediction methods have been utilized [29], which contribute to three main elements [30]; Set of features, Label of Class, and finally the Model. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 3)

5. The prediction of software faults is the subject of several studies. Many techniques have been proposed for predicting a software fault, including Statistical and Machine Learning methods. These are described as:

Statistical methods are used to find a clear mathematical formula that absolutely identifies how classification should be performed. Kapila and Singh [85] used two statistical approaches to carry out his study: Logistic Regression and Univariate Binary Logistic Regression (UBR) which are useful for analysis of data with binary variables. In Bayesian inference [85], the design of the model relates the metrics with the content of software faults and the tendency of faults. The regression analysis is extensively utilized for prediction of bad smell in the code and linear regression in a case where only two classes of the dependent variable exist. The Multilayer Perceptron (MLP) is utilized to control faulty classes and the Radial Base functions are used to classify the faults according to the different categories of faults [87]. Xing et al. defines the significance of the model of Support Vector Machine (SVM). The SVM model can be used for small amount of data. SVM delivers greater Accuracy as compare to other techniques for predicting quality of software, but the performance of SVM is low in public datasets [86]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 4)

6. Object-oriented metrics have been empirically validated to predict design flaws. Large and complex software systems are usually faulty [11]. It is difficult to keep them away from faults or to decrease risk of faults in upcoming version. According to [75], focus of verification and verification activities is to classify and remove high-risk problems in software. In order to avoid or squeeze faults, quality control models for example fault-prone models can be used for prediction of classes likely to be faulty. In order to attain these objectives, several researchers studied faults in software and constructed fault-proneness models base, on the event of failure [10], [34], [47], [76], [77]. Software prediction models are constructed using a variety of machine learning methods, such as Genetic Programming [78], Decision Trees [79], Neural Networks [80], Naive Bayes (NB) [21], Case-Based Reasoning [81], and Blurring Logic [82]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

7. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

8. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

### response

Berikut beberapa cara machine learning dapat digunakan untuk memprediksi software quality:

* Menggunakan metode pengajaran mesin, seperti Support Vector Machines (SVM), Naive Bayes (NB), Decision Trees, dan Neural Networks, untuk membangun model prediksi berdasarkan data metric software.
* Menganalisis data fault dari proyek-software yang serupa atau versi sebelumnya untuk mengembangkan model prediksi.
* Menggunakan teknik machine learning, seperti Logistic Regression dan Univariate Binary Logistic Regression (UBR), untuk menganalisis data dengan variabel binary.
* Menggunakan teknik neural network, seperti Multilayer Perceptron (MLP) dan Radial Base functions, untuk klasifikasi fault berdasarkan kategori-kategori fault yang berbeda.

### reference


Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. Kapila and Singh [85] used two statistical approaches to carry out his study: Logistic Regression and Univariate Binary Logistic Regression (UBR) which are useful for analysis of data with binary variables. Software prediction models are constructed using a variety of machine learning methods, such as Genetic Programming [78], Decision Trees [79], Neural Networks [80], Naive Bayes (NB) [21], Case-Based Reasoning [81], and Blurring Logic [82]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

---

## Sample 20

- conversation_id: 13
- user_chat_id: 519
- bot_chat_id: 520

### user_input

Apa itu machine learning?

### retrieved_context

1. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Deep Learning is designed to continually analyze data with a logic structure as mimicking how a human can draw a conclusion. The deep learning needs a huge number of data sets to use input in the algorithms in order to result in a more accurate prediction. For instance, Google's AlphaGo, a sharp intellect and intuition game, learns by itself without predefined data. It makes a more specific move and becomes the greatest player of all. Deep Learning defines a new paradigm based on data-driven programming. Since Machine Intelligence or Deep Learning depends on the training data, the accuracy and quality of data play a vital role for public safety using machine learning in autonomous vehicles. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

3. TABLE 1. Classification by articles.

Dalam penelitian ini, terdapat beberapa jenis teknik pembelajaran mesin (machine learning) yang digunakan dalam siklus hidup perangkat lunak. Berdasarkan analisis artikel-artikel yang dipilih, dapat dilihat bahwa sekitar 73% dari total artikel (193/263) menggunakan teknik supervised learning untuk mendeteksi kelemahan atau kesalahan dalam kode program.

Dalam supervised learning, model dibuat dengan melibatkan dataset yang telah terlabel. Model ini kemudian digunakan untuk mengklasifikasikan data baru menjadi kategori "Buggy" (kesalahan) atau "Correct" (benar). Sementara itu, sekitar 6% dari artikel-artikel tersebut menggunakan teknik unsupervised learning, di mana model dibuat tanpa melibatkan dataset yang telah terlabel.

Selain itu, juga ditemukan bahwa sekitar 2% dari total artikel (4/263) menggunakan teknik semi-supervised learning dan sekitar 0.4% menggunakan reinforcement learning, serta 17% menggunakan analytical learning. Pada umumnya, metode klasifikasi yang paling banyak digunakan adalah ANN (Artificial Neural Network), diikuti oleh RF (Random Forest), DT (Decision Tree), dan NB (Naïve Bayes).

Dari data ini dapat disimpulkan bahwa artikel-artikel tersebut berfokus pada penggunaan teknik pembelajaran mesin untuk mendeteksi kelemahan dalam kode program, serta perbandingan antara berbagai metode klasifikasi. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 8)

4. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

5. AI-based machine learning requires a huge number of inputs as the knowledge and different intelligent algorithms in order to make the right decision. By looking at an example using technology in unmanned vehicles, there will be a basic understanding of how machine learning or machine intelligence work. The development of machine intelligence is still far from mimicking the cognitive competence of the human brain. It is still challenging to deal with those data effectively and making a driving decision accurately and quickly [17]. Machine learning sometimes returns an inaccurate prediction based on the collection of training data and an engineer needs to make some adjustments to avoid significant losses in terms of public safety. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

6. TABLE 2. Electronic database.

Dalam penelitian ini, ditemukan beberapa pola penting dalam penggunaan teknik kecerdasan buatan (Artificial Intelligence) di bidang rekayasa perangkat lunak. Analisis yang dilakukan menunjukkan bahwa pembelajaran mesin (Machine Learning) adalah teknik AI yang paling umum digunakan.

Data menunjukkan bahwa ML telah digunakan secara luas dalam berbagai fase pengembangan perangkat lunak, termasuk fase analitik desain dan data persiapan. Hal ini menunjukkan bahwa ML dapat membantu mendukung aktivitas-aktivitas yang kompleks dan menghabiskan sumber daya.

Dalam fase pengujian, juga ditemukan bahwa ML digunakan secara luas untuk melakukan automasi tes perangkat lunak, sehingga membantu meningkatkan efisiensi dalam pengembangan perangkat lunak. Pada fase analitik desain dan data persiapan, ML juga menunjukkan kemampuan yang baik dalam mendukung aktivitas-aktivitas.

Dari analisis ini dapat disimpulkan bahwa AI telah menjadi bagian penting dalam rekayasa perangkat lunak modern. Penggunaan AI, terutama pembelajaran mesin, telah meningkatkan efisiensi dan produktivitas dalam pengembangan perangkat lunak. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 5)

7. By the type of ML, we mean how the models have been trained, i.e., supervised, semi-supervised, unsupervised, reinforcement, or analytical learning. Supervised learning is based on a training set and a test set taken from the dataset. The model training is done by taking multiple labeled samples from the train set. After the model is trained, its performance is evaluated using the test set. In semi-supervised learning, both labeled and unlabelled data are employed in order to train the model. The dataset is divided into unsupervised clusters as such. Then, the class information is obtained by learning the clustering outcomes [216]. Unsupervised learning requires no training dataset. For instance, in unsupervised learning for fault detection, software instances are usually grouped into clusters and each cluster is labeled as ''Buggy'' or ''Correct''. However, each cluster needs to be labeled manually by the individuals with expertise [198]. Reinforcement learning refers to unsupervised goal-oriented learning performed by an agent directly interacting with the environment. Analytical learning is aimed at generating solutions based on background knowledge and improving inference iteratively [253]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 8)

8. TABLE 13. Results: ML Algorithms on Case Studies (All Features).

Dalam analisis ini, kita melihat hasil dari beberapa algoritma pemodelan machine learning (ML) pada studi kasus yang berbeda dengan fitur lengkap. Terdapat delapan studi kasus yang dipilih untuk perbandingan, yaitu CS1, CS2, CS3, CS5, CS6, CS7, dan CS8. Model-model ML yang digunakan dalam analisis ini adalah Support Vector Regressor (SVR), Linear Regression, K-Nearest Neighbor (k-NN), XGBoost Regressor, dan Artificial Neural Network (ANN).

Dari hasil perbandingan, terlihat bahwa beberapa algoritma memberikan hasil yang lebih baik daripada yang lain. Misalnya, ANN dan SVR menghasilkan hasil yang paling baik dalam studi kasus CS1 dan CS7 masing-masing dengan PRED - ISBSG = 0.953 dan Case Studies = 0.03, serta MMR E - ISBSG = 1.28 dan Case Studies = 1.28.

Dalam analisis ini juga terlihat bahwa model yang lebih kompleks seperti ANN tidak selalu memberikan hasil yang lebih baik daripada model yang lebih sederhana. Misalnya, CS2 dengan satu aktor kompleks menghasilkan hasil yang kurang baik daripada CS3 dan CS4.

Dari analisis ini dapat disimpulkan bahwa pilihan algoritma ML sangat mempengaruhi akurasi hasil dalam perhitungan biaya efisiensi software. Dengan demikian, penelitian lebih lanjut diperlukan untuk menentukan kombinasi model yang optimal dan fitur-fitur yang relevan bagi setiap studi kasus. (Heterogeneous Ensemble Model to Optimize Software Effort Estimation Accuracy, page 22)

### response

Machine Learning adalah teknik pembelajaran mesin (machine learning) yang digunakan dalam pengembangan perangkat lunak untuk mendeteksi kelemahan atau kesalahan dalam kode program.

### reference


Dari data ini dapat disimpulkan bahwa artikel-artikel tersebut berfokus pada penggunaan teknik pembelajaran mesin untuk mendeteksi kelemahan dalam kode program, serta perbandingan antara berbagai metode klasifikasi. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 8) Berdasarkan analisis artikel-artikel yang dipilih, dapat dilihat bahwa sekitar 73% dari total artikel (193/263) menggunakan teknik supervised learning untuk mendeteksi kelemahan atau kesalahan dalam kode program. Dalam penelitian ini, terdapat beberapa jenis teknik pembelajaran mesin (machine learning) yang digunakan dalam siklus hidup perangkat lunak.
