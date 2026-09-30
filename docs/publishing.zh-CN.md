# 发布到 GitHub

建议仓库名：`dialectic-skill`。这是建议，不代表名称在你的账号中已被占用或已创建。

建议 About 描述：

> A bounded critique-and-refine skill with issue tracking, evidence-aware closure, and actionable next steps.

建议 topics：`agent-skills`、`prompt-engineering`、`critical-thinking`、`self-refinement`。

## 最简单的网页方式

1. 解压完整项目包，打开内层 dialectic-skill 文件夹。
2. 在 GitHub 新建仓库，自行选择 Public 或 Private。因为项目已含 README 和 LICENSE，创建空仓库即可。
3. 上传文件夹内的内容，使 README.md 和 skills/ 位于仓库根目录；不要只上传 ZIP，也不要多套一层 dialectic-skill/。
4. 确认 .github/workflows/check.yml 也上传了。文件选择器可能隐藏以点开头的目录；不能完整上传时改用下面的 Git 方式。
5. 提交后查看 Actions。工作流只做离线检查，不调用付费模型。
6. 查看 README、中文说明、三个示例和评估结果能否正常打开。

## Git 方式

在解压后的项目根目录打开终端：

```bash
git init
git add .
git commit -m "Initial release: Dialectic v0.1.0"
git branch -M main
```

再把 GitHub 新仓库页面提供的真实地址复制到下面命令中；不要原样保留 YOUR_USERNAME：

```bash
git remote add origin https://github.com/YOUR_USERNAME/dialectic-skill.git
git push -u origin main
```

如果已有 origin，先用 `git remote -v` 检查，不要盲目覆盖。登录或身份验证按你的 GitHub 设置完成。

## 发布前检查

```bash
python tools/check_repo.py
python -m unittest discover -s tests -v
```

确认 README 明确标记实验版本、没有编造收益数据；例子与实测记录分开。检查发布内容不含你自己的私密方案、密钥或其他账号资料。

许可证默认采用 MIT，版权署名为 Dialectic contributors；你可以在首次发布前改成你希望公开使用的署名。

## v0.1.0 Release 文案

```text
Dialectic v0.1.0 — experimental

A portable critique-and-refine Skill for ideas and plans.

Includes:
- Explicit constraints and critique adjudication
- Stable issue IDs and evidence-scoped closure
- Bounded review cycles and clear stopping reasons
- English/Chinese documentation and worked examples
- Offline repository checks and inspectable development smoke tests

This release does not establish superiority over ordinary prompting
or existing refinement methods. See evals/results.md for actual evidence.
```

在仓库提交完成并检查通过后，创建 v0.1.0 tag/release。具体发布由你操作；交付这个项目包不代表 GitHub 已经发布成功。
