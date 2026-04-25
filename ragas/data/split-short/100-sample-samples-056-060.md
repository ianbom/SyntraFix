# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 56

- conversation_id: 14
- user_chat_id: 790
- bot_chat_id: 791

### user_input

Apa tujuan software testing?

### retrieved_context

1. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

2. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

3. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

4. Testing is a comprehensive concept related to the development of each system. In the software engineering discipline, testing is a crucial task of the software development life cycle. In contrast, software testing in any field other than software engineering can be considered as an end-user testing focused on the suitability of a software developed for a specific purpose in this field. For this reason, the multidisciplinary use of software testing makes it difficult to create a specific corpus of software testing studies in the scope of software engineering. In this context, to create a specific corpus of software testing within the scope of software engineering, a methodology including two sequential stages was followed for corpus creation, which included identifying core publication sources for the software engineering field and extracting articles specific to software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

5. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

6. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

7. In the software testing stages, the aim is to develop softwareoriented products and services in a systematic and efficient manner, in which a wide range of tasks, methods, and strategies are used. Depending on the type, scope and context of the designed and developed, the methods and strategies  chosen during the software testing stages vary considerably. The findings of this study offer a wide-ranging insight into not only the themes and trends in focus but also the tools, tasks, methods, and strategies specific to software testing. Specifically, the discovered topics reveal that the most focused tasks in software testing are specification, transformation, detection, localization, generation, evaluation, optimization, verification, and prediction. The important background provided by the core tasks highlighted in this study for software testing has also been addressed by previous studies [49]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 9)

8. Why do we need AI software testing? The fast-growing AI software and the popularity of big data-based applications bring new needs and motivations. Numerous current and future software will be built with AI-based features and functions. Existing techniques and tools are not adequate to test AI-based features and functions. There are a lack of well-defined and experience-approved quality validation models and assessment criteria. In addition, there is a lack of AI-based testing methods and solutions for AI software. Thus, the meaning of testing AI software is illustrated in a definition below. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 2)

### response

Menurut konteks yang disediakan, tidak ada jawaban langsung tentang tujuan software testing. Namun, dapat disimpulkan bahwa tujuan software testing adalah untuk memastikan kualitas dan kebenaran sistem perangkat lunak melalui proses observasi dan evaluasi.

Namun, sehubungan dengan pertanyaan tersebut, dapat disebutkan beberapa tujuan dari software testing berdasarkan konteks yang tersedia:

* Menyediakan output yang sesuai (output) [Source: Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years]
* Mengidentifikasi masalah (faults) sebelum masa pengujian (testing phase) [Source: Error-Type—A Novel Set of Software Metrics for Software Fault Prediction]
* Membuat perbandingan antara hasil keluaran dan ekspektasi (result) [Source: Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years]
* Mengoptimalkan alokasi sumber daya pengujian (testing resources) [Source: Error-Type—A Novel Set of Software Metrics for Software Fault Prediction]

Namun, perlu diingat bahwa jawaban ini tidak sepenuhnya menjawab pertanyaan "apa tujuan software testing", karena konteks yang disediakan tidak secara eksplisit menyebutkan tujuan software testing.

### reference


Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process.

Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6].

An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18].

Testing is a comprehensive concept related to the development of each system. In the software engineering discipline, testing is a crucial task of the software development life cycle.

Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2].

Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process.

In the software testing stages, the aim is to develop softwareoriented products and services in a systematic and efficient manner, in which a wide range of tasks, methods, and strategies are used. Depending on the type, scope and context of the designed and developed, the methods and strategies chosen during the software testing stages vary considerably.

Why do we need AI software testing? The fast-growing AI software and the popularity of big data-based applications bring new needs and motivations.

---

## Sample 57

- conversation_id: 14
- user_chat_id: 792
- bot_chat_id: 793

### user_input

Bagaimana software testing meningkatkan software quality?

### retrieved_context

1. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

2. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

3. Humphrey [Humphrey 1989] argued that software quality can be improved by improving its development process. Both academia and industry are striving to find ways for software process improvement (SPI). There are numerous SPI framework and methodologies available today, but they all have one challenge in common: the cost of experimenting with the process change. It is widely claimed that software process simulation modeling can help in predicting the benefits and repercussions of a process change, thus enabling organizations to make more informed decisions and reduce the likelihood of failed SPI initiatives [8]. (Change-Oriented Open Source Software Process Simulation, page 12)

4. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

5. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

6. TABLE 1. Examples of actions to improve software quality for the adalah tabel yang menyajikan contoh tindakan untuk meningkatkan kualitas perangkat lunak dengan menggunakan alat analitik perangkat lunak. Tabel ini terdiri dari 38 baris dan memiliki 8 kolom.

Tabel tersebut menjelaskan beberapa indikator strategis yang digunakan untuk mengevaluasi kinerja perangkat lunak, seperti "Blocking" yang merupakan indikator strategis untuk mengidentifikasi potensi masalah dalam proses pengembangan. Dalam tabel ini juga dapat dilihat bahwa ada empat faktor utama yang digunakan untuk menilai kualitas perangkat lunak: Code Smells, Design Issues, Performance, dan Security.

Salah satu contoh kasus yang disajikan dalam tabel adalah "Blocking" files problem yang dialami oleh perusahaan NeverLate. Dalam kasus ini, analis perangkat lunak dapat menggunakan alat analitik untuk mengidentifikasi klas-klas file yang memiliki kualitas rendah dan membutuhkan perbaikan.

Analisis dari tabel menunjukkan bahwa perusahaan yang menggunakan Q-Rapids dapat meningkatkan kualitas perangkat lunak mereka dengan menggunakan data historis dan visualisasi data. Dengan demikian, mereka dapat mengidentifikasi masalah-masalah yang signifikan dan mengambil tindakan untuk memperbaiki kinerja perangkat lunak.

Dalam kesimpulan, tabel ini menunjukkan bahwa penggunaan alat analitik perangkat lunak dapat membantu meningkatkan kualitas perangkat lunak dengan cara yang lebih objektif dan data-driven. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 6)

7. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

8. Table 3 shows the mapping between the sub-RQs and the Table 3 menunjukkan mapping antara sub-Pertanyaan Penelitian (RQs) dan beberapa variabel utama. Dari tabel tersebut dapat disimpulkan bahwa penulis melakukan studi kasus untuk menginvestigasi bagaimana analisis perangkat lunak digunakan dalam meningkatkan kualitas software.

Tiga pertanyaan penelitian (RQs) yang diidentifikasi oleh penulis adalah:
- RQ1: Bagaimana praktisi memahami integrasi Kualitas Sistem (QS) ke alat analisis perangkat lunak?
- RQ2: Bagaimana praktisi memahami integrasi QS ke alat analisis perangkat lunak ketika mengevaluasi kualitas software dalam ASD?
- RQ3: Apa saja tantangan dan pelajaran yang dipelajari oleh praktisi ketika mengintegrasikan QS ke alat analisis perangkat lunak.

Dengan menggunakan tool Q-Rapids, empat kasus penggunaan (UC) telah dilakukan pada beberapa perusahaan. Pada UC1, perusahaan 1 menggunakan Q-Rapids untuk meningkatkan kualitas produk Modelio 3.8 dan Modelio NG dengan cara menggunakan indikator strategis yang diperoleh dari analisis Q-Rapids.

Pada UC2, perusahaan 2 menggunakan dua strategi berbeda dalam menerapkan Q-Rapids. Mereka melakukan penelitian berorientasi, di mana para mitra peneliti membantu atau berkolaborasi dalam menentukan indikator strategis dan faktor serta metrik yang terkait.

Pada UC3 dan UC4, perusahaan menggunakan Q-Rapids untuk meningkatkan kualitas produk dan proses mereka. Mereka berhasil mendeteksi anomali awal, sehingga dapat merilis produk pada waktu yang lebih cepat dengan jumlah anomali yang lebih sedikit.

Dari hasil studi kasus ini dapat disimpulkan bahwa integrasi QS ke alat analisis perangkat lunak sangat penting dalam meningkatkan kualitas software dan proses pengembangan. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 7)

### response

Software testing meningkatkan software quality dengan beberapa cara:

* Melakukan verifikasi dan validasi terhadap sistem yang dikembangkan untuk memastikan bahwa sistem tersebut sesuai dengan spesifikasi dan tidak memiliki kesalahan.
* Mengidentifikasi potensi masalah dalam proses pengembangan dan memberikan saran perbaikan untuk meningkatkan kualitas software.
* Meningkatkan kepercayaan pengguna terhadap produk akhir melalui pengujian yang lebih komprehensif dan berulang.
* Mengurangi risiko kesalahan dan masalah yang mungkin terjadi dalam proses pengembangan.

Informasi tersebut didapatkan dari [Source: Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years]

### reference


Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2].

An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18].

Humphrey [Humphrey 1989] argued that software quality can be improved by improving its development process. Both academia and industry are striving to find ways for software process improvement (SPI).

Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process.

Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs.

Examples of actions to improve software quality for the adalah tabel yang menyajikan contoh tindakan untuk meningkatkan kualitas perangkat lunak dengan menggunakan alat analitik perangkat lunak. Tabel ini terdiri dari 38 baris dan memiliki 8 kolom.

Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6].

Table 3 shows the mapping between the sub-RQs and the Table 3 menunjukkan mapping antara sub-Pertanyaan Penelitian (RQs) dan beberapa variabel utama. Dari tabel tersebut dapat disimpulkan bahwa penulis melakukan studi kasus untuk menginvestigasi bagaimana analisis perangkat lunak digunakan dalam meningkatkan kualitas software.

---

## Sample 58

- conversation_id: 14
- user_chat_id: 794
- bot_chat_id: 795

### user_input

Apa hubungan software testing dan software development?

### retrieved_context

1. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

2. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

3. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

4. Testing is a comprehensive concept related to the development of each system. In the software engineering discipline, testing is a crucial task of the software development life cycle. In contrast, software testing in any field other than software engineering can be considered as an end-user testing focused on the suitability of a software developed for a specific purpose in this field. For this reason, the multidisciplinary use of software testing makes it difficult to create a specific corpus of software testing studies in the scope of software engineering. In this context, to create a specific corpus of software testing within the scope of software engineering, a methodology including two sequential stages was followed for corpus creation, which included identifying core publication sources for the software engineering field and extracting articles specific to software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

5. Worldwide software development expenditure, for year 2014, was 3.8 billion dollars which included 23% quality control and testing cost for business applications [4]. Early fault detection helps save costs, time, and reduce the complexity of the software because it is proportionate to the testing. It is a well known fact that extensive testing are impossible [5]. Testing cost sometimes amounts to over fifty percent of the The associate editor coordinating the review of this manuscript and approving it for publication was Claudio Agostino Ardagna . entire software development cost. It is for these reasons that it is more feasible to detect and test classes with faults to produce software with better quality. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

6. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

7. Test planning is the first step in the testing phase. The testing team begins planning tests during the implementation phase because test planning does not necessitate access to

TABLE 4. (Continued.) CSSRs and its practices in the secure coding phase of the secure SDLC.

program code. While the developers are working on code, the testing team prepares for the testing activity later. The security testing teams develop test cases based on design papers, threat models, and misuse situations. Security test cases aim to attack software successfully. Any modification to the software design must be disclosed to the testing team during the planning phase of the test. As a result, the testing team may create test cases that aren't relevant. Based on the nature of the software and its threats, the severity of bugs is adjusted. A minor bug in software code that isn't very important to how it works may only take a few minutes to fix, but it can significantly affect how secure it is. A discussion of the revised severities takes place with the development team. Table 5 shows the security operations conducted during the testing phase [3], [17], [80], [84]- [86]. (Security Assurance Model of Software Development for Global Software Development Vendors, page 1)

8. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

### response

Software testing merupakan bagian dari proses software development. Software testing meliputi beberapa aktivitas mulai dari validasi kebutuhan awal sampai dengan akseptansi produk akhir oleh pelanggan [9]. Tes dilakukan pada berbagai tahap proses pengembangan perangkat lunak untuk tujuan yang berbeda-beda, seperti tes garis produk software dan antarmuka pengguna grafis [10] [11].

Selain itu, Software testing merupakan suatu kegiatan yang terkait dengan pengembangan sistem. Dalam disiplin ilmu teknik komputer, Testing adalah tugas penting dalam siklus hidup perangkat lunak. Di sisi lain, pengetesan perangkat lunak pada bidang luar ilmu teknik komputer dapat dianggap sebagai tes pengguna akhir yang berfokus pada kesesuaian suatu perangkat lunak yang dikembangkan untuk tujuan tertentu dalam bidang tersebut [12]. 

Oleh karena itu, hubungan antara software testing dan software development adalah bahwa software testing merupakan bagian integral dari proses pengembangan perangkat lunak.

### reference


Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process.

Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6].

An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18].

Testing is a comprehensive concept related to the development of each system. In the software engineering discipline, testing is a crucial task of the software development life cycle.

Worldwide software development expenditure, for year 2014, was 3.8 billion dollars which included 23% quality control and testing cost for business applications [4]. Early fault detection helps save costs, time, and reduce the complexity of the software because it is proportionate to the testing.

Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2].

Test planning is the first step in the testing phase. The testing team begins planning tests during the implementation phase because test planning does not necessitate access to TABLE 4. (Continued.) CSSRs and its practices in the secure coding phase of the secure SDLC. program code.

Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process.

---

## Sample 59

- conversation_id: 14
- user_chat_id: 796
- bot_chat_id: 797

### user_input

Apa hubungan software testing dan software maintenance?

### retrieved_context

1. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

2. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

3. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

4. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

5. Table 1 shows a total of 14,684 articles related to software Tabel 1 menunjukkan jumlah artikel terkait pengujian perangkat lunak selama 40 tahun terakhir. Total artikel mencapai 14.684 judul, dengan peningkatan jumlah publikasi setiap lima tahun terus meningkat. Analisis ini melibatkan aplikasi teknik modeling topik (topic modeling) pada data tekstual untuk memahami tema dan pola yang ada dalam kumpulan artikel tersebut.

Variabel utama dari tabel ini adalah tanggal publikasi, dengan 5 periode lima-tahunan yang ditunjukkan. Data menunjukkan bahwa jumlah artikel terkait pengujian perangkat lunak terus meningkat seiring waktu. Hal ini dapat diartikan sebagai peningkatan minat dan kebutuhan akademis dalam bidang pengujian perangkat lunak.

Nilai atau pola penting yang muncul dari data ini adalah kenaikan jumlah publikasi secara bertahap, menunjukkan bahwa topik pengujian perangkat lunak semakin banyak diselidiki dan dipublikasikan di kalangan akademisi. Insigh singkat yang dapat diperoleh dari tabel ini adalah bahwa ada peningkatan signifikan dalam jumlah artikel terkait pengujian perangkat lunak, menunjukkan kepentingan meningkat dalam bidang ini.

Namun, data yang tersedia belum memberikan informasi detail tentang jenis atau topik khusus dalam pengujian perangkat lunak yang paling banyak dipublikasikan. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 5)

6. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

7. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

8. We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig. 3. 136 out of 263 (52%) articles belong to quality assurance and analytic. 44 out of 263 (17%) articles have focused on architecture and design. 29 out of 263 (11%) articles have addressed the implementation followed by requirements engineering stage with 24 out of 263 (9%) articles. 11 (4%) articles were focusing on the maintenance phase. The rest of the articles were not particularly focusing on any stage but were generally applicable to SE. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 5)

### response

Tidak ada informasi langsung tentang hubungan antara software testing dan software maintenance dalam konteks yang diberikan.

### reference


Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6].

Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process.

The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks.

An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18].

Table 1 shows a total of 14,684 articles related to software Tabel 1 menunjukkan jumlah artikel terkait pengujian perangkat lunak selama 40 tahun terakhir. Total artikel mencapai 14.684 judul, dengan peningkatan jumlah publikasi setiap lima tahun terus meningkat.

The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is.

Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents.

We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig.

---

## Sample 60

- conversation_id: 14
- user_chat_id: 798
- bot_chat_id: 799

### user_input

Bagaimana software metrics membantu efektivitas software testing?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. TABLE 2. Frequently Used Metrics in Software Fault Prediction.

Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak. Lima belas penelitian yang disebutkan menunjukkan bahwa beberapa metrik telah digunakan secara luas dalam prediksi kegagalan, seperti metrik yang terkait dengan sifat objek-oriented dan perilaku pengguna.

Variabel utama di tabel ini meliputi nama penulis, judul penelitian, metode yang digunakan, serta hasil yang diperoleh. Nilai penting dari tabel ini adalah penemuan bahwa beberapa metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak.

Pola penting dapat dilihat dari kemunculan istilah-istilah seperti "C&K metrics" dan "Li and Henry," yang mengindikasikan bahwa ada metrik yang secara konsisten digunakan dalam penelitian-penelitian ini. Selain itu, juga terlihat bahwa beberapa penulis menggunakan kombinasi berbagai metode analisis untuk mencapai hasil prediksi yang lebih akurat.

Insight singkat dari tabel ini adalah pentingnya penggunaan metrik-metrik tertentu dalam prediksi kegagalan perangkat lunak. Dengan demikian, penelitian ini menunjukkan bahwa dengan memahami dan menggunakan metrik yang tepat, kita dapat meningkatkan akurasi prediksi kegagalan perangkat lunak. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 13)

3. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

4. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

5. TABLE 7. Comparison of CK with inheritance metric. TABLE 7. Perbandingan antara CK dengan Metrik Warisan menunjukkan bahwa penggunaan metrik warisan dapat meningkatkan akurasi prediksi kegagalan perangkat lunak dibandingkan dengan metrik CK biasa. Data ini diperoleh dari eksperimen yang melibatkan berbagai teknik belajar mesin dan metode klasifikasi.

Beberapa variabel utama yang diuji dalam tabel adalah metrik warisan, metrik CK, dan hasil prediksi kegagalan perangkat lunak. Analisis menunjukkan bahwa penggunaan metrik warisan dapat meningkatkan akurasi prediksi sekitar 10-15% dibandingkan dengan metrik CK biasa.

Namun, perlu diingat bahwa data ini hanya berdasarkan eksperimen yang telah dilakukan dan belum tentu dapat diaplikasikan pada konteks lain. Selain itu, tabel juga menyebutkan beberapa sumber referensi yang terkait dengan prediksi kegagalan perangkat lunak, seperti penelitian tentang penggunaan jaringan saraf tiruan untuk prediksi kegagalan.

Dalam kesimpulan, data dalam TABLE 7 menunjukkan bahwa metrik warisan dapat menjadi alternatif yang lebih baik dibandingkan dengan metrik CK biasa dalam memprediksi kegagalan perangkat lunak. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 12)

6. Kupiainen et al. [22] conducted a systematic review of the use and impact of software metrics in ASD in industry. The authors reported that software metrics are mainly used for sprint planning, tracking progress, improving software quality, fixing software process, and motivating people. The authors reported that metrics like velocity, effort estimation, customer satisfaction, defect count, technical debt and build are used prominently in ASD. In their systematic review, Tahir et al. [46] observed that metrics for defects, effort, size, duration, productivity, employee commitment, and customer satisfaction are commonly reported in the state of the art. These findings complement another review by Gómez et al. [15], where complexity and size were found to be the most measured attributes in MPs. Other usage of metrics in ASD discussed in the literature are for planning and tracking software development [22], understanding development performance and product quality [48], measuring process quality [50], estimating effort [47], and reporting progress and quality to stakeholders not involved in the actual development [4]. Taken together, metrics targeting sprint planning, fixing software process, effort estimation, development performance, and software defects can be used to measure an organization's process performance. However, this objective is not expressly stated in any of the reviews mentioned above. On the contrary, [22] remarked that more studies are needed to explore the rationale behind utilizing the metrics the authors found in their review. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3)

7. TABLE 6. Experimental results.

Penelitian ini menunjukkan bahwa metrik software baru yang disebut Error-Type dapat digunakan untuk memprediksi kegagalan sistem dengan lebih akurat. Dalam eksperimen ini, empat model belajar mesin (machine learning) dipadankan menggunakan dataset SoftWare Metrics dan Full Dataset.

Dari hasil eksperimen, ditemukan bahwa ketika feature selection tidak diaplikasikan, performance model belajar mesin berkurang karena masalah multi-kolinieritas yang menyebabkan pengaruh negatif terhadap hasil akhir. Namun, setelah feature selection diterapkan, masalah ini dapat dihilangkan, sehingga penggunaan metrik ESM yang baru memberikan informasi lebih bermanfaat kepada model belajar mesin.

Dengan demikian, penelitian ini berhasil menunjukkan bahwa penggunaan Error-Type sebagai metrik software baru dapat meningkatkan keakuratan prediksi kegagalan sistem dan meningkatkan performa model belajar mesin. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 9)

8. TABLE 5. Experimental results.

Dalam penelitian ini, dilakukan validasi eksperimental terhadap dampak metrik warisan pada prediksi kegagalan perangkat lunak. Variabel utama dalam penelitian ini meliputi dua jenis dataset: CK-Inheritance dan Inheritance+CK. 

Pertama-tama, proses filtrasi dilakukan untuk memastikan bahwa setiap dataset memiliki jumlah instansi yang cukup besar untuk dilakukan 10-kali validasi silang tanpa penggantian data. Proses ini menghapuskan 25 dataset dari CK-Inheritance dan 28 dataset dari Inheritance+CK.

Selain itu, filter skewness digunakan untuk memastikan bahwa setiap dataset memiliki distribusi yang seimbang antara instansi yang baik dan buruk. Filter ini menghapuskan sekitar enam dataset dari masing-masing jenis.

Dengan demikian, setelah proses filtrasi dan penghapusan data yang tidak relevan, jumlah dataset yang tersedia untuk eksperimen menurun menjadi 30 dataset per jenis.

Pada bagian eksperimen, penelitian ini menggunakan dua tool utama: bahasa R versi 3.4.3 dan R Studio 1.1.383. Penelitian ini juga menggunakan fungsi aktivasi sigmoid untuk mendapatkan hasil yang lebih akurat dalam prediksi kegagalan perangkat lunak.

Dengan demikian, penelitian ini menawarkan wawasan terkait dampak metrik warisan pada prediksi kegagalan perangkat lunak dan memberikan sumbangsih penting bagi komunitas akademis. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 9)

### response

Software evaluators dapat membuat rencana tes berdasarkan bagian yang paling rentan akan kegagalan dengan menggunakan metrik.

### reference


Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs.

Frequently Used Metrics in Software Fault Prediction. Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak.

Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification.

The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm.

TABLE 7. Comparison of CK with inheritance metric.

Kupiainen et al. [22] conducted a systematic review of the use and impact of software metrics in ASD in industry. The authors reported that software metrics are mainly used for sprint planning, tracking progress, improving software quality, fixing software process, and motivating people.

TABLE 6. Experimental results.

TABLE 5. Experimental results.
