# 밑바닥부터 시작하는 Agent

<p align="center">
  <img src="assets/agent-from-scratch-cover.png" alt="밑바닥부터 시작하는 Agent 패러디 표지" width="360">
</p>

<p align="center">
  <sub>생성형 AI로 만든 비공식 패러디 표지입니다. 실제 존재하는 책이 아니며 특정 출판사와 관련이 없습니다.</sub>
</p>

**한국어** | [English](README.en.md)

오늘도 나는 "딸깍."을 한다.

테스트 코드는 작성됐고, 테스트는 통과했고, 커밋 메시지도 만들어졌다.  
딸깍이 돌아가는 동안 나는 다음에 무엇을 시킬지 계획만 세우고 있다.

편하다.  
그런데 조금 찝찝하다.

전문가라면, 자신이 쓰는 도구가 어떻게 동작하는지 이해하려고 해야 하지 않을까?

## Goal

딸깍 한 번 뒤에서 어떤 일이 일어나는지 이해하고, 이제는 대충 아는 척이 아니라 설명할 수 있게 되기.

## Roadmap

1. [500줄로 ClaudeCode 만들기](notebooks/001_500_lines_claudecode.ipynb)

## Quick Start

```bash
uv sync
cp .env.example .env
uv run --group dev pytest
```

`.env`에는 OpenRouter 또는 Gemini API 키를 넣습니다. 원본 강의 예제는 OpenRouter를 먼저 쓰고, 인증 실패나 키 누락 시 Gemini로 fallback하는 구조입니다.

1강의 최종 예제 실행:

```bash
uv run python -m lecture_001_500_lines_claudecode.steps.step_05_code_agent
```

## Project Structure

```text
assets/                         표지 이미지
docs/                           장기 문서용 공간
examples/001_500_lines_claudecode/                     1강 실습용 fixture
notebooks/001_500_lines_claudecode.ipynb
src/lecture_001_500_lines_claudecode/      1강 에이전트 구현 코드
tests/                          단계별 동작과 LLM provider 테스트
```

## Repository Policy

- `.env`에는 실제 API 키를 넣되 커밋하지 않습니다.
- 강의 본문은 notebook에, 실행 가능한 코드는 `src`에 둡니다.
- 문서가 아니라 실습 입력으로 쓰는 파일은 `examples`에 둡니다.

## License

This project is licensed under the MIT License.
