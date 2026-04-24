# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 6

- conversation_id: 13
- user_chat_id: 491
- bot_chat_id: 492

### user_input

Mengapa software engineering dibutuhkan untuk software maintenance?

### retrieved_context

1. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

2. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

3. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

4. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

5. We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig. 3. 136 out of 263 (52%) articles belong to quality assurance and analytic. 44 out of 263 (17%) articles have focused on architecture and design. 29 out of 263 (11%) articles have addressed the implementation followed by requirements engineering stage with 24 out of 263 (9%) articles. 11 (4%) articles were focusing on the maintenance phase. The rest of the articles were not particularly focusing on any stage but were generally applicable to SE. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 5)

6. As software products become pervasive in all areas of society, the productive building of high-quality software has become crucial to the software industry. The rise of artificial intelligence (AI) applications is potentially a game-changer in improving Software Engineering (SE) phases to ensure higher-quality software, accelerate productivity, and increase project success rates. AI has the capability to assist software teams in many aspects, from automating certain activities in an SE phase to providing project analytics and actionable recommendations, and even making decisions [1]. AI techniques can support software engineers by detecting parts of the SE phases that are more likely to contain vulnerabilities and raising alerts about these issues. Such techniques can help to prioritize efforts and optimize inspection and testing costs. They (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 1)

7. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

8. Software engineering is a discipline that is concerned with various phases of software production from the preliminary requirement gathering stage through to maintenance of the software system. It is therefore concluded that software engineering is a discipline that leads to a systematic approach where cost effective software development is performed. Regardless of the speedy progress, the software industry is well thought-out by several to be in a crisis. At that time the average software projects exceed the schedule by half. Similarly, large number of projects were either not functioning as expected or were not used at all. There are numerous other challenges, industry needs to deal with, if it continued to step forward for much more mature engineering discipline. Varying situational contexts among team members are one of the many challenges that can lead to failure software if left unattended. Software engineering standards significantly acknowledge the importance of situational contexts. In this study we have investigated the IEEE standards association for the relevant standards. We found 32 most relevant stanafter performing filtration on the data set. We concluded that these software engineering standards significantly acknowledge towards consideration of situational contexts for successful software. Each standard is investigated for the various factors and sub-factors that can lead to varying situational contexts among software engineering team members. Based upon the analysis, we came across a pattern in the identified standards. We reported 8 categories under which these standards are grouped. Each of the standard reports the factors and sub-factors related to its category. The identified factors are 12 in number. Each of them is further grouped with the related sub-factors (52 in number) that ultimately can lead to failure software if not addressed properly. This study provides a guideline for the practitioners to consider these factors and sub-factors while performing software development in order to have a successful software development. (Software Standards and Software Failures: A Review With the Perspective of Varying Situational Contexts, page 11)

### response

Informasi tentang mengapa software engineering dibutuhkan untuk software maintenance tidak ditemukan pada dokumen yang tersedia.

### reference


Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these ma

---

## Sample 7

- conversation_id: 13
- user_chat_id: 493
- bot_chat_id: 494

### user_input

Bagaimana software engineering membantu mengurangi kesalahan dalam software testing?

### retrieved_context

1. Object-oriented metrics have been empirically validated to predict design flaws. Large and complex software systems are usually faulty [11]. It is difficult to keep them away from faults or to decrease risk of faults in upcoming version. According to [75], focus of verification and verification activities is to classify and remove high-risk problems in software. In order to avoid or squeeze faults, quality control models for example fault-prone models can be used for prediction of classes likely to be faulty. In order to attain these objectives, several researchers studied faults in software and constructed fault-proneness models base, on the event of failure [10], [34], [47], [76], [77]. Software prediction models are constructed using a variety of machine learning methods, such as Genetic Programming [78], Decision Trees [79], Neural Networks [80], Naive Bayes (NB) [21], Case-Based Reasoning [81], and Blurring Logic [82]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

2. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

3. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

4. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

5. Software standards can help to deal with software failures [5]. There are numerous standards regarding software engineering. Some of those standards are generic and some are specific towards any industry. Likewise, some of the standards are initiated from procurement agencies and others are either developed by certified bodies or related to certain software categories [6]. These standards comprehensively highlight the factors that can lead to varying situations [4]. These factors should be carefully considered during software development for resisting software failures [4].

In this study, we have reviewed various software engineering standards to investigate the situational factors that can lead to varying situations among software development team members.

Remaining paper comprises of five sections. Section II reports the research background. Section III discusses the research method used to recognize the situational factors. Section IV specifies the IEEE standards. Section V discusses the research elaborating the findings and future work. Section VI discusses the findings. Section VII elaborates some future work that can extend this research. Section VIII reports the limitations of this study, and Section IX concludes the research. (Software Standards and Software Failures: A Review With the Perspective of Varying Situational Contexts, page 1)

6. Software fault prediction process typically involves two phases which are denoted as training phase and the second is prediction phase where in the first phase, a model for prediction is constructed, which utilizes method or class level metrics of software with fault information associated with every single module of the software. Later, the same model is used to predict faulty classes in a new version of the software. SFP is effective to enhance the quality of software along with reducing the cost of testing. Also, it assists testing teams to limit testing on faulty classes only. Fault prediction in software possibly lays down yardstick for knowing, which areas may require attention. Many software fault prediction methods have been utilized [29], which contribute to three main elements [30]; Set of features, Label of Class, and finally the Model. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 3)

7. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

8. As time progresses and technology continues to develop, software has become an increasingly integral part of our daily lives. It is crucial that software functions correctly for endusers, making the assessment of software reliability a critical step in the testing phase. To accurately predict software reliability, various SRGMs have been proposed to describe the process of fault detection and correction [1], [2], [3]. It is important to note that there are still many SRGMs published in the literature. These models vary in terms of their underlying assumptions, mathematical formulations, and applicability to different types of software systems. (Using Modified Diffusion Models for Reliability Estimation of Open Source Software, page 3)

### response

Software engineering dapat membantu mengurangi kesalahan dalam software testing dengan menggunakan berbagai metrik dan model prediksi kerusakan. Misalnya, dengan menggunakan inheritance metrics, developers dapat memprediksi kemungkinan kerusakan pada kelas-kelas tertentu dan meningkatkan kualitas software secara efektif. Selain itu, software standards juga dapat membantu mengurangi kesalahan dalam software testing dengan memberikan pedoman yang jelas tentang bagaimana melakukan pengujian dan analisis keamanan.

Dengan demikian, software engineering berperan penting dalam meningkatkan kualitas software dan mengurangi kemungkinan kerusakan selama fase pengujian.

### reference


Many software fault prediction methods have been utilized [29], which contribute to three main elements [30]; Set of features, Label of Class, and finally the Model. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 3) Software prediction models are constructed using a variety of machine learning methods, such as Genetic Programming [78], Decision Trees [79], Neural Networks [80], Naive Bayes (NB) [21], Case-Based Reasoning [81], and Blurring Logic [82]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1) Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses.

---

## Sample 8

- conversation_id: 13
- user_chat_id: 495
- bot_chat_id: 496

### user_input

Apa peran software metrics dalam software engineering?

### retrieved_context

1. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

3. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

4. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

5. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

6. TABLE 2. Frequently Used Metrics in Software Fault Prediction.

Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak. Lima belas penelitian yang disebutkan menunjukkan bahwa beberapa metrik telah digunakan secara luas dalam prediksi kegagalan, seperti metrik yang terkait dengan sifat objek-oriented dan perilaku pengguna.

Variabel utama di tabel ini meliputi nama penulis, judul penelitian, metode yang digunakan, serta hasil yang diperoleh. Nilai penting dari tabel ini adalah penemuan bahwa beberapa metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak.

Pola penting dapat dilihat dari kemunculan istilah-istilah seperti "C&K metrics" dan "Li and Henry," yang mengindikasikan bahwa ada metrik yang secara konsisten digunakan dalam penelitian-penelitian ini. Selain itu, juga terlihat bahwa beberapa penulis menggunakan kombinasi berbagai metode analisis untuk mencapai hasil prediksi yang lebih akurat.

Insight singkat dari tabel ini adalah pentingnya penggunaan metrik-metrik tertentu dalam prediksi kegagalan perangkat lunak. Dengan demikian, penelitian ini menunjukkan bahwa dengan memahami dan menggunakan metrik yang tepat, kita dapat meningkatkan akurasi prediksi kegagalan perangkat lunak. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 13)

7. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

8. The use of measurement is common in all aspects of human life such as scales for buying vegetables, fruits, grocery items, gold or making estimations for reaching to the home of a friend. The applications of measurement are obvious in all disciplines such as sciences, engineering, medical and others. The measurements play a vital role in software organizations for the improvement of software processes [1], [2]. It is reported by many software quality assurance agencies that the quality of software product is strongly influenced by the quality of software process followed to develop the software product [3]. Software measurement has become an essential process in software organizations for characterizing, evaluating, predicting and improving software products, processes, and resources [4]- [6]. ISO/IEC 15939:2007 [4] defines measurement process as ''a process for establishing, planning, performing and evaluating measurement within an overall project, enterprise or organizational measurement structure''. Despite the acknowledged importance and advocated benefits of measurement processes for software engineering community, their actual applications in the software industry are limited [4], [5], [8], [9]. It is also reported in a systematic review on measurements in software engineering that software process is the least measured entity [35]. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 1)

### response

Software metrics berperan sebagai dasar untuk mengukur kompleksitas, kualitas perangkat lunak, dan perkiraan biaya serta upaya proyek. Mereka juga digunakan untuk menilai efisiensi dan keamanan sistem software. Fungsi point dan cyclomatic complexity adalah contoh metrik tradisional yang digunakan dalam paradigm prosedural, tetapi tidak dapat secara langsung diaplikasikan pada paradigma berorientasi objek.

Beberapa studi telah menunjukkan bahwa penggunaan metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak. Dengan demikian, penelitian ini menunjukkan bahwa dengan memahami dan menggunakan metrik yang tepat, kita dapat meningkatkan akurasi prediksi kegagalan perangkat lunak.

Sumber: [Source: Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper], [Source: Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction]

### reference


Dengan demikian, penelitian ini menunjukkan bahwa dengan memahami dan menggunakan metrik yang tepat, kita dapat meningkatkan akurasi prediksi kegagalan perangkat lunak. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 13) Nilai penting dari tabel ini adalah penemuan bahwa beberapa metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak. Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak.

---

## Sample 9

- conversation_id: 13
- user_chat_id: 497
- bot_chat_id: 498

### user_input

Bagaimana Agile software development mempengaruhi praktik software engineering?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. The software engineering industry is undergoing a rapid transformation driven by the emergence of large language models (LLMs) and their use to create autonomous agents that can perform complex software engineering tasks. This paradigm shift, which we call agentic software engineering (ASE), represents a significant rethinking of how software is designed, developed, and maintained [1], [2], [3]. In contrast to traditional software engineering practices that rely primarily on human developers following established methodologies, ASE advocates the use of AI-based agents that have the autonomy to make decisions, write software, run tests, and interact throughout the software engineering lifecycle-a change reflected in recent work on LLM-based applications in software engineering [4], [5], [6], [7]. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 1)

3. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

4. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

5. FIGURE 6. Frequency of adapted software development standard.

Gambar ini menampilkan sebuah grafik batang yang berisi informasi tentang frekuensi penggunaan standar pengembangan perangkat lunak (software development standard) oleh para pengembang. Grafik tersebut membagi data menjadi beberapa kategori, masing-masing dengan warna yang berbeda.

Grafik menunjukkan bahwa kategori dengan frekuensi tertinggi adalah "Agile" dengan warna hijau. Kemudian diikuti oleh "Waterfall" dengan warna biru, dan terakhir ada "Kanban" dengan warna kuning.

Angka yang paling mencolok adalah 40% untuk kategori "Agile". Ini berarti bahwa 40% dari responden pengembang perangkat lunak menggunakan standar Agile dalam pengembangan proyek mereka. Angka ini mungkin menunjukkan bahwa banyak pengembang memilih untuk menggunakan metodologi Agile karena fleksibilitas dan kemampuannya untuk mendukung kerja sama tim.

Makna singkat dari gambar ini adalah bahwa para pengembang perangkat lunak memiliki preferensi yang beragam dalam hal standar pengembangan. Namun, metodologi Agile terlihat menjadi pilihan populer karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 8)

6. Agentic software engineering is a major development in the design, development, and maintenance of software systems, and its effects extend beyond the simple automation of existing processes. The accelerated development as can be seen in the literature that shows a shift of mere aids to complex autonomous multi-agent systems points out to the fact that the transformation is gaining momentum and is likely to go on redefining the software development environment. Despite the significant difficulties that still remain to be addressed, especially in the following aspects coordination protocols, security systems, evaluation systems, and patterns of human-agent collaboration, the potential gains in the form of productivity enhancement, quality improvement, and accessibility expansion are absolutely convincing and warrant continued expenditure of resources on research and development. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 20)

7. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

8. The software industry has experienced rapid expansion in recent years, with software development now essential to the success of many multinational corporations. The demand for complex software systems has dramatically increased, effective software development has become crucial, given the limitations of resources such as money, time, and labor. Cost and effort calculations significantly impact the development process and client needs, and project failure is often caused by errors in job estimating. Underestimating a project's cost and effort can have severe repercussions, such as exceeding the project's budget. Project overruns, on the other hand, can also have a detrimental impact on software projects' successful completion. Researchers and experts in the software industry are continually exploring ways to keep management and development productivity at high levels. However, standalone estimating models have revealed inadequacies over the last decade, and they have not produced any noteworthy research results. Recent literature suggests that opting for ensemble models would yield better results than standalone models. We have proposed a heterogeneous ensemble effort estimation (EEE) model in this research. Our proposed model comprises standalone estimating models such as Use Case Point, Expert Judgment (EJ), and Artificial Neural Network (ANN). We combined the effort of each unique base model using linear combination rule. To validate our model's effectiveness, we applied it to the benchmark dataset, the International Software Benchmarking Standards Group (ISBSG), using three different variations to avoid biases. We further applied the trained models to industry use cases for cross-validation. Our study's findings demonstrated that, in comparison to stand-alone estimate strategies, the ensemble technique produced better estimation results. Finally, our study proposes a heterogeneous ensemble effort estimation model that outperforms standalone models in terms of accuracy. This model has the potential to aid in effective software development, particularly in project cost and effort estimation. INDEX TERMS Software effort estimation, ensemble effort estimation (EEE), standalone estimation, use case point (UCP), machine learning algorithms, deep learning, expert judgement. (Heterogeneous Ensemble Model to Optimize Software Effort Estimation Accuracy, page 1)

### response

Agile software development telah membawa perubahan signifikan dalam praktik software engineering. Secara khusus, itu telah menyebabkan peningkatan fleksibilitas dan kemampuan untuk beradaptasi dengan perubahan pasar yang cepat. Praktik Agile seperti integrasi kontinu [29] memberikan koneksi erat dengan pengembangan untuk memastikan bahwa kesalahan dapat dideteksi dan diperbaiki secepat mungkin.

Kemampuan ini telah meningkatkan potensi analitis software, yang sangat penting dalam memenuhi kebutuhan pelanggan yang dinamis. Selain itu, Agile juga telah membantu mengurangi waktu pengembangan produk dan meningkatkan kualitas produk.

### reference


Namun, metodologi Agile terlihat menjadi pilihan populer karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 8) Makna singkat dari gambar ini adalah bahwa para pengembang perangkat lunak memiliki preferensi yang beragam dalam hal standar pengembangan. Ini berarti bahwa 40% dari responden pengembang perangkat lunak menggunakan standar Agile dalam pengembangan proyek mereka.

---

## Sample 10

- conversation_id: 13
- user_chat_id: 499
- bot_chat_id: 500

### user_input

Bagaimana software engineering membantu menjaga sistem CNN agar mudah dipelihara?

### retrieved_context

1. The road damage detection research makes use of laser sensors to rebuild 3D road damage as well as stereo vision technologies. Several sensors are required for the stereo vision system, including two cameras, an LED, a laser, and LiDAR. The laser sensor has a small beamwidth; thus, it cannot detect road damage in the form of a large hole, necessitating the use of an array of LEDs, lasers, LiDARs, and other sensors [18], [49]. Reconstructing the pothole takes time, whether using an LED array, laser, or LiDAR. Furthermore, 3D road defect reconstruction and stereo vision require well-lit lighting and slow vehicle speeds [17], [18], [50].

Further research used image-processing techniques. Potholes are a form of road irregularity that can be recognized with traditional image processing techniques. To achieve high accuracy, this technique takes numerous steps, including manual image feature extraction and image processing parameter adjustments. As a result, the image frame rate varies depending on traffic circumstances [21]. Some research that investigated road conditions, pavement conditions, potholes, cracks, smart phone sensors, and accelerometers used machine learning techniques such as support vector machines, neural networks, multilayer perceptron, and decision trees [16]. Furthermore, research is being conducted to detect pavement damage using ML algorithms such as support vector machines, artificial neural networks, and random forests [51]. To improve accuracy, ML models require significant computer resources during data processing, which also includes manual feature analysis.

Several studies used deep convolutional neural network (CNN) techniques to automate the simultaneous feature extraction and categorization of objects [41], [52]. This is challenging to incorporate into real-time road defect detection systems. The deployment of CNN models for road damage detection on devices requires a balance between high accuracy and high efficiency [53]. The use of CNN models for road damage detection on devices requires achieving a balance between high accuracy and high efficiency. The use of CNN models for road damage detection on devices necessitates striking a balance between high accuracy and high efficiency. The parameter system performance deployment model CNN on devices performs well in terms of precision, recall, F1-score, and as well as efficiency of time inference.

The CNN models perform exceptionally well in terms of high accuracy, precision, recall, and low loss. This requires CNN models with large architecture and competitive computing costs that are inefficient. To do this while maintaining high accuracy, a simplified CNN model configuration setting is required to achieve good CNN model system performance. High efficiency, which is the CNN model system performance, enables it to detect road faults on edge devices with a short inference time. Because the CNN model on edge devices have limited storage capacity, inference time must be considered. Taking this into account, the CNN model offers good system performance and a short inference time for simpler model configurations, but high accuracy is difficult to achieve. To obtain optimal system performance, the CNN model parameters must be properly chosen. When selecting a detection model, there is no definitive answer as to which model has the best performance [31], [53].

Improving system performance in computer vision, object recognition, and classification using CNN models can be achieved through various methods. These include modifying or adding components to the CNN model structure and optimizing hyperparameter selection during CNN model training. The strategy of enhancing the CNN structure aims to improve feature extraction efficiency and model accuracy by modifying or incorporating new components into the CNN architecture. Several studies have focused on enhancing CNN models by modifying or adding components to the existing CNN structure [54], [55], [56], [57], [58], [59]. DenseNet was integrated into the YOLOv4 backbone to optimize feature transfer and reuse. This involved several modifications, such as adjusting the Path Aggregation Network (PANet) [54], introducing New Residual Blocks, applying Spatial Pyramid Pooling (SPP), modifying the PANet, and utilizing Hard-Swish activation functions [59]. Similarly, researchers have integrated DenseNet blocks into the YOLOv5 backbone to enhance the preservation and reuse of critical feature information. This was achieved by incorporating a Convolutional Block Attention Module (CBAM) [56]. Another study introduced a novel framework called Multiple Graph Learning Neural Networks (MGLNN) for semi-supervised learning on graph-based data [55]. Additionally, modifications were made to the YOLO model using the CSPDarknet53 backbone structure, which included Residual Blocks, DenseNet, Spatial Pyramid Pooling (SPP), and the Path Aggregation Network (PANet) [57]. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 2)

2. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

3. Nuclear power plants (NPPs) employ several safety systems to protect the public from the release of radioactive material in case of an accident. These safety systems are manipulated by the instrumentation and control (I&C) systems, which provide the control and monitoring functions of the various and diverse components and equipment that are essential to maintain safe operation. Existing I&C systems are currently being replaced with microprocessor-based digital systems because of the obsolescence of analog-based I&C equipment and a lack of vendor support. It is true that digital systems provide better performance such as improved accuracy, computation capabilities, and data handling, as well as the potential for improved capabilities such as fault tolerant techniques [1]. (Input-Domain Software Testing for Failure Probability Estimation of Safety-Critical Applications in Consideration of Past Input Sequence, page 1)

4. [38] C Cavina-Pratesi, C Hesse. Why do the eyes prefer the index finger? Simultaneous recording of eye and hand movements during precision grasping. (2013-04)

[39] TJ Bosch, T Hanna, KA Fercho, LA Baugh. Behavioral performance and visual strategies during skill acquisition using a novel tool use motor learning task. (2018-12)

[40] W Choi. The effect of task-oriented training on upper-limb function, visual perception, and activities of daily living in acute stroke patients: A pilot study. (2022-03)

[41] I Pysmennyi, R Kyslyi, A Petrenko. Edge computing in multi-scope service-oriented mobile healthcare systems. (2019-03)

[42] J Lv, Q Sun, Q Li, L Moreira-Matias. Multi-scale and multiscope convolutional neural networks for destination prediction of trajectories. (2020-08)

[43] AA Saputra, K Wada, S Masuda, N Kubota. Multi-scopic neuro-cognitive adaptation for legged locomotion robots. (2021-08)

[44] AF Zhu, P Rahgozar, KC Chung. Advances in proximal interphalangeal joint arthroplasty. (2018-05)

[45] J.-S Won, S Lee. Geometry-based finger kinematic models for joint rotation configuration and parameter estimation. (2020-07)

[46] AR A Besari, AA Saputra, WH Chin, N Kubota, Kurnianingsih. Feature-based egocentric grasp pose classification for expanding humanobject interactions. (2021-06)

[47] PB Shull, S Jiang, Y Zhu, X Zhu. Hand gesture recognition and finger angle estimation via wrist-worn modified barometric pressure sensing. (2019-04)

[48] I Imbinto, F Montagnani, M Bacchereti, C Cipriani, A Davalli, R Sacchetti, E Gruppioni, S Castellano, M Controzzi. The S-finger: A synergetic externally powered digit with tactile sensing and feedback. (2018-06)

[49] J Mazumder, LN Nahar, M Md Uddin Atique. Finger gesture detection and application using hue saturation value. (2018-08)

[50] WB Dou, WH Chin, N Kubota. Hand gesture communication using deep learning based on relevance theory,'. (2020-12)

[51] AR A Besari, WH Chin, N Kubota, Kurnianingsih. Ecological approach for object relationship extraction in elderly care robot. (2020-12)

[52] Y Cheng. Backpropagation for fully connected cascade networks. (2017-08)

[53] P Gajbhiye, N Mingchinda, W Chen, SC Mukhopadhyay, T Wilaiprasitporn, RK Tripathy. Wavelet domain optimized Savitzky-Golay filter for the removal of motion artifacts from EEG recordings. (2021)

[54] R Chen, M Wang, J.-H Chang. A study of the pinch performance and subjective satisfaction with chopsticks of different lengths. (2017)

[55] AR A Besari, WH Chin, N Kubota, Kurnianingsih. Ecological approach for object relationship extraction in elderly care robot. (2020-12)

[56] YJ R De Kloe, IT C Hooge, C Kemner, DC Niehorster, M Nyström, RS Hessels. Replacing eye trackers in ongoing studies: A comparison of eye-tracking data quality between the Tobii pro TX300 and the tobii pro spectrum. (2022-01)

[57] EP Larsen, JM Kolman, FN Masud, F Sasangohar. Ethical considerations when using a mobile eye tracker in a patient-facing area: Lessons from an intensive care unit observational protocol. (2020-11)

[58] DC Niehorster, T Santini, RS Hessels, IT C Hooge, E Kasneci, M Nyström. The impact of slippage on the data quality of head-worn eye trackers. (2020-06)

[59] C Chen, W Guo, C Ma, Y Yang, Z Wang, C Lin. SEMGbased continuous estimation of finger kinematics via large-scale temporal convolutional network. (2021-05)

[60] C Dai, X Hu. Finger joint angle estimation based on motoneuron discharge activities. (2020-03)

[61] H Eschmann, ME Héroux, JH Cheetham, S Potts, J Diong. Thumb and finger movement is reduced after stroke: An observational study. (2019-06)

[62] SN Emhardt, M Wermeskerken, K Scheiter, T Gog. Inferring task performance and confidence from displays of eye movements. (2020-11)

[63] X Fang, F Yu, G Yang, Y Qu. Regression analysis with differential privacy preserving. (2019)

[64] H Zhu, X You, S Liu. Multiple ant colony optimization based on Pearson correlation coefficient. (2019)

[65] L Ke, A Kamat, J Wang, T Bhattacharjee, C Mavrogiannis, SS Srinivasa. Telemanipulation with Chopsticks: Analyzing human factors in user demonstrations. (2022-06)

[66] A Murata, T Doi, W Kageyama, Karwowski. Development of an eye-gaze input system with high speed and accuracy through target prediction based on homing eye movements. (2021)

[67] B Banire, D Al-Thani, M Qaraqe, K Khowaja, B Mansoor. The effects of visual stimuli on attention in children with autism spectrum disorder: An eye-tracking study. (2020) (Finger Joint Angle Estimation With Visual Attention for Rehabilitation Support: A Case Study of the Chopsticks Manipulation Test, page 2)

5. FIGURE 9. CNN model training result.

Gambar ini menampilkan grafik hasil pelatihan model CNN (Convolutional Neural Network). Grafik ini terlihat seperti garis di atas yang menunjukkan proses pengembangan akurasi model CNN selama proses pelatihan. Pada awalnya, akurasi model cukup rendah, tetapi kemudian meningkat secara signifikan seiring dengan berjalannya waktu dan iterasi pelatihan.

Pada grafik tersebut terdapat beberapa titik tertentu yang menunjukkan peningkatan drastis dalam akurasi. Meskipun tidak ada angka spesifik yang dapat diidentifikasi, namun jelas bahwa model CNN telah berhasil meningkatkan akurasinya hingga mencapai nilai yang sangat tinggi.

Dari grafik ini kita dapat menyimpulkan bahwa proses pelatihan model CNN telah berjalan dengan efektif dan akurasi model meningkat secara signifikan. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 10)

6. As a result, there are numerous research reports made by the academy. As it can be noticed, SBSET allows to reduce software design time, decrease the cost of software testing and maintenance, and therefore, it can produce more reliable software. It is also anticipated that SBSET can help avoiding error-prone work in the different aspects of software engineering process. (The Acceptance of Search-Based Software Engineering Techniques: An Empirical Evaluation Using the Technology Acceptance Model, page 2)

7. Maintainability is the ease with which an AI-based software can be modified, updated, or extended to adapt to changing requirements or environments. This involves aspects such as modularity, reusability, and simplicity of the AI models and codebase. Ensuring maintainability in AI systems requires careful design, adherence to best practices, and documentation of the AI model architecture and development process. Maintainability can be assessed using code-level metrics such as cyclomatic complexity, lines of code, code duplication, and code coverage. For AI systems, the modularity and reusability of model components can also be considered, along with the adherence to best practices and coding standards. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 10)

8. Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment. New threats are tracked during this phase. The software can never be 100 percent secure, and new threats emerge regularly phase [14]. As a result, efforts must be made to secure the software. The maintenance team should keep track of new threats that the system encounters to address them promptly and prevent security breaches [83], [116]. Table 15 presents prescriptive actions to increase security during the maintenance phase of SDLC [14], [65], [105], [114], [117], [118]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

### response

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


The road damage detection research makes use of laser sensors to rebuild 3D road damage as well as stereo vision technologies. Several sensors are required for the stereo vision system, including two cameras, an LED, a laser, and LiDAR. The laser sensor has a small beamwidth; thus, it cannot detect road damage in the form of a large hole, necessitating the use of an array of LEDs, lasers, LiDARs, and other sensors [18], [49]. Reconstructing the pothole takes time, whether using an LED array, laser, or LiDAR. Furthermore, 3D road defect reconstruction and stereo vision require well-lit lighting and slow vehicle speeds [17], [18], [50]. Further research used image-processing techniques. Potholes are a form of road irregularity that can be recognized with traditional image processing techniques. To achieve high accuracy, this technique takes numerous steps, including manual image feature ex
