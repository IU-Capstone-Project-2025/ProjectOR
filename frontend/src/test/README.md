# Frontend Testing Guide

This directory contains the testing setup and utilities for the ProjectOR frontend application.

## Testing Stack

- **Vitest**: Fast unit test framework for Vite projects
- **@testing-library/svelte**: Simple and complete Svelte testing utilities
- **@testing-library/jest-dom**: Custom Jest matchers for DOM testing
- **jsdom**: Pure JavaScript DOM implementation for Node.js

## Test Structure

```
src/
├── test/
│   ├── setup.ts           # Global test setup and mocks
│   ├── setup.test.ts      # Test for setup configuration
│   └── README.md          # This file
├── lib/
│   ├── utils.test.ts      # Unit tests for utility functions
│   ├── validation.ts      # Validation utilities
│   ├── validation.test.ts # Validation function tests
│   └── api/
│       └── client.test.ts # API client tests
└── routes/
    ├── app/(components)/
    │   └── dataLoaders.test.ts     # Project API tests
    └── auth/
        ├── login/
        │   └── dataLoaders.test.ts # Login API tests
        └── register/
            └── dataLoaders.test.ts # Registration API tests
```

## Running Tests

### All tests

```bash
pnpm test
```

### Run tests once

```bash
pnpm test:run
```

### Visual test UI

```bash
pnpm test:ui
```

### With coverage

```bash
pnpm test:coverage
```

## Writing Tests

### Component Tests

```typescript
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/svelte';
import YourComponent from './YourComponent.svelte';

describe('YourComponent', () => {
	it('should render correctly', () => {
		render(YourComponent, { props: { prop1: 'value' } });

		expect(screen.getByText('Expected Text')).toBeInTheDocument();
	});
});
```

### Unit Tests

```typescript
import { describe, it, expect } from 'vitest';
import { yourFunction } from './yourModule';

describe('yourFunction', () => {
	it('should return expected result', () => {
		const result = yourFunction('input');
		expect(result).toBe('expected output');
	});
});
```

### Mocking

```typescript
import { vi } from 'vitest';

// Mock a module
vi.mock('./module', () => ({
	default: vi.fn(),
	namedExport: vi.fn()
}));

// Mock a function
const mockFn = vi.fn();
mockFn.mockReturnValue('mocked value');
```

## Global Mocks

The following are automatically mocked in all tests:

- **localStorage**: Complete localStorage API
- **Environment variables**: `VITE_API_BASE_URL` is set to `http://localhost:8000`
- **SvelteKit modules**: `$env/static/private` and `$env/dynamic/private`

## Best Practices

1. **Test behavior, not implementation**: Focus on what the component does, not how it does it
2. **Use semantic queries**: Prefer `getByRole`, `getByLabelText`, etc. over `getByTestId`
3. **Mock external dependencies**: Mock API calls, third-party libraries, etc.
4. **Test edge cases**: Empty states, error states, loading states
5. **Keep tests simple**: One assertion per test when possible
6. **Use descriptive test names**: Test names should clearly describe what is being tested

## Coverage

Aim for good coverage but focus on testing critical paths and user interactions rather than achieving 100% coverage for its own sake.

## Troubleshooting

### Common Issues

1. **Module not found errors**: Make sure the path aliases are correctly configured in `vitest.config.ts`
2. **DOM not available**: Ensure `environment: 'jsdom'` is set in the Vitest config
3. **Svelte component errors**: Make sure `@testing-library/svelte` is properly installed and imported

### Debug Tips

- Use `screen.debug()` to see the current DOM state
- Use `--reporter=verbose` for more detailed test output
- Use the Vitest UI (`pnpm test:ui`) for interactive debugging
