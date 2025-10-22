
# 🧾 Scraping DAS MEI (ECAC Automático)

Script Node.js para automatizar a extração de informações do **Portal eCAC** e emissão de guias **DAS-MEI** com uso do **Certificado Digital A1**, executando de forma totalmente automatizada via Puppeteer.

---

## 🚀 Funcionalidades
- Acesso automatizado ao **eCAC** com certificado digital A1.
- Consulta de DAS-MEI por CNPJ, ano e mês.
- Execução com **perfil persistente do Chrome**, evitando reautenticação repetida.
- Logs automáticos em `logs/` com timestamp.
- Suporte a modo **interativo** (com navegador visível) e **headless** (oculto).
- Compatível com **macOS**, **Linux** e **Windows**.

---

## 🧩 Estrutura do Projeto

```

📦 scraping-das-mei
┣ 📂 bin
┃ ┣ scraping.js           # Script principal
┣ 📂 chrome-profile        # Perfil persistente do Chrome (ignorado no Git)
┣ 📂 logs                  # Arquivos de log (gerados automaticamente)
┣ 📜 package.json
┣ 📜 .gitignore
┗ 📜 README.md

````

---

## ⚙️ Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/orismarfh/scraping-das-mei_oris.git
   cd scraping-das-mei_oris
````

2. **Instale as dependências**

   ```bash
   npm install
   ```

3. **Execute o script**

   ```bash
   npm start
   ```

---

## 🖥️ Uso

Durante a execução, o script perguntará:

```
? Usar modo interativo (headless off)? Sim/Não
? Informe o CNPJ: 
? Informe o ano:
? Informe o mês:
```

Os logs serão salvos automaticamente em:

```
logs/YYYY-MM-DD_HH-MM-SS_scraping.log
```

---

## 🧠 Desenvolvimento

### 🧭 Atualizar seu fork

Se o repositório original (`engmsilva/scraping-das-mei`) for atualizado:

```bash
git fetch upstream
git checkout main
git rebase upstream/main
git push origin main
```

### 🧱 Trabalhar em novas features

Crie um novo branch antes de fazer melhorias:

```bash
git checkout -b feat/nova-funcionalidade
git push -u origin feat/nova-funcionalidade
```

---

## 🔒 Boas práticas do `.gitignore`

Os diretórios abaixo são ignorados para evitar envio de dados locais:

```
chrome-profile/
logs/
*.bak
*.DS_Store
```

Isso mantém o repositório limpo e evita o upload de perfis ou caches do Chrome.

---

## 🤝 Contribuindo

* Este repositório é um fork de [`engmsilva/scraping-das-mei`](https://github.com/engmsilva/scraping-das-mei).
* PR aberto: **feat/ecac-cert-a1-auto-profile**
* “Allow edits from maintainers” está habilitado — o mantenedor pode revisar e integrar quando desejar.

Se o PR não for aceito, este fork evoluirá independentemente, mantendo as atualizações de compatibilidade com ECAC e melhorias de automação.

---

## 🧾 Licença

Distribuído sob a licença MIT. Consulte `LICENSE` para mais detalhes.
