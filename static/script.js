form.addEventListener("submit", (e) => {
  e.preventDefault();
  document.querySelector(".answer").innerText = `Calculating...`;
  const formData = new FormData(e.target);
  const formProps = Object.fromEntries(formData);
  for (let key in formProps) {
    formProps[key] = Number(formProps[key]);
  }
  axios
    .post("/predict", formProps)
    .then((res) => {
      let price = res.data;
      document.querySelector(".answer").innerText = `${price}/-`;
    })
    .catch((err) => {
      console.log(err);
    });
});
