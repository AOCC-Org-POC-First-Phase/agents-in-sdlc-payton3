import { test, expect } from '@playwright/test';

test.describe('Home Page', () => {
  test('should display the correct title', async ({ page }) => {
    await page.goto('/');
    
    // Check that the page title is correct
    await expect(page).toHaveTitle('Tailspin Toys - Crowdfunding your new favorite game!');
  });

  test('should display the main heading', async ({ page }) => {
    await page.goto('/');
    
    // Check that the main heading is present - updated to look for the page heading, not the header
    const mainHeading = page.locator('h1').nth(1); // Second h1 is the main page heading
    await expect(mainHeading).toHaveText('Welcome to Tailspin Toys');
  });

  test('should display the welcome message', async ({ page }) => {
    await page.goto('/');
    
    // Check that the welcome message is present - updated to match new content
    const welcomeMessage = page.locator('p').first();
    await expect(welcomeMessage).toContainText('Discover your next favorite game!');
  });
});
