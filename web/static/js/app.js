(function () {
  const defaultBase = "http://localhost:8765";
  const apiBase = () => localStorage.getItem("airsApiBase") || defaultBase;
  const write = (id, value) => {
    const el = document.getElementById(id);
    if (el) el.textContent = typeof value === "string" ? value : JSON.stringify(value, null, 2);
  };
  const remember = (item) => {
    const history = JSON.parse(localStorage.getItem("airsHistory") || "[]");
    history.unshift({ at: new Date().toISOString(), item });
    localStorage.setItem("airsHistory", JSON.stringify(history.slice(0, 20)));
  };
  async function request(path, options) {
    const response = await fetch(apiBase() + path, options);
    const body = await response.json();
    if (!response.ok) throw new Error(JSON.stringify(body));
    return body;
  }

  const healthButton = document.getElementById("healthButton");
  if (healthButton) {
    healthButton.addEventListener("click", async () => {
      try {
        const body = await request("/health");
        write("apiStatus", body.status);
        write("dashboardOutput", body);
      } catch (error) {
        write("apiStatus", "不可用");
        write("dashboardOutput", String(error));
      }
    });
  }

  const researchForm = document.getElementById("researchForm");
  if (researchForm) {
    researchForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      const form = new FormData(researchForm);
      const payload = Object.fromEntries(form.entries());
      write("researchOutput", "运行中...");
      try {
        const body = await request("/research", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });
        remember({ request_id: body.request_id, company: body.company.company_name, endpoint: body.endpoint });
        write("researchOutput", body);
      } catch (error) {
        write("researchOutput", String(error));
      }
    });
  }

  const workspaceButton = document.getElementById("workspaceButton");
  if (workspaceButton) {
    workspaceButton.addEventListener("click", async () => {
      try { write("workspaceOutput", await request("/workspace")); }
      catch (error) { write("workspaceOutput", String(error)); }
    });
  }

  const memoryButton = document.getElementById("memoryButton");
  if (memoryButton) {
    memoryButton.addEventListener("click", async () => {
      try { write("memoryOutput", await request("/memory")); }
      catch (error) { write("memoryOutput", String(error)); }
    });
  }

  const historyList = document.getElementById("historyList");
  if (historyList) {
    const history = JSON.parse(localStorage.getItem("airsHistory") || "[]");
    historyList.innerHTML = history.length ? history.map((row) => (
      `<article><strong>${row.item.company || "Unknown"}</strong><p>${row.item.request_id || ""}</p><small>${row.at}</small></article>`
    )).join("") : "<p>暂无本地历史。</p>";
  }

  const input = document.getElementById("apiBaseInput");
  if (input) input.value = apiBase();
  const save = document.getElementById("saveSettings");
  if (save) {
    save.addEventListener("click", () => {
      localStorage.setItem("airsApiBase", input.value || defaultBase);
      alert("设置已保存。免责声明：AIRS 不构成投资建议。");
    });
  }
}());

