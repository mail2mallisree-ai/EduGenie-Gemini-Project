const form =
    document.getElementById("edu-form");

const taskSelect =
    document.getElementById("task");

const input =
    document.getElementById("input-text");

const submitButton =
    document.getElementById("submit-btn");

const charCount =
    document.getElementById("char-count");

const statusBadge =
    document.getElementById("status-badge");

const resultCard =
    document.getElementById("result-card");

const resultTitle =
    document.getElementById("result-title");

const resultContent =
    document.getElementById("result-content");

const clearButton =
    document.getElementById("clear-btn");


const endpointMap = {

    qa: {
        url: "/qa",
        title: "Question Answer"
    },

    explain: {
        url: "/explain",
        title: "Concept Explanation"
    },

    quiz: {
        url: "/quiz",
        title: "Practice Quiz"
    },

    summarize: {
        url: "/summarize",
        title: "Summary"
    },

    learn: {
        url: "/learn/recommendations",
        title: "Learning Path"
    }

};


const placeholderMap = {

    qa:
        "Example: Which is the largest ocean?",

    explain:
        "Example: Explain the Pythagoras theorem with a simple example.",

    quiz:
        "Paste a lesson, paragraph, or topic here to generate 3 MCQs.",

    summarize:
        "Paste a long educational paragraph here.",

    learn:
        "Example: SQL"

};


function setStatus(
    text,
    state = ""
) {

    statusBadge.textContent = text;

    statusBadge.className =
        `status-badge ${state}`.trim();
}


function renderTextResult(
    result
) {

    const block =
        document.createElement("div");

    block.className =
        "result-text";

    block.textContent =
        String(result ?? "");

    resultContent.replaceChildren(
        block
    );
}


function renderQuiz(
    data
) {

    const wrapper =
        document.createElement("div");

    wrapper.className =
        "quiz-list";


    data.questions.forEach(
        (item, questionIndex) => {

            const card =
                document.createElement("div");

            card.className =
                "quiz-item";

            card.dataset.index =
                questionIndex;


            const heading =
                document.createElement("h3");

            heading.textContent =
                `${questionIndex + 1}. ${item.question}`;

            card.appendChild(
                heading
            );


            const options =
                document.createElement("div");

            options.className =
                "quiz-options";


            item.options.forEach(
                (optionText, optionIndex) => {

                    const label =
                        document.createElement("label");

                    label.className =
                        "option";


                    const radio =
                        document.createElement("input");

                    radio.type =
                        "radio";

                    radio.name =
                        `question-${questionIndex}`;

                    radio.value =
                        String(optionIndex);


                    const text =
                        document.createElement("span");

                    text.textContent =
                        optionText;


                    label.append(
                        radio,
                        text
                    );


                    options.appendChild(
                        label
                    );

                }
            );


            const note =
                document.createElement("div");

            note.className =
                "answer-note";

            note.hidden =
                true;

            note.dataset.note =
                String(questionIndex);


            card.append(
                options,
                note
            );


            wrapper.appendChild(
                card
            );

        }
    );


    const actions =
        document.createElement("div");

    actions.className =
        "quiz-actions";


    const score =
        document.createElement("span");

    score.className =
        "score";

    score.textContent =
        "Choose an option for each question, then check your answers.";


    const checkButton =
        document.createElement("button");

    checkButton.type =
        "button";

    checkButton.className =
        "secondary-btn";

    checkButton.textContent =
        "Check Answers";


    checkButton.addEventListener(
        "click",
        () => {

            let answered = 0;

            let correct = 0;


            data.questions.forEach(
                (item, index) => {

                    const card =
                        wrapper.querySelector(
                            `.quiz-item[data-index="${index}"]`
                        );


                    const selected =
                        card.querySelector(
                            `input[name="question-${index}"]:checked`
                        );


                    const note =
                        card.querySelector(
                            `[data-note="${index}"]`
                        );


                    const labels =
                        [
                            ...card.querySelectorAll(
                                ".option"
                            )
                        ];


                    labels.forEach(
                        label => {

                            label.classList.remove(
                                "correct",
                                "incorrect"
                            );

                        }
                    );


                    if (selected) {

                        answered += 1;


                        const selectedIndex =
                            Number(
                                selected.value
                            );


                        if (
                            selectedIndex ===
                            item.correct_answer
                        ) {

                            correct += 1;

                            labels[
                                selectedIndex
                            ].classList.add(
                                "correct"
                            );


                            note.textContent =
                                `Correct. ${item.explanation}`;

                        } else {

                            labels[
                                selectedIndex
                            ].classList.add(
                                "incorrect"
                            );


                            labels[
                                item.correct_answer
                            ].classList.add(
                                "correct"
                            );


                            note.textContent =
                                `Correct answer: ${item.options[item.correct_answer]}. ${item.explanation}`;

                        }

                    } else {

                        labels[
                            item.correct_answer
                        ].classList.add(
                            "correct"
                        );


                        note.textContent =
                            `Not answered. Correct answer: ${item.options[item.correct_answer]}. ${item.explanation}`;

                    }


                    note.hidden =
                        false;

                }
            );


            score.textContent =
                `Score: ${correct} / ${data.questions.length} • Answered: ${answered} / ${data.questions.length}`;

        }
    );


    actions.append(
        score,
        checkButton
    );


    resultContent.replaceChildren(
        wrapper,
        actions
    );
}


function renderResult(
    data,
    type
) {

    resultTitle.textContent =
        endpointMap[type].title;


    if (type === "quiz") {

        renderQuiz(data);

    } else {

        renderTextResult(
            data.result
        );

    }


    resultCard.classList.remove(
        "hidden"
    );


    resultCard.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}


taskSelect.addEventListener(
    "change",
    () => {

        input.placeholder =
            placeholderMap[
                taskSelect.value
            ];

    }
);


input.addEventListener(
    "input",
    () => {

        charCount.textContent =
            `${input.value.length} / 12000`;

    }
);


clearButton.addEventListener(
    "click",
    () => {

        resultCard.classList.add(
            "hidden"
        );

        resultContent.replaceChildren();

        setStatus("Ready");

    }
);


form.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();


        const type =
            taskSelect.value;


        const config =
            endpointMap[type];


        const text =
            input.value.trim();


        if (!text) {
            return;
        }


        submitButton.disabled =
            true;

        submitButton.textContent =
            "Working...";


        setStatus(
            "Generating",
            "loading"
        );


        try {

            const response =
                await fetch(
                    config.url,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            text: text
                        })
                    }
                );


            const payload =
                await response.json();


            if (!response.ok) {

                throw new Error(
                    payload.detail ||
                    "The server could not complete this request."
                );

            }


            renderResult(
                payload,
                type
            );


            setStatus(
                "Complete"
            );


        } catch (error) {

            resultTitle.textContent =
                "Something went wrong";


            const block =
                document.createElement("div");


            block.className =
                "result-text";


            block.textContent =
                error.message;


            resultContent.replaceChildren(
                block
            );


            resultCard.classList.remove(
                "hidden"
            );


            setStatus(
                "Error",
                "error"
            );


        } finally {

            submitButton.disabled =
                false;

            submitButton.textContent =
                "Generate Answer";

        }

    }
);