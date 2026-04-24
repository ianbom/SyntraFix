# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 31

- conversation_id: 13
- user_chat_id: 557
- bot_chat_id: 558

### user_input

Mengapa software maintenance penting?

### retrieved_context

1. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

2. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

3. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

4. Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment. New threats are tracked during this phase. The software can never be 100 percent secure, and new threats emerge regularly phase [14]. As a result, efforts must be made to secure the software. The maintenance team should keep track of new threats that the system encounters to address them promptly and prevent security breaches [83], [116]. Table 15 presents prescriptive actions to increase security during the maintenance phase of SDLC [14], [65], [105], [114], [117], [118]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

5. According to a 2013 study by the University of Cambridge [17], [18], the global cost of finding and removing bugs from software has risen to $312 billion annually, and it makes up half of the development time of the average project. Furthermore, constant change makes matters worse. Changes are the main causes of software bugs and major issues faced by the software industry. Studies conducted by Javed et al. [1] indicated that there is a significant relationship between change requests and overall bugs. Based on Mozilla quality assurance process [19], the focus of the quality assurance is correcting bugs. Therefore, based on these studies, our Quality Assurance Subsystem is modeled and depicted in Figure 7. (Change-Oriented Open Source Software Process Simulation, page 1)

6. Software development and evolution is a dynamic process and is characterized by change. Software projects often begin with unclear, ambiguous, and incomplete requirements which give rise to intrinsic volatility [1]. Meanwhile, the project team members, software users, environment and technologies are also likely to change throughout the life of the project as different versions of their software are released. When these important factors change and affect the software products, projects, and processes, these changes must be carefully planned [2]. Especially, when additions, deletions and modifications are made to previous generated or in process project artifacts, additional time investment, scrapped effort, and even bugs can result. Therefore, it is important to understand the changing dynamics overtime, the complex interaction effects, and to find the way to control the negative effects of the changes. System dynamics (SD) modeling is one of the best techniques to enable project personnel to software process and model change effects and run the models to better understand the implications of candidate project strategies and decisions [3]. (Change-Oriented Open Source Software Process Simulation, page 1)

7. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

8. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

### response

Menurut konteks tersebut, software maintenance penting karena dapat membantu mengurangi biaya dan meningkatkan kualitas software. Biaya perawatan software setiap tahunnya telah meningkat menjadi $312 miliar secara global [17], [18]. Selain itu, software yang tidak dipelihara dengan baik dapat menyebabkan kerusakan pada software dan bahkan kehilangan ekonomi sebesar 1,1 triliun dolar pada tahun 2016 karena kesalahan software [38].

### reference


According to a 2013 study by the University of Cambridge [17], [18], the global cost of finding and removing bugs from software has risen to $312 billion annually, and it makes up half of the development time of the average project.

---

## Sample 32

- conversation_id: 13
- user_chat_id: 565
- bot_chat_id: 566

### user_input

Apa hubungan software maintenance dengan software engineering?

### retrieved_context

1. We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig. 3. 136 out of 263 (52%) articles belong to quality assurance and analytic. 44 out of 263 (17%) articles have focused on architecture and design. 29 out of 263 (11%) articles have addressed the implementation followed by requirements engineering stage with 24 out of 263 (9%) articles. 11 (4%) articles were focusing on the maintenance phase. The rest of the articles were not particularly focusing on any stage but were generally applicable to SE. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 5)

2. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

3. From SWEBOK ISO/IEC TR 1975:2015, we adopt the critical knowledge areas in software engineering to use as synonyms for software engineering. Twelve knowledge areas identified from the keywords were selected as most prevalent in the literature. These include software requirements, software design, software construction, software maintenance, software testing, software configuration management, software management, software process, software models and methods, and software quality. This is seen in similar SMSs in software engineering by other researchers Klotins et al. [40]. These formed the first part of the search string, the terminology software was then coined with the Boolean ''AND'' to the terminology identified from the keywords to synonymise engineering, and we used the Boolean OR as presented in Listing 1. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1)

4. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

5. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

6. A close look at the knowledge areas of software engineering used by the companies as reported in the selected articles indicates that general software development and project management are most prominent in the knowledge area frequency distribution, as presented in Figure 7.

The data detail specifically indicates the most covered knowledge area of software engineering by the articles selected in the study. Figure . 7, illustrates 3 most dominant knowledge areas presenting up to 46 studies identified on the knowledge areas of software development design and construction (33), project management ( 16), and quality (7). The remaining 31 studies covered the knowledge areas of process (5), models and methods (5), maintenance (4), testing (3), requirements (3) and management (1) with the respective number of studies. Although the knowledge areas that ultimately are observed at a point in time are presented decimally in the empirical literature, the initial 10 years show that these knowledge areas are not reflected in the empirical studies around this time. Figure 6(a) shows the studies in the years between 2016 and 2021 present interest in the knowledge area of quality, requirements, models and methods, and maintenance. Although the numbers are minimal, the growing interest of researchers is important for the industry and for the transformation of software development practice in SSCs. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 9)

7. The software engineering research will be defined by a more intensive interest in the meta-engineering problems, which include designing processes and systems that can guarantee successful collaboration of the agents and humans in the software creation, maintenance and evolution areas. It can be taken as a transition to the research priorities towards optimization not of single development tasks, but the optimization of the whole ecosystem of human-agent collaboration. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 20)

8. The study of human-computer interaction provides the necessary prerequisites to the creation of more efficient interfaces and cooperative frameworks between humans and autonomous agents, which will overcome the most crucial usability and acceptance issues that currently limit practical implementations. Another critical integration point of software engineering education is the requirement to systematically change the approach to pedagogical practices and curricula to prepare future developers to effectively work with AI-based tools and agents [50]. Additionally, the principles and methodologies existing in software engineering should be periodically updated and extended to control the conduct of agents and to guarantee quality in the AI-influenced development processes [3], [54], [55]. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 17)

### response

Software maintenance adalah salah satu tahapan dalam siklus hidup perangkat lunak yang terkait dengan software engineering. Pada konteks ini, software maintenance meliputi kegiatan seperti prediksi kemantapan perangkat lunak, deteksi penuaan perangkat lunak, dan perkiraan upaya pemeliharaan.

Berdasarkan [Source: A Literature Review of Using Machine Learning in Software Development Life Cycle Stages], software maintenance adalah salah satu tahapan yang kurang difokuskan oleh peneliti dalam domain ini. Namun, pada konteks ini juga disebutkan bahwa research lebih condong ke arah perkiraan biaya/effort daripada tugas pemeliharaan lainnya.

Selain itu, [Source: Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework] menyatakan bahwa knowledge area dalam software engineering yang terkait dengan software maintenance adalah salah satu dari 12 knowledge area yang paling berpengaruh.

### reference


These formed the first part of the search string, the terminology software was then coined with the Boolean ''AND'' to the terminology identified from the keywords to synonymise engineering, and we used the Boolean OR as presented in Listing 1. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1) Although the numbers are minimal, the growing interest of researchers is important for the industry and for the transformation of software development practice in SSCs. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 9) The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

---

## Sample 33

- conversation_id: 13
- user_chat_id: 567
- bot_chat_id: 568

### user_input

Bagaimana software metrics membantu proses software maintenance?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

4. We observed that the metrics strategy solutions were the most frequently used in identifying the architectural decay, thereby these metrics can determine the architectural instability growth with the system evolution, identify the probability of the classes contributing to architectural inconsistencies, and diagnose the anomalies, whether agglomerations or individual is more correlated to architectural problems. However, the use of current metrics at the class level may be affected by size bias significantly and inefficiency automatically in detecting architectural problems, indicating that the most likely cause is the problem on how these metrics are implemented through tools and reconsideration in specifying the selection of the appropriate metrics at different locations of software components, especially when compared to the same results that achieved efficiency manually. (Software Architecture Degradation in Open Source Software: A Systematic Literature Review, page 22)

5. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

6. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

7. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

8. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

### response

Menurut Konteks "A Literature Review of Using Machine Learning in Software Development Life Cycle Stages", software metrics membantu proses software maintenance dengan:

* Memprediksi ketersediaan perawatan untuk memperbaiki maintainability
* Mendeteksi kemungkinan kebocoran sumber daya, seperti kerusakan memori, penggunaan CPU yang tinggi, dan waktu lama
* Mengestimasikan upaya perawatan dengan menggunakan model regresi SVM

### reference


The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7) Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45].

---

## Sample 34

- conversation_id: 13
- user_chat_id: 569
- bot_chat_id: 570

### user_input

Mengapa software testing tetap penting saat software maintenance?

### retrieved_context

1. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

2. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

3. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

4. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

5. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

6. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

7. As time progresses and technology continues to develop, software has become an increasingly integral part of our daily lives. It is crucial that software functions correctly for endusers, making the assessment of software reliability a critical step in the testing phase. To accurately predict software reliability, various SRGMs have been proposed to describe the process of fault detection and correction [1], [2], [3]. It is important to note that there are still many SRGMs published in the literature. These models vary in terms of their underlying assumptions, mathematical formulations, and applicability to different types of software systems. (Using Modified Diffusion Models for Reliability Estimation of Open Source Software, page 3)

8. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

### response

Tidak ada jawaban langsung terkait pertanyaan user. Namun, dapat ditemukan beberapa fakta yang mendukung pentingnya software testing dalam konteks lain.

- Dalam sumber [Source: Error-Type—A Novel Set of Software Metrics for Software Fault Prediction], disebutkan bahwa software testing sangat penting karena memastikan kualitas dan akurasi sistem perangkat lunak. Namun, tidak ada jawaban langsung terkait pentingnya software testing dalam konteks pemeliharaan.
- Dalam sumber [Source: Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review], disebutkan bahwa agen otomatis saat ini menangani tugas pemeliharaan perangkat lunak yang dulunya memerlukan banyak waktu dan keahlian manusia. Namun, tidak ada jawaban langsung terkait pentingnya software testing dalam konteks pemeliharaan.

Jawaban: Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1) Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13) It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

---

## Sample 35

- conversation_id: 13
- user_chat_id: 571
- bot_chat_id: 572

### user_input

Bagaimana software development yang buruk dapat menyulitkan software maintenance?

### retrieved_context

1. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

2. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

3. Vulnerability-oriented architectural research provides a systematic and thorough approach to evaluating a wide variety of possible vulnerabilities, but it is time-consuming and costly [91]. For estimating the severity and cost of security threats, Table 9 presents, some maintenance and stakeholder considerations may be considered [78], [91], [103].

Software development iterations are of limited time, often few weeks, which makes fitting security activities (e.g., security requirement elicitation) challenging because they are often time-consuming'' [65]. Furthermore, defining security policies takes time and raises the cost of software development [65]. Some of the common issues due to

TABLE 11. (Continued.) Secure design practices (SDP).

time pressure in the secure software development process are [65], [83],

i. Organizations compromise security activities to accommodate the accelerated releasing schedule ii. Timing attacks iii. Insufficient time for the teams to get to the security activities iv. pressure to deliver to tight deadlines. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

4. Software development and evolution is a dynamic process and is characterized by change. Software projects often begin with unclear, ambiguous, and incomplete requirements which give rise to intrinsic volatility [1]. Meanwhile, the project team members, software users, environment and technologies are also likely to change throughout the life of the project as different versions of their software are released. When these important factors change and affect the software products, projects, and processes, these changes must be carefully planned [2]. Especially, when additions, deletions and modifications are made to previous generated or in process project artifacts, additional time investment, scrapped effort, and even bugs can result. Therefore, it is important to understand the changing dynamics overtime, the complex interaction effects, and to find the way to control the negative effects of the changes. System dynamics (SD) modeling is one of the best techniques to enable project personnel to software process and model change effects and run the models to better understand the implications of candidate project strategies and decisions [3]. (Change-Oriented Open Source Software Process Simulation, page 1)

5. SA degrades as the system evolves [26]. Interestingly, the eroded architecture impulses the system to complexity, difficulty, and frequent changes than before [27]. The repeated architectural decay leads to a shortening lifetime of the system or rather affects the architecture entirely, resulting in redesigning the architecture of the system from scratch [28]. As a consequence, the SA of system erode over time. This phenomenon is known as architectural degeneration [23], [29], design erosion [30], architectural erosion [11], [23], [31], drift [15], [23], [32], mismatch [33], architectural decay [34], design decay [35], code decay [12], [27], software entropy [36], architecture erosion (or decay) [37], software architecture degradation [9], [15], [38] or software aging [11]. (Software Architecture Degradation in Open Source Software: A Systematic Literature Review, page 3)

6. According to a 2013 study by the University of Cambridge [17], [18], the global cost of finding and removing bugs from software has risen to $312 billion annually, and it makes up half of the development time of the average project. Furthermore, constant change makes matters worse. Changes are the main causes of software bugs and major issues faced by the software industry. Studies conducted by Javed et al. [1] indicated that there is a significant relationship between change requests and overall bugs. Based on Mozilla quality assurance process [19], the focus of the quality assurance is correcting bugs. Therefore, based on these studies, our Quality Assurance Subsystem is modeled and depicted in Figure 7. (Change-Oriented Open Source Software Process Simulation, page 1)

7. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

8. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

### response

Software development yang buruk dapat menyulitkan software maintenance karena:

• Menghasilkan software dengan kualitas rendah, sehingga memerlukan biaya besar untuk perbaikan dan pemeliharaan.
• Meningkatkan kemungkinan terjadinya kerusakan software, yang dapat menyebabkan kerugian ekonomi yang signifikan. Contohnya, dunia ekonomi telah kehilangan 1,1 triliun dolar pada tahun 2016 karena kerusakan software.
• Membutuhkan waktu dan biaya besar untuk perbaikan dan pemeliharaan software.
• Meningkatkan kompleksitas sistem software, sehingga sulit untuk diubah atau diperbarui.

Sumber: [Source: How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success], [Source: Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction], dan [Source: Systematic Literature Review on Security Risks and its Practices in Secure Software Development]

### reference


A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2) It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1) Insufficient time for the teams to get to the security activities iv. pressure to deliver to tight deadlines. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)
