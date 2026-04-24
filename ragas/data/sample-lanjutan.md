# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 1

- conversation_id: 13
- user_chat_id: 587
- bot_chat_id: 588

### user_input

Apa hubungan software metrics dengan software testing?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. The use of measurement is common in all aspects of human life such as scales for buying vegetables, fruits, grocery items, gold or making estimations for reaching to the home of a friend. The applications of measurement are obvious in all disciplines such as sciences, engineering, medical and others. The measurements play a vital role in software organizations for the improvement of software processes [1], [2]. It is reported by many software quality assurance agencies that the quality of software product is strongly influenced by the quality of software process followed to develop the software product [3]. Software measurement has become an essential process in software organizations for characterizing, evaluating, predicting and improving software products, processes, and resources [4]- [6]. ISO/IEC 15939:2007 [4] defines measurement process as ''a process for establishing, planning, performing and evaluating measurement within an overall project, enterprise or organizational measurement structure''. Despite the acknowledged importance and advocated benefits of measurement processes for software engineering community, their actual applications in the software industry are limited [4], [5], [8], [9]. It is also reported in a systematic review on measurements in software engineering that software process is the least measured entity [35]. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 1)

4. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

5. TABLE 2. Class-level software metric used in this study.

Tabel ini memuat beberapa metrik kelas untuk prediksi kesalahan perangkat lunak. Data tabel menunjukkan bahwa ada dua dataset utama: Software Metrics dan Full Dataset. Kedua dataset tersebut berbeda dalam hal variabel independen yang digunakan, yaitu ESM (Error-Severity Metric) values dan software metrics yang diekstraksi dari modul perangkat lunak.

Pada tabel ini, kita dapat melihat bahwa terdapat tiga jenis metrik ESM: IndexOutOfBounds, NullPointer, dan ClassCast. Masing-masing metrik tersebut memiliki nilai-nilai yang berbeda-beda pada kedua dataset. Pada Software Metrics Dataset, variabel independen hanya mencakup software metrics, sedangkan pada Full Dataset juga termasuk ESM values.

Dengan memperhatikan tabel ini, kita dapat menyimpulkan bahwa peneliti menggunakan metrik-metrik tersebut untuk memprediksi kesalahan perangkat lunak. Pada dataset yang lebih lengkap (Full Dataset), penulis juga melibatkan ESM values sebagai variabel independen tambahan. Hal ini menunjukkan bahwa penulis ingin mengetahui bagaimana pengaruh nilai-nilai ESM terhadap performa model pelatihan machine learning.

Dalam konteks yang lebih luas, tabel ini memberikan gambaran tentang cara peneliti menggunakan metrik kelas untuk prediksi kesalahan perangkat lunak. Penemuan penulis dapat berguna dalam meningkatkan akurasi model pemodelan perangkat lunak dan mengidentifikasi potensi masalah yang mungkin terjadi pada sistem. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 6)

6. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

7. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

8. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

### response

Berikut adalah jawaban berdasarkan konteks yang diberikan:

Software metrics digunakan untuk memprediksi kemungkinan adanya kesalahan pada kelas-kelas perangkat lunak, sehingga dapat membantu software engineers untuk meningkatkan kualitas perangkat lunak dan mengurangi biaya pengujian dan pemeliharaan. Dengan menggunakan software metrics, software evaluators dapat merencanakan ujian berdasarkan bagian-bagian yang paling rentan akan kesalahan.

Selain itu, software metrics juga digunakan untuk meningkatkan efektivitas testing, seperti disebutkan dalam konteks [Source: Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction].

### reference


Penemuan penulis dapat berguna dalam meningkatkan akurasi model pemodelan perangkat lunak dan mengidentifikasi potensi masalah yang mungkin terjadi pada sistem. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 6) Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3) Dengan memperhatikan tabel ini, kita dapat menyimpulkan bahwa peneliti menggunakan metrik-metrik tersebut untuk memprediksi kesalahan perangkat lunak.

---

## Sample 2

- conversation_id: 13
- user_chat_id: 589
- bot_chat_id: 590

### user_input

Bagaimana software metrics membantu software maintenance?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

4. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

5. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

6. We observed that the metrics strategy solutions were the most frequently used in identifying the architectural decay, thereby these metrics can determine the architectural instability growth with the system evolution, identify the probability of the classes contributing to architectural inconsistencies, and diagnose the anomalies, whether agglomerations or individual is more correlated to architectural problems. However, the use of current metrics at the class level may be affected by size bias significantly and inefficiency automatically in detecting architectural problems, indicating that the most likely cause is the problem on how these metrics are implemented through tools and reconsideration in specifying the selection of the appropriate metrics at different locations of software components, especially when compared to the same results that achieved efficiency manually. (Software Architecture Degradation in Open Source Software: A Systematic Literature Review, page 22)

7. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

8. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

### response

Software metrics membantu software maintenance dengan:

• Memprediksi keterampilan maintainability 
• Mengidentifikasi anomali dan masalah arsitektur
• Menilai efisiensi, kemudahan perawatan, dan kompleksitas struktur program

### reference


We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability.

---

## Sample 3

- conversation_id: 13
- user_chat_id: 591
- bot_chat_id: 592

### user_input

Bagaimana software metrics dapat memantau software development?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

4. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

5. Kupiainen et al. [22] conducted a systematic review of the use and impact of software metrics in ASD in industry. The authors reported that software metrics are mainly used for sprint planning, tracking progress, improving software quality, fixing software process, and motivating people. The authors reported that metrics like velocity, effort estimation, customer satisfaction, defect count, technical debt and build are used prominently in ASD. In their systematic review, Tahir et al. [46] observed that metrics for defects, effort, size, duration, productivity, employee commitment, and customer satisfaction are commonly reported in the state of the art. These findings complement another review by Gómez et al. [15], where complexity and size were found to be the most measured attributes in MPs. Other usage of metrics in ASD discussed in the literature are for planning and tracking software development [22], understanding development performance and product quality [48], measuring process quality [50], estimating effort [47], and reporting progress and quality to stakeholders not involved in the actual development [4]. Taken together, metrics targeting sprint planning, fixing software process, effort estimation, development performance, and software defects can be used to measure an organization's process performance. However, this objective is not expressly stated in any of the reviews mentioned above. On the contrary, [22] remarked that more studies are needed to explore the rationale behind utilizing the metrics the authors found in their review. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3)

6. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

7. Once the selection was made, at each Scrum Team retrospective meeting, the team usually spends 15 to 20 minutes on visualizing and analysing these selected process metrics. Process metrics are a great fit since this part of the meeting is devoted to people, processes, tools, lessons learnt and how to improve the way of working. Of course the role of the Product Owner and Scrum Master is to make those discussions and displays interesting, but this turned out to be an easy job for them, because developers usually like statistics and some trends/graphs, such as those shown in the previous section. These results, trends and metrics values are used to motivate the team and improve the process, and also to find the problems in order to resolve them. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

8. Different models for assessing the maturity of software products have been created and implemented:

• The Software Engineering Institute (SEI) at Carnegie Mellon University developed the Capability Maturity Model Integration (CMMI) [31] process model, which assists companies measure and improving their development processes while also delivering high-quality products.

• Alshayeb et al. [32], [33], proposed a framework to evaluate the maturity of software products called Technical-CMMI (T-CMMI).

• Eckert et al. [34] developed a model to measure the maturity level of Inner Source implementation, which is the process of adopting open-source software development practices for the internal development activities of an organization.

• Al-Qutaish and Abran [35] proposed the Software Product Quality Maturity Model (SPQMM), which measures the quality of a software product.

• The EuroScope consortium [36] developed a model to assess software product quality called the SCOPE Maturity Model (SMM).

• April et al. [37] proposed the Software Maintenance Maturity Model (SMmm), based on the CMMI, to assess and improve the quality of software maintenance activities.

• Da Silva and de Barros [38] presented an information security maturity model for software developers based on ISO 27001; it was evaluated by subject experts and utilized to measure the maturity level of several organizations. (Security Assurance Model of Software Development for Global Software Development Vendors, page 1)

### response

Menurut konteks, software metrics dapat memantau software development dengan cara:

* Mengukur kompleksitas dan kualitas software
* Mengestimasikan biaya dan upaya proyek
* Mendukung penilaian mutu software
* Memperkirakan keandalan software
* Mendukung pengambilan keputusan di seluruh siklus pengembangan perangkat lunak (SDLC)

Sumber: [Source: Measuring and Improving Agile Processes in a Small-Size Software Development Company]

### reference


On the contrary, [22] remarked that more studies are needed to explore the rationale behind utilizing the metrics the authors found in their review. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3) These results, trends and metrics values are used to motivate the team and improve the process, and also to find the problems in order to resolve them. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1) Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24].

---

## Sample 4

- conversation_id: 13
- user_chat_id: 593
- bot_chat_id: 594

### user_input

Bagaimana machine learning dapat memanfaatkan software metrics untuk prediksi defect?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Object-oriented metrics have been empirically validated to predict design flaws. Large and complex software systems are usually faulty [11]. It is difficult to keep them away from faults or to decrease risk of faults in upcoming version. According to [75], focus of verification and verification activities is to classify and remove high-risk problems in software. In order to avoid or squeeze faults, quality control models for example fault-prone models can be used for prediction of classes likely to be faulty. In order to attain these objectives, several researchers studied faults in software and constructed fault-proneness models base, on the event of failure [10], [34], [47], [76], [77]. Software prediction models are constructed using a variety of machine learning methods, such as Genetic Programming [78], Decision Trees [79], Neural Networks [80], Naive Bayes (NB) [21], Case-Based Reasoning [81], and Blurring Logic [82]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

4. The set of features are consisting of single or multiple metrics derived through artifacts of software, it is believed that these are useful to predict labels of class. All of the metrics are grouped into the product, project, and process metrics. It is observed that metrics of the product are mostly utilized in the research arena [31]. The further level of product metrics includes method, class, and file levels where overall 60% method-level metrics are utilized followed by 24% classlevel metrics [15]. Metrics of the product also consist of, volume, design, code, and complexity metrics. The performance of SFP heavily depends on these metrics. Researchers have assessed the utilization rate of metrics in [32] where highly use product metrics in software fault prediction are Halstead [1], McCabe [3], LoC in structural programming, and in object-oriented paradigm C&K metrics suite [33]. The subject metrics are become the approved standard metrics in software fault prediction. PROMISE and D'Ambros [34] are frequently used datasets repositories having these metrics. Both the repositories encompass datasets of about fifty-two percent of the research paper published after 2005 [9]. Since these datasets are publicly available therefore it is frequently used. The other reason is the non-availability of bug's data of industrial software. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 4)

5. TABLE 2. Frequently Used Metrics in Software Fault Prediction.

Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak. Lima belas penelitian yang disebutkan menunjukkan bahwa beberapa metrik telah digunakan secara luas dalam prediksi kegagalan, seperti metrik yang terkait dengan sifat objek-oriented dan perilaku pengguna.

Variabel utama di tabel ini meliputi nama penulis, judul penelitian, metode yang digunakan, serta hasil yang diperoleh. Nilai penting dari tabel ini adalah penemuan bahwa beberapa metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak.

Pola penting dapat dilihat dari kemunculan istilah-istilah seperti "C&K metrics" dan "Li and Henry," yang mengindikasikan bahwa ada metrik yang secara konsisten digunakan dalam penelitian-penelitian ini. Selain itu, juga terlihat bahwa beberapa penulis menggunakan kombinasi berbagai metode analisis untuk mencapai hasil prediksi yang lebih akurat.

Insight singkat dari tabel ini adalah pentingnya penggunaan metrik-metrik tertentu dalam prediksi kegagalan perangkat lunak. Dengan demikian, penelitian ini menunjukkan bahwa dengan memahami dan menggunakan metrik yang tepat, kita dapat meningkatkan akurasi prediksi kegagalan perangkat lunak. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 13)

6. The metrics of object-oriented are utilized for prediction of software quality. The characteristics that ascertain the software quality are understandability, fault tolerance, maintainability, defect density, reusability, normalized rework rate, and many others. Numerous studies have been performed including object-oriented metrics verification through empirical research paper on open-source software in the context of fault prediction utilizing {loc}, {lcom}, {cbo}, {dit}, and {noc} metrics [80]. Reusability investigation on systems based on object-oriented utilizing metrics of coupling, inheritance, and cohesion [81], heuristic-based C&K metrics evaluation [82], reusability metrics for the design of objectoriented [83], empirical scrutiny of C&K metrics for the complexity of object-oriented design [84]. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 12)

7. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

8. The prediction of software faults is the subject of several studies. Many techniques have been proposed for predicting a software fault, including Statistical and Machine Learning methods. These are described as:

Statistical methods are used to find a clear mathematical formula that absolutely identifies how classification should be performed. Kapila and Singh [85] used two statistical approaches to carry out his study: Logistic Regression and Univariate Binary Logistic Regression (UBR) which are useful for analysis of data with binary variables. In Bayesian inference [85], the design of the model relates the metrics with the content of software faults and the tendency of faults. The regression analysis is extensively utilized for prediction of bad smell in the code and linear regression in a case where only two classes of the dependent variable exist. The Multilayer Perceptron (MLP) is utilized to control faulty classes and the Radial Base functions are used to classify the faults according to the different categories of faults [87]. Xing et al. defines the significance of the model of Support Vector Machine (SVM). The SVM model can be used for small amount of data. SVM delivers greater Accuracy as compare to other techniques for predicting quality of software, but the performance of SVM is low in public datasets [86]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 4)

### response

Machine learning dapat memanfaatkan software metrics untuk prediksi defect dengan menggunakan beberapa metode, seperti:

* Menggunakan algoritma klasifikasi untuk mengidentifikasi pola dalam data metrics yang terkait dengan kegagalan perangkat lunak.
* Membuat model prediktif berdasarkan hubungan antara metrics dan kegagalan perangkat lunak.
* Menggunakan teknik pemodelan statistik, seperti Regresi Logistik dan UBR, untuk menganalisis data metrics yang terkait dengan kegagalan perangkat lunak.

Beberapa contoh metode machine learning yang digunakan dalam prediksi defect adalah:

* Neural Networks (NN) untuk membuat model prediktif berdasarkan pola dalam data metrics.
* Support Vector Machine (SVM) untuk mengidentifikasi hubungan antara metrics dan kegagalan perangkat lunak.
* Decision Trees untuk menganalisis data metrics yang terkait dengan kegagalan perangkat lunak.

Informasi tersebut ditemukan pada dokumen yang tersedia.

### reference


Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak. Nilai penting dari tabel ini adalah penemuan bahwa beberapa metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak. Insight singkat dari tabel ini adalah pentingnya penggunaan metrik-metrik tertentu dalam prediksi kegagalan perangkat lunak.

---

## Sample 5

- conversation_id: 13
- user_chat_id: 595
- bot_chat_id: 596

### user_input

Apa itu software testing?

### retrieved_context

1. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

2. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

3. Testing is a comprehensive concept related to the development of each system. In the software engineering discipline, testing is a crucial task of the software development life cycle. In contrast, software testing in any field other than software engineering can be considered as an end-user testing focused on the suitability of a software developed for a specific purpose in this field. For this reason, the multidisciplinary use of software testing makes it difficult to create a specific corpus of software testing studies in the scope of software engineering. In this context, to create a specific corpus of software testing within the scope of software engineering, a methodology including two sequential stages was followed for corpus creation, which included identifying core publication sources for the software engineering field and extracting articles specific to software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

4. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

5. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

6. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

7. The testing phase of the SDLC aims to make sure that all the system components provide their required functionality alone and as part of the whole system. Software testing is the most time-consuming, complicated, and costly process of the SDLC [92]. This phase is an important component of improving the efficiency of software development projects [32]. While it is an essential part of software development, rigorous testing is not always a focus of software engineering education [93]. As a result of this shortcoming, software developers often regard software testing as a liability, lowering overall software quality. Threat modeling is a systematic method for identifying threats that may compromise security, and it is considered a well-known accepted practice by the software testing industry [94]. This phase aims to find possible bugs and errors in the system and remove them. The present study identified 64 papers to discuss software security risks during software testing phase of SDLC. Some common security risks involved in this phase are as follows [5], [22], [95]- [98]: (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 11)

8. In the software testing stages, the aim is to develop softwareoriented products and services in a systematic and efficient manner, in which a wide range of tasks, methods, and strategies are used. Depending on the type, scope and context of the designed and developed, the methods and strategies  chosen during the software testing stages vary considerably. The findings of this study offer a wide-ranging insight into not only the themes and trends in focus but also the tools, tasks, methods, and strategies specific to software testing. Specifically, the discovered topics reveal that the most focused tasks in software testing are specification, transformation, detection, localization, generation, evaluation, optimization, verification, and prediction. The important background provided by the core tasks highlighted in this study for software testing has also been addressed by previous studies [49]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 9)

### response

Menurut ISO/IEC 24765, 2006, software testing adalah "aktivitas di mana sebuah sistem dieksekusi di bawah kondisi tertentu, hasilnya diamati atau direkam, dan evaluasi dilakukan atas beberapa aspek sistem" [6].

### reference


Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6].

---

## Sample 6

- conversation_id: 13
- user_chat_id: 597
- bot_chat_id: 598

### user_input

Mengapa software testing penting?

### retrieved_context

1. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

2. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

3. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

4. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

5. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

6. The testing phase of the SDLC aims to make sure that all the system components provide their required functionality alone and as part of the whole system. Software testing is the most time-consuming, complicated, and costly process of the SDLC [92]. This phase is an important component of improving the efficiency of software development projects [32]. While it is an essential part of software development, rigorous testing is not always a focus of software engineering education [93]. As a result of this shortcoming, software developers often regard software testing as a liability, lowering overall software quality. Threat modeling is a systematic method for identifying threats that may compromise security, and it is considered a well-known accepted practice by the software testing industry [94]. This phase aims to find possible bugs and errors in the system and remove them. The present study identified 64 papers to discuss software security risks during software testing phase of SDLC. Some common security risks involved in this phase are as follows [5], [22], [95]- [98]: (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 11)

7. Why do we need AI software testing? The fast-growing AI software and the popularity of big data-based applications bring new needs and motivations. Numerous current and future software will be built with AI-based features and functions. Existing techniques and tools are not adequate to test AI-based features and functions. There are a lack of well-defined and experience-approved quality validation models and assessment criteria. In addition, there is a lack of AI-based testing methods and solutions for AI software. Thus, the meaning of testing AI software is illustrated in a definition below. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 2)

8. Software Defects Prediction (SDP) consists in identifying defective software components, being considered an essential activity during software development. It represents the activity of identifying defective software modules in new versions of a software system [1]. SDP is considered of great importance in software engineering, as it contributes to continuously improving the software quality. Developing high quality software systems is expensive and, in this context, SDP is used for increasing the cost effectiveness of quality assurance and testing [2]. By detecting fault-prone modules in new versions of a software system, SDP helps to allocate the effort so as to test more thoroughly those modules [1]. (An in-Depth Analysis of the Software Features’ Impact on the Performance of Deep Learning-Based Software Defect Predictors, page 1)

### response

Berikut adalah jawaban berdasarkan konteks yang diberikan:

Software testing penting karena:

* Menjamin kualitas dan ketepatan sistem perangkat lunak (lihat [Source: Error-Type—A Novel Set of Software Metrics for Software Fault Prediction])
* Mengidentifikasi masalah sebelum produk akhir disetujui oleh pelanggan (lihat [Source: Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years])
* Meningkatkan efisiensi pengembangan perangkat lunak dengan memprioritaskan modul yang paling mungkin mengandung kesalahan (lihat [Source: Systematic Literature Review on Security Risks and its Practices in Secure Software Development])

### reference


Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2) Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2) As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

---

## Sample 7

- conversation_id: 13
- user_chat_id: 599
- bot_chat_id: 600

### user_input

Apa tujuan software testing?

### retrieved_context

1. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

2. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

3. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

4. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

5. Testing is a comprehensive concept related to the development of each system. In the software engineering discipline, testing is a crucial task of the software development life cycle. In contrast, software testing in any field other than software engineering can be considered as an end-user testing focused on the suitability of a software developed for a specific purpose in this field. For this reason, the multidisciplinary use of software testing makes it difficult to create a specific corpus of software testing studies in the scope of software engineering. In this context, to create a specific corpus of software testing within the scope of software engineering, a methodology including two sequential stages was followed for corpus creation, which included identifying core publication sources for the software engineering field and extracting articles specific to software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

6. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

7. In the software testing stages, the aim is to develop softwareoriented products and services in a systematic and efficient manner, in which a wide range of tasks, methods, and strategies are used. Depending on the type, scope and context of the designed and developed, the methods and strategies  chosen during the software testing stages vary considerably. The findings of this study offer a wide-ranging insight into not only the themes and trends in focus but also the tools, tasks, methods, and strategies specific to software testing. Specifically, the discovered topics reveal that the most focused tasks in software testing are specification, transformation, detection, localization, generation, evaluation, optimization, verification, and prediction. The important background provided by the core tasks highlighted in this study for software testing has also been addressed by previous studies [49]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 9)

8. The testing phase of the SDLC aims to make sure that all the system components provide their required functionality alone and as part of the whole system. Software testing is the most time-consuming, complicated, and costly process of the SDLC [92]. This phase is an important component of improving the efficiency of software development projects [32]. While it is an essential part of software development, rigorous testing is not always a focus of software engineering education [93]. As a result of this shortcoming, software developers often regard software testing as a liability, lowering overall software quality. Threat modeling is a systematic method for identifying threats that may compromise security, and it is considered a well-known accepted practice by the software testing industry [94]. This phase aims to find possible bugs and errors in the system and remove them. The present study identified 64 papers to discuss software security risks during software testing phase of SDLC. Some common security risks involved in this phase are as follows [5], [22], [95]- [98]: (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 11)

### response

Menurut konteks, beberapa tujuan software testing adalah:

* Memastikan bahwa sistem berfungsi dengan benar dan sesuai dengan spesifikasi
* Mengidentifikasi kesalahan atau kegagalan dalam sistem
* Meningkatkan kualitas dan keandalan sistem
* Menghemat waktu dan sumber daya dalam proses pengembangan perangkat lunak

Namun, perlu diingat bahwa tujuan software testing dapat bervariasi tergantung pada konteks dan jenis proyek.

### reference


Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

---

## Sample 8

- conversation_id: 13
- user_chat_id: 601
- bot_chat_id: 602

### user_input

Bagaimana software testing meningkatkan software quality?

### retrieved_context

1. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

2. Humphrey [Humphrey 1989] argued that software quality can be improved by improving its development process. Both academia and industry are striving to find ways for software process improvement (SPI). There are numerous SPI framework and methodologies available today, but they all have one challenge in common: the cost of experimenting with the process change. It is widely claimed that software process simulation modeling can help in predicting the benefits and repercussions of a process change, thus enabling organizations to make more informed decisions and reduce the likelihood of failed SPI initiatives [8]. (Change-Oriented Open Source Software Process Simulation, page 12)

3. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

4. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

5. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

6. TABLE 1. Examples of actions to improve software quality for the adalah tabel yang menyajikan contoh tindakan untuk meningkatkan kualitas perangkat lunak dengan menggunakan alat analitik perangkat lunak. Tabel ini terdiri dari 38 baris dan memiliki 8 kolom.

Tabel tersebut menjelaskan beberapa indikator strategis yang digunakan untuk mengevaluasi kinerja perangkat lunak, seperti "Blocking" yang merupakan indikator strategis untuk mengidentifikasi potensi masalah dalam proses pengembangan. Dalam tabel ini juga dapat dilihat bahwa ada empat faktor utama yang digunakan untuk menilai kualitas perangkat lunak: Code Smells, Design Issues, Performance, dan Security.

Salah satu contoh kasus yang disajikan dalam tabel adalah "Blocking" files problem yang dialami oleh perusahaan NeverLate. Dalam kasus ini, analis perangkat lunak dapat menggunakan alat analitik untuk mengidentifikasi klas-klas file yang memiliki kualitas rendah dan membutuhkan perbaikan.

Analisis dari tabel menunjukkan bahwa perusahaan yang menggunakan Q-Rapids dapat meningkatkan kualitas perangkat lunak mereka dengan menggunakan data historis dan visualisasi data. Dengan demikian, mereka dapat mengidentifikasi masalah-masalah yang signifikan dan mengambil tindakan untuk memperbaiki kinerja perangkat lunak.

Dalam kesimpulan, tabel ini menunjukkan bahwa penggunaan alat analitik perangkat lunak dapat membantu meningkatkan kualitas perangkat lunak dengan cara yang lebih objektif dan data-driven. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 6)

7. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

8. Worldwide software development expenditure, for year 2014, was 3.8 billion dollars which included 23% quality control and testing cost for business applications [4]. Early fault detection helps save costs, time, and reduce the complexity of the software because it is proportionate to the testing. It is a well known fact that extensive testing are impossible [5]. Testing cost sometimes amounts to over fifty percent of the The associate editor coordinating the review of this manuscript and approving it for publication was Claudio Agostino Ardagna . entire software development cost. It is for these reasons that it is more feasible to detect and test classes with faults to produce software with better quality. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

### response

Software testing meningkatkan kualitas perangkat lunak dengan cara:

* Mengevaluasi dan menunjukkan perilaku sistem perangkat lunak untuk memastikan bahwa itu sesuai dengan spesifikasinya (ISO/IEC 24765, 2006) [6].
* Mengidentifikasi potensi masalah dalam proses pengembangan dan memperbaiki kinerja perangkat lunak (contoh kasus "Blocking" files problem di NeverLate).
* Meningkatkan efisiensi alokasi sumber daya testing dengan melakukan prediksi kegagalan perangkat lunak (SFP) untuk mengidentifikasi modul perangkat lunak yang paling mungkin gagal.
* Mengurangi biaya dan waktu pengembangan perangkat lunak dengan mendeteksi kegagalan awal dan memperbaiki kualitas perangkat lunak.

Informasi tersebut ditemukan pada dokumen "Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years", "Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study", dan "Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper".

### reference


Dalam kesimpulan, tabel ini menunjukkan bahwa penggunaan alat analitik perangkat lunak dapat membantu meningkatkan kualitas perangkat lunak dengan cara yang lebih objektif dan data-driven. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 6) Tabel tersebut menjelaskan beberapa indikator strategis yang digunakan untuk mengevaluasi kinerja perangkat lunak, seperti "Blocking" yang merupakan indikator strategis untuk mengidentifikasi potensi masalah dalam proses pengembangan. Analisis dari tabel menunjukkan bahwa perusahaan yang menggunakan Q-Rapids dapat meningkatkan kualitas perangkat lunak mereka dengan menggunakan data historis dan visualisasi data.

---

## Sample 9

- conversation_id: 13
- user_chat_id: 603
- bot_chat_id: 604

### user_input

Apa hubungan software testing dengan software development?

### retrieved_context

1. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

2. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

3. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

4. Testing is a comprehensive concept related to the development of each system. In the software engineering discipline, testing is a crucial task of the software development life cycle. In contrast, software testing in any field other than software engineering can be considered as an end-user testing focused on the suitability of a software developed for a specific purpose in this field. For this reason, the multidisciplinary use of software testing makes it difficult to create a specific corpus of software testing studies in the scope of software engineering. In this context, to create a specific corpus of software testing within the scope of software engineering, a methodology including two sequential stages was followed for corpus creation, which included identifying core publication sources for the software engineering field and extracting articles specific to software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

5. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

6. The testing phase of the SDLC aims to make sure that all the system components provide their required functionality alone and as part of the whole system. Software testing is the most time-consuming, complicated, and costly process of the SDLC [92]. This phase is an important component of improving the efficiency of software development projects [32]. While it is an essential part of software development, rigorous testing is not always a focus of software engineering education [93]. As a result of this shortcoming, software developers often regard software testing as a liability, lowering overall software quality. Threat modeling is a systematic method for identifying threats that may compromise security, and it is considered a well-known accepted practice by the software testing industry [94]. This phase aims to find possible bugs and errors in the system and remove them. The present study identified 64 papers to discuss software security risks during software testing phase of SDLC. Some common security risks involved in this phase are as follows [5], [22], [95]- [98]: (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 11)

7. Test planning is the first step in the testing phase. The testing team begins planning tests during the implementation phase because test planning does not necessitate access to

TABLE 4. (Continued.) CSSRs and its practices in the secure coding phase of the secure SDLC.

program code. While the developers are working on code, the testing team prepares for the testing activity later. The security testing teams develop test cases based on design papers, threat models, and misuse situations. Security test cases aim to attack software successfully. Any modification to the software design must be disclosed to the testing team during the planning phase of the test. As a result, the testing team may create test cases that aren't relevant. Based on the nature of the software and its threats, the severity of bugs is adjusted. A minor bug in software code that isn't very important to how it works may only take a few minutes to fix, but it can significantly affect how secure it is. A discussion of the revised severities takes place with the development team. Table 5 shows the security operations conducted during the testing phase [3], [17], [80], [84]- [86]. (Security Assurance Model of Software Development for Global Software Development Vendors, page 1)

8. In the software testing stages, the aim is to develop softwareoriented products and services in a systematic and efficient manner, in which a wide range of tasks, methods, and strategies are used. Depending on the type, scope and context of the designed and developed, the methods and strategies  chosen during the software testing stages vary considerably. The findings of this study offer a wide-ranging insight into not only the themes and trends in focus but also the tools, tasks, methods, and strategies specific to software testing. Specifically, the discovered topics reveal that the most focused tasks in software testing are specification, transformation, detection, localization, generation, evaluation, optimization, verification, and prediction. The important background provided by the core tasks highlighted in this study for software testing has also been addressed by previous studies [49]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 9)

### response

Software testing memiliki hubungan yang erat dengan software development karena proses testing dianggap sebagai bagian penting dalam siklus hidup perangkat lunak (SDLC). Software testing dilakukan untuk memastikan bahwa sistem komponen dapat memberikan fungsi yang dibutuhkan secara tunggal dan sebagai bagian dari sistem keseluruhan.

Menurut konteks, software testing adalah proses pengamatan dan demontrasi perilaku sistem perangkat lunak untuk memenuhi spesifikasi. Proses ini dilakukan pada berbagai tahap dalam SDLC, termasuk validasi persyaratan awal hingga penerimaan produk akhir oleh pelanggan.

Selain itu, konteks juga menyebutkan bahwa software testing memiliki hubungan dengan kegiatan lain seperti:

* Validasi persyaratan awal
* Penerimaan produk akhir oleh pelanggan
* Pengembangan perangkat lunak
* Kegiatan pengujian yang dilakukan pada tahap-tahap tertentu dalam SDLC.

### reference


The testing phase of the SDLC aims to make sure that all the system components provide their required functionality alone and as part of the whole system. The present study identified 64 papers to discuss software security risks during software testing phase of SDLC. Software testing is the most time-consuming, complicated, and costly process of the SDLC [92].

---

## Sample 10

- conversation_id: 13
- user_chat_id: 605
- bot_chat_id: 606

### user_input

Bagaimana software testing membantu software maintenance?

### retrieved_context

1. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

2. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

3. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

4. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

5. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

6. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

7. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

8. Worldwide software development expenditure, for year 2014, was 3.8 billion dollars which included 23% quality control and testing cost for business applications [4]. Early fault detection helps save costs, time, and reduce the complexity of the software because it is proportionate to the testing. It is a well known fact that extensive testing are impossible [5]. Testing cost sometimes amounts to over fifty percent of the The associate editor coordinating the review of this manuscript and approving it for publication was Claudio Agostino Ardagna . entire software development cost. It is for these reasons that it is more feasible to detect and test classes with faults to produce software with better quality. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

### response

Berikut adalah jawaban berdasarkan konteks yang diberikan:

Software testing membantu software maintenance dengan cara:

* Mengidentifikasi bug dan kesalahan dalam kode, sehingga dapat diatasi sebelum menimbulkan masalah lebih besar.
* Meningkatkan kualitas kode melalui refactoring dan perbaikan desain.
* Mendeteksi "code smells" yang dapat mengganggu kinerja software.
* Menggunakan agent autonomi untuk melakukan pemeliharaan kode, seperti bug-fixing agents, migration agents, dan lain-lain.

Sumber: [Source: Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review], [Source: Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction]

### reference


It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1) Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3) Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

---

## Sample 11

- conversation_id: 13
- user_chat_id: 609
- bot_chat_id: 610

### user_input

Bagaimana Agile software development mempengaruhi software testing?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. Generally, many of the traditional SRGMs are based on similar assumptions [1], [8]. In some cases, faults detected during testing may not be corrected immediately. This delay in fault correction can be caused by various factors such as prioritization of tasks, availability of resources, or complexity of the fault. As a result, the software reliability growth process can be impacted, and traditional SRGMs may not accurately reflect the actual reliability of the software. To address this, some SRGMs have been developed to account for delayed fault correction and other factors that may affect the software reliability growth process [11], [12], [15]. Raymond and O'Reilly [6] noticed that beta testing plays a crucial role in the testing of OSS. Therefore, the test team for OSS is often separate from the development team. When a fault is detected in OSS, developers typically require additional time to communicate with testers and rectify the issue. This situation often leads to longer debugging times for OSS, and delays in the fault correction process are more likely to occur. (Using Modified Diffusion Models for Reliability Estimation of Open Source Software, page 3)

3. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

4. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

5. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

6. Worldwide software development expenditure, for year 2014, was 3.8 billion dollars which included 23% quality control and testing cost for business applications [4]. Early fault detection helps save costs, time, and reduce the complexity of the software because it is proportionate to the testing. It is a well known fact that extensive testing are impossible [5]. Testing cost sometimes amounts to over fifty percent of the The associate editor coordinating the review of this manuscript and approving it for publication was Claudio Agostino Ardagna . entire software development cost. It is for these reasons that it is more feasible to detect and test classes with faults to produce software with better quality. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

7. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

8. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

### response

Agile software development dapat mempengaruhi software testing dengan cara:

* Meningkatkan frekuensi perilisan produk sehingga software testing harus dilakukan lebih sering dan dalam waktu yang singkat.
* Membutuhkan tight connection antara pengembangan dan integrasi untuk mendeteksi kesalahan secepat mungkin.
* Menggunakan praktek-praktek agile seperti continuous integration untuk memastikan bahwa kesalahan dapat dikenali dan diperbaiki segera.

Referensi: 
- [Source: Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study]
- [Source: Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years]

### reference


Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2) Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3) As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

---

## Sample 12

- conversation_id: 13
- user_chat_id: 611
- bot_chat_id: 612

### user_input

Bagaimana software testing dilakukan pada sistem machine learning?

### retrieved_context

1. Although there are many successful studies about the automated generation of test cases, determining whether a program has passed a given test remains largely manual. Langdon et al. [16] proposed the use of search-based learning from existing open-source test suites to automatically generate partially correct test oracles. They argued that mutation testing, n-version computing, and machine learning could be combined to allow automated output checking to catch up with progress on automated input generation.

AI software testing differs from AI-based software testing in diverse views such as test objectives, test focuses, test scope, test coverage as well as test techniques and tools. For example, AI-based testing primarily aims to increase efficiency for a test process, reduce testing costs by reduce human operations, and increase bug detection effectiveness and speed. AI testing aims to provide on-demand testing services for AI software to support software validation and quality engineering process. AI-based testing majorly focuses on test selection, automatic test execution, bug detection and prediction based large-scale testing history data and AI techniques. In addition, AI testing needs innovative continuous, timeliness, and currency testing techniques. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

2. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

3. AI software testing could be performed using the following approaches from different perspectives.

-Classification-based AI software testing, in which classification models for test inputs, contexts, and outputs and events are set up to ensure the adequate testing coverage of diverse input data classes, classified contexts and conditions, and corresponding outputs and classes [20]- [24]. -Model-based AI software testing, in which selected intelligent learning models and data models are extended to be traceable and testable AI test models to facilitate AI software testing and operations in quality assessment of training data and test data. -Metamorphic (Non-Oracle) testing, in which a property-based software testing technique is used as an effective approach for addressing the test oracle problem and test case generation problem [25]- [28].

The key element of metamorphic testing (MT) is a set of Metamorphic Relations (MRs), which are necessary features of the target function or algorithm in relation to multiple inputs and their expected outputs. -Learning-based AI software testing using the crowdsourced approach, in which selected machine learning models and approaches are used to learn from crowd-sources testers in a service platform [30]. -Rule-based AI software testing, in which pre-defined expert-based rules are established and used in AI test generation and validation [32], [34].

Nevertheless, how to utilize the existing traditional or intelligent approaches to AI software testing is still a great challenge currently. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 6)

4. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

5. AI-based software testing refers to the leverage and applications of AI methods and solutions to automatically optimize a software testing process in test strategy selection, test generation, test selection and execution, bug detection and analysis, and quality prediction [39], [42], [47]. It includes different testing activities in AI-based software testing. Due to the complexity of AI software and applications, traditional methods and test tools cannot meet the demands of testing these AI systems. Given this, a more effective method to test AI systems is desirable. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 1)

6. Some studies, e.g., [8], [10]- [12], have already analyzed the application of ML in SE in the past. Durelli et al. [8] conducts a systematic mapping study on the application of ML for software testing. The study highlights the use of ML techniques in various software testing activities such as testcase generation and oracle construction. Results of the study show that a vast majority of articles employ supervised learning, such as ANN and DT, to solve testing-related problems. Moreover, the key advantages and disadvantages of using ML for software testing are discussed. Mainly, the advantage of ML techniques is their scalability and efficient application to large-scale and complex software systems. The disadvantage, on the other hand, is the unavailability of data that fits well with the learning process. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

7. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

8. TABLE 6. Experimental results.

Penelitian ini menunjukkan bahwa metrik software baru yang disebut Error-Type dapat digunakan untuk memprediksi kegagalan sistem dengan lebih akurat. Dalam eksperimen ini, empat model belajar mesin (machine learning) dipadankan menggunakan dataset SoftWare Metrics dan Full Dataset.

Dari hasil eksperimen, ditemukan bahwa ketika feature selection tidak diaplikasikan, performance model belajar mesin berkurang karena masalah multi-kolinieritas yang menyebabkan pengaruh negatif terhadap hasil akhir. Namun, setelah feature selection diterapkan, masalah ini dapat dihilangkan, sehingga penggunaan metrik ESM yang baru memberikan informasi lebih bermanfaat kepada model belajar mesin.

Dengan demikian, penelitian ini berhasil menunjukkan bahwa penggunaan Error-Type sebagai metrik software baru dapat meningkatkan keakuratan prediksi kegagalan sistem dan meningkatkan performa model belajar mesin. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 9)

### response

Pada konteks [Source: A Literature Review of Using Machine Learning in Software Development Life Cycle Stages], beberapa studi telah menganalisis aplikasi ML dalam SE, termasuk pada tahapan software testing. Durelli et al. [8] melakukan studimapping sistematis tentang penggunaan ML untuk testing software.

ML digunakan dalam berbagai kegiatan testing software seperti testcase generation dan oracle construction. Hasil penelitian menunjukkan bahwa sebagian besar artikel menggunakan supervised learning, seperti ANN dan DT, untuk mengatasi masalah terkait testing. Manfaat utama penggunaan ML adalah skalabilitas dan efisiensi aplikasinya pada skala besar dan kompleks software.

Namun, kekurangan penggunaan ML dalam testing software adalah ketidaktelitian data yang sesuai dengan proses pembelajaran.

### reference


Dengan demikian, penelitian ini berhasil menunjukkan bahwa penggunaan Error-Type sebagai metrik software baru dapat meningkatkan keakuratan prediksi kegagalan sistem dan meningkatkan performa model belajar mesin. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 9) The disadvantage, on the other hand, is the unavailability of data that fits well with the learning process. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1) AI software testing could be performed using the following approaches from different perspectives. -Classification-based AI software testing, in which classification models for test inputs, contexts, and outputs and events are set up to ensure the adequate testing coverage of diverse input data classes, classified contexts and conditions, and corresponding outputs and classes [20]- [24]. -Model-based AI software testing, in which selected intelligent learning models and data models are extended to be traceable and testable AI test models to facilitate AI software testing and operations in quality assessment of training data and test data. -Metamorphic (Non-Oracle) testing, in which a property-based software testing technique is used as an effective approach for addressing the test oracle problem and test case generation problem [25]- [28].

---

## Sample 13

- conversation_id: 13
- user_chat_id: 613
- bot_chat_id: 614

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

Systematic Literature Review adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan. Fase perencanaan melibatkan menentukan topik atau pertanyaan penelitian, serta mengidentifikasi sumber-sumber informasi yang relevan. Fase pelaksanaan melibatkan mencari dan menganalisis artikel-artikel yang telah dipilih berdasarkan kriteria sebelumnya. Fase tinjauan adalah tahap akhir dalam proses SLR, di mana para peneliti akan meninjau dan menganalisis hasil-hasil dari fase sebelumnya.

### reference


Secara singkat, SLR adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan. Fase pelaksanaan melibatkan proses mencari dan menganalisis artikel-artikel yang telah dipilih berdasarkan kriteria sebelumnya. Dalam fase perencanaan, para peneliti harus menentukan topik atau pertanyaan penelitian, serta mengidentifikasi sumber-sumber informasi yang relevan.

---

## Sample 14

- conversation_id: 13
- user_chat_id: 615
- bot_chat_id: 616

### user_input

Mengapa systematic literature review penting?

### retrieved_context

1. A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49]. According to Kitchenham [49], [50], an SLR has three main phases: planning, conducting and reviewing the review, as shown in Table 1. Researchers have used the SLR process in several domains [2], [51]- [55].

The authors of this work completed all three phases of the SLR. Inter-rate reliability analyses were undertaken during the initial and final selection phases of the SLR to reduce inter-person bias. The findings of the inter-rater reliability review are discussed in Section 3.2. We followed all of the processes in the three phases of the SLR, as stated in Table 1.

TABLE 1. SLR phases. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

2. The SLR was conducted to extract critical success factors, barriers, and implementation practices from the literature. Rockart [38] defined SLR as a method of systematically collecting, analyzing, and reporting data from the literature of a specific research area and questions of interest [38].

The SLR technique was used to search for the most relevant literature by applying explicit inclusion and exclusion criteria for primary studies [38].

We followed the guidelines provided by Rockart [38] to conduct our SLR study. The approach consists of three main phases: planning, conducting, and reporting the review. A thorough discussion of the SLR study conducted for this research project can be found in our previously published articles [25], [63], [64]. (SPIIMM: Toward a Model for Software Process Improvement Implementation and Management in Global Software Development, page 3)

3. Table 1. Researchers have used the SLR process in several domain sebagai dasar penelitian ini membagikan beberapa metode dan langkah dalam melakukan Systematic Literature Review (SLR). Secara singkat, SLR adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan.

Dalam fase perencanaan, para peneliti harus menentukan topik atau pertanyaan penelitian, serta mengidentifikasi sumber-sumber informasi yang relevan. Mereka juga harus menetapkan kriteria inklusi dan eksklusi untuk memilih artikel-artikel yang akan diintervensi.

Fase pelaksanaan melibatkan proses mencari dan menganalisis artikel-artikel yang telah dipilih berdasarkan kriteria sebelumnya. Para peneliti harus mengidentifikasi informasi yang relevan, mengumpulkan data, serta melakukan analisis untuk mendapatkan hasil yang diinginkan.

Fase tinjauan adalah tahap akhir dalam proses SLR. Pada fase ini, para peneliti akan meninjau dan menganalisis hasil-hasil dari fase sebelumnya. Mereka juga harus memastikan bahwa hasil penelitian mereka tidak memiliki bias atau kesalahan.

Dalam beberapa domain yang telah diidentifikasi oleh peneliti, metode SLR digunakan untuk mengurangi ketidakakuratan dan kesalahan dalam penelitian. Penulis juga menggunakan teknik inter-rater reliability analisis untuk memastikan bahwa hasil-hasil dari fase tinjauan tidak memiliki bias.

Dalam beberapa kasus, metode SLR digunakan dalam beberapa domain, seperti informasi keamanan (security), pengembangan perangkat lunak (software development) dan sebagainya. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

4. FIGURE 1. Steps of the systematic literature review process.

Gambar ini merupakan sebuah diagram alur proses sistematis tinjauan literatur, dengan menggunakan jenis visual yang disebut flowchart. Elemen yang tampak dalam gambar tersebut adalah serangkaian simbol dan garis yang membentuk alur proses. Terdapat beberapa elemen kunci yang dapat dilihat, yaitu:

* Simbol "1." pada bagian atas gambar yang menunjukkan tahap awal dari sistematis tinjauan literatur.
* Garis horizontal yang menghubungkan simbol "1." dengan simbol berikutnya, menunjukkan bahwa tahap tersebut adalah langkah awal dalam proses sistematis tinjauan literatur.
* Simbol lainnya seperti lingkaran dan persegi panjang yang menggambarkan tahapan-tahapan selanjutnya dalam proses tersebut.

Meskipun tidak terdapat angka atau label penting secara eksplisit, namun dapat disimpulkan bahwa gambar ini menunjukkan bahwa sistematis tinjauan literatur dilakukan melalui beberapa tahap yang jelas dan sistematik. Maka dari itu, makna singkat yang dapat ditarik adalah bahwa proses sistematis tinjauan literatur merupakan suatu proses yang terstruktur dengan baik untuk mencari dan menganalisis informasi yang relevan. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

5. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

6. In this systematic literature review (SLR), we focused on examining the most reputable and reliable databases available to researchers, as previously mentioned. It is important to note that we allocated publications to specific databases based on the chronological order of the searches conducted, even though some papers might be present across multiple databases. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 5)

7. FIGURE 1. Steps of the systematic literature review process.

Gambar tersebut menampilkan langkah-langkah proses tinjauan literatur sistematis dalam format diagram alir. Diagram ini terdiri atas beberapa langkah yang disajikan secara linear, dengan koneksi antar langkah menggunakan garis berwarna biru.

Pertama-tama, gambar menunjukkan langkah persiapan (Preparation), yang mencakup identifikasi topik penelitian dan perumusan pertanyaan penelitian. Langkah ini diikuti oleh langkah pencarian literatur, yaitu proses pengumpulan dan seleksi artikel yang relevan dengan topik penelitian.

Selanjutnya, gambar menampilkan langkah analisis data, dimana hasil dari literatur yang dipilih akan dianalisis untuk mengidentifikasi temuan-temuan penting. Langkah ini diakhiri dengan konfirmasi keabsahan dan kualitas hasil penelitian, yang merupakan langkah yang sangat penting dalam proses tinjauan literatur sistematis.

Terdapat beberapa elemen yang tampak pada gambar ini, seperti simbol-simbol yang merepresentasikan masing-masing langkah, serta garis-garis yang menghubungkan antar langkah. Namun, tidak terdapat angka atau label penting yang menonjol dalam diagram ini.

Makna singkat dari gambar ini adalah sebagai peta proses tinjauan literatur sistematis, memberikan panduan langkah demi langkah untuk mengembangkan penelitian dan memastikan kualitas hasilnya. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

8. This systematic review follows a structured approach aligned with prior systematic reviews on LLM-based agents in software engineering [1], [13]. The methodology ensures comprehensive coverage of relevant literature while maintaining rigor and transparency throughout the review process. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 3)

### response

Systematic Literature Review (SLR) penting karena dapat membantu peneliti untuk mendapatkan gambaran yang lebih komprehensif tentang suatu topik atau pertanyaan penelitian. Dengan menggunakan metode SLR, peneliti dapat mengidentifikasi informasi yang relevan, menganalisis data, dan menemukan temuan-temuan penting yang terkait dengan topik tersebut.

SLR juga dapat membantu peneliti untuk:

* Mengurangi ketidakakuratan dan kesalahan dalam penelitian
* Meningkatkan kualitas hasil penelitian
* Mendapatkan gambaran yang lebih lengkap tentang suatu topik atau pertanyaan penelitian

Dalam beberapa domain, seperti informasi keamanan (security), pengembangan perangkat lunak (software development), dan sebagainya, metode SLR telah digunakan untuk mengidentifikasi kritikalitas faktor kesuksesan, hambatan, dan praktik implementasi.

### reference


Dalam beberapa domain yang telah diidentifikasi oleh peneliti, metode SLR digunakan untuk mengurangi ketidakakuratan dan kesalahan dalam penelitian. Dalam fase perencanaan, para peneliti harus menentukan topik atau pertanyaan penelitian, serta mengidentifikasi sumber-sumber informasi yang relevan. Dalam beberapa kasus, metode SLR digunakan dalam beberapa domain, seperti informasi keamanan (security), pengembangan perangkat lunak (software development) dan sebagainya. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

---

## Sample 15

- conversation_id: 13
- user_chat_id: 617
- bot_chat_id: 618

### user_input

Apa tujuan systematic literature review dalam penelitian software engineering?

### retrieved_context

1. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

2. This systematic review follows a structured approach aligned with prior systematic reviews on LLM-based agents in software engineering [1], [13]. The methodology ensures comprehensive coverage of relevant literature while maintaining rigor and transparency throughout the review process. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 3)

3. Systematic mapping or scoping studies are conducted to provide an overview of a research domain through classification. These studies mainly explore the existing literature to investigate the coverage of multiple topics, the frequency of publications, the research trends, and the publication venues where relevant studies have been published [14]. The systematic mapping in the current study mainly follows the guidelines suggested by Petersen et al. [15]. According to the guidelines for systematic mapping studies in SE [15], the essential process steps of the current systematic mapping study were defining the research questions, searching for relevant papers, screening the papers, keywording the abstracts, extracting the data, and mapping, as shown in Fig. 1. Each process step has an outcome and the outcome of the complete process is the systematic map, which is explained as follows [15]: Definition of Research Questions (Research Scope) -The primary goal of a systematic mapping study is to provide an overview of a research area and identify the quantity and type of research and results available within this area. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 1)

4. Once the conducting process had been identified, the outcomes of a systematic review could be carried out adequately by extracting the appropriate data in line with the defined research questions. Then, the data were synthesized to identify the final view of the research and a conclusion was made on what revolves around the scope of this research in the current time and future research. (Software Architecture Degradation in Open Source Software: A Systematic Literature Review, page 1)

5. The initial step in conducting a literature review is to identify a set of individual research questions. These questions guide the development of this work and inform the readers about the main focus of the study. To formulate the most appropriate research questions, we referred to the ''Goal Question Metric'' model developed by Caldiera et al. [16]. With this model, it is necessary to predetermine the analysis's objectives, target objects and issues, as well as the analytical vantage points. According to the model, we specified the purpose, target objectives, issues, and viewpoints of the analysis as follows: (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 3)

6. Although not explicitly studying SSCs, different researchers have expressed concern over the gaps in the literature on software development practice. For example, the different researchers in [2], [7], [40] explored the gaps in the literature using SMS to look at software engineering in start-ups, while others have explored gaps in software engineering in SSCs through Systematic Literature Reviews [1], [4] Studying these gaps helps researchers appreciate how research has transformed software engineering practices and is helpful to map existing studies. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 3)

7. The 3-point guideline set out statements on processes of writing the methodology, reporting the results, and writing the conclusions in a manuscript intentioned to determine a course of action while conducting research software engineering research. This guideline aims to streamline processes of writing to ensure quality of research.

The guideline is important because it has been derived from evidence in empirical literature that highlights the areas in research writing which require attention [40], [2], [148]; it takes care of the parts which are most wanting and has a significant effect on the quality of research in software engineering. The guidelines cover only what has been identified as the areas that remain unclear in software engineering literature yet are important in reproducibility, generalisability and transferability.

Akin to this, researchers are advised to make an effort to collaborate with industry to ensure transfer and widespread use of research results in industry. This will also ensure that research results are evidence-based. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 17)

8. Evidence-based software engineering prospects motivated the researchers to conduct a systematic literature review. However, the topic of EDI in software engineering is not studied in detail. Spichkova et al. [16] performed a literature review to investigate diversity in the software architecture field. Fazli and Bittner [17] also used the systematic literature review approach and studied the cultural factors of diversity and its impact on collaborative software development approaches. They analyzed 20 papers and highlighted the issues due to cultural diversity such as differences in communication, decision-making and interaction during collaboration. Menzez and Prikladnicki [18] performed a systematic literature review on team diversity in software engineering. They included only 11 papers in the study and conducted semi-structured interviews to observe the impact of diverse software development teams. They reported on the challenges and barriers faced by team members at the workplace. They concluded that the consideration of diversity and inclusion has a positive impact on software development. Traylor [19] conducted a meta-analytic investigation on the topic of team diversity-process relationships. (Practicing Equity Diversity Inclusion (EDI) in Software Development Teams: A Systematic Literature Survey, page 3)

### response

Menurut konteks, tujuan systematic literature review dalam penelitian software engineering adalah untuk:

* Mempresentasikan gambaran yang komprehensif tentang kualitas AI-based software (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review)
* Mengidentifikasi kesenjangan dan mendukung kualitas perangkat lunak dalam konteks sistem AI berbasis (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review)
* Mencapai pemahaman yang lebih baik tentang keadaan suatu bidang penelitian tertentu (Systematic literature studies in software engineering dapat mencakup tinjauan dan sintesis dari karya-karya sebelumnya, sehingga para peneliti dapat memperoleh pemahaman tentang keadaan suatu bidang penelitian tertentu)

### reference


The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2) According to the model, we specified the purpose, target objectives, issues, and viewpoints of the analysis as follows: (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 3) The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems.

---

## Sample 16

- conversation_id: 13
- user_chat_id: 621
- bot_chat_id: 622

### user_input

Bagaimana systematic literature review digunakan untuk menemukan faktor software quality?

### retrieved_context

1. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

2. Table 1 show a large number of results found by using the Tabel ini membahas tentang taksonomi penilaian kualitas untuk sistem perangkat lunak cerdas. Tabel ini menjelaskan langkah-langkah dalam melakukan tinjauan pustaka sistematis, termasuk identifikasi pertanyaan penelitian individu yang dapat memandu pengembangan dan informasi bagi pembaca tentang fokus utama dari studi tersebut.

Dari tabel ini kita bisa melihat bahwa ada beberapa langkah penting dalam melakukan tinjauan pustaka sistematis. Pertama, kita harus menentukan tujuan dan objek penelitian dengan jelas. Kemudian, kita harus mengidentifikasi pertanyaan penelitian individu yang dapat memandu pengembangan dan informasi bagi pembaca tentang fokus utama dari studi tersebut.

Kita juga bisa melihat bahwa tabel ini membahas tentang beberapa hal penting seperti:

* Identifikasi pertanyaan penelitian individu
* Menentukan tujuan dan objek penelitian
* Mengidentifikasi database literatur yang relevan
* Menggunakan teknik ekstraksi data untuk memperoleh hasil

Dari analisis tabel ini, kita bisa menyimpulkan bahwa melakukan tinjauan pustaka sistematis memerlukan langkah-langkah yang sistematis dan metodeologi. Kita harus memiliki pertanyaan penelitian individu yang jelas, menentukan tujuan dan objek penelitian dengan baik, serta menggunakan database literatur yang relevan untuk memperoleh hasil yang akurat. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 3)

3. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

4. TABLE 20. Quality assessment criterion.

Data dari tabel ini memuat informasi tentang kriteria penilaian kualitas dalam sistem literatur ulasan yang sistematis. Data menunjukkan bahwa ada dua buah karya ilmiah yang dinilai, yaitu "SA Degradation in OSS" oleh Baabad et al. dan beberapa artikel lainnya. Dua kolom utama di tabel ini adalah 'QUALITY ASSESSMENT CRI' (kriteria penilaian kualitas) dan 'TERION' (terdapat nilai yang dituliskan). Namun, dari data yang tersedia, tidak jelas arti dari isi pada kolom 'TERION'. Data juga mencakup daftar referensi yang menunjukkan beberapa artikel ilmiah terkait arsitektur perangkat lunak dan sistem penilaian kualitas. (Software Architecture Degradation in Open Source Software: A Systematic Literature Review, page 27)

5. • Purpose -Systematic literature review.

• Objective -Peer-reviewed research papers in computer science and software engineering.

• Issue -Taxonomies for evaluating the quality of intelligent software systems.

• Viewpoint -Software engineers and industry practitioners.

This SLR aims to answer the general question, ''How is quality defined or studied for AI-based software?'' Using the formulated GQM model above, this review focused on AIbased software attributes and attempted to find answers to the following research questions: RQ1: What are the existing approaches for assessing the quality of software systems for artificial intelligence? RQ2: Which measurable attributes of software systems for artificial intelligence, and which statistical or machine learning models are commonly used for estimating the quality of such systems? RQ3: How effective are such attributes and models?

The motivation for RQ1 was to understand what existing research has produced in terms of general approaches to evaluate the quality of AI-based software projects originating from open-source software project sources.

The motivation for RQ2 was to identify which particular subsets of measurable software attributes are used to define the ongoing status of intelligent systems and which methods are commonly used for the quality assessment of such systems.

The motivation for RQ3 was to rank such methods, approaches, and attributes in terms of effectiveness and reliability. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 1)

6. TABLE 8. Methods used in the reviewed papers.

Tabel ini menjabarkan metode-metode yang digunakan dalam kajian-kajian literatur terkait asesmen mutu sistem perangkat lunak cerdas. Terdapat 29 baris data dan 9 kolom variabel utama, meliputi: nama penulis, judul publikasi, tahun publikasi, metode pengukuran atribut kualitas, model pengukuran, metode analisis, alat analisis, hasil penelitian, dan catatan tambahan.

Variabel utama dalam tabel ini adalah 'Metode Pengukuran Atribut Kualitas' yang menjabarkan berbagai cara untuk mengukur atribut-atribut mutu sistem perangkat lunak cerdas. Nilai penting yang dapat dilihat dari tabel ini adalah bahwa mayoritas penelitian fokus pada pengembangan model khusus yang disesuaikan dengan konteks aplikasi tertentu, serta adanya kesenjangan dalam penggunaan metode pengukuran atribut mutu.

Insight singkat yang dapat diambil dari tabel ini adalah bahwa masih banyak penelitian yang memfokuskan pada adaptasi model kualitas yang sudah ada tanpa mengembangkan model yang lebih luas dan fleksibel untuk konteks aplikasi berbeda. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 12)

7. TABLE 1. Examples of actions to improve software quality for the adalah tabel yang menyajikan contoh tindakan untuk meningkatkan kualitas perangkat lunak dengan menggunakan alat analitik perangkat lunak. Tabel ini terdiri dari 38 baris dan memiliki 8 kolom.

Tabel tersebut menjelaskan beberapa indikator strategis yang digunakan untuk mengevaluasi kinerja perangkat lunak, seperti "Blocking" yang merupakan indikator strategis untuk mengidentifikasi potensi masalah dalam proses pengembangan. Dalam tabel ini juga dapat dilihat bahwa ada empat faktor utama yang digunakan untuk menilai kualitas perangkat lunak: Code Smells, Design Issues, Performance, dan Security.

Salah satu contoh kasus yang disajikan dalam tabel adalah "Blocking" files problem yang dialami oleh perusahaan NeverLate. Dalam kasus ini, analis perangkat lunak dapat menggunakan alat analitik untuk mengidentifikasi klas-klas file yang memiliki kualitas rendah dan membutuhkan perbaikan.

Analisis dari tabel menunjukkan bahwa perusahaan yang menggunakan Q-Rapids dapat meningkatkan kualitas perangkat lunak mereka dengan menggunakan data historis dan visualisasi data. Dengan demikian, mereka dapat mengidentifikasi masalah-masalah yang signifikan dan mengambil tindakan untuk memperbaiki kinerja perangkat lunak.

Dalam kesimpulan, tabel ini menunjukkan bahwa penggunaan alat analitik perangkat lunak dapat membantu meningkatkan kualitas perangkat lunak dengan cara yang lebih objektif dan data-driven. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 6)

8. There are two different techniques to identify the primary sources for literature review studies [44]. In the first technique, which is common in the software engineering community, search strings are developed and then executed on different digital libraries (e.g., ACM Digital Library) [45].

The second one is more common in the information systems community and starts with identifying a pool of initial papers, followed by the backward snowballing technique [23]. Jalali and Wohlin [44] applied both techniques on Agile practices in Global Software Engineering (GSD) and realized that although these techniques led to the identification of different sets of studies, no significant differences were observed in the findings. Human values have been researched in many domains across different research areas. In Section II, we discussed that there is no consensus on what human values are, and there are many values models that cover a different number of human values with various terminologies. Further to this, there is no established theory on human values within the software engineering community [19]. Due to these limitations, it was not possible for us to build a search string that covers all human values and execute it on different digital libraries. Hence, we decided to follow the approach proposed by Webster and Watson in the information systems community, which includes the following two steps [23]. Figure 2 shows our paper collection process. (Operationalizing Human Values in Software Engineering: A Survey, page 6)

### response

Systematic literature review digunakan untuk menemukan faktor-faktor yang mempengaruhi kualitas perangkat lunak melalui analisis literatur yang sistematis. Berdasarkan konteks yang diberikan, systematic literature review digunakan untuk:

* Menentukan tujuan dan objek penelitian dengan jelas
* Mengidentifikasi pertanyaan penelitian individu yang dapat memandu pengembangan dan informasi bagi pembaca tentang fokus utama dari studi tersebut
* Menggunakan teknik ekstraksi data untuk memperoleh hasil
* Menganalisis hasil penelitian untuk menemukan faktor-faktor yang mempengaruhi kualitas perangkat lunak

Dalam konteks ini, systematic literature review digunakan untuk menemukan faktor-faktor yang mempengaruhi kualitas perangkat lunak melalui analisis literatur yang sistematis dan metodeologi.

### reference


Kita juga bisa melihat bahwa tabel ini membahas tentang beberapa hal penting seperti: * Identifikasi pertanyaan penelitian individu * Menentukan tujuan dan objek penelitian * Mengidentifikasi database literatur yang relevan * Menggunakan teknik ekstraksi data untuk memperoleh hasil Dari analisis tabel ini, kita bisa menyimpulkan bahwa melakukan tinjauan pustaka sistematis memerlukan langkah-langkah yang sistematis dan metodeologi. Tabel ini menjelaskan langkah-langkah dalam melakukan tinjauan pustaka sistematis, termasuk identifikasi pertanyaan penelitian individu yang dapat memandu pengembangan dan informasi bagi pembaca tentang fokus utama dari studi tersebut. Kita harus memiliki pertanyaan penelitian individu yang jelas, menentukan tujuan dan objek penelitian dengan baik, serta menggunakan database literatur yang relevan untuk memperoleh hasil yang akurat. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 3)

---

## Sample 17

- conversation_id: 13
- user_chat_id: 623
- bot_chat_id: 624

### user_input

Apa hubungan systematic literature review dengan software metrics?

### retrieved_context

1. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

3. Kupiainen et al. [22] conducted a systematic review of the use and impact of software metrics in ASD in industry. The authors reported that software metrics are mainly used for sprint planning, tracking progress, improving software quality, fixing software process, and motivating people. The authors reported that metrics like velocity, effort estimation, customer satisfaction, defect count, technical debt and build are used prominently in ASD. In their systematic review, Tahir et al. [46] observed that metrics for defects, effort, size, duration, productivity, employee commitment, and customer satisfaction are commonly reported in the state of the art. These findings complement another review by Gómez et al. [15], where complexity and size were found to be the most measured attributes in MPs. Other usage of metrics in ASD discussed in the literature are for planning and tracking software development [22], understanding development performance and product quality [48], measuring process quality [50], estimating effort [47], and reporting progress and quality to stakeholders not involved in the actual development [4]. Taken together, metrics targeting sprint planning, fixing software process, effort estimation, development performance, and software defects can be used to measure an organization's process performance. However, this objective is not expressly stated in any of the reviews mentioned above. On the contrary, [22] remarked that more studies are needed to explore the rationale behind utilizing the metrics the authors found in their review. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3)

4. TABLE 1. Rank wise comparison of success factors across SLR and empirical study.

Data di dalam tabel menampilkan perbandingan antara faktor keberhasilan (success factors) dari studi literatur sistematis (SLR) dan penelitian empiris. Ada dua kolom utama yang dapat dilihat, yaitu peringkat (rank) untuk setiap faktor keberhasilan di SLR dan penelitian empiris.

Dari data yang tersedia, tidak ada informasi tentang variabel/kolom yang lebih spesifik selain nama-nama faktor keberhasilan. Namun, nilai atau pola penting dapat dilihat dari perbandingan antara kedua metode. Contohnya, faktor "SF20: proses evaluasi peningkatan" menerima peringkat yang lebih tinggi di penelitian empiris dibandingkan dengan SLR.

Insight singkat yang dapat disimpulkan adalah bahwa ada perbedaan dalam prioritas penilaian faktor keberhasilan antara studi literatur sistematis dan penelitian empiris. Penelitian ini menunjukkan pentingnya memahami bagaimana praktisi melihat kriteria keberhasilan dalam implementasi proses perbaikan software, yang berbeda dari apa yang telah ditulis di literatur. (SPIIMM: Toward a Model for Software Process Improvement Implementation and Management in Global Software Development, page 5)

5. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

6. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

7. There is a long history of research on metrics programs (MPs) [24], and plenty of literature recommending success factors for their implementation [17], [28], [34], [44]. However, literature on SMEs using MPs in the context of Agile is rather scarce. Moreover, the literature on measuring software processes and their role in improving SME processes is even scarcer. Measuring software processes with the use of process metrics enables objective and quantitative evaluation of software processes, which can lead to continuous improvement and learning [34], [42]. However, measuring process metrics is a challenge [43]. Software processes are inherently complex and intangible, which makes their measurement more difficult than their product counterparts [19], [41]. Ideally, measurement activities should consume little effort and time, while being adequate enough to meet an organization's measurement demands. Software organizations need to weigh in cost-efficiency while prioritizing measurement objectives and targets. SMEs have the added constraints of limited budget, ambitious deadlines, and short-term strategy [45]. Due to these reasons, measuring software processes, especially in an SME, becomes a bigger challenge. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3)

8. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

### response

Systematic Literature Review digunakan untuk melakukan analisis literatur sistematis mengenai software metrics, seperti yang disebutkan dalam konteks "Measuring and Improving Agile Processes in a Small-Size Software Development Company" [24] dan "Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review".

### reference


On the contrary, [22] remarked that more studies are needed to explore the rationale behind utilizing the metrics the authors found in their review. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3) Due to these reasons, measuring software processes, especially in an SME, becomes a bigger challenge. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3) The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

---

## Sample 18

- conversation_id: 13
- user_chat_id: 627
- bot_chat_id: 628

### user_input

Bagaimana systematic literature review dapat mengevaluasi penelitian deep learning?

### retrieved_context

1. A comprehensive literature review is imperative to identify and analyze recent advances and contributions to GAI in SD. To facilitate a systematic and rigorous examination, it is essential to implement well-defined review protocols and structured methodologies. These protocols and methodologies must be employed to ensure the efficient organization, synthesis, and interpretation of the collected evidence.

The methodology adopted for this systematic literature review followed a modified version of the guidelines for systematic literature reviews in software engineering proposed by Kitchenham and Charters [45]. This approach has been extensively applied in the field of software engineering research, including software testing [46], software quality assessment [47], software defect prediction using artificial intelligence [40], application of AI in software design [41], [48], and more recently, GAI in software design [11].

The review process consists of a sequence of structured stages, as illustrated in Fig. 1, and is aligned with the PRISMA workflow, shown in Fig. 2  [49]. The methodology comprises three main phases: planning, execution, and reporting. During the planning phase, the review scope was defined, including the study period, research questions, inclusion and exclusion criteria, and the search strategy. In the execution phase, the previously defined protocol was applied to identify, screen, and select primary studies that addressed the research

TABLE 1. SD dimension in the GAI.

questions. The selected studies were systematically analyzed and synthesized during the final phase of the study.

The results of the review included statistical analyses of the publication trends, journal distributions, and quartile rankings. These findings were examined in detail to address the research questions formulated during the planning phase and provide a comprehensive understanding of the current state of research on GAI in the SDLC.

To identify GAI opportunities for SD, it is necessary to examine the following research questions, which correspond to the four aspects of this study. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 4)

2. A comprehensive literature review is imperative to identify and analyze recent advances and contributions to GAI in SD. To facilitate a systematic and rigorous examination, it is essential to implement well-defined review protocols and structured methodologies. These protocols and methodologies must be employed to ensure the efficient organization, synthesis, and interpretation of the collected evidence.

The methodology adopted for this systematic literature review followed a modified version of the guidelines for systematic literature reviews in software engineering proposed by Kitchenham and Charters [45]. This approach has been extensively applied in the field of software engineering research, including software testing [46], software quality assessment [47], software defect prediction using artificial intelligence [40], application of AI in software design [41], [48], and more recently, GAI in software design [11].

The review process consists of a sequence of structured stages, as illustrated in Fig. 1, and is aligned with the PRISMA workflow, shown in Fig. 2  [49]. The methodology comprises three main phases: planning, execution, and reporting. During the planning phase, the review scope was defined, including the study period, research questions, inclusion and exclusion criteria, and the search strategy. In the execution phase, the previously defined protocol was applied to identify, screen, and select primary studies that addressed the research

TABLE 1. SD dimension in the GAI.

questions. The selected studies were systematically analyzed and synthesized during the final phase of the study.

The results of the review included statistical analyses of the publication trends, journal distributions, and quartile rankings. These findings were examined in detail to address the research questions formulated during the planning phase and provide a comprehensive understanding of the current state of research on GAI in the SDLC.

To identify GAI opportunities for SD, it is necessary to examine the following research questions, which correspond to the four aspects of this study. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 4)

3. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

4. Many kinds of research attempt to find solutions for the current obstacles of Machine Learning Systems. To draw optimal decision making, approaches such as Fault Tree Analysis, Fuzzy Logic, Metaheuristic Algorithm, and Artificial Neural Network are developed to test with a huge amount of training data by using different algorithms. However, the sufficiency and versatility of Deep Learning systems are based on the accuracy of the test data set. It is difficult to provide adequate support due to the accessibility of test data quality issue. The current Deep Learning systems have various vulnerabilities and their system analysis and defect detection are extremely difficult. Unlike traditional software systems, Machine Intelligence does not have a clear controllable logic and understandability since the process to make decisions rely on the training data. The recent study shows two major vulnerabilities in Deep Learning systems: Software quality from the output of Deep Learning alone is not adequate; and Failure in unseen attacks even though Deep Learning is immune to known types of attacks [18], [19]. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 1)

5. A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49]. According to Kitchenham [49], [50], an SLR has three main phases: planning, conducting and reviewing the review, as shown in Table 1. Researchers have used the SLR process in several domains [2], [51]- [55].

The authors of this work completed all three phases of the SLR. Inter-rate reliability analyses were undertaken during the initial and final selection phases of the SLR to reduce inter-person bias. The findings of the inter-rater reliability review are discussed in Section 3.2. We followed all of the processes in the three phases of the SLR, as stated in Table 1.

TABLE 1. SLR phases. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

6. The present study was carried out using one of the SLR methods most successfully and widely applied in software engineering field. Specially, the Kitchenham's method [30]. This method present rigorous stages to analyze research knowledge using a trustworthy and auditable methodology. Some authors, however, have criticized Kitchenham's method and/or proposed improvements on this one [15], [31].

In the wake of these criticisms and suggestions for improvement, Kitchenham published an updated version of her method in [30]. But, at present, some authors [15] admit that an important gap still exists regarding the evaluation of quality in studies based on empirical methods.

This SLR follows the latest version of Kitchenham's method, referenced above. It describes three phases for executing a systematic review: (1) planning, which defines aspects such as the need for the research, review protocol and research questions; (2) conducting, which the previously established protocol is carried out; and (3) reporting, which presents the final analysis to answer each research question.

Figure 1 shows these phases and their tasks on a timeline to achieve research objective of this article. (Model-Based Software Design and Testing in Blockchain Smart Contracts: A Systematic Literature Review, page 2)

7. Deep Learning is designed to continually analyze data with a logic structure as mimicking how a human can draw a conclusion. The deep learning needs a huge number of data sets to use input in the algorithms in order to result in a more accurate prediction. For instance, Google's AlphaGo, a sharp intellect and intuition game, learns by itself without predefined data. It makes a more specific move and becomes the greatest player of all. Deep Learning defines a new paradigm based on data-driven programming. Since Machine Intelligence or Deep Learning depends on the training data, the accuracy and quality of data play a vital role for public safety using machine learning in autonomous vehicles. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

8. [50] AF Agarap. Deep learning using rectified linear units (ReLU). (2018)

[51] D Boob, SS Dey, G Lan. Complexity of training ReLU neural network. (2020-05)

[52] M Jørgensen. Unit effects in software project effort estimation: Workhours gives lower effort estimates than workdays. (2016-07)

[53] A Idri, M Hosni, A Abran. Systematic literature review of ensemble effort estimation. (2016-08)

[54] Y Mahmood, N Kama, A Azmi, AS Khan, M Ali. Software effort estimation accuracy prediction of machine learning techniques: A systematic performance evaluation. (2022-01)

[55] SS Ali, MS Zafar, MT Saeed. Effort estimation problems in software maintenance-A survey. (2020-01)

[56] CF Kemerer. An empirical validation of software cost estimation models. (1987-05)

[57] Z Li. Intelligently predict project effort by reduced models based on multiple regressions and genetic algorithms with neural networks. (2010-05)

[58] A Idri, I Abnane, A Abran. Evaluating Pred(p) and standardized accuracy criteria in software development effort estimation. (2018-04)

[59] S.-J Huang, N.-H Chiu. Applying fuzzy neural network to estimate software development effort. (2009-04)

[60] SH S Moosavi, VK Bardsiri. Satin bowerbird optimizer: A new optimization algorithm to optimize ANFIS for software development effort estimation. (2017-04)

[61] F González-Ladrón-De-Guevara, M Fernández-Diego, C Lokan. The usage of ISBSG data fields in software effort estimation: A systematic mapping study. (2016-03)

[62] WD O Bussab, PA Morettin, Estatística Básica. (2010)

[63] G Schneider, JP Winters. Applying Use Cases: A Practical Guide. (2001) (Heterogeneous Ensemble Model to Optimize Software Effort Estimation Accuracy, page 1)

### response

Menurut konteks yang diberikan, systematic literature review dapat mengevaluasi penelitian deep learning dengan menggunakan metode Kitchenham. Metode ini terdiri dari tiga fase: planning (perencanaan), conducting (pengembangan), dan reporting (laporan). Fase planning meliputi definisi aspek-aspek seperti kebutuhan penelitian, protokol tinjauan, dan pertanyaan penelitian. Fase conducting melibatkan pelaksanaan protokol yang telah ditetapkan sebelumnya, sedangkan fase reporting melibatkan presentasi hasil analisis akhir untuk menjawab masing-masing pertanyaan penelitian.

Sumber: [Source: Model-Based Software Design and Testing in Blockchain Smart Contracts: A Systematic Literature Review]
The present study was carried out using one of the SLR methods most successfully and widely applied in software engineering field. Specially, the Kitchenham's method [30]. This method present rigorous stages to analyze research knowledge using a trustworthy and auditable methodology. 

Pertanyaan lainnya tidak dapat dijawab berdasarkan konteks yang diberikan.

### reference


The present study was carried out using one of the SLR methods most successfully and widely applied in software engineering field. This method present rigorous stages to analyze research knowledge using a trustworthy and auditable methodology. It describes three phases for executing a systematic review: (1) planning, which defines aspects such as the need for the research, review protocol and research questions; (2) conducting, which the previously established protocol is carried out; and (3) reporting, which presents the final analysis to answer each research question.

---

## Sample 19

- conversation_id: 13
- user_chat_id: 629
- bot_chat_id: 630

### user_input

Mengapa systematic literature review berguna untuk topik software maintenance?

### retrieved_context

1. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

2. The current research involves collecting data through an online questionnaire based survey. Adopting online survey for data collection is more effective technique compared to other observational approaches as it allows for a broader reach within the population [30], [31], [32], [33]. The questionnaire is designed using the online survey tool (Google form) to receive the experts' responses. It consists of questions that focus on the importance of software maintenance in GSD context. Specifically, the designing purpose of questionnaire is to uncover the interconnectedness among the factors. (An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective, page 4)

3. The current research involves collecting data through an online questionnaire based survey. Adopting online survey for data collection is more effective technique compared to other observational approaches as it allows for a broader reach within the population [30], [31], [32], [33]. The questionnaire is designed using the online survey tool (Google form) to receive the experts' responses. It consists of questions that focus on the importance of software maintenance in GSD context. Specifically, the designing purpose of questionnaire is to uncover the interconnectedness among the factors. (An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective, page 4)

4. We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig. 3. 136 out of 263 (52%) articles belong to quality assurance and analytic. 44 out of 263 (17%) articles have focused on architecture and design. 29 out of 263 (11%) articles have addressed the implementation followed by requirements engineering stage with 24 out of 263 (9%) articles. 11 (4%) articles were focusing on the maintenance phase. The rest of the articles were not particularly focusing on any stage but were generally applicable to SE. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 5)

5. This systematic review follows a structured approach aligned with prior systematic reviews on LLM-based agents in software engineering [1], [13]. The methodology ensures comprehensive coverage of relevant literature while maintaining rigor and transparency throughout the review process. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 3)

6. First, a list of factors is finalized for the decision making of software maintenance in the context of global software development. For this purpose the most relevant published literature [4], [6], [7], [8], [10], [14], [15], [16] showing the lists of relevant factors is thoroughly reviewed. After an in-depth analysis the similar factors are merged based on their relevancy and impact on software maintenance that results into a list of 10 factors. In the next step these factors are evaluated to extract their interrelationships, and also utilized in the proposed integrated approach of software maintenance process. (An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective, page 3)

7. First, a list of factors is finalized for the decision making of software maintenance in the context of global software development. For this purpose the most relevant published literature [4], [6], [7], [8], [10], [14], [15], [16] showing the lists of relevant factors is thoroughly reviewed. After an in-depth analysis the similar factors are merged based on their relevancy and impact on software maintenance that results into a list of 10 factors. In the next step these factors are evaluated to extract their interrelationships, and also utilized in the proposed integrated approach of software maintenance process. (An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective, page 3)

8. Although not explicitly studying SSCs, different researchers have expressed concern over the gaps in the literature on software development practice. For example, the different researchers in [2], [7], [40] explored the gaps in the literature using SMS to look at software engineering in start-ups, while others have explored gaps in software engineering in SSCs through Systematic Literature Reviews [1], [4] Studying these gaps helps researchers appreciate how research has transformed software engineering practices and is helpful to map existing studies. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 3)

### response

Menurut [Source: An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective], systematic literature review membantu dalam menentukan daftar faktor yang relevan untuk pengambilan keputusan software maintenance dalam konteks GSD (Global Software Development), serta memungkinkan untuk menganalisis interrelasinya.

### reference


Specifically, the designing purpose of questionnaire is to uncover the interconnectedness among the factors. (An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective, page 4) In the next step these factors are evaluated to extract their interrelationships, and also utilized in the proposed integrated approach of software maintenance process. (An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective, page 3) First, a list of factors is finalized for the decision making of software maintenance in the context of global software development.

---

## Sample 20

- conversation_id: 13
- user_chat_id: 631
- bot_chat_id: 632

### user_input

Apa itu Agile software development?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. FIGURE 6. Frequency of adapted software development standard.

Gambar ini menampilkan sebuah grafik batang yang berisi informasi tentang frekuensi penggunaan standar pengembangan perangkat lunak (software development standard) oleh para pengembang. Grafik tersebut membagi data menjadi beberapa kategori, masing-masing dengan warna yang berbeda.

Grafik menunjukkan bahwa kategori dengan frekuensi tertinggi adalah "Agile" dengan warna hijau. Kemudian diikuti oleh "Waterfall" dengan warna biru, dan terakhir ada "Kanban" dengan warna kuning.

Angka yang paling mencolok adalah 40% untuk kategori "Agile". Ini berarti bahwa 40% dari responden pengembang perangkat lunak menggunakan standar Agile dalam pengembangan proyek mereka. Angka ini mungkin menunjukkan bahwa banyak pengembang memilih untuk menggunakan metodologi Agile karena fleksibilitas dan kemampuannya untuk mendukung kerja sama tim.

Makna singkat dari gambar ini adalah bahwa para pengembang perangkat lunak memiliki preferensi yang beragam dalam hal standar pengembangan. Namun, metodologi Agile terlihat menjadi pilihan populer karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 8)

3. Keywords: Agile software development, software reuse, user stories, information retrieval, technology acceptance model (Enabling the Reuse of Software Development Assets Through a Taxonomy for User Stories, page 1)

4. Two well-accepted strategies that software companies can implement to preserve their competitive advantage, reducing their time to market, are Agile Software Development (ASD) and Reuse-Driven Software Engineering (RDSE) [1]. While ASD achieves this by having short validation cycles, incremental delivery and minimizing activities not directly related to executable code, RDSE reduces the effort necessary to pro-The associate editor coordinating the review of this manuscript and approving it for publication was Adnan Abid. duce artifacts by reusing existent knowledge (i.e., artifacts) such as source code, requirements, and test cases. (Enabling the Reuse of Software Development Assets Through a Taxonomy for User Stories, page 1)

5. [42] R Van Solingen, E Berghout. The Goal/Question/Metric Method: A Practical Guide for Quality Improvement of Software Development. (1999)

[43] M Söylemez, A Tarhan. Challenges of software process and product quality improvement: Catalyzing defect root-cause investigation by process enactment data analysis. (2018-06)

[44] M Staron, W Meding. Factors determining long-term success of a measurement program: An industrial case study. (2012-01)

[45] M Sulayman, E Mendes. A systematic literature review of software process improvement in small and medium Web companies. (2009)

[46] T Tahir, G Rasool, W Mehmood, C Gencel. An evaluation of software measurement processes in pakistani software industry. (2018)

[47] B Tanveer, L Guzmán, UM Engel. Understanding and improving effort estimation in agile software development. (2016)

[48] A Tarhan, SG Yilmaz. Systematic analyses and comparison of development performance and product quality of incremental process and agile process. (2014-05)

[49] A Tosun, A Bener, B Turhan. Implementation of a software quality improvement project in an SME: A before and after comparison. (2009)

[50] M Unterkalmsteiner, T Gorschek, AK M M Islam, CK Cheng, RB Permadi, R Feldt. Evaluation and measurement of software process Improvement-A systematic literature review. (2012-04) (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

6. Currently, in many software development companies, teams are using various specific tools (such as Jira, GitLab and SonarQube) in order to support the development process and the quality of the code and products. This is usually done in a regular retrospective meeting that involves all the team. As far as the code quality is concerned, those tools provide sufficient information for the Scrum Team. However, there is still a gap and the need for more solutions reflecting team effectiveness and process quality. It can be stated that, at present, process improvement activities are mainly based on developers' perceptions and little support is given to make process wise data-driven decisions. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

7. Pellegrini et al. (P34) argue that many accessibility issues in software projects are due to (1) postponing the implementation of accessibility features by teams that adopt Agile methods (for example, because they adopt the Minimum Viable Product approach), and (2) a lack of knowledge on the implementation of accessibility. Pellegrini et al. (P34) define a set of new responsibilities for roles involved in software development to address this issue. For example, Product Owner should prioritize accessibility from the beginning of the project and produce user stories that take into account disabled people and their needs. Scrum Master should guarantee that the DONE definition covers accessibility. (Operationalizing Human Values in Software Engineering: A Survey, page 19)

8. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

### response

Agile Software Development (ASD) adalah strategi yang digunakan oleh perusahaan-perusahaan pengembangan perangkat lunak untuk mengurangi waktu ke pasar dan meningkatkan kualitas produk. ASD mencapai ini dengan memiliki siklus validasi pendek, pengiriman bertahap, dan mengurangi aktivitas yang tidak terkait langsung dengan kode eksekutif.

### reference


Makna singkat dari gambar ini adalah bahwa para pengembang perangkat lunak memiliki preferensi yang beragam dalam hal standar pengembangan. Namun, metodologi Agile terlihat menjadi pilihan populer karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 8) Ini berarti bahwa 40% dari responden pengembang perangkat lunak menggunakan standar Agile dalam pengembangan proyek mereka.

---

## Sample 21

- conversation_id: 13
- user_chat_id: 633
- bot_chat_id: 634

### user_input

Mengapa Agile software development penting?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. FIGURE 6. Frequency of adapted software development standard.

Gambar ini menampilkan sebuah grafik batang yang berisi informasi tentang frekuensi penggunaan standar pengembangan perangkat lunak (software development standard) oleh para pengembang. Grafik tersebut membagi data menjadi beberapa kategori, masing-masing dengan warna yang berbeda.

Grafik menunjukkan bahwa kategori dengan frekuensi tertinggi adalah "Agile" dengan warna hijau. Kemudian diikuti oleh "Waterfall" dengan warna biru, dan terakhir ada "Kanban" dengan warna kuning.

Angka yang paling mencolok adalah 40% untuk kategori "Agile". Ini berarti bahwa 40% dari responden pengembang perangkat lunak menggunakan standar Agile dalam pengembangan proyek mereka. Angka ini mungkin menunjukkan bahwa banyak pengembang memilih untuk menggunakan metodologi Agile karena fleksibilitas dan kemampuannya untuk mendukung kerja sama tim.

Makna singkat dari gambar ini adalah bahwa para pengembang perangkat lunak memiliki preferensi yang beragam dalam hal standar pengembangan. Namun, metodologi Agile terlihat menjadi pilihan populer karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 8)

3. Two well-accepted strategies that software companies can implement to preserve their competitive advantage, reducing their time to market, are Agile Software Development (ASD) and Reuse-Driven Software Engineering (RDSE) [1]. While ASD achieves this by having short validation cycles, incremental delivery and minimizing activities not directly related to executable code, RDSE reduces the effort necessary to pro-The associate editor coordinating the review of this manuscript and approving it for publication was Adnan Abid. duce artifacts by reusing existent knowledge (i.e., artifacts) such as source code, requirements, and test cases. (Enabling the Reuse of Software Development Assets Through a Taxonomy for User Stories, page 1)

4. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

5. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

6. Pellegrini et al. (P34) argue that many accessibility issues in software projects are due to (1) postponing the implementation of accessibility features by teams that adopt Agile methods (for example, because they adopt the Minimum Viable Product approach), and (2) a lack of knowledge on the implementation of accessibility. Pellegrini et al. (P34) define a set of new responsibilities for roles involved in software development to address this issue. For example, Product Owner should prioritize accessibility from the beginning of the project and produce user stories that take into account disabled people and their needs. Scrum Master should guarantee that the DONE definition covers accessibility. (Operationalizing Human Values in Software Engineering: A Survey, page 19)

7. There is a long history of research on metrics programs (MPs) [24], and plenty of literature recommending success factors for their implementation [17], [28], [34], [44]. However, literature on SMEs using MPs in the context of Agile is rather scarce. Moreover, the literature on measuring software processes and their role in improving SME processes is even scarcer. Measuring software processes with the use of process metrics enables objective and quantitative evaluation of software processes, which can lead to continuous improvement and learning [34], [42]. However, measuring process metrics is a challenge [43]. Software processes are inherently complex and intangible, which makes their measurement more difficult than their product counterparts [19], [41]. Ideally, measurement activities should consume little effort and time, while being adequate enough to meet an organization's measurement demands. Software organizations need to weigh in cost-efficiency while prioritizing measurement objectives and targets. SMEs have the added constraints of limited budget, ambitious deadlines, and short-term strategy [45]. Due to these reasons, measuring software processes, especially in an SME, becomes a bigger challenge. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3)

8. The software engineering industry is undergoing a rapid transformation driven by the emergence of large language models (LLMs) and their use to create autonomous agents that can perform complex software engineering tasks. This paradigm shift, which we call agentic software engineering (ASE), represents a significant rethinking of how software is designed, developed, and maintained [1], [2], [3]. In contrast to traditional software engineering practices that rely primarily on human developers following established methodologies, ASE advocates the use of AI-based agents that have the autonomy to make decisions, write software, run tests, and interact throughout the software engineering lifecycle-a change reflected in recent work on LLM-based applications in software engineering [4], [5], [6], [7]. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 1)

### response

Agile software development penting karena dapat memberikan beberapa keuntungan, antara lain:

* Mengurangi waktu pasar (timeto-market)
* Meningkatkan kenyamanan pelanggan
* Mengurangi biaya pengembangan
* Fleksibilitas dan kemampuan untuk mendukung kerja sama tim

Agile software development juga dapat membantu meningkatkan efisiensi dan produktivitas dalam pengembangan perangkat lunak.

### reference


Angka ini mungkin menunjukkan bahwa banyak pengembang memilih untuk menggunakan metodologi Agile karena fleksibilitas dan kemampuannya untuk mendukung kerja sama tim. Namun, metodologi Agile terlihat menjadi pilihan populer karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 8) Makna singkat dari gambar ini adalah bahwa para pengembang perangkat lunak memiliki preferensi yang beragam dalam hal standar pengembangan.

---

## Sample 22

- conversation_id: 13
- user_chat_id: 635
- bot_chat_id: 636

### user_input

Apa manfaat Agile software development?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. Two well-accepted strategies that software companies can implement to preserve their competitive advantage, reducing their time to market, are Agile Software Development (ASD) and Reuse-Driven Software Engineering (RDSE) [1]. While ASD achieves this by having short validation cycles, incremental delivery and minimizing activities not directly related to executable code, RDSE reduces the effort necessary to pro-The associate editor coordinating the review of this manuscript and approving it for publication was Adnan Abid. duce artifacts by reusing existent knowledge (i.e., artifacts) such as source code, requirements, and test cases. (Enabling the Reuse of Software Development Assets Through a Taxonomy for User Stories, page 1)

3. FIGURE 6. Frequency of adapted software development standard.

Gambar ini menampilkan sebuah grafik batang yang berisi informasi tentang frekuensi penggunaan standar pengembangan perangkat lunak (software development standard) oleh para pengembang. Grafik tersebut membagi data menjadi beberapa kategori, masing-masing dengan warna yang berbeda.

Grafik menunjukkan bahwa kategori dengan frekuensi tertinggi adalah "Agile" dengan warna hijau. Kemudian diikuti oleh "Waterfall" dengan warna biru, dan terakhir ada "Kanban" dengan warna kuning.

Angka yang paling mencolok adalah 40% untuk kategori "Agile". Ini berarti bahwa 40% dari responden pengembang perangkat lunak menggunakan standar Agile dalam pengembangan proyek mereka. Angka ini mungkin menunjukkan bahwa banyak pengembang memilih untuk menggunakan metodologi Agile karena fleksibilitas dan kemampuannya untuk mendukung kerja sama tim.

Makna singkat dari gambar ini adalah bahwa para pengembang perangkat lunak memiliki preferensi yang beragam dalam hal standar pengembangan. Namun, metodologi Agile terlihat menjadi pilihan populer karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 8)

4. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

5. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

6. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

7. Our review demonstrates that agentic software engineering has transformative potential for software development practices. The incorporation of autonomous agents, which are driven by large language models, into the software development lifecycle inculcates an increased level of automation, collaboration, and intelligence in the software engineering processes.

Key potential benefits emerging from our analysis include improved developer productivity, as agentic approaches can amplify developer capabilities by automating routine tasks, suggesting candidate solutions, and handling parts of complex implementations that would otherwise require substantial human effort [62]. Improved code quality is another frequently reported benefit, with multi-agent review and testing processes capable of identifying issues and suggesting improvements that might be missed by individual human developers, particularly in complex systems with multiple interdependent components.

Agents may also facilitate more rapid experimentation and innovation by reducing the implementation burden on human developers and allowing them to focus more attention on high-level problem-solving and design. In addition, more natural language interfaces and autonomous agents could make aspects of software development more accessible to non-specialists, potentially broadening participation in software-related activities and enabling new forms of human-computer collaboration in development processes. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 20)

8. Currently, in many software development companies, teams are using various specific tools (such as Jira, GitLab and SonarQube) in order to support the development process and the quality of the code and products. This is usually done in a regular retrospective meeting that involves all the team. As far as the code quality is concerned, those tools provide sufficient information for the Scrum Team. However, there is still a gap and the need for more solutions reflecting team effectiveness and process quality. It can be stated that, at present, process improvement activities are mainly based on developers' perceptions and little support is given to make process wise data-driven decisions. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

### response

Berikut beberapa manfaat Agile Software Development (ASD) yang dapat dilihat dari konteks-konteks yang tersedia:

* Mengurangi waktu pemasaran (reduced timeto-market)
* Meningkatkan kepuasan pelanggan (increased customer satisfaction)
* Menurunkan biaya pengembangan (reduced development costs)

Selain itu, ASD juga dapat memberikan fleksibilitas dan kemampuan untuk menyesuaikan diri dengan perubahan pasar yang cepat.

### reference


1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. While ASD achieves this by having short validation cycles, incremental delivery and minimizing activities not directly related to executable code, RDSE reduces the effort necessary to pro-The associate editor coordinating the review of this manuscript and approving it for publication was Adnan Abid. duce artifacts by reusing existent knowledge (i.e., artifacts) such as source code, requirements, and test cases. (Enabling the Reuse of Software Development Assets Through a Taxonomy for User Stories, page 1) Two well-accepted strategies that software companies can implement to preserve their competitive advantage, reducing their time to market, are Agile Software Development (ASD) and Reuse-Driven Software Engineering (RDSE) [1].

---

## Sample 23

- conversation_id: 13
- user_chat_id: 639
- bot_chat_id: 640

### user_input

Bagaimana Agile software development mendukung software quality?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

3. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

4. Currently, in many software development companies, teams are using various specific tools (such as Jira, GitLab and SonarQube) in order to support the development process and the quality of the code and products. This is usually done in a regular retrospective meeting that involves all the team. As far as the code quality is concerned, those tools provide sufficient information for the Scrum Team. However, there is still a gap and the need for more solutions reflecting team effectiveness and process quality. It can be stated that, at present, process improvement activities are mainly based on developers' perceptions and little support is given to make process wise data-driven decisions. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

5. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

6. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

7. [42] R Van Solingen, E Berghout. The Goal/Question/Metric Method: A Practical Guide for Quality Improvement of Software Development. (1999)

[43] M Söylemez, A Tarhan. Challenges of software process and product quality improvement: Catalyzing defect root-cause investigation by process enactment data analysis. (2018-06)

[44] M Staron, W Meding. Factors determining long-term success of a measurement program: An industrial case study. (2012-01)

[45] M Sulayman, E Mendes. A systematic literature review of software process improvement in small and medium Web companies. (2009)

[46] T Tahir, G Rasool, W Mehmood, C Gencel. An evaluation of software measurement processes in pakistani software industry. (2018)

[47] B Tanveer, L Guzmán, UM Engel. Understanding and improving effort estimation in agile software development. (2016)

[48] A Tarhan, SG Yilmaz. Systematic analyses and comparison of development performance and product quality of incremental process and agile process. (2014-05)

[49] A Tosun, A Bener, B Turhan. Implementation of a software quality improvement project in an SME: A before and after comparison. (2009)

[50] M Unterkalmsteiner, T Gorschek, AK M M Islam, CK Cheng, RB Permadi, R Feldt. Evaluation and measurement of software process Improvement-A systematic literature review. (2012-04) (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

8. Two well-accepted strategies that software companies can implement to preserve their competitive advantage, reducing their time to market, are Agile Software Development (ASD) and Reuse-Driven Software Engineering (RDSE) [1]. While ASD achieves this by having short validation cycles, incremental delivery and minimizing activities not directly related to executable code, RDSE reduces the effort necessary to pro-The associate editor coordinating the review of this manuscript and approving it for publication was Adnan Abid. duce artifacts by reusing existent knowledge (i.e., artifacts) such as source code, requirements, and test cases. (Enabling the Reuse of Software Development Assets Through a Taxonomy for User Stories, page 1)

### response

Agile software development mendukung software quality dengan menggunakan praktek-praktek seperti:

* Kontinu integrasi untuk mendeteksi dan memperbaiki kesalahan secepat mungkin
* Penggunaan alat-alat seperti Jira, GitLab, dan SonarQube untuk mendukung proses pengembangan dan kualitas kode produk
* Keterlibatan tim dalam pertemuan retrospektif untuk mengevaluasi dan meningkatkan proses pengembangan

Informasi tersebut didapat dari konteks dokumen "Measuring and Improving Agile Processes in a Small-Size Software Development Company".

### reference


Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1) It can be stated that, at present, process improvement activities are mainly based on developers' perceptions and little support is given to make process wise data-driven decisions. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1) Evaluation and measurement of software process Improvement-A systematic literature review. (2012-04) (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

---

## Sample 24

- conversation_id: 13
- user_chat_id: 641
- bot_chat_id: 642

### user_input

Bagaimana Agile software development mempengaruhi software testing?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

3. Generally, many of the traditional SRGMs are based on similar assumptions [1], [8]. In some cases, faults detected during testing may not be corrected immediately. This delay in fault correction can be caused by various factors such as prioritization of tasks, availability of resources, or complexity of the fault. As a result, the software reliability growth process can be impacted, and traditional SRGMs may not accurately reflect the actual reliability of the software. To address this, some SRGMs have been developed to account for delayed fault correction and other factors that may affect the software reliability growth process [11], [12], [15]. Raymond and O'Reilly [6] noticed that beta testing plays a crucial role in the testing of OSS. Therefore, the test team for OSS is often separate from the development team. When a fault is detected in OSS, developers typically require additional time to communicate with testers and rectify the issue. This situation often leads to longer debugging times for OSS, and delays in the fault correction process are more likely to occur. (Using Modified Diffusion Models for Reliability Estimation of Open Source Software, page 3)

4. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

5. Worldwide software development expenditure, for year 2014, was 3.8 billion dollars which included 23% quality control and testing cost for business applications [4]. Early fault detection helps save costs, time, and reduce the complexity of the software because it is proportionate to the testing. It is a well known fact that extensive testing are impossible [5]. Testing cost sometimes amounts to over fifty percent of the The associate editor coordinating the review of this manuscript and approving it for publication was Claudio Agostino Ardagna . entire software development cost. It is for these reasons that it is more feasible to detect and test classes with faults to produce software with better quality. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

6. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

7. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

8. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

### response

Berdasarkan konteks yang disediakan, tidak ada informasi spesifik tentang bagaimana Agile software development mempengaruhi software testing. Namun, beberapa teks mungkin relevan:

* Di sumber [1], dijelaskan bahwa Agile development methodologies memiliki banyak manfaat, termasuk reduksi waktu ke pasar, peningkatan kepuasan pelanggan, dan pengurangan biaya pengembangan.
* Sumber [2] menyebutkan bahwa praktisi melaporkan banyak manfaat dari menggunakan Agile, termasuk reduksi waktu ke pasar, peningkatan kepuasan pelanggan, dan pengurangan biaya pengembangan.
* Di sumber [6], Raymond dan O'Reilly menyebutkan bahwa beta testing memainkan peran penting dalam pengujian OSS. 
* Sumber [7] menjelaskan bahwa ASD (Agile Software Development) bergantung pada siklus umpan balik yang singkat untuk memberikan fleksibilitas dan adaptasi cepat terhadap fluktuasi pasar.

Namun, tidak ada informasi spesifik tentang bagaimana Agile software development mempengaruhi software testing.

### reference


Raymond and O'Reilly [6] noticed that beta testing plays a crucial role in the testing of OSS. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. When a fault is detected in OSS, developers typically require additional time to communicate with testers and rectify the issue.

---

## Sample 25

- conversation_id: 13
- user_chat_id: 645
- bot_chat_id: 646

### user_input

Bagaimana Agile software development diterapkan dalam software engineering?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. FIGURE 6. Frequency of adapted software development standard.

Gambar ini menampilkan sebuah grafik batang yang berisi informasi tentang frekuensi penggunaan standar pengembangan perangkat lunak (software development standard) oleh para pengembang. Grafik tersebut membagi data menjadi beberapa kategori, masing-masing dengan warna yang berbeda.

Grafik menunjukkan bahwa kategori dengan frekuensi tertinggi adalah "Agile" dengan warna hijau. Kemudian diikuti oleh "Waterfall" dengan warna biru, dan terakhir ada "Kanban" dengan warna kuning.

Angka yang paling mencolok adalah 40% untuk kategori "Agile". Ini berarti bahwa 40% dari responden pengembang perangkat lunak menggunakan standar Agile dalam pengembangan proyek mereka. Angka ini mungkin menunjukkan bahwa banyak pengembang memilih untuk menggunakan metodologi Agile karena fleksibilitas dan kemampuannya untuk mendukung kerja sama tim.

Makna singkat dari gambar ini adalah bahwa para pengembang perangkat lunak memiliki preferensi yang beragam dalam hal standar pengembangan. Namun, metodologi Agile terlihat menjadi pilihan populer karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 8)

3. The software engineering industry is undergoing a rapid transformation driven by the emergence of large language models (LLMs) and their use to create autonomous agents that can perform complex software engineering tasks. This paradigm shift, which we call agentic software engineering (ASE), represents a significant rethinking of how software is designed, developed, and maintained [1], [2], [3]. In contrast to traditional software engineering practices that rely primarily on human developers following established methodologies, ASE advocates the use of AI-based agents that have the autonomy to make decisions, write software, run tests, and interact throughout the software engineering lifecycle-a change reflected in recent work on LLM-based applications in software engineering [4], [5], [6], [7]. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 1)

4. Pellegrini et al. (P34) argue that many accessibility issues in software projects are due to (1) postponing the implementation of accessibility features by teams that adopt Agile methods (for example, because they adopt the Minimum Viable Product approach), and (2) a lack of knowledge on the implementation of accessibility. Pellegrini et al. (P34) define a set of new responsibilities for roles involved in software development to address this issue. For example, Product Owner should prioritize accessibility from the beginning of the project and produce user stories that take into account disabled people and their needs. Scrum Master should guarantee that the DONE definition covers accessibility. (Operationalizing Human Values in Software Engineering: A Survey, page 19)

5. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

6. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

7. Two well-accepted strategies that software companies can implement to preserve their competitive advantage, reducing their time to market, are Agile Software Development (ASD) and Reuse-Driven Software Engineering (RDSE) [1]. While ASD achieves this by having short validation cycles, incremental delivery and minimizing activities not directly related to executable code, RDSE reduces the effort necessary to pro-The associate editor coordinating the review of this manuscript and approving it for publication was Adnan Abid. duce artifacts by reusing existent knowledge (i.e., artifacts) such as source code, requirements, and test cases. (Enabling the Reuse of Software Development Assets Through a Taxonomy for User Stories, page 1)

8. [42] R Van Solingen, E Berghout. The Goal/Question/Metric Method: A Practical Guide for Quality Improvement of Software Development. (1999)

[43] M Söylemez, A Tarhan. Challenges of software process and product quality improvement: Catalyzing defect root-cause investigation by process enactment data analysis. (2018-06)

[44] M Staron, W Meding. Factors determining long-term success of a measurement program: An industrial case study. (2012-01)

[45] M Sulayman, E Mendes. A systematic literature review of software process improvement in small and medium Web companies. (2009)

[46] T Tahir, G Rasool, W Mehmood, C Gencel. An evaluation of software measurement processes in pakistani software industry. (2018)

[47] B Tanveer, L Guzmán, UM Engel. Understanding and improving effort estimation in agile software development. (2016)

[48] A Tarhan, SG Yilmaz. Systematic analyses and comparison of development performance and product quality of incremental process and agile process. (2014-05)

[49] A Tosun, A Bener, B Turhan. Implementation of a software quality improvement project in an SME: A before and after comparison. (2009)

[50] M Unterkalmsteiner, T Gorschek, AK M M Islam, CK Cheng, RB Permadi, R Feldt. Evaluation and measurement of software process Improvement-A systematic literature review. (2012-04) (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

### response

Agile software development diimplementasikan dalam software engineering melalui beberapa prinsip dan praktik, seperti:

*   Menggunakan Short Feedback Cycles untuk memberikan fleksibilitas dan penyesuaian yang cepat terhadap fluktuasi pasar.
*   Membuat keputusan lebih sering dan dalam jangka waktu singkat.
*   Menggunakan praktek-praktik agile seperti Continuous Integration untuk memastikan kesalahan terdeteksi dan diperbaiki secara cepat.
*   Menerapkan pendekatan Holistik dengan menghubungkan semua aktivitas pengembangan perangkat lunak, termasuk Aspek Bisnis dan Pengembangan (BizDez), serta Pengembangan dan Operasi (DevOps).

Informasi lebih lanjut dapat ditemukan di sumber-sumber yang terkait.

### reference


Makna singkat dari gambar ini adalah bahwa para pengembang perangkat lunak memiliki preferensi yang beragam dalam hal standar pengembangan. Gambar ini menampilkan sebuah grafik batang yang berisi informasi tentang frekuensi penggunaan standar pengembangan perangkat lunak (software development standard) oleh para pengembang. Namun, metodologi Agile terlihat menjadi pilihan populer karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 8)

---

## Sample 26

- conversation_id: 13
- user_chat_id: 649
- bot_chat_id: 650

### user_input

Apa itu CNN?

### retrieved_context

1. [38] C Cavina-Pratesi, C Hesse. Why do the eyes prefer the index finger? Simultaneous recording of eye and hand movements during precision grasping. (2013-04)

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

2. Qurishee [71] presented an autonomous pavement condition evaluation employing deep learning, an unmanned aerial vehicle (UAV), and Raspberry Pi tiny computer technologies, which improves road maintenance and renovation management efficiency and cost effectiveness. A lowcost Raspberry Pi smart defect-detecting camera was set up with the trained SSD MobileNet v1, which can be deployed with a UAV for real-time and remote pavement condition inspection. According to preliminary data, the smart pavement detector camera achieves 60% accuracy at 1.2 frames per second on the Raspberry Pi and 96% accuracy at 13.8 frames per second on a CPU-based computer. Hassan et al. [72] employs CNN models that are improved tiny YOLO V3 on UAVs and achieves good results, with precision, sensitivity, and F1 score values better than 85%, but without considering FPS. Sathvik et al. [39] introduce

TABLE 1. Comparison of object detection models deployed on edge device.

pothole detection, an edge computing framework that runs efficient deep neural networks, lowering the latency of earlier techniques. Using transfer learning-based models, an F1 score of 0.64. The YOLO V7 model had an F1 score of 0.51, which improved proportionally (the higher the F1 score, the more efficient the training model) as the number of epochs increased. The YOLO V7 runs on a CPU-based computer, however it does not consider run on edge devices.

Several studies using CNN models deployed on NVIDIA Jetson Nano devices include the SSD-MobileNet model with a batch size of 64 and mAP of 0.22 [48], the MobileNet V2 model, and the SSD Resnet50V1 model [34], [35]. The MobileNet V2 model using hyperparameter settings has a higher mAP of 0.0869 and average recall 0.241 than the SSD Resnet50V1. Yebes et al. [40] created a massive dataset of images with pothole annotations and road scenes from many cities across the world, captured with various cameras, vehicles, and viewpoints under varying environmental circumstances. Their fine-tuned Faster R-CNN Inception v2, Faster R-CNN Resnet101, and Faster R-CNN Inception-Resnet v2 models reached precision 75%, and their CNN model deployed the pothole detector on the Nvidia DrivePX2 platform running at 5-6 frames per second. Based on the findings of this investigation, CNN models were included in the hardware, as indicated in Table 1, although further research is needed to improve system performance (mAP, AR, F1 score) and speed up inference time. Based on previous studies on road damage, several researchers have utilized the CNN model by optimizing its network structure. Specifically, the YOLO model automates the network structure through the introduction of a new module. However, few YOLOv3 models incorporate hyperparameter optimization, with only one study utilizing the Bayesian method. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 1)

3. FIGURE 6. CNN block diagram.

Gambar ini menampilkan skema blok CNN (Convolutional Neural Network). Elemen visual utama adalah beberapa lapisan konvolusi yang dihubungkan dengan satu sama lain melalui proses pemrosesan suatu gambar. Lapisan-lapisan tersebut terlihat seperti kotak-kotak persegi panjang yang berurutan, masing-masing memiliki label yang menunjukkan jenis operasi yang dilakukan: Conv2D (lapisan konvolusi), MaxPooling2D (proses downsampling dengan memilih maksimum nilai), Flatten (mengubah pola input 3 dimensi menjadi array satu dimensi).

Pada bagian atas skema, terdapat label "Input" dan "Output", yang menunjukkan bahwa gambar ini berfungsi untuk menerima input suatu citra dan menghasilkan output berupa hasil pengenalan atau klasifikasi. Namun, detail tentang jenis citra yang digunakan sebagai input masih tidak dapat diidentifikasi secara pasti dari gambar ini.

Dari skema blok CNN ini, dapat disimpulkan bahwa proses pemrosesan gambar dilakukan melalui beberapa tahap konvolusi dan downsampling dengan maksimum. Fungsi utamanya adalah untuk mengekstrak fitur-fitur penting dalam citra dan menghasilkan klasifikasi yang akurat terhadap suatu tipe objek atau kategori.

Perlu diingat bahwa karena hanya ada skema blok saja, detail tentang parameter atau nilai spesifik dari setiap lapisan konvolusi tidak dapat dilihat. Oleh karena itu, interpretasi harus berfokus pada gambaran umum proses yang terjadi dalam CNN daripada detil teknis parametris. (Development of a Speech Emotion Recognition Dataset for Indonesian, page 6)

4. FIGURE 8. Confusion matrix result of ball detection using CNN. FIGURE 8. Confusion Matrix Hasil Deteksi Bola Menggunakan CNN.

Gambar ini menampilkan sebuah grafik yang disebut "confusion matrix". Grafik ini digunakan untuk mengukur akurasi model klasifikasi, yaitu model CNN (Convolutional Neural Network) dalam deteksi bola. Terdapat empat sudut dalam grafik: TP (True Positive), FP (False Positive), TN (True Negative), dan FN (False Negative).

Gambar menunjukkan bahwa di bagian atas kiri terdapat nilai 85, yang kemungkinan besar mewakili jumlah kejadian TP. Nilai ini mungkin merupakan akurasi model CNN dalam mendeteksi bola dengan tepat. Di bawahnya, ada label "Recall" dengan nilai sekitar 88%, menunjukkan bahwa model dapat mendeteksi bola dengan tingkat akuransi yang tinggi.

Di bagian kanan atas terdapat nilai 15, mungkin merupakan jumlah kejadian FP (False Positive), yaitu kesalahan dalam mengidentifikasi objek sebagai bola padahal sebenarnya bukan. Di bawahnya ada label "Precision" dengan nilai sekitar 97%, menunjukkan bahwa model dapat membedakan bola dari non-bola dengan tingkat akuransi yang sangat tinggi.

Di bagian bawah kiri terdapat label "F1-score" dengan nilai sekitar 91%, ini merupakan skor yang dihitung berdasarkan recall dan precision untuk memberikan gambaran lebih komprehensif tentang akurasi model. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 10)

5. [37] AR A Besari, AA Saputra, WH Chin, N Kurnianingsih, Kubota. Hand-object interaction recognition based on visual attention using multiscopic cyber-physical-social system. (2023-07)

[38] KD Nguyen, LA Corben, PN Pathirana, MK Horne, MB Delatycki, DJ Szmulewicz. The assessment of upper limb functionality in friedreich ataxia via self-feeding activity. (2020-04)

[39] A Ganguly, G Rashidi, K Mombaur. Comparison of the performance of the leap motion controller TM with a standard marker-based motion capture system. (2021-03)

[40] C Dai, X Hu. Finger joint angle estimation based on motoneuron discharge activities. (2020-03)

[41] S Jegelka. Theory of graph neural networks: Representation and learning. (2022)

[42] M Fey, JEric Lenssen. Fast graph representation learning with PyTorch geometric. (2019)

[43] AR A Besari, WH Chin, N Kubota, Kurnianingsih. Ecological approach for object relationship extraction in elderly care robot. (2020-12)

[44] HR Nasrabadi, J.-M Alonso. Modular streaming pipeline of eye/head tracking data using Tobii pro glasses 3. (2022-09)

[45] C.-Y Wang, A Bochkovskiy, H.-Y. Mark Liao. Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors. (2022)

[46] H Fu, L Wu, M Jian, Y Yang, X Wang. MF-SORT: Simple online and realtime tracking with motion features,'' in Image Graphics. (2019)

[47] F Zhang, V Bazarevsky, A Vakunov, A Tkachenka, G Sung, C.-L Chang, M Grundmann. MediaPipe hands: On-device real-time hand tracking. (2020)

[48] Q Cai, J Li, J Long. Effect of physical and virtual feedback on reach-to-grasp movements in virtual environments. (2022-06)

[49] S Shin, W Kim. Skeleton-based dynamic hand gesture recognition using a part-based GRU-RNN for gesture-based interface. (2020)

[50] EP Larsen, JM Kolman, FN Masud, F Sasangohar. Ethical considerations when using a mobile eye tracker in a patient-facing area: Lessons from an intensive care unit observational protocol. (2020-11)

[51] AR A Besari, AA Saputra, WH Chin, N Kubota, Kurnianingsih. Feature-based egocentric grasp pose classification for expanding humanobject interactions. (2021-06)

[52] MK Cain, Z Zhang, K.-H Yuan. Univariate and multivariate skewness and kurtosis for measuring nonnormality: Prevalence, influence and estimation. (2017-10)

[53] TJ Bosch, T Hanna, KA Fercho, LA Baugh. Behavioral performance and visual strategies during skill acquisition using a novel tool use motor learning task. (2018-09)

[54] M Yani, AR A Besari, N Yamada, N Kubota. Ecological-inspired system design for safety manipulation strategy in home-care robot. (2020-09)

[55] S Wang, J Zhao, C Shao, C Dong, C Yin. Truck traffic flow prediction based on LSTM and GRU methods with sampled GPS data. (2020)

[56] M Kunda, ME Banani, JM Rehg. A computational exploration of problem-solving strategies and gaze behaviors on the block design task. (2016)

[57] S Li, Y Li, Y Li, M Li, X Xu. YOLO-FIRI: Improved YOLOv5 for infrared image object detection. (2021)

[58] NA Hashim, NA A Razak, NA A Osman. Comparison of conventional and virtual reality box and blocks tests in upper limb amputees: A case-control study. (2021)

[59] J Négyesi, P Négyesi, T Hortobágyi, S Sun, J Kusuyama, RM Kiss, R Nagatomi. Handedness did not affect motor skill acquisition by the dominant hand or interlimb transfer to the non-dominant hand regardless of task complexity level. (2022-10)

[60] L Wang, J Liu, J Lan. Feature evaluation of upper limb exercise rehabilitation interactive system based on kinect. (2019)

[61] Takenori Obo (member, Ieee. he became an Assistant Professor with the Department of Mechanical Systems Engineering, Faculty of System Design, Tokyo Metropolitan University. He is currently with the Department of Mechanical Systems Engineering, Faculty of System Design, Tokyo Metropolitan University. He is a member of the Society of Instrument and Control Engineers, the Japan Society of Intelligent Information Fuzzy. (2014-04)

[62] Negeri Semarang, Indonesia. He is currently a Professor with the Department of Mechanical Systems Engineering, Graduate School of Systems Design, Tokyo Metropolitan University, Japan. His current research interests include coevolutionary computing, fuzzy computing, topological mapping, cognitive robotics, social robotics, and informationally structured space. He has published more than 500 refereed journals and conference papers in the above research fields. He received the Best Paper Award from IEEE IECON 1996 and the Best Paper Award from IEEE CIRA 1997, amongst others. (1997) (Multiscopic CPSS for Independent Block-Design Test Based on Hand–Object Interaction Recognition With Visual Attention, page 2)

6. The Convolutional Neural Network (CNN) model is trained using the prepared dataset. CNN is a type of deep neural network that is highly effective for the analysis and processing of visual data such as images and videos. In this context, CNN is used to predict the position of the ball based on the position data that has been collected during the training session. The training process involves adjusting the weights of the model through the backpropagation technique to minimize the prediction error. The Fig. 7 is a sequential model of the CNN architecture for ball position prediction. A sequential model is a series of layers that are processed sequentially from input to output. The given model consists of several types of layers: Conv1D, AveragePooling1D, Dropout, MaxPooling1D, Flatten, and Dense. The operation process is in equations ( 4) to (9). (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 7)

7. The road damage detection research makes use of laser sensors to rebuild 3D road damage as well as stereo vision technologies. Several sensors are required for the stereo vision system, including two cameras, an LED, a laser, and LiDAR. The laser sensor has a small beamwidth; thus, it cannot detect road damage in the form of a large hole, necessitating the use of an array of LEDs, lasers, LiDARs, and other sensors [18], [49]. Reconstructing the pothole takes time, whether using an LED array, laser, or LiDAR. Furthermore, 3D road defect reconstruction and stereo vision require well-lit lighting and slow vehicle speeds [17], [18], [50].

Further research used image-processing techniques. Potholes are a form of road irregularity that can be recognized with traditional image processing techniques. To achieve high accuracy, this technique takes numerous steps, including manual image feature extraction and image processing parameter adjustments. As a result, the image frame rate varies depending on traffic circumstances [21]. Some research that investigated road conditions, pavement conditions, potholes, cracks, smart phone sensors, and accelerometers used machine learning techniques such as support vector machines, neural networks, multilayer perceptron, and decision trees [16]. Furthermore, research is being conducted to detect pavement damage using ML algorithms such as support vector machines, artificial neural networks, and random forests [51]. To improve accuracy, ML models require significant computer resources during data processing, which also includes manual feature analysis.

Several studies used deep convolutional neural network (CNN) techniques to automate the simultaneous feature extraction and categorization of objects [41], [52]. This is challenging to incorporate into real-time road defect detection systems. The deployment of CNN models for road damage detection on devices requires a balance between high accuracy and high efficiency [53]. The use of CNN models for road damage detection on devices requires achieving a balance between high accuracy and high efficiency. The use of CNN models for road damage detection on devices necessitates striking a balance between high accuracy and high efficiency. The parameter system performance deployment model CNN on devices performs well in terms of precision, recall, F1-score, and as well as efficiency of time inference.

The CNN models perform exceptionally well in terms of high accuracy, precision, recall, and low loss. This requires CNN models with large architecture and competitive computing costs that are inefficient. To do this while maintaining high accuracy, a simplified CNN model configuration setting is required to achieve good CNN model system performance. High efficiency, which is the CNN model system performance, enables it to detect road faults on edge devices with a short inference time. Because the CNN model on edge devices have limited storage capacity, inference time must be considered. Taking this into account, the CNN model offers good system performance and a short inference time for simpler model configurations, but high accuracy is difficult to achieve. To obtain optimal system performance, the CNN model parameters must be properly chosen. When selecting a detection model, there is no definitive answer as to which model has the best performance [31], [53].

Improving system performance in computer vision, object recognition, and classification using CNN models can be achieved through various methods. These include modifying or adding components to the CNN model structure and optimizing hyperparameter selection during CNN model training. The strategy of enhancing the CNN structure aims to improve feature extraction efficiency and model accuracy by modifying or incorporating new components into the CNN architecture. Several studies have focused on enhancing CNN models by modifying or adding components to the existing CNN structure [54], [55], [56], [57], [58], [59]. DenseNet was integrated into the YOLOv4 backbone to optimize feature transfer and reuse. This involved several modifications, such as adjusting the Path Aggregation Network (PANet) [54], introducing New Residual Blocks, applying Spatial Pyramid Pooling (SPP), modifying the PANet, and utilizing Hard-Swish activation functions [59]. Similarly, researchers have integrated DenseNet blocks into the YOLOv5 backbone to enhance the preservation and reuse of critical feature information. This was achieved by incorporating a Convolutional Block Attention Module (CBAM) [56]. Another study introduced a novel framework called Multiple Graph Learning Neural Networks (MGLNN) for semi-supervised learning on graph-based data [55]. Additionally, modifications were made to the YOLO model using the CSPDarknet53 backbone structure, which included Residual Blocks, DenseNet, Spatial Pyramid Pooling (SPP), and the Path Aggregation Network (PANet) [57]. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 2)

8. TABLE 1. The proposed system with related works.

Tabel ini menjelaskan sistem yang diusulkan bersama dengan karya terkait dalam penelitian "Penginderaan Bola Menggunakan Metode CNN Dengan Kamera Zed pada Aplikasi Robot Penjaga Gawang". Tabel ini berisi 39 baris dan 9 kolom, tetapi hanya memuat informasi singkat tentang beberapa studi terkait.

Variabel/kolom utama adalah:

* Judul penelitian yang berkaitan dengan metode CNN dan kamera Zed.
* Karya-karya yang relevan yang dikemukakan sebagai referensi.
* Deskripsi singkat tentang aplikasi robot penjaga gawang dan penggunaan metode CNN.

Nilai atau pola penting dari tabel ini adalah:

* Penggunaan metode CNN untuk mendeteksi posisi bola dalam lingkungan tiga dimensi, yang merupakan kemampuan utama dari metode tersebut.
* Aplikasi robot penjaga gawang sebagai salah satu penggunaan metode CNN.

Insight singkat yang bisa dibaca manusia adalah bahwa penelitian ini berusaha mengembangkan sistem kombinasi antara kamera Zed dan metode CNN untuk mendeteksi posisi bola dengan akurasi tinggi, serta memahami pergerakan bola dalam lingkungan yang beragam. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 3)

### response

CNN (Convolutional Neural Network) adalah jenis jaringan saraf tiruan yang sangat efektif untuk menganalisis dan memproses data visual seperti gambar dan video. Dalam konteks penelitian "Penginderaan Bola Menggunakan Metode CNN Dengan Kamera Zed pada Aplikasi Robot Penjaga Gawang", CNN digunakan untuk memprediksi posisi bola berdasarkan data posisi yang telah dikumpulkan selama sesi pelatihan.

### reference


Tabel ini menjelaskan sistem yang diusulkan bersama dengan karya terkait dalam penelitian "Penginderaan Bola Menggunakan Metode CNN Dengan Kamera Zed pada Aplikasi Robot Penjaga Gawang". Nilai atau pola penting dari tabel ini adalah: * Penggunaan metode CNN untuk mendeteksi posisi bola dalam lingkungan tiga dimensi, yang merupakan kemampuan utama dari metode tersebut. * Aplikasi robot penjaga gawang sebagai salah satu penggunaan metode CNN. Insight singkat yang bisa dibaca manusia adalah bahwa penelitian ini berusaha mengembangkan sistem kombinasi antara kamera Zed dan metode CNN untuk mendeteksi posisi bola dengan akurasi tinggi, serta memahami pergerakan bola dalam lingkungan yang beragam. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 3)

---

## Sample 27

- conversation_id: 13
- user_chat_id: 651
- bot_chat_id: 652

### user_input

Mengapa CNN digunakan dalam deep learning?

### retrieved_context

1. [38] C Cavina-Pratesi, C Hesse. Why do the eyes prefer the index finger? Simultaneous recording of eye and hand movements during precision grasping. (2013-04)

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

2. Qurishee [71] presented an autonomous pavement condition evaluation employing deep learning, an unmanned aerial vehicle (UAV), and Raspberry Pi tiny computer technologies, which improves road maintenance and renovation management efficiency and cost effectiveness. A lowcost Raspberry Pi smart defect-detecting camera was set up with the trained SSD MobileNet v1, which can be deployed with a UAV for real-time and remote pavement condition inspection. According to preliminary data, the smart pavement detector camera achieves 60% accuracy at 1.2 frames per second on the Raspberry Pi and 96% accuracy at 13.8 frames per second on a CPU-based computer. Hassan et al. [72] employs CNN models that are improved tiny YOLO V3 on UAVs and achieves good results, with precision, sensitivity, and F1 score values better than 85%, but without considering FPS. Sathvik et al. [39] introduce

TABLE 1. Comparison of object detection models deployed on edge device.

pothole detection, an edge computing framework that runs efficient deep neural networks, lowering the latency of earlier techniques. Using transfer learning-based models, an F1 score of 0.64. The YOLO V7 model had an F1 score of 0.51, which improved proportionally (the higher the F1 score, the more efficient the training model) as the number of epochs increased. The YOLO V7 runs on a CPU-based computer, however it does not consider run on edge devices.

Several studies using CNN models deployed on NVIDIA Jetson Nano devices include the SSD-MobileNet model with a batch size of 64 and mAP of 0.22 [48], the MobileNet V2 model, and the SSD Resnet50V1 model [34], [35]. The MobileNet V2 model using hyperparameter settings has a higher mAP of 0.0869 and average recall 0.241 than the SSD Resnet50V1. Yebes et al. [40] created a massive dataset of images with pothole annotations and road scenes from many cities across the world, captured with various cameras, vehicles, and viewpoints under varying environmental circumstances. Their fine-tuned Faster R-CNN Inception v2, Faster R-CNN Resnet101, and Faster R-CNN Inception-Resnet v2 models reached precision 75%, and their CNN model deployed the pothole detector on the Nvidia DrivePX2 platform running at 5-6 frames per second. Based on the findings of this investigation, CNN models were included in the hardware, as indicated in Table 1, although further research is needed to improve system performance (mAP, AR, F1 score) and speed up inference time. Based on previous studies on road damage, several researchers have utilized the CNN model by optimizing its network structure. Specifically, the YOLO model automates the network structure through the introduction of a new module. However, few YOLOv3 models incorporate hyperparameter optimization, with only one study utilizing the Bayesian method. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 1)

3. The Convolutional Neural Network (CNN) model is trained using the prepared dataset. CNN is a type of deep neural network that is highly effective for the analysis and processing of visual data such as images and videos. In this context, CNN is used to predict the position of the ball based on the position data that has been collected during the training session. The training process involves adjusting the weights of the model through the backpropagation technique to minimize the prediction error. The Fig. 7 is a sequential model of the CNN architecture for ball position prediction. A sequential model is a series of layers that are processed sequentially from input to output. The given model consists of several types of layers: Conv1D, AveragePooling1D, Dropout, MaxPooling1D, Flatten, and Dense. The operation process is in equations ( 4) to (9). (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 7)

4. The pooling layer, which comes after the convolution layer, is meant to combine key information and lower the dimensionality of the feature map. Max pooling, which chooses the maximum value within each condensed area of the feature map, is a frequently used kind of pooling. This lessens the number of parameters that must be computed and increases the model's resistance to slight variations in the input features' locations.

CNNs typically have multiple sets of successive convolution and pooling layers, which allow the network to detect increasingly complex features at each layer. Early layers may detect simple edges and lines, while deeper layers may detect more complex objects, such as specific shapes and patterns.

The final input is supplied into the fully connected layer after passing through several convolution and pooling layers. Every neuron in this layer is connected to every other neuron in the layer before it, enabling the network to compile the features that were taken out of the earlier levels and come to a conclusion. An activation function that aids in the final classification, such as ReLU (Rectified Linear Unit) or Softmax, typically follows this completely connected layer.

This study designs and implements appropriate parameter values in each layer of the CNN used. Previous researchers have created several methods for artificial intelligence that have been tried to be implemented on the ERSOW robot. These methods are Label Propagation, Extra Tree Classifier, Ridge Classifier, Linear SVC, Passive Aggressive Classifier, AdaBoost, Label Spreading, Nearest Centroid, GaussianNB, and Dummy Classifier (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 5)

5. Keywords: Ball position prediction, ZED camera, deep learning, convolutional neural network, ERSOW goalkeeper robot (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 1)

6. FIGURE 6. CNN block diagram.

Gambar ini menampilkan skema blok CNN (Convolutional Neural Network). Elemen visual utama adalah beberapa lapisan konvolusi yang dihubungkan dengan satu sama lain melalui proses pemrosesan suatu gambar. Lapisan-lapisan tersebut terlihat seperti kotak-kotak persegi panjang yang berurutan, masing-masing memiliki label yang menunjukkan jenis operasi yang dilakukan: Conv2D (lapisan konvolusi), MaxPooling2D (proses downsampling dengan memilih maksimum nilai), Flatten (mengubah pola input 3 dimensi menjadi array satu dimensi).

Pada bagian atas skema, terdapat label "Input" dan "Output", yang menunjukkan bahwa gambar ini berfungsi untuk menerima input suatu citra dan menghasilkan output berupa hasil pengenalan atau klasifikasi. Namun, detail tentang jenis citra yang digunakan sebagai input masih tidak dapat diidentifikasi secara pasti dari gambar ini.

Dari skema blok CNN ini, dapat disimpulkan bahwa proses pemrosesan gambar dilakukan melalui beberapa tahap konvolusi dan downsampling dengan maksimum. Fungsi utamanya adalah untuk mengekstrak fitur-fitur penting dalam citra dan menghasilkan klasifikasi yang akurat terhadap suatu tipe objek atau kategori.

Perlu diingat bahwa karena hanya ada skema blok saja, detail tentang parameter atau nilai spesifik dari setiap lapisan konvolusi tidak dapat dilihat. Oleh karena itu, interpretasi harus berfokus pada gambaran umum proses yang terjadi dalam CNN daripada detil teknis parametris. (Development of a Speech Emotion Recognition Dataset for Indonesian, page 6)

7. This research uses the ROS system because it has the ability to integrate camera sensors with artificial intelligence methods and several other combined sensors in the robot. Fig. 4 shows the basic communication system for accessing the ZED camera on the robot. Image information is acquired over time and processed in real-time.  The prediction system that has been created using the CNN algorithm tries to change the layer parameter model to get the best results in classifying the position of the predicted direction of the ball. The dataset was collected as shown in Fig. 6. The CNN design used is as in Fig. 7 and equations ( 4) to (9). Convolutional Neural Network (CNN) is a type of artificial neural network specifically designed to process two-dimensional grid-shaped data, such as images. The convolution layer, pooling layer, and fully connected layer are the three primary hierarchical layers of a CNN. The central component of a CNN is the convolution layer, where different visual elements like edges, textures, and patterns are detected by applying filters or kernels to the input. A feature map reflecting the position of a certain feature in the original image is produced by the convolution layer's filters scanning the entire input. The way that neurons in the human brain react to visual stimuli is comparable to this mechanism. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 4)

8. The road damage detection research makes use of laser sensors to rebuild 3D road damage as well as stereo vision technologies. Several sensors are required for the stereo vision system, including two cameras, an LED, a laser, and LiDAR. The laser sensor has a small beamwidth; thus, it cannot detect road damage in the form of a large hole, necessitating the use of an array of LEDs, lasers, LiDARs, and other sensors [18], [49]. Reconstructing the pothole takes time, whether using an LED array, laser, or LiDAR. Furthermore, 3D road defect reconstruction and stereo vision require well-lit lighting and slow vehicle speeds [17], [18], [50].

Further research used image-processing techniques. Potholes are a form of road irregularity that can be recognized with traditional image processing techniques. To achieve high accuracy, this technique takes numerous steps, including manual image feature extraction and image processing parameter adjustments. As a result, the image frame rate varies depending on traffic circumstances [21]. Some research that investigated road conditions, pavement conditions, potholes, cracks, smart phone sensors, and accelerometers used machine learning techniques such as support vector machines, neural networks, multilayer perceptron, and decision trees [16]. Furthermore, research is being conducted to detect pavement damage using ML algorithms such as support vector machines, artificial neural networks, and random forests [51]. To improve accuracy, ML models require significant computer resources during data processing, which also includes manual feature analysis.

Several studies used deep convolutional neural network (CNN) techniques to automate the simultaneous feature extraction and categorization of objects [41], [52]. This is challenging to incorporate into real-time road defect detection systems. The deployment of CNN models for road damage detection on devices requires a balance between high accuracy and high efficiency [53]. The use of CNN models for road damage detection on devices requires achieving a balance between high accuracy and high efficiency. The use of CNN models for road damage detection on devices necessitates striking a balance between high accuracy and high efficiency. The parameter system performance deployment model CNN on devices performs well in terms of precision, recall, F1-score, and as well as efficiency of time inference.

The CNN models perform exceptionally well in terms of high accuracy, precision, recall, and low loss. This requires CNN models with large architecture and competitive computing costs that are inefficient. To do this while maintaining high accuracy, a simplified CNN model configuration setting is required to achieve good CNN model system performance. High efficiency, which is the CNN model system performance, enables it to detect road faults on edge devices with a short inference time. Because the CNN model on edge devices have limited storage capacity, inference time must be considered. Taking this into account, the CNN model offers good system performance and a short inference time for simpler model configurations, but high accuracy is difficult to achieve. To obtain optimal system performance, the CNN model parameters must be properly chosen. When selecting a detection model, there is no definitive answer as to which model has the best performance [31], [53].

Improving system performance in computer vision, object recognition, and classification using CNN models can be achieved through various methods. These include modifying or adding components to the CNN model structure and optimizing hyperparameter selection during CNN model training. The strategy of enhancing the CNN structure aims to improve feature extraction efficiency and model accuracy by modifying or incorporating new components into the CNN architecture. Several studies have focused on enhancing CNN models by modifying or adding components to the existing CNN structure [54], [55], [56], [57], [58], [59]. DenseNet was integrated into the YOLOv4 backbone to optimize feature transfer and reuse. This involved several modifications, such as adjusting the Path Aggregation Network (PANet) [54], introducing New Residual Blocks, applying Spatial Pyramid Pooling (SPP), modifying the PANet, and utilizing Hard-Swish activation functions [59]. Similarly, researchers have integrated DenseNet blocks into the YOLOv5 backbone to enhance the preservation and reuse of critical feature information. This was achieved by incorporating a Convolutional Block Attention Module (CBAM) [56]. Another study introduced a novel framework called Multiple Graph Learning Neural Networks (MGLNN) for semi-supervised learning on graph-based data [55]. Additionally, modifications were made to the YOLO model using the CSPDarknet53 backbone structure, which included Residual Blocks, DenseNet, Spatial Pyramid Pooling (SPP), and the Path Aggregation Network (PANet) [57]. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 2)

### response

CNN (Convolutional Neural Network) digunakan dalam deep learning karena dapat memproses data dua dimensi, seperti citra dan video, dengan efisiensi tinggi. CNN memiliki struktur hierarkis yang terdiri dari lapisan konvolusi, pooling, dan fully connected, yang memungkinkannya untuk mendeteksi fitur-fitur visual dalam citra.

Dalam konteks penelitian ini, CNN digunakan untuk memprediksi posisi bola menggunakan kamera ZED. CNN dapat mengambil citra dari kamera dan menghasilkan klasifikasi pada posisi bola dengan akurasi tinggi.

CNN juga digunakan dalam beberapa penelitian lainnya, seperti deteksi kerusakan jalan, pengenalan emosi suara, dan pengenalan objek. Dalam semua kasus, CNN dapat memproses data visual dengan efisiensi tinggi dan menghasilkan hasil yang akurat.

Dalam konteks ini, CNN digunakan karena kemampuannya untuk:

1. Memproses citra dua dimensi
2. Mendeteksi fitur-fitur visual
3. Menghasilkan klasifikasi pada posisi bola dengan akurasi tinggi

Jadi, CNN digunakan dalam deep learning karena dapat memproses data visual dengan efisiensi tinggi dan menghasilkan hasil yang akurat.

### reference


Fungsi utamanya adalah untuk mengekstrak fitur-fitur penting dalam citra dan menghasilkan klasifikasi yang akurat terhadap suatu tipe objek atau kategori. Pada bagian atas skema, terdapat label "Input" dan "Output", yang menunjukkan bahwa gambar ini berfungsi untuk menerima input suatu citra dan menghasilkan output berupa hasil pengenalan atau klasifikasi. CNN is a type of deep neural network that is highly effective for the analysis and processing of visual data such as images and videos.

---

## Sample 28

- conversation_id: 13
- user_chat_id: 653
- bot_chat_id: 654

### user_input

Bagaimana CNN bekerja secara sederhana?

### retrieved_context

1. FIGURE 6. CNN block diagram.

Gambar ini menampilkan skema blok CNN (Convolutional Neural Network). Elemen visual utama adalah beberapa lapisan konvolusi yang dihubungkan dengan satu sama lain melalui proses pemrosesan suatu gambar. Lapisan-lapisan tersebut terlihat seperti kotak-kotak persegi panjang yang berurutan, masing-masing memiliki label yang menunjukkan jenis operasi yang dilakukan: Conv2D (lapisan konvolusi), MaxPooling2D (proses downsampling dengan memilih maksimum nilai), Flatten (mengubah pola input 3 dimensi menjadi array satu dimensi).

Pada bagian atas skema, terdapat label "Input" dan "Output", yang menunjukkan bahwa gambar ini berfungsi untuk menerima input suatu citra dan menghasilkan output berupa hasil pengenalan atau klasifikasi. Namun, detail tentang jenis citra yang digunakan sebagai input masih tidak dapat diidentifikasi secara pasti dari gambar ini.

Dari skema blok CNN ini, dapat disimpulkan bahwa proses pemrosesan gambar dilakukan melalui beberapa tahap konvolusi dan downsampling dengan maksimum. Fungsi utamanya adalah untuk mengekstrak fitur-fitur penting dalam citra dan menghasilkan klasifikasi yang akurat terhadap suatu tipe objek atau kategori.

Perlu diingat bahwa karena hanya ada skema blok saja, detail tentang parameter atau nilai spesifik dari setiap lapisan konvolusi tidak dapat dilihat. Oleh karena itu, interpretasi harus berfokus pada gambaran umum proses yang terjadi dalam CNN daripada detil teknis parametris. (Development of a Speech Emotion Recognition Dataset for Indonesian, page 6)

2. The Convolutional Neural Network (CNN) model is trained using the prepared dataset. CNN is a type of deep neural network that is highly effective for the analysis and processing of visual data such as images and videos. In this context, CNN is used to predict the position of the ball based on the position data that has been collected during the training session. The training process involves adjusting the weights of the model through the backpropagation technique to minimize the prediction error. The Fig. 7 is a sequential model of the CNN architecture for ball position prediction. A sequential model is a series of layers that are processed sequentially from input to output. The given model consists of several types of layers: Conv1D, AveragePooling1D, Dropout, MaxPooling1D, Flatten, and Dense. The operation process is in equations ( 4) to (9). (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 7)

3. Here is the complete sequence of transformations that occur to the input signal as it passes through each layer in the model: 1. Conv1D 1:

• Input: (None, 10, 512)

• Output: (None, 10, 512)

• Convolution operation with a certain filter size. 2. AveragePooling1D 1:

• Input: (None, 10, 512)

• Output: (None, 5, 512)

• Takes the average of every two consecutive values, halving the length of the signal. The model takes an input signal, operates it through multiple layers of convolution, pooling, dropout, and finally dense layers to produce the output. Each layer has specific functions that help in extracting important features from the signal and finally make predictions based on those features.

To train the CNN, a loss function is used which measures the difference between the model's prediction and the true value. The loss function used is the Mean Squared Error (MSE), which can be expressed by the following formula:

where:

• ŷi is the model prediction for the i-th sample,

• y i is the actual value for the i-th sample,

• N is total number of samples in the dataset.

During the training phase, the model weights are updated using the average square of the difference between the predicted and actual values, which is computed using this loss function. By minimizing this loss value, the CNN model is expected to improve its prediction accuracy of the ball position. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 8)

4. The road damage detection research makes use of laser sensors to rebuild 3D road damage as well as stereo vision technologies. Several sensors are required for the stereo vision system, including two cameras, an LED, a laser, and LiDAR. The laser sensor has a small beamwidth; thus, it cannot detect road damage in the form of a large hole, necessitating the use of an array of LEDs, lasers, LiDARs, and other sensors [18], [49]. Reconstructing the pothole takes time, whether using an LED array, laser, or LiDAR. Furthermore, 3D road defect reconstruction and stereo vision require well-lit lighting and slow vehicle speeds [17], [18], [50].

Further research used image-processing techniques. Potholes are a form of road irregularity that can be recognized with traditional image processing techniques. To achieve high accuracy, this technique takes numerous steps, including manual image feature extraction and image processing parameter adjustments. As a result, the image frame rate varies depending on traffic circumstances [21]. Some research that investigated road conditions, pavement conditions, potholes, cracks, smart phone sensors, and accelerometers used machine learning techniques such as support vector machines, neural networks, multilayer perceptron, and decision trees [16]. Furthermore, research is being conducted to detect pavement damage using ML algorithms such as support vector machines, artificial neural networks, and random forests [51]. To improve accuracy, ML models require significant computer resources during data processing, which also includes manual feature analysis.

Several studies used deep convolutional neural network (CNN) techniques to automate the simultaneous feature extraction and categorization of objects [41], [52]. This is challenging to incorporate into real-time road defect detection systems. The deployment of CNN models for road damage detection on devices requires a balance between high accuracy and high efficiency [53]. The use of CNN models for road damage detection on devices requires achieving a balance between high accuracy and high efficiency. The use of CNN models for road damage detection on devices necessitates striking a balance between high accuracy and high efficiency. The parameter system performance deployment model CNN on devices performs well in terms of precision, recall, F1-score, and as well as efficiency of time inference.

The CNN models perform exceptionally well in terms of high accuracy, precision, recall, and low loss. This requires CNN models with large architecture and competitive computing costs that are inefficient. To do this while maintaining high accuracy, a simplified CNN model configuration setting is required to achieve good CNN model system performance. High efficiency, which is the CNN model system performance, enables it to detect road faults on edge devices with a short inference time. Because the CNN model on edge devices have limited storage capacity, inference time must be considered. Taking this into account, the CNN model offers good system performance and a short inference time for simpler model configurations, but high accuracy is difficult to achieve. To obtain optimal system performance, the CNN model parameters must be properly chosen. When selecting a detection model, there is no definitive answer as to which model has the best performance [31], [53].

Improving system performance in computer vision, object recognition, and classification using CNN models can be achieved through various methods. These include modifying or adding components to the CNN model structure and optimizing hyperparameter selection during CNN model training. The strategy of enhancing the CNN structure aims to improve feature extraction efficiency and model accuracy by modifying or incorporating new components into the CNN architecture. Several studies have focused on enhancing CNN models by modifying or adding components to the existing CNN structure [54], [55], [56], [57], [58], [59]. DenseNet was integrated into the YOLOv4 backbone to optimize feature transfer and reuse. This involved several modifications, such as adjusting the Path Aggregation Network (PANet) [54], introducing New Residual Blocks, applying Spatial Pyramid Pooling (SPP), modifying the PANet, and utilizing Hard-Swish activation functions [59]. Similarly, researchers have integrated DenseNet blocks into the YOLOv5 backbone to enhance the preservation and reuse of critical feature information. This was achieved by incorporating a Convolutional Block Attention Module (CBAM) [56]. Another study introduced a novel framework called Multiple Graph Learning Neural Networks (MGLNN) for semi-supervised learning on graph-based data [55]. Additionally, modifications were made to the YOLO model using the CSPDarknet53 backbone structure, which included Residual Blocks, DenseNet, Spatial Pyramid Pooling (SPP), and the Path Aggregation Network (PANet) [57]. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 2)

5. [38] C Cavina-Pratesi, C Hesse. Why do the eyes prefer the index finger? Simultaneous recording of eye and hand movements during precision grasping. (2013-04)

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

6. • Function: Converts multi-dimensional signals into onedimensional (1D) signals.

• Output: 1D signal. 6. Dense (Fully Connected) layer

• Function: Linearly combine all the signal features and apply an activation function.

• Operation:

where x is the input, σ is the activation function, w is the weight matrix, and b is the bias vector.

• Output: The signal that has been transformed by the dense layer. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 1)

7. FIGURE 9. CNN model training result.

Gambar ini menampilkan grafik hasil pelatihan model CNN (Convolutional Neural Network). Grafik ini terlihat seperti garis di atas yang menunjukkan proses pengembangan akurasi model CNN selama proses pelatihan. Pada awalnya, akurasi model cukup rendah, tetapi kemudian meningkat secara signifikan seiring dengan berjalannya waktu dan iterasi pelatihan.

Pada grafik tersebut terdapat beberapa titik tertentu yang menunjukkan peningkatan drastis dalam akurasi. Meskipun tidak ada angka spesifik yang dapat diidentifikasi, namun jelas bahwa model CNN telah berhasil meningkatkan akurasinya hingga mencapai nilai yang sangat tinggi.

Dari grafik ini kita dapat menyimpulkan bahwa proses pelatihan model CNN telah berjalan dengan efektif dan akurasi model meningkat secara signifikan. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 10)

8. This research uses the ROS system because it has the ability to integrate camera sensors with artificial intelligence methods and several other combined sensors in the robot. Fig. 4 shows the basic communication system for accessing the ZED camera on the robot. Image information is acquired over time and processed in real-time.  The prediction system that has been created using the CNN algorithm tries to change the layer parameter model to get the best results in classifying the position of the predicted direction of the ball. The dataset was collected as shown in Fig. 6. The CNN design used is as in Fig. 7 and equations ( 4) to (9). Convolutional Neural Network (CNN) is a type of artificial neural network specifically designed to process two-dimensional grid-shaped data, such as images. The convolution layer, pooling layer, and fully connected layer are the three primary hierarchical layers of a CNN. The central component of a CNN is the convolution layer, where different visual elements like edges, textures, and patterns are detected by applying filters or kernels to the input. A feature map reflecting the position of a certain feature in the original image is produced by the convolution layer's filters scanning the entire input. The way that neurons in the human brain react to visual stimuli is comparable to this mechanism. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 4)

### response

CNN (Convolutional Neural Network) bekerja dengan beberapa lapisan utama, yaitu:

1.  Lapisan Konvolusi (Convolution Layer): Mencari fitur-fitur visual seperti garis-garis, tekstur-teksur, dan pola-polaa dalam citra input dengan menggunakan filter atau kernel.
2.  Lapisan Pooling (Pooling Layer): Mengurangi dimensi dari feature map yang dihasilkan oleh lapisan konvolusi untuk menghemat jumlah parameter yang perlu diproses.
3.  Lapisan Fully Connected (Fully Connected Layer): Menggabungkan semua fitur-fitur yang telah ditemukan sebelumnya untuk membuat prediksi.

CNN bekerja dengan cara memproses citra-citra input secara sequential, yaitu:

1.  Citra input diproses oleh lapisan konvolusi untuk menemukan fitur-fitur visual.
2.  Fitur-fitur yang ditemukan kemudian diolah oleh lapisan pooling untuk menghemat jumlah parameter.
3.  Lalu hasilnya dikirim ke lapisan fully connected untuk membuat prediksi.

Dengan cara ini, CNN dapat menemukan fitur-fitur yang relevan dalam citra-citra input dan membuat prediksi yang akurat.

### reference


Lapisan-lapisan tersebut terlihat seperti kotak-kotak persegi panjang yang berurutan, masing-masing memiliki label yang menunjukkan jenis operasi yang dilakukan: Conv2D (lapisan konvolusi), MaxPooling2D (proses downsampling dengan memilih maksimum nilai), Flatten (mengubah pola input 3 dimensi menjadi array satu dimensi). Perlu diingat bahwa karena hanya ada skema blok saja, detail tentang parameter atau nilai spesifik dari setiap lapisan konvolusi tidak dapat dilihat. Elemen visual utama adalah beberapa lapisan konvolusi yang dihubungkan dengan satu sama lain melalui proses pemrosesan suatu gambar.
