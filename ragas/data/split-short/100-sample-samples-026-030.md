# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 26

- conversation_id: 14
- user_chat_id: 722
- bot_chat_id: 723

### user_input

Apa hubungan software development dan software testing?

### retrieved_context

1. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

2. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

3. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

4. Testing is a comprehensive concept related to the development of each system. In the software engineering discipline, testing is a crucial task of the software development life cycle. In contrast, software testing in any field other than software engineering can be considered as an end-user testing focused on the suitability of a software developed for a specific purpose in this field. For this reason, the multidisciplinary use of software testing makes it difficult to create a specific corpus of software testing studies in the scope of software engineering. In this context, to create a specific corpus of software testing within the scope of software engineering, a methodology including two sequential stages was followed for corpus creation, which included identifying core publication sources for the software engineering field and extracting articles specific to software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

5. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

6. Barmi et al. conducted a systematic review to better understand the connections between the specifications and testing requirements and reported that ''Model-based testing'' was the most commonly studied topic (26%), followed by ''Formal Approaches'' (24%), and ''Traceability'' (18%) and concluded that there was a significant gap between the specification and testing requirements [31]. Their study is considering the relationship between the specifications and testing requirements, not the whole process of software testing. In this context, Garousi and Mäntylä reported that over 101 secondary research studies (as a study of studies) had been published in the area of software testing since 1994, with model-based software testing being the most popular method, web-services the most popular system, and regression testing the most popular testing phase [32]. Since this was a ternary study, it has limitations in showing the whole picture of the software testing studies. Zein et al. performed a systematic mapping study in order to reveal testing techniques for mobile application and mapped 79 empirical studies to a taxonomy [33]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

7. The testing phase of the SDLC aims to make sure that all the system components provide their required functionality alone and as part of the whole system. Software testing is the most time-consuming, complicated, and costly process of the SDLC [92]. This phase is an important component of improving the efficiency of software development projects [32]. While it is an essential part of software development, rigorous testing is not always a focus of software engineering education [93]. As a result of this shortcoming, software developers often regard software testing as a liability, lowering overall software quality. Threat modeling is a systematic method for identifying threats that may compromise security, and it is considered a well-known accepted practice by the software testing industry [94]. This phase aims to find possible bugs and errors in the system and remove them. The present study identified 64 papers to discuss software security risks during software testing phase of SDLC. Some common security risks involved in this phase are as follows [5], [22], [95]- [98]: (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 11)

8. Test planning is the first step in the testing phase. The testing team begins planning tests during the implementation phase because test planning does not necessitate access to

TABLE 4. (Continued.) CSSRs and its practices in the secure coding phase of the secure SDLC.

program code. While the developers are working on code, the testing team prepares for the testing activity later. The security testing teams develop test cases based on design papers, threat models, and misuse situations. Security test cases aim to attack software successfully. Any modification to the software design must be disclosed to the testing team during the planning phase of the test. As a result, the testing team may create test cases that aren't relevant. Based on the nature of the software and its threats, the severity of bugs is adjusted. A minor bug in software code that isn't very important to how it works may only take a few minutes to fix, but it can significantly affect how secure it is. A discussion of the revised severities takes place with the development team. Table 5 shows the security operations conducted during the testing phase [3], [17], [80], [84]- [86]. (Security Assurance Model of Software Development for Global Software Development Vendors, page 1)

### response

Software development dan software testing memiliki hubungan yang sangat erat, karena testing adalah bagian integral dari proses pengembangan perangkat lunak. Menurut konteks, "software testing is a major task of the software development process" (ISO/IEC 24765, 2006) [6] dan juga merupakan "phase of the SDLC" yang sangat penting untuk memastikan bahwa sistem komponen memberikan fungsi yang dibutuhkan sendiri dan sebagai bagian dari sistem keseluruhan.

### reference


Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6].

Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process.

An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18].

Testing is a comprehensive concept related to the development of each system. In the software engineering discipline, testing is a crucial task of the software development life cycle.

Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process.

Barmi et al. conducted a systematic review to better understand the connections between the specifications and testing requirements and reported that ''Model-based testing'' was the most commonly studied topic (26%), followed by ''Formal Approaches'' (24%), and ''Traceability'' (18%) and concluded that there was a significant gap between the specification and testing requirements [31].

The testing phase of the SDLC aims to make sure that all the system components provide their required functionality alone and as part of the whole system. Software testing is the most time-consuming, complicated, and costly process of the SDLC [92].

Test planning is the first step in the testing phase. The testing team begins planning tests during the implementation phase because test planning does not necessitate access to TABLE 4. (Continued.) CSSRs and its practices in the secure coding phase of the secure SDLC. program code.

---

## Sample 27

- conversation_id: 14
- user_chat_id: 724
- bot_chat_id: 725

### user_input

Bagaimana software quality mempengaruhi software development?

### retrieved_context

1. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

2. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

3. The quality of software continues to be a significant challenge in the software industry, and this challenge is more visible in the Small Software Companies (SSCs) to the extent that up to 70 percent of software projects are challenged either due to defects, cost overruns or overshot scheduling related challenges [1]. Although the products produced by the SSCs fail to meet the expected quality, software is still central in influencing human activity. Recent studies indicate that most aspects of society depend on software; moreover, SSCs are responsible for up to 80 percent of software produced on the market. The contribution of SSCs cannot be underestimated since they represent up to 90 percent of software companies in the industry [2]. (Theory on Non-Technical Characteristics Affecting Process Adoption in Small Software Companies: A Grounded Theory Study, page 1)

4. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

5. TABLE 5. Total effects.

Analisis menunjukkan bahwa kualitas perangkat lunak (software quality) memiliki dampak yang paling besar pada kesuksesan perusahaan software terbuka komersial (COSS). Dalam jaringan, nilai total efeknya adalah 0,554, yang menunjukkan bahwa kualitas perangkat lunak sangat berpengaruh. Sebaliknya, modal intelektual (intellectual capital) memiliki dampak kecil, dengan nilai total efek yang relatif rendah.

Sementara itu, modal struktural dan modal hubungan memiliki dampak sedang, tetapi lebih kuat daripada modal manusia dalam beberapa hal. Dalam jaringan, modal struktur menunjukkan pengaruh yang cukup besar pada kualitas perangkat lunak dan modal manusia. Modal hubungan memiliki pengaruh yang lebih kecil.

Insight ini sangat relevan untuk organisasi COSS karena menunjukkan bahwa fokus utama dalam meningkatkan kesuksesan haruslah pada kualitas perangkat lunak. Oleh karena itu, penting bagi manajemen untuk memprioritaskan investasi dan sumber daya yang lebih besar dalam meningkatkan teknologi dan kualitas produk software mereka.

Dalam mengevaluasi model ini, hasil dari prosedur blindefolding (Q2) menunjukkan bahwa model memiliki relevansi prediktif tinggi. Selain itu, evaluasi power prediksi menggunakan PLS-predict menunjukkan bahwa model dapat memberikan prediksi yang lebih akurat daripada model regresi linear biasa. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 8)

6. TABLE 4. Path coefficients.

Analisis terbaru mengenai komponen kualitas perangkat lunak (software quality) dalam menengahi dampak modal intelektual (intellectual capital) pada kesuksesan perusahaan swasta open-source software (COSS) telah membawa beberapa temuan penting. Data yang dianalisis menunjukkan bahwa ada hubungan positif signifikan antara kualitas perangkat lunak dan kesuksesan COSS (β = 0,581, T-value = 10,842, P-value = 0,000). Sebenarnya, kualitas perangkat lunak memainkan peran mediasi yang signifikan dalam menengahi hubungan antara modal intelektual dan kesuksesan COSS.

Penelitian ini juga menemukan bahwa ada hubungan positif antara kapital struktural (structural capital) dan kualitas perangkat lunak, serta antara kapital manusia (human capital) dan kualitas perangkat lunak. Dalam beberapa kasus, mediasi efektif kapital manusia pada relasi tersebut terbukti signifikan.

Kemudian, hasil analisis menunjukkan bahwa kualitas perangkat lunak merupakan faktor yang sangat penting dalam mempengaruhi kesuksesan COSS. Dengan demikian, penelitian ini mendukung asumsi-asumsi yang telah diusulkan (H1-H11) mengenai hubungan antara modal intelektual dan kualitas perangkat lunak terhadap kesuksesan COSS.

Dari hasil analisis, dapat disimpulkan bahwa kualitas perangkat lunak merupakan faktor penting dalam menengahi dampak kapital manusia terhadap kesuksesan COSS. Hasil ini dapat dijadikan sebagai rujukan bagi pihak manajemen dan strategis dalam mengembangkan kebijakan yang lebih efektif untuk meningkatkan kinerja perusahaan open-source software mereka. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 7)

7. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

8. Quality is the most important factor for software development as it mainly defines customer satisfaction that is directly related to the success of a software project. The software process model is used to ensure software quality, represent a variety of task settings, manage project duration, improve the process and range to execute the process understanding, and to appropriate implicit conjecture for all task settings. Several software processes models exist in software albeit with limited scope. Given this viewpoint, this paper presents a new software development life cycle model, ''AZ-Model,'' for software development by introducing new activities during software development life cycle. It overcomes the limitations of traditional models and significantly impacts the production of a quality product in a time-box. This paper also presents a comprehensive comparative study and statistical analyses to examine the significance of AZ-Model for software development. INDEX TERMS Software development model (SDM), project management (PM), AZ-Model, software development life cycle (SDLC), six pointed star model, project management factors. (Improving the Quality of Software Development Process by Introducing a New Methodology–AZ-Model, page 1)

### response

Software quality sangat berpengaruh pada kesuksesan perusahaan software terbuka komersial (COSS). Menurut analisis yang dilakukan, nilai total efeknya adalah 0,554, yang menunjukkan bahwa kualitas perangkat lunak sangat berpengaruh. Dengan demikian, fokus utama dalam meningkatkan kesuksesan haruslah pada kualitas perangkat lunak.

Selain itu, kualitas perangkat lunak juga merupakan faktor yang penting dalam mempengaruhi kesuksesan COSS. Dalam mengevaluasi model ini, hasil dari prosedur blindefolding (Q2) menunjukkan bahwa model memiliki relevansi prediktif tinggi. Selain itu, evaluasi power prediksi menggunakan PLS-predict menunjukkan bahwa model dapat memberikan prediksi yang lebih akurat daripada model regresi linear biasa.

Dalam konteks software development, kualitas perangkat lunak sangat penting dalam mempengaruhi kesuksesan proyek. Menurut penelitian ini, ada hubungan positif signifikan antara kualitas perangkat lunak dan kesuksesan COSS (β = 0,581, T-value = 10,842, P-value = 0,000). Sebenarnya, kualitas perangkat lunak memainkan peran mediasi yang signifikan dalam menengahi hubungan antara modal intelektual dan kesuksesan COSS.

Dalam beberapa kasus, mediasi efektif kapital manusia pada relasi tersebut terbukti signifikan. Dengan demikian, penelitian ini mendukung asumsi-asumsi yang telah diusulkan (H1-H11) mengenai hubungan antara modal intelektual dan kualitas perangkat lunak terhadap kesuksesan COSS.

Dalam kesimpulan, software quality sangat berpengaruh pada kesuksesan perusahaan software terbuka komersial (COSS). Dengan demikian, fokus utama dalam meningkatkan kesuksesan haruslah pada kualitas perangkat lunak.

### reference


In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41].

Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38].

The quality of software continues to be a significant challenge in the software industry, and this challenge is more visible in the Small Software Companies (SSCs) to the extent that up to 70 percent of software projects are challenged either due to defects, cost overruns or overshot scheduling related challenges [1].

In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976.

TABLE 5. Total effects.

TABLE 4. Path coefficients.

Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9].

Quality is the most important factor for software development as it mainly defines customer satisfaction that is directly related to the success of a software project.

---

## Sample 28

- conversation_id: 14
- user_chat_id: 726
- bot_chat_id: 727

### user_input

Bagaimana software metrics digunakan dalam software development?

### retrieved_context

1. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

3. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

4. Most software organizations initiate measurement programs (MPs) as pilot projects to plan and establish their measurement processes [5], [26]. The aim of MPs is to evaluate the measurement processes for their benefits and improvements in software processes and products [4], [5], [26]. However, sustaining the MPs organization-wide for all/ multiple projects and gauging their actual impact to characterize, evaluate, improve and predict software processes, products and resources remain challenging [4], [5], [26]. Moreover, there are many organizations which implicitly use the data generated through their software processes (e.g., source lines of code, function points, number of defects, number of defects fixed, time spent on specification/design/code/test etc.) for project management purposes even though they do not have a defined measurement process. Unterkalmsteiner et al. [4] and Tahir et al. [5] reported that the majority of MP studies lack the description of context in which they were conducted. The context description includes organizational context (e.g., size of organization, measurement scope, and project/organization level of measurement), stakeholders of measurement datasets, measurement process details (e.g., metrics collection and analysis methods, business goals, measurement goals, source/timestamp of measurement, and artifacts used for measurement). Due to lack of these details, it is very difficult to generalize the state measurement practices in the software industry. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 1)

5. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

6. In SLR [5], lack of real-time metrics (e.g., cyclomatic complexity, dynamic function calls, no of unused objects and variables) to monitor and control the actual software development progress is observed to be least discussed. A survey in Finish software industry specifically reported lack of realtime metrics used during software development process. In this survey, we realized that 89% of organizations don't use real-time metrics as shown in Figure 18. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 1)

7. Object-oriented metrics are used to predict the quality of object-oriented software. The attributes that determine software quality include maintainability, fault tolerance, understandability, fault density, standardized rework rate, reusability, etc. Several studies were carried out, including the empirical verification of the object-oriented metrics in open source software for the prediction of faults using CBO, LOC, LCOM, NOC and DIT [10], reuse analysis of objectoriented systems using metrics of inheritance, coupling and cohesion [92], heuristic review of CK metrics [93], reusable metrics for object-oriented design [94] and empirical analysis of CK metrics for object-oriented design complexity [95]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 5)

8. TABLE 5. Mitigation strategies for key issues found in the survey.

Pada penelitian ini, ditemukan bahwa sebagian besar perusahaan di industri software Pakistan tidak menggunakan metrik waktu nyata untuk mengukur dan mengontrol proses pengembangan perangkat lunak mereka. Hanya 11% saja dari perusahaan yang menggunakan metrik waktu nyata seperti cyclomatic complexity, dynamic function calls, jumlah obyek dan variabel yang tidak digunakan.

Kebanyakan perusahaan juga tidak memiliki kamus ukuran yang komprehensif. Dari total 57 responden, hanya 38% saja yang memiliki kamus ukuran lengkap, sementara 19% menggunakan kamus ukuran secara parsial dan 16% tidak menggunakan kamus ukuran sama sekali.

Dalam hal penggunaan data historis untuk prediksi, kurang dari 50% perusahaan yang diwawancarai mengaku sering menggunakan data historis tersebut. Bahkan sekitar 58% perusahaan di industri software Pakistan tidak memiliki kriteria validasi metrik sama sekali.

Selain itu, penelitian ini juga menemukan bahwa model keberhasilan implementasi proses pengukuran berbasis MP dapat dibangun dengan analisis SLR. Dalam model tersebut, ada tiga faktor utama yang mempengaruhi sukses atau tidaknya implementasi proses pengukuran: faktor eksternal, adaptasi ukuran, dan penerimaan ukuran.

Model ini kemudian diperkuat dengan hasil analisis statistik multivariat terhadap respons 200 profesional perangkat lunak. Hasil analisis menunjukkan bahwa model keberhasilan implementasi proses pengukuran berbasis MP memiliki faktor-faktor yang signifikan dan dapat membantu meningkatkan efisiensi proses pengembangan perangkat lunak. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 16)

### response

Software metrics digunakan untuk mengukur dan mengontrol proses pengembangan perangkat lunak. Metrics tersebut dapat berupa metrik waktu nyata seperti cyclomatic complexity, dynamic function calls, jumlah obyek dan variabel yang tidak digunakan. Selain itu, software metrics juga digunakan untuk memvalidasi efektifitas proses pengembangan perangkat lunak dengan menggunakan pengukuran-pengukuran seperti fungsi titik analisis dan kompleksitas siklus cyclomatic.

Pada dasarnya, software metrics digunakan sebagai alat untuk meningkatkan efisiensi proses pengembangan perangkat lunak. Dengan demikian, penggunaan software metrics dapat membantu meningkatkan kualitas perangkat lunak yang dikembangkan dan mempercepat waktu pengembangannya.

### reference


Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification.

Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency.

Most software organizations initiate measurement programs (MPs) as pilot projects to plan and establish their measurement processes [5], [26]. The aim of MPs is to evaluate the measurement processes for their benefits and improvements in software processes and products [4], [5], [26].

The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6].

In SLR [5], lack of real-time metrics (e.g., cyclomatic complexity, dynamic function calls, no of unused objects and variables) to monitor and control the actual software development progress is observed to be least discussed. A survey in Finish software industry specifically reported lack of realtime metrics used during software development process.

Object-oriented metrics are used to predict the quality of object-oriented software. The attributes that determine software quality include maintainability, fault tolerance, understandability, fault density, standardized rework rate, reusability, etc.

TABLE 5. Mitigation strategies for key issues found in the survey.

---

## Sample 29

- conversation_id: 14
- user_chat_id: 730
- bot_chat_id: 731

### user_input

Bagaimana machine learning diterapkan dalam software development?

### retrieved_context

1. Many types of research in the past have applied ML to software architecture and design. The applications include design models, which are comprised of recommendation models for software processes/services. Apart from this, model smells and refactoring techniques of object-oriented structures using ML have also been proposed in the articles. White et al. [26] introduced DL to software language modeling based on information retrieval models. Design pattern prediction primarily focuses on recognizing design patterns in software through source code or user interface layout using ML techniques. For example, Nguyen et al. [27] proposed an approach known as DeepUI in order to semi-automate the design tasks by learning from previous UI design patterns. Development effort estimation refers to estimating effort for the development of software projects using ML techniques. Ionescu [28] used ANN to automate effort estimation by learning from textual features of project tasks. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 6)

2. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

3. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

4. Some studies, e.g., [8], [10]- [12], have already analyzed the application of ML in SE in the past. Durelli et al. [8] conducts a systematic mapping study on the application of ML for software testing. The study highlights the use of ML techniques in various software testing activities such as testcase generation and oracle construction. Results of the study show that a vast majority of articles employ supervised learning, such as ANN and DT, to solve testing-related problems. Moreover, the key advantages and disadvantages of using ML for software testing are discussed. Mainly, the advantage of ML techniques is their scalability and efficient application to large-scale and complex software systems. The disadvantage, on the other hand, is the unavailability of data that fits well with the learning process. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

5. The conclusion of the study is manifold. We have provided an overview of the state-of-the-art in the area of machine learning for software engineering by evaluating carefully selected studies. We also proposed a classification scheme that highlights the overall applications of machine learning for software engineering in terms of SDLC stages. The classification shows the primary focus of researchers towards specific stages. This observation is one of the major contributions of this study. This study also reveals that the quality of primary studies in the domain of ML and SE is evidence-based with respect to the techniques being empirically evaluated by the researchers. We have also shown the relationship of SDLC stages with ML types, tools, and techniques. Although this research area is showing moderate growth in terms of the number of publications, further primary studies need to be conducted to emphasize other lesser explored SDLC stages such as maintenance. The challenges, limitations and future directions reported in this article should motivate and further guide researchers in the future. We believe this study provides the necessary impetus and further motivation to explore those SDLC stages, which have been given lesser attention to date with respect to the application of ML. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 18)

6. ML has been widely used to facilitate the software requirements stage. For instance, in requirements modeling and analysis, articles focused on distinguishing ambiguous requirements [21], resolving incompleteness, the correctness of requirements [22], etc. Requirements selection/prioritization/classification deals with articles proposing ML techniques that emphasize on automating prioritization of requirements or their classification. Perini et al. [23] employed an ML technique to generate approximate rank in order to prioritize requirements. Navarro-Almanza et al. [24] used a convolutional neural network (CNN) to classify functional requirements by analyzing textual features. We further found articles focusing on requirements traceability. Requirements traceability refers to the ML approaches that assist in linking requirements to code or other artifacts as shown by Guo et al. [25], who used deep learning (DL) techniques in order to generate a trace link of requirements with other artifacts. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 6)

7. TABLE 3. (Continued.) Articles by ML techniques.

Dalam penelitian ini, beberapa teknik Machine Learning (ML) digunakan dalam berbagai tahapan siklus pengembangan perangkat lunak. Hasil survei menunjukkan bahwa metode klasifikasi paling banyak digunakan dalam proses analisis data. Dari 10 artikel yang dianalisis, terdapat empat artikel yang menggunakan teknik klasifikasi untuk memprediksi perilaku pengguna dan kinerja sistem.

Satu artikel lainnya menggunakan teknik rekomendasi untuk memberikan saran kepada pengembang perangkat lunak dalam memilih teknologi yang sesuai. Dari analisis ini, dapat disimpulkan bahwa peneliti menggunakan berbagai jenis ML untuk meningkatkan efisiensi dan kualitas dalam proses pengembangan perangkat lunak.

Namun demikian, terdapat beberapa kelemahan dalam penelitian ini. Salah satu masalahnya adalah kompleksitas data yang digunakan sebagai input untuk model ML. Hal ini menyebabkan kesulitan dalam mendapatkan hasil akurasi yang tinggi. Oleh karena itu, diperlukan perhatian lebih dalam hal pengumpulan dan proses pengolahan data.

Dalam penelitian ini, analisis kualitas juga menjadi perhatian utama. Dua artikel di antaranya menggunakan teknik klasifikasi untuk menganalisis perilaku pengguna dan memberikan rekomendasi kepada pengembang perangkat lunak. Dari hasil survei yang dilakukan, dapat disimpulkan bahwa peneliti menggunakan berbagai jenis ML dalam proses pengembangan perangkat lunak.

Masalah lainnya adalah adanya kekurangan data yang memadai untuk digunakan sebagai input model ML. Hal ini menyebabkan sulitnya mendapatkan hasil akurasi yang tinggi. Oleh karena itu, diperlukan perhatian lebih dalam hal pengumpulan dan proses pengolahan data.

Selain itu, juga ditemukan bahwa peneliti menggunakan teknik rekomendasi untuk memberikan saran kepada pengembang perangkat lunak dalam memilih teknologi yang sesuai. Dari analisis ini dapat disimpulkan bahwa penelitian tersebut berfokus pada penerapan ML dalam meningkatkan efisiensi dan kualitas proses pengembangan perangkat lunak.

Dalam keseluruhan, hasil survei menunjukkan bahwa peneliti menggunakan beberapa jenis teknik ML untuk memenuhi kebutuhan pengembangan perangkat lunak. Namun demikian, masih terdapat kelemahan dalam penelitian ini yang perlu diperhatikan dan ditangani dengan lebih baik di masa depan. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 17)

8. The software engineering community is rapidly adopting machine learning for transitioning modern-day software towards highly intelligent and self-learning systems. However, the software engineering community is still discovering new ways how machine learning can offer help for various software development life cycle stages. In this article, we present a study on the use of machine learning across various software development life cycle stages. The overall aim of this article is to investigate the relationship between software development life cycle stages, and machine learning tools, techniques, and types. We attempt a holistic investigation in part to answer the question of whether machine learning favors certain stages and/or certain techniques. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

### response

Machine learning digunakan dalam berbagai tahapan siklus pengembangan perangkat lunak, seperti analisis data, pemrediksi perilaku pengguna, kinerja sistem, dan memberikan saran kepada pengembang perangkat lunak. Beberapa teknik machine learning yang digunakan adalah klasifikasi, rekomendasi, dan pengolahan data.

Dalam beberapa penelitian, machine learning digunakan untuk:

* Memprediksi perilaku pengguna
* Mengklasifikasikan perilaku pengguna
* Memberikan saran kepada pengembang perangkat lunak dalam memilih teknologi yang sesuai
* Menganalisis kinerja sistem
* Meningkatkan efisiensi dan kualitas proses pengembangan perangkat lunak

Namun, masih terdapat kelemahan dalam penelitian ini, seperti kompleksitas data yang digunakan sebagai input untuk model machine learning dan adanya kekurangan data yang memadai.

### reference


Many types of research in the past have applied ML to software architecture and design. The applications include design models, which are comprised of recommendation models for software processes/services.

The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations.

Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases.

Some studies, e.g., [8], [10]- [12], have already analyzed the application of ML in SE in the past. Durelli et al. [8] conducts a systematic mapping study on the application of ML for software testing.

The conclusion of the study is manifold. We have provided an overview of the state-of-the-art in the area of machine learning for software engineering by evaluating carefully selected studies.

ML has been widely used to facilitate the software requirements stage. For instance, in requirements modeling and analysis, articles focused on distinguishing ambiguous requirements [21], resolving incompleteness, the correctness of requirements [22], etc.

TABLE 3. (Continued.) Articles by ML techniques. Dalam penelitian ini, beberapa teknik Machine Learning (ML) digunakan dalam berbagai tahapan siklus pengembangan perangkat lunak.

The software engineering community is rapidly adopting machine learning for transitioning modern-day software towards highly intelligent and self-learning systems. However, the software engineering community is still discovering new ways how machine learning can offer help for various software development life cycle stages.

---

## Sample 30

- conversation_id: 14
- user_chat_id: 732
- bot_chat_id: 733

### user_input

Apa itu software maintenance?

### retrieved_context

1. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

2. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

3. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

4. We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig. 3. 136 out of 263 (52%) articles belong to quality assurance and analytic. 44 out of 263 (17%) articles have focused on architecture and design. 29 out of 263 (11%) articles have addressed the implementation followed by requirements engineering stage with 24 out of 263 (9%) articles. 11 (4%) articles were focusing on the maintenance phase. The rest of the articles were not particularly focusing on any stage but were generally applicable to SE. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 5)

5. Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment. New threats are tracked during this phase. The software can never be 100 percent secure, and new threats emerge regularly phase [14]. As a result, efforts must be made to secure the software. The maintenance team should keep track of new threats that the system encounters to address them promptly and prevent security breaches [83], [116]. Table 15 presents prescriptive actions to increase security during the maintenance phase of SDLC [14], [65], [105], [114], [117], [118]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

6. Software Project Management (SPM) includes a set of activities to deliver a software product and related artifacts (e.g., source code, models, test case, and documentation) to accomplish specific goals while satisfying a set of constraints [1]. A widely used model of SPM constraints, suggested in the Project Management Body of Knowledge (PMBOK), is known as the triple constraint that include cost, time, and scope. In the software industry, it is common to classify projects that satisfy the triple constraint as successful [2]. (Team Formation in Software Engineering: A Systematic Mapping Study, page 1)

7. Software Project Management (SPM) includes a set of activities to deliver a software product and related artifacts (e.g., source code, models, test case, and documentation) to accomplish specific goals while satisfying a set of constraints [1]. A widely used model of SPM constraints, suggested in the Project Management Body of Knowledge (PMBOK), is known as the triple constraint that include cost, time, and scope. In the software industry, it is common to classify projects that satisfy the triple constraint as successful [2]. (Team Formation in Software Engineering: A Systematic Mapping Study, page 1)

8. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

### response

Software maintenance adalah tahap di mana pengguna atau pengembang menemukan masalah dan mungkin memperbaikinya sebelum rilis berikutnya, tergantung pada seriusitasnya.

### reference


The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is.

Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents.

The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks.

We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig.

Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment.

Software Project Management (SPM) includes a set of activities to deliver a software product and related artifacts (e.g., source code, models, test case, and documentation) to accomplish specific goals while satisfying a set of constraints [1]. A widely used model of SPM constraints, suggested in the Project Management Body of Knowledge (PMBOK), is known as the triple constraint that include cost, time, and scope.

Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38].
