<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sarcoma Classification by DNA Methylation</title>
    <!-- Chosen Palette: Calm Harmony -->
    <!-- Application Structure Plan: A single-page dashboard structure is chosen to present a narrative flow. It starts with a high-level overview, moves to an interactive results dashboard (metrics, charts), provides a qualitative analysis of those results, and finally details the project's methodology. This guides the user from the "what" to the "why" and "how," making the project's status and next steps intuitive and easy to grasp. A top navigation bar allows for quick access to each thematic section. -->
    <!-- Visualization & Content Choices: 
        - Key Metrics (Accuracy): HTML cards; Goal: Inform; Interaction: None; Justification: Provides a quick, high-level summary.
        - Classification Report: HTML table; Goal: Organize; Interaction: None; Justification: Standard, detailed presentation of metrics.
        - Performance Scores: Grouped Bar Chart (Chart.js); Goal: Compare; Interaction: Tooltips on hover; Justification: Visually compares precision, recall, and f1-score across classes more effectively than text.
        - Class Distribution: Donut Chart (Chart.js); Goal: Inform (Proportions); Interaction: Tooltips on hover; Justification: Clearly shows the composition of the test set.
        - Project Workflow: Styled HTML divs; Goal: Organize; Interaction: None; Justification: Simple, clear visualization of the project pipeline without complex graphics.
        - All visualizations are implemented using Chart.js on Canvas or styled HTML/CSS, adhering to the requirements. -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 300px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 350px;
            }
        }
    </style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body class="bg-gray-50 text-gray-800">

    <div class="container mx-auto p-4 sm:p-6 lg:p-8">
        
        <header class="text-center mb-12">
            <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-2">Sarcoma Classification by DNA Methylation</h1>
            <p class="text-lg text-gray-600 max-w-3xl mx-auto">An interactive report on the development of a machine learning model for classifying sarcoma subtypes based on epigenetic data.</p>
        </header>

        <nav class="sticky top-0 bg-gray-50/80 backdrop-blur-sm z-10 mb-12 py-3 border-b">
            <ul class="flex justify-center space-x-4 sm:space-x-8">
                <li><a href="#dashboard" class="text-gray-600 hover:text-blue-600 font-medium transition-colors">Dashboard</a></li>
                <li><a href="#analysis" class="text-gray-600 hover:text-blue-600 font-medium transition-colors">Analysis</a></li>
                <li><a href="#methodology" class="text-gray-600 hover:text-blue-600 font-medium transition-colors">Methodology</a></li>
            </ul>
        </nav>

        <main>
            <section id="dashboard" class="mb-16 scroll-mt-24">
                <h2 class="text-3xl font-bold text-center mb-8">Model Performance Dashboard</h2>
                <p class="text-center text-gray-600 max-w-2xl mx-auto mb-10">This section provides an interactive overview of the initial model's performance. The model, a Random Forest Classifier, was trained on a preliminary dataset with placeholder labels to establish a functional workflow. The results reflect this initial test phase.</p>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12 text-center">
                    <div class="bg-white p-6 rounded-xl shadow-md">
                        <h3 class="text-lg font-semibold text-gray-500 mb-2">Overall Accuracy</h3>
                        <p id="accuracy-metric" class="text-5xl font-bold text-blue-600">32.8%</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-md">
                        <h3 class="text-lg font-semibold text-gray-500 mb-2">Macro Avg F1-Score</h3>
                        <p id="f1-metric" class="text-5xl font-bold text-blue-600">0.16</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-md">
                        <h3 class="text-lg font-semibold text-gray-500 mb-2">Test Samples</h3>
                        <p id="samples-metric" class="text-5xl font-bold text-blue-600">122</p>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
                    <div class="bg-white p-6 rounded-xl shadow-md">
                        <h3 class="text-xl font-bold text-center mb-4">Classification Metrics</h3>
                        <div class="chart-container">
                            <canvas id="classificationChart"></canvas>
                        </div>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-md">
                        <h3 class="text-xl font-bold text-center mb-4">Test Set Class Distribution</h3>
                         <div class="chart-container">
                            <canvas id="supportChart"></canvas>
                        </div>
                    </div>
                </div>
            </section>

            <section id="analysis" class="mb-16 scroll-mt-24">
                <h2 class="text-3xl font-bold text-center mb-8">Analysis of Results</h2>
                 <div class="bg-white p-8 rounded-xl shadow-md max-w-4xl mx-auto">
                    <p class="text-lg text-gray-700 leading-relaxed mb-4">The performance results on the dashboard clearly indicate that the current model is not yet effective. This outcome is entirely expected and serves as a crucial validation of our project workflow rather than a measure of final classification ability.</p>
                    <div class="bg-amber-100 border-l-4 border-amber-500 text-amber-800 p-4 rounded-r-lg" role="alert">
                        <p class="font-bold">Key Insight</p>
                        <p>The model was trained on placeholder data where sample labels (`Type_0`, `Type_1`, `Type_2`) were assigned randomly. The model's low accuracy and its tendency to predict only a single class (`Type_2`) demonstrate that it could not find any meaningful patterns in this dummy data.</p>
                    </div>
                    <h3 class="text-2xl font-bold mt-6 mb-3">Next Steps</h3>
                    <p class="text-lg text-gray-700 leading-relaxed">The immediate and most critical next step is to integrate the actual clinical metadata from the GEO dataset. This involves sourcing the correct labels (i.e., the true sarcoma subtypes) for each sample and retraining the model. This will allow the algorithm to learn the real epigenetic signatures that differentiate sarcoma types, and we anticipate a significant improvement in performance.</p>
                </div>
            </section>

            <section id="methodology" class="scroll-mt-24">
                <h2 class="text-3xl font-bold text-center mb-8">Methodology & Data</h2>
                <div class="bg-white p-8 rounded-xl shadow-md max-w-4xl mx-auto">
                    <p class="text-lg text-gray-700 leading-relaxed mb-6">This project follows a standard data science workflow to ensure reproducibility and clarity. The process begins with raw data from a public repository, which is then cleaned, processed, and used to train and evaluate a classification model. The repository is structured to reflect these distinct stages.</p>

                    <h3 class="text-2xl font-bold mb-4">Project Workflow</h3>
                    <div class="flex flex-col md:flex-row items-center justify-center space-y-4 md:space-y-0 md:space-x-4 text-center">
                        <div class="p-4 bg-gray-100 rounded-lg w-full md:w-1/4">
                            <h4 class="font-bold text-gray-700">1. Raw Data</h4>
                            <p class="text-sm text-gray-600">Acquire data from GEO</p>
                        </div>
                        <div class="text-2xl font-bold text-blue-500 transform md:rotate-0 rotate-90">&rarr;</div>
                        <div class="p-4 bg-gray-100 rounded-lg w-full md:w-1/4">
                             <h4 class="font-bold text-gray-700">2. Preprocessing</h4>
                            <p class="text-sm text-gray-600">Clean, filter & impute data</p>
                        </div>
                        <div class="text-2xl font-bold text-blue-500 transform md:rotate-0 rotate-90">&rarr;</div>
                        <div class="p-4 bg-gray-100 rounded-lg w-full md:w-1/4">
                             <h4 class="font-bold text-gray-700">3. Model Training</h4>
                            <p class="text-sm text-gray-600">Train Random Forest model</p>
                        </div>
                        <div class="text-2xl font-bold text-blue-500 transform md:rotate-0 rotate-90">&rarr;</div>
                        <div class="p-4 bg-gray-100 rounded-lg w-full md:w-1/4">
                            <h4 class="font-bold text-gray-700">4. Evaluation</h4>
                            <p class="text-sm text-gray-600">Assess performance</p>
                        </div>
                    </div>
                    
                    <h3 class="text-2xl font-bold mt-8 mb-4">Data Source</h3>
                    <p class="text-lg text-gray-700 leading-relaxed">The raw data for this project is sourced from the <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE140686" target="_blank" class="text-blue-600 hover:underline font-medium">GSE140686 dataset on NCBI GEO</a>. This public dataset contains DNA methylation profiles of over 1,500 sarcoma samples, providing a rich resource for epigenetic research.</p>
                </div>
            </section>
        </main>
        
        <footer class="text-center mt-16 py-6 border-t">
            <p class="text-gray-500">Interactive Report generated from project `README.md`.</p>
        </footer>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const reportData = {
                accuracy: 0.3279,
                macroAvgF1: 0.16,
                weightedAvgF1: 0.16,
                samples: 122,
                labels: ['Type_0', 'Type_1', 'Type_2'],
                precision: [0.00, 0.00, 0.33],
                recall: [0.00, 0.00, 1.00],
                f1_score: [0.00, 0.00, 0.49],
                support: [41, 41, 40]
            };
            
            document.getElementById('accuracy-metric').textContent = (reportData.accuracy * 100).toFixed(1) + '%';
            document.getElementById('f1-metric').textContent = reportData.macroAvgF1.toFixed(2);
            document.getElementById('samples-metric').textContent = reportData.samples;

            const classificationCtx = document.getElementById('classificationChart').getContext('2d');
            new Chart(classificationCtx, {
                type: 'bar',
                data: {
                    labels: reportData.labels,
                    datasets: [
                        {
                            label: 'Precision',
                            data: reportData.precision,
                            backgroundColor: 'rgba(59, 130, 246, 0.6)',
                            borderColor: 'rgba(59, 130, 246, 1)',
                            borderWidth: 1
                        },
                        {
                            label: 'Recall',
                            data: reportData.recall,
                            backgroundColor: 'rgba(16, 185, 129, 0.6)',
                            borderColor: 'rgba(16, 185, 129, 1)',
                            borderWidth: 1
                        },
                        {
                            label: 'F1-Score',
                            data: reportData.f1_score,
                            backgroundColor: 'rgba(239, 68, 68, 0.6)',
                            borderColor: 'rgba(239, 68, 68, 1)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 1.0
                        }
                    },
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    let label = context.dataset.label || '';
                                    if (label) {
                                        label += ': ';
                                    }
                                    if (context.parsed.y !== null) {
                                        label += context.parsed.y.toFixed(2);
                                    }
                                    return label;
                                }
                            }
                        }
                    }
                }
            });

            const supportCtx = document.getElementById('supportChart').getContext('2d');
            new Chart(supportCtx, {
                type: 'doughnut',
                data: {
                    labels: reportData.labels,
                    datasets: [{
                        label: 'Number of Samples',
                        data: reportData.support,
                        backgroundColor: [
                            'rgba(59, 130, 246, 0.6)',
                            'rgba(16, 185, 129, 0.6)',
                            'rgba(239, 68, 68, 0.6)'
                        ],
                        borderColor: [
                            'rgba(59, 130, 246, 1)',
                            'rgba(16, 185, 129, 1)',
                            'rgba(239, 68, 68, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        tooltip: {
                             callbacks: {
                                label: function(context) {
                                    let label = context.label || '';
                                    if (label) {
                                        label += ': ';
                                    }
                                    if (context.parsed !== null) {
                                        label += context.parsed;
                                    }
                                    return label + ' samples';
                                }
                            }
                        }
                    }
                }
            });

            document.querySelectorAll('nav a').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });
        });
    </script>
</body>
</html>
